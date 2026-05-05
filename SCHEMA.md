---
title: SCHEMA
created: 2026-04-11
updated: 2026-04-11
layer: meta
type: meta
tags: [meta]
---
# Wiki Schema

## Domain
AI Agent 技术、自动化工作流、知识管理、LLM 应用实践、OPC 社区执行

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `graphify-token-reduction.md`)
- Every wiki page starts with YAML frontmatter (see below)
- Use wikilinks to link between pages (minimum 2 outbound links per page)
- When updating a page, always bump the `updated` date
- Every new page must be added to `index.md` under the correct section
- Every action must be appended to `log.md`
- **录入前必读 `purpose.md`** — 理解知识库方向，防止盲目录入
- **两步录入原则** — 先分析（找关联/缺口），再生成（写页面/建链接）

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
layer: raw | processed | summary | synthesis | action
type: concept | entity | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
derived_from: []   # list of pages this was synthesized from (synthesis layer only)
action_id: null    # cron job ID or task reference if this led to an action
solves_what:       # 知识可复用的前提——不知道解决什么就不知道何时用它
  - "解决：<这个知识解决的是什么类型的问题>"
  - "用户：<核心用户是谁>"
  - "失效：<什么条件下这个知识失效>"
  - "相关：<与它最相关的现有知识>"
---
```

## Tag Taxonomy
- AI-Agent: agent, autonomous, hermes, openclaw, claude-code
- Knowledge: knowledge-base, wiki, rag, graphify, memory
- Productivity: automation, workflow, cron, scheduling
- LLM: llm, gpt, minimax, context-window, token
- Tools: skill, mcp, browser-use, Obsidian
- Research: research, paper, arxiv, notes
- Meta: comparison, timeline, workflow

---

# Two-Dimensional Classification

## Dimension 1: Knowledge Layer（知识层 - 来源阶段）

| Layer | 说明 | 规则 |
|-------|------|------|
| `raw` | 原始文章 | 只读存档，保留原文、来源链接、日期，不做任何修改 |
| `processed` | 整理笔记 | 划重点、批注、提取关键段落，仍保持与原文对应 |
| `summary` | 单篇总结 | 一句话摘要 + 核心要点，不含综合分析 |
| `synthesis` | 综合分析 | 多来源跨文章分析，含对比、推断、开放问题 |
| `action` | 行动触发 | 导致具体任务、代码、cron job、决策的文章，记录行动结果 |
| `conversations` | 对话存档 | Hermes 有价值对话记录，核心推理和决策沉淀 |

### Layer Rules
- `raw/` 目录：文件进来后**永不编辑**，只标记 `archived: true` 后移入 `_archive/raw/`
- `action/` 页面：必须填 `action_id` 指向具体产生的任务
- `synthesis/` 页面：必须填 `derived_from` 列出综合来源
- `conversations/` 页面：记录 Hermes 有价值对话，必须填 `key_insights`
- 层与层之间用 `sources` 和 `derived_from` 建立溯源链

## Dimension 2: Content Type（内容类型）

| Type | 说明 |
|------|------|
| `concept` | 概念、理论、方法论 |
| `entity` | 实体（工具/人/产品/服务） |
| `comparison` | 对比分析（表格格式优先） |
| `query` | 开放问题、探索笔记 |
| `summary` | 总结（继承自 summary 层，可含 action 结果） |

---

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central to one source
- **Add to existing page** when a source mentions something already covered
- **DON'T create a page** for passing mentions, minor details
- **Split a page** when it exceeds ~200 lines
- **Archive a page** when fully superseded — move to `_archive/`, remove from index

## Layer-Specific Templates

### raw/ article
```yaml
---
title: ...
created: YYYY-MM-DD
updated: YYYY-MM-DD
layer: raw
type: summary
tags: [...]
source_url: https://...
source_domain: ...
source_author: ...
source_published: YYYY-MM-DD
original_length: N words
archived: false
---
```

### action/ page
```yaml
---
title: ...
created: YYYY-MM-DD
updated: YYYY-MM-DD
layer: action
type: summary
tags: [...]
sources: [raw/articles/..., processed/..., ...]
action_id: cronjob_xxx  # or null
action_outcome: success | failed | pending
action_summary: "What was done as a result"
---
```

## Entity Pages
One page per notable entity. Include:
- Overview / what it is
- Key facts and dates
- Relationships to other entities
- Source references

## Concept Pages
One page per concept or topic. Include:
- Definition / explanation
- Current state of knowledge
- Open questions or debates
- Related concepts

## Comparison Pages
Side-by-side analyses. Include:
- What is compared and why
- Dimensions of comparison (table format preferred)
- Verdict or synthesis
- Sources

## Update Policy
When new information conflicts with existing content:
1. Check the dates — newer sources generally supersede older ones
2. If genuinely contradictory, note both positions with dates and sources
3. Mark the contradiction in frontmatter: `contradictions: [page-name]`
4. Flag for user review in the lint report
