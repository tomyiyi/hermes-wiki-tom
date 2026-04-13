---
title: Graphify：给 AI 编码助手装上知识库，Token 消耗降到 1/72
author: 寂寞的熊猫
date: 2026-04-10
source: 微信文章
url: (internal document)
created: 2026-04-11
updated: 2026-04-11
layer: raw
type: summary
tags: [knowledge-base, graphify, token-reduction]
archived: false
---

# Graphify：给 AI 编码助手装上知识库，Token 消耗降到 1/72

## 核心信息

- Graphify v3：将任意文件夹（代码+文档+图片）编译成持久化知识图谱
- 支持 Claude Code、Codex、OpenCode、OpenClaw、Trae、Factory Droid
- Token 消耗降至约 1/72（52 文件混合语料库基准测试）
- 零 Token 用 Tree-sitter 本地解析代码 AST
- 支持 8 种导出格式，包括 Obsidian Vault、Neo4j、MCP Server

## 核心机制

### 双通道提取
1. **第一通道：AST 解析**（零 Token）
   - Tree-sitter 支持 20 种编程语言
   - 提取类/函数/接口作为节点
   - import/require 关系作为 IMPORTS 边
   - 跨文件调用栈作为 CALLS 边
   - 特殊注释（# TODO: / # HACK: / # WHY:）生成 rationale_for 节点

2. **第二通道：多模态语义提取**
   - PDF、架构图、会议纪要、截图
   - Claude Vision 子智能体并行处理
   - 提取概念、实体和设计原理
   - 附带置信度分数

### 三种关系标签
- EXTRACTED：AST 解析，100% 事实
- INFERRED：LLM 推断，概率假设
- AMBIGUOUS：证据不足，需人工审查

### Leiden 聚类
- 纯图拓扑聚类，不走向量嵌入
- 自动发现业务模块群落
- 识别上帝节点（God Nodes）——被大量模块依赖的核心节点
- 发现意外的深层耦合

## 导出格式
| 格式 | 用途 |
|------|------|
| graph.html | 浏览器交互图 |
| GRAPH_REPORT.md | 纯文本架构审计报告 |
| graph.json | 序列化图谱，跨会话持久化 |
| --obsidian | Obsidian Vault |
| --wiki | Wikipedia 风格离线知识库 |
| --neo4j | Cypher 语句或直接推送 Neo4j |
| --graphml | Gephi/yEd 格式 |
| --svg | 静态矢量图 |
| --mcp | MCP 服务器供其他 AI IDE 实时调用 |

## 常驻机制
- `graphify claude install` 拦截 AI 工具调用链
- 强制 AI 先查图谱报告再搜原始文件
- `--watch` 模式监听文件变更，增量更新
- Git hooks 自动重建图谱

## 隐私模型
- 代码 AST 解析完全本地运行，零网络请求
- 只有文档/图片语义提取发到 Claude API
- 零遥测，不收集使用数据

## Token 消耗对比
| 语料规模 | 文件数 | Token 变化 |
|----------|--------|------------|
| Karpathy 代码仓库 + 5 篇论文 + 4 张图 | 52 | 降至约 1/72 |
| 小型项目 | 4 | 降至约 1/5 |
| 极小项目 | 6 | 基本持平 |
