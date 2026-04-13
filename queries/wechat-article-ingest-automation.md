---
title: "微信文章摄取流程的自动化上限"
created: 2026-04-13
updated: 2026-04-13
layer: query
type: query
tags: [hermes, wechat, ingest, workflow, automation]
sources: [synthesis/hermes-wechat-integration.md]
status: open
priority: medium
owner: hermes
---

# 微信文章摄取流程的自动化上限

## 背景

Hermes Wiki 的核心价值来源是微信文章摄取，但目前 ingest 流程需要人工介入。

## 具体问题

### Q1: 当前 ingest 的自动化程度
- 文章链接发来后，哪些步骤是 AI 自动完成，哪些需要人工？
- ingest 时 AI 自动判断 layer + type 的准确率有多高？
- 哪些类型的文章最难自动分类？

### Q2: frontmatter 的自动化填充
- `source_url`、`source_domain`、`source_author` 能否自动提取？
- `tags` 的自动生成质量如何？
- 哪些字段必须人工填写？

### Q3: ingest 的质量控制
- 如何发现和处理重复文章？
- 文章"价值判断"的标准是什么？
- 无价值文章是否直接归档到 `_archive/`？

## 开放问题

1. **ingest 的 token 成本**：每篇文章的 ingest 平均消耗多少 token？
2. **批量 ingest 的策略**：一次发 10+ 篇时，如何排序处理优先级？
3. **ingest 的时序依赖**：processed → summary → synthesis 的晋升条件是什么？

## 相关
- [[synthesis/hermes-wechat-integration]] — 微信接入全貌
- [[backlog/ingest-ai-recommend]] — ingest 时 AI 自动推荐 layer+type 待办
- [[knowledge-management-ai-era]] — 知识管理流程参考
