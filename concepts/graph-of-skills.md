---
title: "Graph of Skills (GoS)"
created: 2026-04-20
updated: 2026-04-20
layer: summary
type: concept
tags: [knowledge-base, skills, graph, retrieval, mcp, karpathy, dependency-aware]
sources: [raw/articles/graph-of-skills-2026-04-20.md]
derived_from: []
---

# Graph of Skills (GoS)

## 一句话

> David Liu 等人开发的**技能图谱检索系统**：把一堆 `SKILL.md` 构建成依赖图，查询时只返回最相关的技能及其前置依赖，避免把整个技能库塞进 context。

## 核心机制：Seed → Merge → Rerank → Return

| 阶段 | 方法 | 作用 |
|------|------|------|
| **Seed** | 语义相似度（embedding）+ 词元精确匹配 | 双通道召回候选 |
| **Merge** | 合并两个候选池 | 融合不同检索逻辑 |
| **Rerank** | 基于图的结构性重排（PPR等）| 利用依赖关系筛选 |
| **Return** | 截断输出 + 依赖_bundle | 只返回 agent 真的需要的 |

## 关键数据

- Token 降低最高 **56×**（ALFWorld, Claude Sonnet 4.5）vs 全量塞入
- 奖励提升显著（SkillsBench + Graph of Skills > 其他所有方法）
- 支持 MCP server 导出，接入 Claude Code

## 与我的系统的关系

**已对标：**
- `hermes-wiki` 的 `skill-authoring` + `knowledge-to-behavior` = 两通道机制 ✅
- `synthesis/knowledge-compilation-pattern` = 知识编译思路 ✅

**值得借鉴的：**
- **依赖感知的技能检索**：不是返回相似技能，而是返回「这个技能 + 它的前置依赖」
- 类比：Hermes Agent 的 Skills 自进化触发条件（>5次工具调用等）也是一种隐式依赖图
- Graph of Skills 的检索 pipeline（seed/merge/rerank/return）可以作为我检索 skills 时的方法论

## 关联

- [[graphify]] — 代码领域的知识图谱（Token降至1/72）
- [[karpathy-llm-wiki]] — 文档/知识编译（同属 Karpathy 知识复利体系）
- [[synthesis/knowledge-compilation-pattern]] — RAG vs 知识编译对比
- [[概念/skills-auto-evolution]] — Hermes Skills 自动进化机制
