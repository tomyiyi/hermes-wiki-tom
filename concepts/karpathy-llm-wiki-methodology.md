---
title: "Karpathy LLM Wiki 方法论"
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: concept
tags: [knowledge-management, llm, wiki, obsidian, karpathy, rag, personal-knowledge-management, claude-code]
sources: [raw/articles/240f27478bcf_Karpathy-AI+Obsidian知识库教程-栗氪聊AI.md, raw/articles/395f4636416e_Karpathy的LLM-Wiki火了我改造了一下比原版更好用.md]
derived_from: [240f27478bcf_Karpathy-AI+Obsidian知识库教程-栗氪聊AI, 395f4636416e_Karpathy的LLM-Wiki火了-我改造了一下-比原版更好用]
---

# Karpathy LLM Wiki 方法论

## 一句话定义

> **LLM Wiki 是一种知识管理范式**：不是每次查询时从原始文档重新检索（RAG），而是 LLM 增量构建并持久维护一个结构化的双向链接 Markdown 知识库，知识被"编译"一次，之后持续保持最新。

## 核心洞察

### RAG vs Wiki 的本质差异

| | RAG（大多数 AI 知识库）| LLM Wiki（Karpathy 方法）|
|--|----------------------|------------------------|
| 查询时 | 从原始文档检索片段，每次重新拼装 | 直接读已编译好的 wiki 页 |
| 知识积累 | 每次问题独立，无积累 | 跨文档链接、矛盾标记、综合分析持续沉淀 |
| 回答质量 | 依赖检索质量，容易碎片化 | 链接已建好，综合分析已存在 |
| 维护方式 | 文档静默堆积 | LLM 主动更新矛盾、更新关联 |

> "好的答案本身可以作为新页面存回 wiki——你的探索和摄入的文章一样有价值" — Karpathy

## 三层架构

```
┌─────────────────────────────────────────────┐
│  Schema 层（CLAUDE.md / AGENTS.md）         │
│  告诉 LLM：wiki 结构、约定、工作流           │
├─────────────────────────────────────────────┤
│  Wiki 层（LLM 维护的 Markdown 文件）          │
│  摘要页、概念页、实体页、对比页、综合页       │
│  LLM 完全拥有此层，用户只读不写               │
├─────────────────────────────────────────────┤
│  Raw Sources 层（原始文档）                   │
│  文章、论文、图片、数据文件                    │
│  不可变，LLM 只读不修改                       │
└─────────────────────────────────────────────┘
```

### Schema 的关键作用
Schema（AGENTS.md / CLAUDE.md）是 LLM 的"行为规范"——它让 LLM 成为"有纪律的 wiki 维护者"而非"通用聊天机器人"。随着你对领域理解的深入，Schema 也会共同演化。

## 三个核心操作

### 1. Ingest（摄取）
- 用户将新文档放入 raw sources
- LLM 读取 → 讨论核心要点 → 写摘要页 → 更新 index → 更新相关实体/概念页 → 追加 log
- 单篇可能涉及 10-15 个 wiki 页面
- 建议单篇摄入 + 保持参与，而非批量无人监督摄入

### 2. Query（查询）
- LLM 先读 index.md 定位相关页面，再深入阅读
- 回答可以是 Markdown 页面、对比表、幻灯片、图表
- **关键**：好的答案应该作为新页面存回 wiki，而非消失在聊天记录里

### 3. Lint（健康检查）
- 定期检查：矛盾页面、陈旧内容被新来源取代、孤立页面（无入站链接）、缺失交叉引用
- LLM 擅长建议新问题和寻找新来源

## 两个特殊文件

| 文件 | 性质 | 作用 |
|------|------|------|
| `index.md` | 内容目录 | 每个页面的链接 + 一句话摘要 + 元数据，按分类组织 |
| `log.md` | 时间线 | append-only 记录所有 ingest/query/lint 操作，格式统一便于解析 |

## Obsidian + Claude Code 工具链

### 工具链组合
- **Obsidian**：本地笔记软件，LLM Wiki 的前端界面
- **Claudian**：将 Claude Code 以图形界面接入 Obsidian 的插件
- **obsidian-skills**：Obsidian CEO 亲做的 5 个 skill（操作规范+最佳实践）
- **cc-switch**：切换不同国产模型和 API 的工具（非官方订阅用户推荐）

### Claudian 安装
1. 安装 Obsidian 插件 BRAT
2. 添加：`https://github.com/YishenTu/claudian`
3. 安装后在 Obsidian 右上角出现机器人按钮，即可图形化对话

## 与当前 hermes-wiki 的关系

**已对齐的部分：**
- `SCHEMA.md` = Schema 层 ✅
- `index.md` = 内容目录 ✅
- `log.md` = 时间线记录 ✅
- `raw/` = Raw Sources 层 ✅
- `概念/` = Wiki 层（实体/概念/对比页）✅
- 两维分类（layer × type）= Wiki 层 + 内容类型 ✅

**可优化的地方：**
- Lint 操作（`scripts/lint.py` 已有，但可强化矛盾检测）
- Query 操作目前是手动发问，未实现"先读 index → 再 drill down"的自动化流程
- ingest → wiki 更新的自动化程度（当前是手动触发）

## 辩证视角

**局限：**
- 初期冷启动：没有积累时，wiki 的价值不如直接 RAG
- LLM 的 Wikipedia 式幻觉风险：wiki 页可能被 LLM 悄然改写或删除关键内容
- 对低频使用者边际价值递减

**核心前提：**
- 知识需要**长期积累**才有价值（适合研究方向、职业成长）
- 不适合**一次性查询**场景（那是传统搜索和 RAG 的主场）

## 关联
- [[hermes-four-layer-memory-architecture]]（Hermes 四层记忆 vs Wiki 三层的对应关系）
- [[skills-auto-evolution]]（Skills 的自我进化与 wiki 的增量积累是同一模式）
- [[knowledge-compilation-pattern]]（知识编译模式 vs RAG 的技术路径对比）
