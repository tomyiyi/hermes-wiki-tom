---
title: Agent Skills by Google (addyosmani)
created: 2026-05-02
updated: 2026-05-02
layer: processed
type: entity
tags: [AI-Agent, knowledge-management, AI-Agent]
---

# Agent Skills by Google (addyosmani)

## Source

- GitHub: https://github.com/addyosmani/agent-skills
- Stars: **19k+**（2026-05-01 调研，含 google/skills 官方库；2026-04-27 初调 ~12.6k）
- Author: Addy Osmani (Google Gemini 团队主管)
- License: MIT
- 最新更新：2026-04-28（PR #100：gemini-cli commands）

## 核心概念

把资深工程师的工作流和开发规范封装成 Skills 技能包，让 AI 在每个开发阶段都能保持一致的高标准。底层源自《Software Engineering at Google》。

## 开发生命周期

```
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
  /spec   /plan   /build   /test   /review   /ship
```

## 7 个 Slash 命令

| 命令 | 用途 | 原则 |
|------|------|------|
| `/spec` | 定义要做什么 | 先规范再代码 |
| `/plan` | 规划如何做 | 小而原子化任务 |
| `/build` | 增量构建 | 一次一块 |
| `/test` | 证明它能工作 | 测试即证据 |
| `/review` | 评审后再合并 | 提升代码健康度 |
| `/code-simplify` | 简化代码 | 清晰优于巧妙 |
| `/ship` | 发布到生产 | 更快反而更安全 |

## 20 个 Skill

### Define - 澄清做什么
- `idea-refine` — 粗糙概念需要探索时
- `spec-driven-development` — 新项目/功能启动时

### Plan - 拆分任务
- `planning-and-task-breakdown` — 有规范但需要可执行单元时

### Build - 写代码
- `incremental-implementation` — 任何涉及 >1 文件的改动
- `test-driven-development` — 实现逻辑或修复 bug 时
- `context-engineering` — Session 启动、任务切换、质量下降时
- `source-driven-development` — 需要权威的、引用源码的代码时
- `frontend-ui-engineering` — 构建用户界面时
- `api-and-interface-design` — 设计 API 或公共接口时

### Verify - 证明能工作
- `browser-testing-with-devtools` — 构建/调试浏览器代码时
- `debugging-and-error-recovery` — 测试失败、构建破坏时

### Review - 质量门禁
- `code-review-and-quality` — 任何合并前的改动
- `code-simplification` — 代码能工作但难维护时
- `security-and-hardening` — 用户输入、认证、数据存储时
- `performance-optimization` — 有性能要求时

### Ship - 部署
- `git-workflow-and-versioning` — 任何代码改动（始终）
- `ci-cd-and-automation` — 构建/部署流水线改动时
- `deprecation-and-migration` — 移除旧系统时
- `documentation-and-adrs` — 架构决策时
- `shipping-and-launch` — 部署到生产环境时

## 3 个 Agent 人设

| Agent | 角色 | 标准 |
|-------|------|------|
| `code-reviewer` | 资深 Staff 工程师 | "Staff 工程师会批准这个吗？" |
| `test-engineer` | QA 专家 | Prove-It 模式，覆盖率分析 |
| `security-auditor` | 安全工程师 | OWASP 评估，威胁建模 |

## Skill Anatomy（Skill 标准结构）

```
SKILL.md
├── Frontmatter (name, description)
├── Overview          → 这个 skill 做什么
├── When to Use       → 触发条件
├── Process           → 逐步工作流
├── Rationalizations  → 借口 + 反驳（核心！）
├── Red Flags         → 出错的信号
└── Verification      → 证据要求
```

**关键设计：**
- **Process, not prose** — 带步骤、检查点、退出标准的工作流
- **Anti-rationalization** — 借口与反驳表格
- **Verification non-negotiable** — 必须有证据要求
- **Progressive disclosure** — 引用文件只在需要时加载

## 新增：Hooks 系统（Anti-Rationalization 自动化）

`hooks/` 目录实现"让 AI 看到借口就想起反驳"的自动化机制：

### session-start hook
- 每次新 session 自动注入 `using-agent-skills` meta-skill
- AI 每次启动都能看到 skill 触发流程图
- 实现：每次会话自动激活 skill 发现流程

### simplify-ignore hook（最关键）
- 在代码中插入 `simplify-ignore-start/end` 标记块
- Hook 在 Read 时将标记块替换为 `BLOCK_<hash>` 占位符，AI 看不到复杂代码
- 在 Edit/Write 后展开占位符还原，并重新过滤
- Session 结束时自动恢复原始文件
- **效果**：AI 无法修改受保护的代码块（如 Anti-Rationalization 段落），必须先说服人类

### sdd-cache hook（Structured Data Debugging）
- 缓存结构化调试数据，减少重复信息抓取

