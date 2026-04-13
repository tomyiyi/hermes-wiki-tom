#!/usr/bin/env python3
"""
Wiki Query — Search hermes-wiki for answers
Usage: python query.py "<question>"
"""
import sys
import re
from pathlib import Path

WIKI_ROOT = Path(__file__).parent.parent
INDEX_PATH = WIKI_ROOT / "index.md"

# Search priority: concept pages first, then comparisons, then processed
PRIORITY_DIRS = ["概念", "comparisons", "processed", "action", "backlog"]


def extract_keywords(question: str) -> list[str]:
    """Extract search keywords from a natural-language question."""
    # Remove common question words and punctuation
    cleaned = re.sub(r"[吗呢吧啊呀的|是|在|有|和|与|对|从|到|为|了|被|让|把|给|让|叫|比|于]", " ", question)
    cleaned = re.sub(r"[^\w\u4e00-\u9fff]", " ", cleaned)
    words = [w.strip() for w in cleaned.split() if len(w.strip()) >= 2]

    # Also yield each individual token for mixed English+CJK strings (e.g. "Skills进化" → "Skills" + "进化")
    mixed = re.findall(r"[a-zA-Z]+", question)
    for m in mixed:
        if m.lower() not in [w.lower() for w in words]:
            words.append(m)

    return words


def search_pages(question: str) -> list[tuple[str, str, str]]:
    """
    Search wiki pages for the question.
    Returns list of (rel_path, title, snippet) sorted by relevance.
    """
    keywords = extract_keywords(question)
    if not keywords:
        keywords = [question.strip()[:10]]

    scored = []

    for md in WIKI_ROOT.rglob("*.md"):
        if "/_archive/" in str(md):
            continue
        rel = md.relative_to(WIKI_ROOT)
        rel_str = str(rel)

        # Skip meta files
        if rel_str in ("index.md", "log.md", "SCHEMA.md"):
            continue

        text = md.read_text(encoding="utf-8")

        # Extract title
        title_match = re.search(r"^title:\s*\"?(.+?)\"?\s*$", text, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else rel.stem
        title_lower = title.lower()

        # Score by keyword matches
        score = 0
        matched_keywords = []
        text_lower = text.lower()

        for kw in keywords:
            kw_lower = kw.lower()
            title_hit = kw_lower in title_lower
            body_hit = kw_lower in text_lower
            if title_hit:
                score += 10
            if body_hit:
                score += 3
                matched_keywords.append(kw)

        # Boost priority layers (synthesis/concept pages score much higher)
        for i, d in enumerate(PRIORITY_DIRS):
            if str(rel).startswith(d):
                score += (len(PRIORITY_DIRS) - i) * 8
                break

        # Penalize long processed/raw pages (less curated)
        if str(rel).startswith("raw/") or str(rel).startswith("processed/"):
            score -= 5

        if score > 0:
            # Extract snippet (first 200 chars of body, skip frontmatter)
            body_start = 0
            fm_match = re.search(r"^---\n.*?\n---\n", text, re.DOTALL)
            if fm_match:
                body_start = fm_match.end()

            snippet = text[body_start:body_start + 300].strip()
            snippet = re.sub(r"#+\s*", "", snippet)[:200]

            scored.append((score, str(rel), title, snippet, matched_keywords))

    # Sort by score descending
    scored.sort(key=lambda x: -x[0])
    return scored


def format_result(score: int, rel: str, title: str, snippet: str, matched: list[str], rank: int) -> str:
    """Format a single search result."""
    layer = rel.split("/")[0] if "/" in rel else "root"
    match_str = ", ".join(matched[:5]) if matched else "general"
    bar = "█" * min(score // 5, 20)
    lines = [
        f"",
        f"  {rank}. **{title}**",
        f"     📁 {rel}  |  相关度: {bar} ({score}pt)  |  命中: {match_str}",
        f"     {snippet}...",
    ]
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print("Usage: python query.py \"<question>\"")
        sys.exit(0)

    question = " ".join(sys.argv[1:])

    print()
    print(f"  ╭{'─' * 52}╮")
    print(f"  │  🔍 Wiki Query                                  │")
    print(f"  ╰{'─' * 52}╯")
    print()
    print(f"  问题: {question}")
    print()

    results = search_pages(question)

    if not results:
        print("  未找到相关内容，建议用更宽泛的关键词重试。")
        print()
        return 0

    # Show top result in full, rest abbreviated
    top = results[0]
    print(f"  ── 相关度最高的页面 ─────────────────────────────")

    # Read full content of top result
    top_path = WIKI_ROOT / top[1]
    top_text = top_path.read_text(encoding="utf-8")

    # Extract frontmatter
    fm_match = re.search(r"^---\n(.*?)\n---\n", top_text, re.DOTALL)
    frontmatter = fm_match.group(1) if fm_match else ""

    body = top_text[fm_match.end():] if fm_match else top_text

    # Extract tags
    tags_match = re.search(r"tags:\s*\[(.*?)\]", frontmatter)
    tags = tags_match.group(1) if tags_match else ""

    layer_match = re.search(r"layer:\s*(\w+)", frontmatter)
    layer = layer_match.group(1) if layer_match else "unknown"

    type_match = re.search(r"type:\s*(\w+)", frontmatter)
    doc_type = type_match.group(1) if type_match else "unknown"

    print(f"")
    print(f"  ▶ {top[2]}")
    print(f"    📂 {top[1]}")
    print(f"    🏷️  layer={layer}  type={doc_type}  tags=[{tags}]")
    print(f"    ────────────────────────────────────────────")
    print(f"    {body[:600].strip()}")
    if len(body) > 600:
        print(f"    …（还有 {len(body)-600} 字）")
    print(f"")

    if len(results) > 1:
        print(f"  ── 其他相关页面 ────────────────────────────────")
        for i, r in enumerate(results[1:6], 2):
            print(format_result(r[0], r[1], r[2], r[3], r[4], i))
        if len(results) > 6:
            print(f"")
        print(f"  共找到 {len(results)} 个相关页面，前 {min(6, len(results))} 个已显示。")

    print()
    print(f"  💡 如需查看完整内容，告诉我页名或路径。")
    print(f"  💡 如果这回答了你的问题，可以让我把答案存为 [[Queries/...]] 页。")
    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
