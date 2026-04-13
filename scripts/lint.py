#!/usr/bin/env python3
"""
Wiki Lint — Health check for hermes-wiki
Checks: orphaned pages, stale content, missing links, frontmatter validity
Run: python lint.py [wiki_path]
"""

import sys
import os
import re
from datetime import datetime, timedelta
from pathlib import Path

WIKI_ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parent.parent
STALE_DAYS = 90

issues = []
warnings = []


def get_all_pages():
    """Find all markdown pages excluding _archive."""
    pages = {}
    for md in WIKI_ROOT.rglob("*.md"):
        if "/_archive/" in str(md):
            continue
        rel = md.relative_to(WIKI_ROOT)
        pages[str(rel)] = md
    return pages


def get_outlinks(content):
    """Extract [[wikilinks]] from content, handling piped [[target|display]] syntax.

    hermes-wiki uses [[target|display]] format — path BEFORE |, display AFTER |.
    Standard candidates are tried to resolve partial paths.
    """
    links = set()
    for match in re.findall(r'\[\[([^\]]+)\]\]', content):
        # Piped syntax: [[target|display]] — |前是路径
        if '|' in match:
            target = match.split('|', 1)[0].strip()
        else:
            target = match
        if target in ('wikilinks', 'pagename'):
            continue
        links.add(target)
    return links


def parse_frontmatter(text):
    """Parse YAML frontmatter. Returns (frontmatter_dict, body)."""
    match = re.match(r'^---\n(.*?)\n---\n', text, re.DOTALL)
    if not match:
        return {}, text
    fm_text = match.group(1)
    body = text[match.end():]
    fm = {}
    for line in fm_text.splitlines():
        if ':' in line:
            key, val = line.split(':', 1)
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm, body


def check_frontmatter(pages):
    """Check every page has required frontmatter fields."""
    for rel_path, md in pages.items():
        text = md.read_text()
        fm, body = parse_frontmatter(text)
        missing = []
        for field in ['title', 'created', 'layer', 'type']:
            if field not in fm:
                missing.append(field)
        if missing:
            issues.append(f"  [{rel_path}] Missing frontmatter: {', '.join(missing)}")


def check_orphaned(pages):
    """Find pages with no incoming wikilinks.

    raw/ pages are archives — exempt from orphaned check.
    """
    all_links = {}
    for rel_path in pages:
        all_links[rel_path] = set()

    for rel_path, md in pages.items():
        text = md.read_text()
        for link in get_outlinks(text):
            # Skip literal "wikilinks" used as syntax example text
            if link == 'wikilinks':
                continue
            # Skip template placeholders like [[pagename]] in draft sections
            if link == 'pagename':
                continue
            # Normalize: "graphify" -> "graphify.md" or "concepts/graphify.md"
            candidates = [
                link + ".md",
                f"backlog/{link}.md",
                f"concepts/{link}.md",
                f"entities/{link}.md",
                f"summary/concepts/{link}.md",
                f"summary/entities/{link}.md",
                f"summary/{link}.md",
                f"概念/{link}.md",
                f"comparisons/{link}.md",
                f"processed/{link}.md",
                f"synthesis/{link}.md",
                f"action/{link}.md",
                f"conversations/{link}.md",
            ]
            for cand in candidates:
                if cand in all_links:
                    all_links[cand].add(rel_path)
                    break

    for rel_path, links in all_links.items():
        # raw/ pages are read-only archives — never orphaned
        if rel_path.startswith("raw/"):
            continue
        if not links and rel_path != "index.md":
            # index.md is allowed to have no incoming links
            warnings.append(f"  [{rel_path}] ORPHANED — no pages link to it")


def check_stale(pages):
    """Flag pages not updated in > STALE_DAYS days."""
    cutoff = datetime.now() - timedelta(days=STALE_DAYS)
    for rel_path, md in pages.items():
        fm, _ = parse_frontmatter(md.read_text())
        if 'updated' in fm and fm['updated'] and fm['updated'].lower() != 'null':
            try:
                updated = datetime.strptime(fm['updated'], '%Y-%m-%d')
                if updated < cutoff:
                    issues.append(f"  [{rel_path}] STALE — not updated since {fm['updated']}")
            except ValueError:
                warnings.append(f"  [{rel_path}] Malformed updated date: {fm['updated']}")