## 新增：编排模式（Orchestration Patterns）

### 5 个推荐模式

| 模式 | 适用场景 | 成本 |
|------|---------|------|
| 1. 直接调用 | 单一视角看单一产物 | 最低 |
| 2. 单人 slash command | 同一组合重复执行 | 同直接调用 |
| 3. **并行 fan-out + merge** | `/ship` = code-reviewer + security-auditor + test-engineer 并行，合并 go/no-go | N 并行上下文 + 1 merge |
| 4. 顺序 pipeline | 用户驱动 slash 命令序列（DEFINE→PLAN→BUILD→VERIFY→REVIEW→SHIP）| 每步 1 上下文 |
| 5. 研究隔离 | 子代理读大量材料 → 返回摘要 → 主上下文保持干净 | 1 隔离上下文 |

### `/ship` 是唯一认可的 fan-out 编排
```
/ship
  ├── (parallel) code-reviewer    → review report
  ├── (parallel) security-auditor → audit report
  └── (parallel) test-engineer    → coverage report
                  ↓
        merge phase (main agent)
                  ↓
        go/no-go decision + rollback plan
```
**前提条件**：子任务相互独立（无共享状态），每个子代理有自己的上下文窗口，合并步骤足够小。

### 4 个反模式（不要做）

| 反模式 | 描述 |
|--------|------|
| A. Router persona | "元编排"角色决定调用谁 → 信息丢失 × 2 |
| B. Persona 调用 Persona | code-reviewer 内部调用 security-auditor → 违反单一视角原则 |
| C. 顺序编排器 | AI 代理顺序调用 /spec → /plan → /build → ... → 双重 token 成本 + 丢失人工检查点 |
| D. 深 persona 树 | /ship → pre-ship-coordinator → quality-coordinator → code-reviewer → 层级无决策价值 |

## 新增：Agent Personas（3 个专家角色）

| Persona | 角色 | 视角 |
|---------|------|------|
| `code-reviewer` | Staff 工程师 | 五轴评审，"Staff 工程师会批准吗？" |
| `test-engineer` | QA 专家 | 测试策略、覆盖率分析、Prove-It 模式 |
| `security-auditor` | 安全工程师 | 漏洞检测、OWASP 评估、威胁建模 |

**编排规则**：用户（或 slash command）是编排者，Persona 不调用 Persona，Skill 是 Persona 工作流内的强制性跳转。

## 新增：Reference Checklists（4 个参考清单）

- `testing-patterns.md` — 测试结构/命名/模拟/React/API/E2E 示例 + 反模式
- `security-checklist.md` — 提交前检查、认证、输入验证、头部、CORS、OWASP Top 10
- `performance-checklist.md` — Core Web Vitals 目标、前后端清单、测量命令
- `accessibility-checklist.md` — 键盘导航、屏幕阅读器、视觉设计、ARIA、测试工具

## 新增：Simplify-Ignore 机制详解

### 原理
在源代码中用特殊标记包围需要保护的段落：
```python
def complex_auth_flow():
    # simplify-ignore-start: 不要简化这个逻辑，它处理竞态条件
    if not token:
        if not refresh_token:
            raise AuthError("No credentials")
        token = refresh(refresh_token)
    # simplify-ignore-end
    return validate(token)
```

### 效果
- AI 读文件时看到的是 `BLOCK_<hash>: 不要简化这个逻辑...`
- AI 尝试编辑时，占位符被替换回原始代码
- AI 无法在不经过人类明确批准的情况下修改受保护段落
- **不是阻止 AI 看到复杂代码**，而是阻止 AI 在没有人类认可的情况下"简化"掉关键逻辑

## 与 Hermes Skill 体系的对应

| Agent Skills | Hermes Skill |
|--------------|--------------|
| TDD | `software-development/test-driven-development` ✓ 已更新 v1.2.0 |
| Incremental Implementation | `software-development/incremental-implementation` ✓ 新建 |
| Code Review | `github/github-code-review` 参考 |
| Planning | `software-development/plan` 参考 |
| Debugging | `software-development/systematic-debugging` 参考 |

## 对 Hermes 有用的设计

### 1. Rationalizations（反合理化）— 最值钱
预判 AI 会找的借口，给出反驳。如：
- "没时间写测试" → "测试是证明代码工作的证据"
- "一次做更快" → "感觉更快直到某天 break 了找不到原因"

### 2. Red Flags
判断 Skill 是否被正确执行的信号。

### 3. Skill Anatomy 统一结构
`Overview → When to Use → Process → Rationalizations → Red Flags → Verification`
比 Hermes 现有 skill 更完整。

## 一句话总结

- **Spec Kit**：用文档定 AI
- **Superpowers**：用流程带 AI
- **Agent Skills**：用纪律管 AI

## 归档时间

2026-04-27
