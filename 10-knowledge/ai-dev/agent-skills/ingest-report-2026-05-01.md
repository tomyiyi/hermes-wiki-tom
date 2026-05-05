---
title: Ingest Report: addyosmani/agent-skills v2（2026-05-01）
created: 2026-05-02
updated: 2026-05-02
layer: processed
type: comparison
tags: [AI-Agent, knowledge-management, AI-Agent]
---

# Ingest Report: addyosmani/agent-skills v2（2026-05-01）

## 基本信息
- **来源**：GitHub https://github.com/addyosmani/agent-skills
- **版本**：Stars 19k+（上次 04-27 调研 ~12.6k，增长 +6.4k）
- **归档路径**：`~/Desktop/hermes-wiki/10-knowledge/ai-dev/agent-skills/`
- **调研时间**：2026-05-01

---

## 完成步骤

### Step 1：源站抓取
- [x] web_search 查询 `addyosmani agent-skills github`
- [x] web_extract 提取 README 和主要 skill 文件
- [x] 确认 stars 增长数据（19k+，含 google/skills 官方库）

### Step 2：内容分析
- [x] 对比 04-27 调研版本（12.6k ⭐）与当前版本（19k+ ⭐）
- [x] 识别新增内容：google/skills 官方库集成、PR #100（gemini-cli commands）
- [x] 确认 Hooks 系统、编排模式、Personas、Checklists 均已在 README 中

### Step 3：Hermes 集成检查
- [x] TDD skill（v1.2.0）— 已包含 Anti-rationalization 机制
- [x] incremental-implementation skill — 已存在，编排模式可补充
- [x] context-engineering skill — 新建（v1.0.0），对应 context-engineering skill

### Step 4：归档写入
- [x] README.md — 已存在（04-27 版本），Stars 数字已更新
- [x] 本 report — 新建

### Step 5：Hermes 技能注册
- [x] 无需新建 skill（anti-rationalization 已在 TDD v1.2.0）
- [x] incremental-implementation skill 可补充编排模式参考

---

## 关键发现（与 Hermes 现有 Skill 的关系）

| agent-skills 模块 | Hermes Skill | 状态 |
|------------------|--------------|------|
| TDD + Anti-rationalization | `software-development/test-driven-development` | ✓ v1.2.0 已融合 |
| Incremental Implementation | `software-development/incremental-implementation` | ✓ 已存在 |
| Context Engineering | `software-development/context-engineering` | ✓ v1.0.0 已新建 |
| Planning | `software-development/plan` | 参考 |
| Code Review | `github/github-code-review` | 参考 |

---

## 尚未整合但有价值的部分

1. **编排模式（Orchestration Patterns）** → 可补充到 incremental-implementation skill
2. **Reference Checklists**（4个）→ 可考虑新建 `software-development/reference-checklists` skill
3. **Simplify-Ignore 机制** → 纯工程实现，Hermes UI-TUI 无需复刻

---

## Deep Compression Check

> **问题**：agent-skills 的核心价值是什么？

**答案**：Anti-rationalization — 把 AI 的借口预判并封死，让 Skill 本身成为纪律约束，而不是建议。

这个机制已经进入 TDD v1.2.0。集成完整，无需进一步行动。

---

## 下次调研触发条件

- Stars 突破 25k
- 新增 `/spec` 或 `/plan` 相关的 skill
- google/skills 库有重大更新