def check_wikilinks(pages):
    """Check all [[wikilinks]] resolve to existing pages."""
    for rel_path, md in pages.items():
        text = md.read_text()
        for link in get_outlinks(text):
            # Try to resolve
            candidates = [
                link + ".md",
                f"backlog/{link}.md",
                f"concepts/{link}.md",
                f"概念/{link}.md",
                f"entities/{link}.md",
                f"summary/concepts/{link}.md",
                f"summary/entities/{link}.md",
                f"processed/{link}.md",
                f"processed/articles/{link}.md",
                f"synthesis/{link}.md",
                f"action/{link}.md",
                f"conversations/{link}.md",
                f"raw/{link}.md",
                f"raw/articles/{link}.md",
                f"comparisons/{link}.md",
            ]
            found = any(str(WIKI_ROOT / c) in [str(m) for m in pages.values()] for c in candidates)
            if not found:
                issues.append(f"  [{rel_path}] BROKEN LINK: [[{link}]] — target not found")


def check_layer_dirs():
    """Ensure required layer directories exist."""
    required = ['raw', 'processed', 'summary', 'synthesis', 'action']
    for layer in required:
        d = WIKI_ROOT / layer
        if not d.exists():
            issues.append(f"  [/{layer}/] MISSING directory — layer defined in SCHEMA but not created")


def check_contradictions(pages):
    """
    Detect potential contradictions across pages.
    Flags pages that:
    1. Have the 'contradictions:' frontmatter field set
    2. Cover overlapping topics but have diverging claims
    """
    # Group pages by tags (excluding meta tags)
    tag_groups = {}
    meta_tags = {'meta', 'ai-agent', 'hermes', 'openclaw', 'llm'}
    for rel_path, md in pages.items():
        fm, body = parse_frontmatter(md.read_text())
        tags = fm.get('tags', '')
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.strip('[]').split(',')]
        for tag in tags:
            tag = tag.lower()
            if tag not in meta_tags and tag not in ('meta',):
                if tag not in tag_groups:
                    tag_groups[tag] = []
                tag_groups[tag].append((rel_path, fm, body))

    # Flag explicit contradictions declared in frontmatter
    for rel_path, md in pages.items():
        fm, body = parse_frontmatter(md.read_text())
        explicit = fm.get('contradictions', '')
        if explicit:
            warnings.append(f"  [{rel_path}] CONTRADICTION declared → {explicit}")

    # Detect same-tag pages with conflicting dates and non-overlapping content
    # Heuristic: if two pages share a meaningful tag but have very different body lengths
    # AND were updated >30 days apart, surface as potential stale-vs-fresh conflict
    for tag, group in tag_groups.items():
        if len(group) < 2:
            continue
        sorted_group = []
        for rel_path, fm, body in group:
            updated_str = fm.get('updated', '2000-01-01')
            if not updated_str or updated_str.lower() in ('null', 'none', ''):
                updated = None
            else:
                try:
                    updated = datetime.strptime(updated_str, '%Y-%m-%d')
                except (ValueError, TypeError):
                    updated = None
            word_count = len(body.split())
            sorted_group.append((updated, word_count, rel_path, fm))
        # Sort by date, None dates treated as very old (skip them in drift check)
        sorted_group.sort(key=lambda x: (x[0] is None, x[0]))
        if len(sorted_group) >= 2:
            newest = sorted_group[-1]
            oldest = sorted_group[0]
            # Skip if either has no date
            if oldest[0] is None or newest[0] is None:
                continue
            days_diff = (newest[0] - oldest[0]).days
            # If newest is much longer AND older than 30 days, flag for review
            if days_diff > 30 and newest[1] > oldest[1] * 3:
                warnings.append(
                    f"  [{tag}] TOPIC DRIFT — newest={newest[2]} ({newest[0].date()}), "
                    f"oldest={oldest[2]} ({oldest[0].date()}), {days_diff}d apart, "
                    f"lengths {oldest[1]} vs {newest[1]} words — older page may be stale"
                )


