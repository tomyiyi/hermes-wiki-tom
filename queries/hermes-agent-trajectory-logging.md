---
title: "Hermes Agent 轨迹记录与 Learning Loop 机制"
created: 2026-04-13
updated: 2026-04-13
layer: query
type: query
tags: [AI-Agent, hermes, learning-loop, memory, Nous-Research]
sources: [concepts/hermes-agent-core-concepts.md, raw/articles/simin-hermes-architecture-business-model.md]
status: open
priority: high
owner: hermes
---

# Hermes Agent 轨迹记录与 Learning Loop 机制

## 核心问题

Hermes 的"越用越懂你"依赖 Learning Loop，但轨迹记录的具体机制不清晰。

## 具体问题

### Q1: trajectory 数据存在哪？
- 文件路径是什么？
- 格式是 JSON 还是 SQLite？
- 数据保留多久？何时清理？

### Q2: Learning Loop 的触发时机
- 每次对话结束都会更新 trajectory？
- 还是只有特定操作才记录？
- 如何影响下一次对话的上下文？

### Q3: 四层记忆与 trajectory 的关系
- L1/L2/L3 的数据来源是否都依赖 trajectory？
- 还是 L4（心智模型）是独立机制？
- 四层如何协同工作？

## 验证方法

1. 搜索 hermes 代码中 `trajectory`、`learning`、`loop` 相关文件
2. 检查 `~/.hermes/` 目录结构
3. 对比两次对话，看上下文是否有明显差异

## 相关
- [[concepts/hermes-agent-core-concepts]] — 四层记忆架构
- [[概念/hermes-four-layer-memory-architecture]] — 更详细的记忆拆解
- [[hermes-vs-openclaw-vs-claude-code]] — Learning Loop 对比
