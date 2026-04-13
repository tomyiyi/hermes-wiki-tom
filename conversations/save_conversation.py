#!/usr/bin/env python3
"""
save_conversation.py — Save a valuable Hermes conversation to the wiki.
Usage: python3 save_conversation.py "<topic>" "<key_insight1>" "<key_insight2>" ...
Writes to: conversations/[topic]-[date].md
"""
import sys
import os
from datetime import datetime

WIKI_ROOT = "/Users/tom/Desktop/hermes-wiki"
DATE = datetime.now().strftime("%Y-%m-%d")

def slugify(s):
    import re
    s = s.lower()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[-\s]+', '-', s)
    return s[:60]

def auto_certainty(topic: str, insights: list[str]) -> str:
    """
    Auto-judge certainty level based on content signals.
    Returns: 'confirmed' | 'inferred' | 'speculative'
    """
    text = topic + " " + " ".join(insights)

    # confirmed signals: explicit facts, code, URLs, numbers, config
    confirmed_signals = [
        "http://", "https://", "ftp://",
        "api_key", "API_KEY", "password", "token",
        "def ", "class ", "import ", "fn ", "pub fn",
        "yaml", "json", "toml", "config",
        "0.0.0.0", "localhost", "192.168.",
        "id:", "ID:", "UUID:",
    ]

    # speculative signals: hedging, uncertainty
    speculative_signals = [
        "可能", "也许", "如果", "假设", "大概", "推测",
        "猜测", "不确定", "todo", "TBD", "待定",
        "要不要", "要不要", "要不要",
    ]

    has_confirmed = any(s in text for s in confirmed_signals)
    has_speculative = any(s in text for s in speculative_signals)

    if has_confirmed and not has_speculative:
        return "confirmed"
    elif has_speculative and not has_confirmed:
        return "speculative"
    return "inferred"


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 save_conversation.py <topic> <insight1> <insight2> ...")
        sys.exit(1)

    topic = sys.argv[1]
    insights = sys.argv[2:]
    certainty = auto_certainty(topic, insights)
    slug = f"{slugify(topic)}-{DATE}"
    path = f"{WIKI_ROOT}/conversations/{slug}.md"

    lines = [
        "---",
        f"title: {topic}",
        f"created: {DATE}",
        "updated: null",
        "layer: conversations",
        "type: summary",
        f'tags: [{", ".join(["conversation"] + topic.split()[:3])}]',
        "sources: []",
        "derived_from: []",
        f"certainty: {certainty}",
        "participants: [human, hermes]",
        f"conversation_date: {DATE}",
        "outcome: (填写这次对话产生了什么)",
        "key_insights: (填写核心洞察)",
        "archived: false",
        "---",
        "",
        f"# {topic}",
        "",
        f"**日期:** {DATE}",
        f"**确定性:** {certainty}（confirmed / inferred / speculative）",
        f"**参与者:** human + Hermes",
        "",
        "## 对话摘要",
        "",
        "（在此粘贴对话中的关键内容片段）",
        "",
        "## 核心洞察",
        "",
    ]

    for i, insight in enumerate(insights, 1):
        lines.append(f"{i}. {insight}")

    lines.extend([
        "",
        "## 对话结果",
        "",
        "（填写：产生了什么决策/代码/知识/行动）",
        "",
        "## 来源文章",
        "",
        "（如有相关 wiki 页面，用 [[pagename]] 链接）",
    ])

    with open(path, "w") as f:
        f.write("\n".join(lines))

    print(f"Saved: {path} [certainty={certainty}]")

    # Update conversations-archive.md if this is the first entry
    archive_path = f"{WIKI_ROOT}/conversations/conversations-archive.md"
    entry = f"- [[{slug}]] — {DATE}: {topic} [{certainty}]"
    with open(archive_path, "r") as f:
        content = f.read()
    if slug not in content:
        content = content.replace(
            "## 收录标准",
            f"## 最近对话\n\n{entry}\n\n## 收录标准"
        )
        with open(archive_path, "w") as f:
            f.write(content)
        print(f"Updated: {archive_path}")

if __name__ == "__main__":
    main()
