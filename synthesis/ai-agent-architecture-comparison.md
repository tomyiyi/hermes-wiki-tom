---
title: AI Agent 架构对比
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: comparison
tags: [AI-Agent, hermes, openclaw, claude-code, architecture, memory, skills, self-evolution]
sources:
  - processed/hermes-agent.md
  - comparisons/hermes-vs-openclaw-vs-claude-code.md
derived_from:
  - Hermes Agent 评测笔记
  - AI Agent 对比：Hermes vs OpenClaw vs Claude Code
---

# AI Agent 架构对比

> Hermes vs OpenClaw vs Claude Code 三者代表三条不同的 Agent 进化路线。

## 一句话定位

| 产品 | 架构路线 | 进化方式 | 记忆机制 |
|------|---------|---------|---------|
| Claude Code | 会话级工具 | 无（靠版本更新）| 会话内 | 
| OpenClaw | 多 Agent 协作 | 人工配置 | 记事本式持久 |
| Hermes | 单一自进化 | 使用中自动 | 四层记忆+心智建模 |

## 核心维度对比

| 维度 | Claude Code | OpenClaw | Hermes |
|------|------------|----------|--------|
| 记忆 | 会话内 | 文件持久化 | 四层（含 Honcho）|
| Skills | 人工编写 | 人工编写 | **自动生成+迭代** |
| 进化 | 无 | 无 | **闭合学习循环** |
| 平台 | 终端 | 多平台 | 15+ 平台 |
| 执行环境 | 本地 | 本地/Docker | 6种含 Serverless |
| 数据存储 | 云端 | 本地 | 本地 |
| 成本 | 订阅制 | 自托管 | <$1/月 |

## 记忆系统深度对比

| 层 | Claude Code | OpenClaw | Hermes |
|----|------------|---------|--------|
| L1 | 会话上下文 | 持久文件 | MEMORY.md + USER.md（常驻）|
| L2 | — | — | 会话归档（SQLite+全文索引）|
| L3 | — | — | 技能文件（按需调入）|
| L4 | — | — | Honcho（用户心智建模）|

**关键洞察**：OpenClaw 第15天 = 第1天（无自我进化）；Hermes 越用越懂用户。

## 学习循环触发条件（Hermes）

满足任一即触发 Skill 自生成：
- 工具调用超过 5 次
- 中途出错并自我修复
- 用户做过纠正
- 走了非显而易见但有效的路径

## Skills 三层模型

| 层级 | 编写者 | 内容 | 可替代性 |
|------|--------|------|---------|
| 方法论层 | 人工 | 价值判断、质量标准 | 不可替代 |
| 流程层 | 人工+Agent | 大框架人定，细节优化 | 半可替代 |
| 执行层 | Agent自动 | 工具选择、错误处理 | 完全可替代 |

## Auxiliary Models（Hermes 独有）

主模型（昂贵）处理对话，侧任务自动切换 Gemini Flash（便宜）：

| 侧任务 | 模型 |
|--------|------|
| 图像分析 | Gemini Flash |
| 网页提取 | Gemini Flash |
| Skill 匹配 | Gemini Flash |
| 记忆管理 | Gemini Flash |

## 数据主权

| | Claude | OpenClaw | Hermes |
|--|--------|---------|--------|
| 存储位置 | 云端（Anthropic）| 本地 | 本地 |
| 隐私风险 | 需信任厂商 | 无 | 无 |

## 相关

- [[hermes-agent-core-concepts]] — Hermes 核心概念
- [[hermes-vs-openclaw-vs-claude-code]] — 详细对比
- [[hermes-wechat-integration]] — 15+平台接入矩阵、飞书重点、MMX-CLI 全模态扩展
- [[knowledge-management-ai-era]] — Wiki vs RAG vs Graphify 三路对比
- [[knowledge-compilation-pattern]] — 知识编译 vs RAG 路线对比
