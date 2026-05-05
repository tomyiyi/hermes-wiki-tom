---
title: CodeBuddy 能力增强记录
created: 2026-04-26
updated: 2026-04-26
layer: synthesis
type: concept
tags: [codebuddy,skill,enhancement]
sources: []
synced_from: "CodeBuddy"
---

# CodeBuddy 能力增强记录

## 背景

基于 hermes-wiki 中的知识管理方法论和 CodeBuddy 最佳实践，对 CodeBuddy 进行了系统性增强。

## 增强内容

### 1. 记忆系统增强

新增记忆分类：user_profile、project_context、knowledge_base、preferences、action_items

### 2. 上下文能力增强

创建项目配置文件：.codebuddy/CONFIG.md、rules/coding-standards.md、skills/README.md

### 3. 阅读能力增强

多格式支持、自动提取摘要、阅读后同步记忆体

### 4. Wiki 双向同步机制

创建 scripts/wiki_sync.py 和 sync-protocol.md

## 创建的 Skills

- knowledge-to-behavior.md：双通道机制
- context-manager.md：上下文管理
- wiki-reader.md：Wiki 阅读助手
- codebuddy-master.md：核心整合 Skill

## 创建的工具

wiki_lint.py：健康检查工具（孤立页面、过时内容、断裂引用检测）

## 关键洞察

1. 知识不在 Skill 里就不会改变行为
2. 上下文窗口是最重要的资源
3. 验证优先
