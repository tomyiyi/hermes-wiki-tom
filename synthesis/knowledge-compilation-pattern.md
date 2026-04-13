---
title: 知识编译模式 — 从 RAG 到持久化知识图谱
created: 2026-04-11
updated: 2026-04-11
layer: synthesis
type: concept
tags: [knowledge-base, rag, graphify, karpathy, compounding-knowledge, token-reduction]
sources: [raw/articles/graphify-token-reduction-1-72.md, raw/articles/karpathy-llm-wiki-personal-knowledge-base.md, raw/articles/karpathy-obsidian-claudian-tutorial.md]
derived_from: [summary/concepts/graphify.md, summary/concepts/karpathy-llm-wiki.md, summary/concepts/knowledge-management-principles.md]
---

# 知识编译模式

## 核心命题
**RAG 每次从零检索，知识编译让知识滚雪球。**

两篇文章从不同角度论证了同一件事：
- Graphify → 代码领域的知识编译（Token 降至 1/72）
- Karpathy LLM Wiki → 文档/知识领域的知识编译（复利增长）

## RAG vs 知识编译

| | RAG | 知识编译 |
|--|-----|---------|
| 查询方式 | 每次从零检索 | 先查已编译的知识 |
| 知识积累 | 无，每次独立 | 有，复利增长 |
| Token 消耗 | 高 | 低（Graphify 降至 1/72） |
| 认知持久性 | 无 | 有，跨会话 |
| 适用场景 | 简单问答 | 复杂推理、架构分析 |

## 两条技术路径

### 路径一：Graphify（图拓扑）
- **输入**：代码库 + 文档 + 图片
- **处理**：AST 解析（零 Token）+ Claude Vision 多模态
- **输出**：持久化图谱，支持 MCP 实时调用
- **代表场景**：中大型代码项目、架构分析、技术债评估

### 路径二：Karpathy Wiki（层级结构）
- **输入**：文章、对话、笔记
- **处理**：AI 阅读 → 摘要 → 判断位置 → 更新链接
- **输出**：层级 Wiki，schema 驱动
- **代表场景**：个人知识管理、内容创作者工作流

## 共鸣：五层架构

Graphify 文章中提到代码库知识编译，Karpathy 文章中扩展了五层架构：
```
输入层 → 知识层 → 技能层 → 行动层 → 产出层
```

这个结构和 Graphify 的双通道提取异曲同工：
- Graphify **结构层**（AST）= 知识编译的"硬"一面
- Wiki **语义层**（LLM 摘要）= 知识编译的"软"一面

## 实际应用分层（与当前 Hermes Wiki 对应）

| Layer | 对应内容 | 状态 |
|-------|---------|------|
| raw/ | 原始文章，只读存档 | ✓ 已建立 |
| processed/ | 划重点、批注、整理 | ✓ 刚填充 |
| summary/ | 单篇总结，要点提炼 | ✓ 已建立 |
| synthesis/ | 跨篇综合分析 | ✓ 刚填充 |
| action/ | 导致具体任务的阅读 | 待填充 |

## 开放问题
1. **对话存档**：AI 对话本身是否算 raw source？Karpathy 把它列为 Notes/Conversation 层，Hermes Wiki 尚未对应
2. **token 阈值**：Graphify 实测 1/72 对哪些项目成立？多小算"不值得用"？
3. **MCP 集成**：Graphify MCP 导出是否能直接接入 Hermes？

## 结论
知识编译 = 把每次 AI 使用变成长期投资。RAG 是租房，知识编译是买房。