def main():
    pages = get_all_pages()

    check_layer_dirs()
    check_frontmatter(pages)
    check_orphaned(pages)
    check_stale(pages)
    check_wikilinks(pages)
    check_contradictions(pages)

    # ── Categorise issues ──────────────────────────────────────────────────
    categories = {
        "🔴 Missing Frontmatter":    [],
        "🔴 Broken Link":            [],
        "🔴 Stale Content":         [],
        "🔴 Missing Directory":     [],
    }
    for issue in issues:
        if "Missing frontmatter" in issue:
            categories["🔴 Missing Frontmatter"].append(issue)
        elif "BROKEN LINK" in issue:
            categories["🔴 Broken Link"].append(issue)
        elif "STALE" in issue:
            categories["🔴 Stale Content"].append(issue)
        elif "MISSING directory" in issue:
            categories["🔴 Missing Directory"].append(issue)
        else:
            categories["🔴 Broken Link"].append(issue)

    warn_categories = {
        "🟡 Orphaned":              [],
        "🟡 Topic Drift":           [],
        "🟡 Contradiction":          [],
        "🟡 Malformed Date":        [],
    }
    for w in warnings:
        if "TOPIC DRIFT" in w:
            warn_categories["🟡 Topic Drift"].append(w)
        elif "CONTRADICTION" in w:
            warn_categories["🟡 Contradiction"].append(w)
        elif "Malformed updated date" in w:
            warn_categories["🟡 Malformed Date"].append(w)
        elif "ORPHANED" in w:
            warn_categories["🟡 Orphaned"].append(w)

    # ── Header ─────────────────────────────────────────────────────────────
    total_pages = len(pages)
    divider = "─" * 54

    print()
    print(f"  ╭{'─' * 52}╮")
    print(f"  │  📋 Wiki Lint Report                         │")
    print(f"  │  {WIKI_ROOT.name:<46} │")
    print(f"  ╰{'─' * 52}╯")
    print()
    print(f"  📄 Pages scanned : {total_pages}")
    print(f"  ⏱  过期阈值     : {STALE_DAYS} 天")
    print()

    # ── Summary table ──────────────────────────────────────────────────────
    has_issues   = any(categories.values())
    has_warnings = any(warn_categories.values())

    if has_issues or has_warnings:
        print(f"  {divider}")
        print(f"  {'类别':<24} {'数量':>6}")
        print(f"  {divider}")
        for label, items in categories.items():
            if items:
                print(f"  {label:<24} {len(items):>6}")
        for label, items in warn_categories.items():
            if items:
                print(f"  {label:<24} {len(items):>6}")
        print(f"  {divider}")
        total_issues   = sum(len(v) for v in categories.values())
        total_warnings = sum(len(v) for v in warn_categories.values())
        print(f"  {'❌ Issues':<24} {total_issues:>6}")
        print(f"  {'⚠️  Warnings':<24} {total_warnings:>6}")
        print(f"  {divider}")
        print()

    # ── Detail sections ────────────────────────────────────────────────────
    for label, items in categories.items():
        if items:
            print(f"  {label}")
            for item in items:
                print(f"    {item}")
            print()

    if not has_issues and not has_warnings:
        print("  ✅ 所有检查通过，无问题")

    for label, items in warn_categories.items():
        if items:
            print(f"  {label} ({len(items)})")
            for item in items[:5]:
                print(f"    {item}")
            if len(items) > 5:
                print(f"    … 还有 {len(items) - 5} 项")
            print()

    # ── Footer ─────────────────────────────────────────────────────────────
    print(f"  {'─' * 54}")
    print(f"  Issues: {len(issues)}  |  Warnings: {len(warnings)}")
    print()
    return 1 if issues else 0


if __name__ == '__main__':
    sys.exit(main())
