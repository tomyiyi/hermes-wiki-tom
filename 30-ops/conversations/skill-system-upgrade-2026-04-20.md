---
title: Skill 系统升级 — Wiki 知识转化为 Skills
created: 2026-04-20
updated: 2026-04-20
layer: conversations
type: summary
certainty: confirmed
participants: [human, Hermes]
outcome: |
  建立了双通道知识流入机制：Wiki 持久化 + Skill 行为改变。
  从 hermes-wiki synthesis 层提取了3个核心 Skill：
  skill-authoring、wiki-knowledge-channel、wiki-ingest-flow。
key_insights:
  - "知识存入 Wiki 后必须同步提取为 Skill，否则不会改变行为"
  - "Skill 三层模型：方法论层（人工）、流程层（人工+Agent）、执行层（Agent自动）"
  - "Patch > Overwrite：更新 Skill 用打补丁而非覆写"
  - "每周 Cron job 名为 Weekly Nudge，log 里有但 cron list 为空，需重建"
---

# Skill 系统升级对话

## 背景

用户重启系统后发现 cron job 没建成功（log 里有记录但 cronjob list 为空）。
用户问："如何将别人好的东西学习到你的系统里面？"

## 核心问题诊断

Hermes Agent 的知识管理有两条通道：
1. **Wiki 通道**（持久化）：URL/文章 → Ingest → Summary → Synthesis
2. **Skill 通道**（行为改变）：从 wiki 提取 → 写成 Skill 文件 → 下次自动调用

**问题：只做了通道1，没做通道2。**

读了大量 Hermes Agent / Karpathy LLM Wiki 文章，知识存进了 wiki，但我的行为没有任何改变。

## 解决方案

从 hermes-wiki synthesis 层提取3个核心 Skill：

### 1. skill-authoring
从 `概念/skills-auto-evolution.md` 提取：
- 三层模型：方法论层（人工）/ 流程层（人工+Agent）/ 执行层（Agent自动）
- 生成 Skill 的触发条件
- Patch > Overwrite 原则
- agentskills.io 格式

### 2. wiki-knowledge-channel
从 `概念/karpathy-llm-wiki-methodology.md` 提取：
- 两条通道的定义
- Channel 2 (Skill) 的检查清单
- 关键洞察："不在 Skill 里的知识不会改变行为"

### 3. wiki-ingest-flow
从 `synthesis/knowledge-compilation-pattern.md` + `concepts/hermes-agent-core-concepts.md` 提取：
- Karpathy LLM Wiki 操作流程
- 每个步骤的具体命令
- **两步强制检查**：ingest 完成后必须问"需要提取为 Skill 吗？"

## 发现的其他问题

- WIKI_PATH 环境变量未设置（llm-wiki skill 指向 ~/wiki，实际在 ~/Desktop/hermes-wiki）
- .env 受保护无法写入，通过记忆机制处理
- Weekly Nudge cron job 有 log 记录但实际不存在，需重建

## 技术细节

- 3个新 Skill 写入 `~/.hermes/skills/software-development/`
- WIKI_PATH 通过记忆机制处理（手动设置需改 ~/.hermes/.env）
- 所有变更记录到 wiki log.md

## 相关 wiki 页面
- [[概念/skills-auto-evolution]]
- [[概念/karpathy-llm-wiki-methodology]]
- [[synthesis/knowledge-compilation-pattern]]
- [[concepts/hermes-agent-core-concepts]]
