---
title: "Wiki 知识编译复利效应的量化验证"
created: 2026-04-13
updated: 2026-04-13
layer: query
type: query
tags: [knowledge-base, wiki, karpathy, compounding-knowledge, llm-wiki]
sources: [synthesis/knowledge-management-ai-era.md, concepts/karpathy-llm-wiki-methodology.md]
status: open
priority: medium
owner: hermes
---

# Wiki 知识编译复利效应的量化验证

## 核心问题

Karpathy 的 LLM Wiki 核心主张是"知识滚雪球"——每次使用让 AI 变得更有知识。hermes-wiki 复制了这个理念，但没有验证机制。

## 具体问题

### Q1: 复利效应的量化指标
- 如何衡量"Wiki 让 AI 变得更有知识"？
- token 消耗降低有数据支撑吗（vs RAG baseline）？
- 回答质量提升如何测量？

### Q2: Wiki 与 RAG 的实际差距
- 对同一个问题，Wiki 回答 vs RAG 回答的质量差异多大？
- Wiki 在哪些类型问题上优势最明显？
- 在当前 34 篇 raw 文章规模下，优势是否已显现？

### Q3: 复利的时间窗口
- 多少篇文章开始能看到复利效应？
- Wiki 的知识腐烂（stale content）如何处理？
- 定期 lint 能替代人工维护吗？

## 验证方法

1. 对比实验：同一个问题，用 Wiki 知识回答 vs 不用
2. 记录每次 wiki-output 的质量反馈（参考 backlog/wiki-output-challenge）

## 相关
- [[synthesis/knowledge-management-ai-era]] — Wiki vs RAG vs Graphify 路线对比
- [[backlog/wiki-output-challenge]] — Wiki 价值验证待办
- [[概念/karpathy-llm-wiki-methodology]] — LLM Wiki 方法论
