---
title: "[ingest] ingest 时 AI 自动推荐 layer + type"
created: 2026-04-11
updated: 2026-04-11
layer: backlog
type: action
status: completed
priority: high
owner: hermes
execution_target: "2026-04-12"
tags: [backlog, ingest, workflow]
sources: [summary/concepts/karpathy-llm-wiki.md, summary/concepts/knowledge-management-principles.md]
---

# [Backlog] ingest AI 推荐

## 做什么
修改 `fetch_wechat.py`，在抓取完成后自动调用 LLM 推荐：
- `layer`: raw / processed / summary / synthesis / action / conversations
- `type`: concept / entity / comparison / query / summary
- `rationale`: 一句话说明为什么推荐这个分类

## 什么时候做
2026-04-12（明天）

## 怎么做
在 `fetch_wechat.py` 的 Markdown 输出末尾追加 LLM 推荐段落（不修改已存在的 frontmatter），格式：
```
## AI 推荐分类

- **Layer:** xxx
- **Type:** xxx
- **Rationale:** xxx

> 此推荐由 Hermes 基于文章内容自动生成，人工确认后写入 frontmatter。
```

## 反馈要求
完成后在当前文件记录：
- 实际推荐的 layer/type 分布（是否有规律）
- 推荐质量如何（是否合理）
- 是否需要调整 prompt
