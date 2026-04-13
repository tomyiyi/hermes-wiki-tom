---
title: Hermes Wiki 初始化与两维分类重构
created: 2026-04-11
updated: 2026-04-11
layer: action
type: summary
tags: [hermes, wiki, knowledge-base, llm-wiki, graphify]
sources: [raw/articles/graphify-token-reduction-1-72.md, raw/articles/karpathy-llm-wiki-personal-knowledge-base.md, raw/articles/karpathy-obsidian-claudian-tutorial.md]
derived_from: []
action_id: wiki-init-20260411
action_outcome: success
action_summary: |
  1. 初始化 Hermes Wiki（/Users/tom/Desktop/hermes-wiki）
  2. 三篇原始文章 ingest 到 raw/articles/
  3. 单篇总结写入 summary/
  4. 重构为两维分类体系：layer（知识层）+ type（内容类型）
  5. processed/ synthesis/ action/ 三个空层已填充
---

# Action: Hermes Wiki 初始化与重构

## 背景
读了 Graphify 和 Karpathy LLM Wiki 三篇文章后，决定把 Hermes 的知识管理从"临时对话"升级为持久化 wiki。

## 做了什么

### 1. 初始化 Wiki
- 创建 `/Users/tom/Desktop/hermes-wiki`
- 三篇原始文章存入 `raw/articles/`

### 2. 两维分类体系重构
原有的 `concepts/` + `entities/` 是单维分类（只有 type）。
扩展为两维：

**维度一：知识层（layer）**
```
raw → processed → summary → synthesis → action
只读    整理       单篇      跨篇       行动
```

**维度二：内容类型（type）**
```
concept / entity / comparison / query / summary
```

layer 是一级目录，type 降为 frontmatter 属性。

### 3. processed/ 填充
- `graphify.md` → 划重点：Token 数据、双通道机制、三种关系标签
- `karpathy-llm-wiki.md` → 划重点：三层 vs 五层架构、Ingest/Lint 流程
- `obsidian-tutorial.md` → 划重点：工具链、最佳实践、对 Hermes 的意义

### 4. synthesis/ 填充
- `knowledge-compilation-pattern.md` → RAG vs 知识编译、两条技术路径对比、五层架构共鸣

## 结果
- Hermes Wiki 现在是完整的五层结构
- 后续新文章按流程：raw/ → processed/ → summary/synthesis/action/

## 待落地
- Graphify MCP 导出能否直接接入 Hermes（需要测试）
- 对话存档策略（Notes/Conversation 层尚未建立）
- Lint 健康检查（孤立页面、过时内容检测）尚未实现
