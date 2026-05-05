---
title: Graphify
created: 2026-04-11
updated: 2026-04-11
layer: summary
type: concept
tags: [knowledge-base, graphify, token-reduction, ast, tree-sitter, mcp]
sources: [raw/articles/graphify-token-reduction-1-72.md]
---

# Graphify

## 是什么
AI 编码助手的知识图谱工具，将代码库编译成持久化图谱，Token 消耗降至 1/72。

## 核心特点
- **双通道提取**：AST 解析（零 Token）+ Claude Vision 多模态语义提取
- **零 Token 建图**：代码结构用 Tree-sitter 本地解析，不走 LLM
- **MCP 服务器导出**：可接入 Cursor、Windsurf 等支持 MCP 的 AI IDE
- **--watch 模式**：文件变更自动增量更新

## 关键机制
- **God Nodes**：被大量模块依赖的核心节点，评估技术债
- **三种关系标签**：EXTRACTED（100%事实）、INFERRED（概率）、AMBIGUOUS（需人工）
- **Leiden 聚类**：纯图拓扑，不走向量嵌入

## 与 [[karpathy-llm-wiki]] 的关系
两者都是 Karpathy"知识编译"理论的应用：
- Graphify → 代码领域的知识编译
- [[karpathy-llm-wiki]] → 文档/知识领域的知识编译

## 相关工具
- [[obsidian]]（见 summary/entities/obsidian.md）
- MCP servers（待补充具体页面）

## 适用场景
- 中大型代码项目（文件越多收益越大）
- 需要架构分析和技术债评估
- 需要跨 AI 工具共享代码认知
