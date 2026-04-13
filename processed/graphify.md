---
title: Graphify — Processed Notes
created: 2026-04-11
updated: 2026-04-11
layer: processed
type: concept
tags: [knowledge-base, graphify, token-reduction, ast, tree-sitter, mcp]
sources: [raw/articles/graphify-token-reduction-1-72.md]
derived_from: []
---

# Graphify Processed Notes

## 划重点

### Token 降低数据（关键卖点）
- 52 文件混合语料：降至 1/72
- 小型项目（4 文件）：降至 1/5
- 极小项目（6 文件）：基本持平

→ **文件越多收益越大**，极小项目不值得用

### 双通道提取（核心创新）
- 通道一：AST 解析（零 Token，Tree-sitter，20 种语言）
- 通道二：Claude Vision 多模态（PDF、架构图、截图）

→ 纯代码结构不需要 LLM，只把语义内容发给 API

### 三种关系标签
| 标签 | 性质 | 置信度 |
|------|------|--------|
| EXTRACTED | AST 解析，100% 事实 | 最高 |
| INFERRED | LLM 推断 | 概率性 |
| AMBIGUOUS | 证据不足 | 需人工 |

→ 使用时要区分，不能把推断当事实

### Leiden 聚类
- 纯图拓扑，不走向量嵌入
- 自动发现 God Nodes（被大量依赖的核心节点）
- 可发现意外深层耦合

### 导出格式优先级
1. `--mcp` → 其他 AI IDE 实时调用（最有价值）
2. `--obsidian` → 直接进 Obsidian 图谱
3. `--neo4j` → 复杂查询场景

### 常驻机制
- `--watch` 增量更新，不是每次全量重建
- Git hooks 触发自动重建

## 待验证
- Token 1/72 数据来源：52 文件混合语料，具体场景是否适用需实测
- Claude Vision 子智能体并行处理 → 需要多 API key 或并发配置
