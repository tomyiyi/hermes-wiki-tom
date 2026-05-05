---
title: "Hermes 智能体开发工作流完整指南 v2.1"
description: "gstack + Hermes 融合的 8 阶段完整工程环，114 个 Skills，完整 Skill 地图"
source: Hermes hermes-two 内部文档 / 用户提供
date: 2026-04-14
tags: [Hermes, workflow, gstack, skills, engineering, Auto_Absorbed]
created: 2026-04-14
value_classification: 实操指南
---

# Hermes 智能体开发工作流完整指南 v2.1

> 版本：v2.1 | 更新：2026-04-14
> 适用：Hermes hermes-two (Claude Code on Mac mini)
> 核心：gstack + Hermes 融合的 8 阶段完整工程环

## 一、整体架构

```text
┌─────────────────────────────────────────────────────────┐
│                 Hermes Workflow Ring v2.1               │
│                                                         │
│   Think ──→ Plan ──→ Build ──→ Review ──→ Ship          │
│     │                                          │        │
│     │                                    Deploy│        │
│     │                                          ↓        │
│     │              Reflect ←── QA ←────────────────     │
│     │                                          ↑        │
│     └──────────────────────────────────────────┘        │
│                                                         │
│   ══════════ Hotfix 快速闭环（任意阶段触发）═════════   │
└─────────────────────────────────────────────────────────┘
```
**8 阶段完整环：** Think / Plan / Build / Review / Ship / Deploy / QA / Reflect
**2 个变体分支：** Hotfix（快速闭环）/ Upgrade（标准环）

## 二、逐阶段详解

### 🔵 Stage 1 · Think
**目标：** 重新定义问题，找到正确的方向
**主 Skill：** `hermes-office-hours`
**触发词：** "brainstorm"、"idea"、"help me think through"、"值得做吗"
**产出：** 设计文档（DESIGN.md）
**铁律：** 不写代码，不做技术选型，先问"为什么"再问"怎么做"
**gstack 对应：** `/office-hours`（6 个强制问题暴露需求真相）

### 🟢 Stage 2 · Plan
**目标：** 锁定架构，拆任务，定验收标准
**主 Skill：** `plan` + `writing-plans`
**辅助：** `systematic-debugging`（遇未知先调查）
**触发词：** "plan"、"规划"、"拆任务"、"怎么做"
**产出：** `.hermes/plans/YYYY-MM-DD_<slug>.md`
**铁律：** 先读现有代码，任务拆到 2 小时内，验收标准明确
**gstack 对应：** `/plan-ceo-review` + `/plan-eng-review`

### 🟡 Stage 3 · Build
**目标：** 按计划写代码
**主 Skill：** `test-driven-development` + `subagent-driven-development`
**触发词：** "build"、"写代码"、"实现"、"开始做"
**产出：** 通过测试的代码
**铁律：** 不偏离 Plan，不跳过测试，遇未知先调查
**gstack 对应：** `Build` + `/design-review`

### 🟠 Stage 4 · Review
**目标：** 代码质量门禁，找出问题
**主 Skill：** `review`（Scope Drift + Plan Completion）+ `requesting-code-review`
**辅助：** `systematic-debugging`
**触发词：** "review"、"PR review"、"代码审查"、"检查 diff"
**产出：** 审查报告 + PR 创建
**审查标准：**
- P0（Critical）：安全漏洞、数据丢失、核心功能 broken
- P1（High）：性能问题、代码重复、缺少测试
- P2（Medium）：代码风格
**gstack 对应：** `/review`（Scope Drift Detection + Greptile 集成）

### 🔴 Stage 5 · Ship
**目标：** 代码合并 + 文档同步
**主 Skill：** `hermes-ship`
**辅助：** `document-release`
**触发词：** "ship"、"发布"、"deploy"、"push"
**产出：** PR/MR + 更新的文档
**铁律：** Ship 完成 = hermes-ship（代码+PR）+ document-release（文档同步），**缺一不算完成**
**gstack 对应：** `/ship`

### 🟣 Stage 6 · Deploy
**目标：** 验证部署成功 + 监控健康
**主 Skill：** `hermes-canary`
**辅助：** `hermes-rollback`
**触发词：** "deploy"、"上线"、"检查状态"
**流程：**
部署完成 → hermes-canary 检查
         → ✅ 健康 → 进入 QA
         → ❌ 异常 → hermes-rollback → 复盘
**告警规则：**
- HTTP 状态 ≠ 2xx/3xx → 立即告警
- 响应时间 > 2x 基准 → 降级告警
- 新出现错误日志 → 视严重程度决定
**gstack 对应：** `/canary` + `/land-and-deploy`

### 🔵 Stage 7 · QA（可选）
**目标：** 真实浏览器遍历测试，发现自动化测试遗漏的边缘问题
**主 Skill：** `qa`
**触发词：** "qa"、"QA"、"测试"、"找 bug"、"test this site"

### ⚪ Stage 8 · Reflect
**目标：** 沉淀经验，持续改进
**主 Skill：** `hermes-retro` + `autonomous-learning`
**辅助：** `memory-iteratpr`
**触发：** Ship+Deploy 完成后自动，或每周日 cron
**产出：** 更新的知识库 + Skill 补丁
**gstack 对应：** `/retro`

## 三、Hotfix 快速闭环
**触发：** 线上发现 Bug，需要紧急修复
发现 Bug → hermes-canary 确认 → systematic-debugging 调查根因 → 紧急 Plan → Build → Review → Ship → Deploy → 48h 内 Reflect 回主环

## 四、gstack 协同关系
gstack（`~/.claude/skills/gstack/`）与 Hermes 的分工：
| 场景 | 调用 Hermes | 调用 gstack |
|---|---|---|
| 系统管理 / 记忆任务 | ✅ Hermes 原生 skills | — |
| git repo 项目级开发 | ✅ Hermes workflow skills | ✅ gstack 补充（checklist、greptile） |
| Office 文档处理 | ✅ `office-xlsx` | — |
| 浏览器测试 | ✅ Playwright MCP | ✅ gstack browse（更成熟） |
| 飞书消息 | ✅ send_message | — |

