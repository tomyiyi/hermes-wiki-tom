---
title: "gstack - 自动化软件工程团队工具集"
description: "Garry Tan (YC CEO) 开源的 28 个 Skills，将 AI 编码助手升级为 23 人虚拟工程团队"
source: https://mp.weixin.qq.com/s/iAsu9_AlIfw2fdqPJRVKgQ
author: i龙虾
date: 2026-05-04
tags: [gstack, YC, GarryTan, software-engineering, skills, Auto_Absorbed]
layer: 10-knowledge
type: entity
created: 2026-05-04
updated: 2026-05-04
value_classification: 实操工具
solves_what:
  - "解决：AI 编码助手缺乏结构化开发流程和质量门禁的问题"
  - "用户：开发者个人、创业团队、技术负责人"
  - "失效：非软件开发场景（如纯写作、客服）"
  - "相关：hermes-agent, openclaw, claude-code"
---

# gstack - 自动化软件工程团队工具集

> Garry Tan（YC CEO）开源，发布 <1 周获得 84,000+ GitHub stars
> 核心：将单独 AI 编码助手变成完整虚拟软件工程团队（23 个专家角色）

---

## 一、核心定位

| 属性 | 内容 |
|------|------|
| 作者 | Garry Tan（YC CEO） |
| 授权 | MIT，免费 |
| Skills 数量 | 28 个（覆盖完整 SDLC） |
| 支持 Agents | Claude Code、OpenClaw、Hermes、Cursor、Codex 等 10+ |
| 效果 | 作者声称 810x 编码速度 vs 2013 年个人产出，60 个兼职日完成 40+ 生产功能 |

---

## 二、28 Skills 分类速查

### A. 规划与策略（编码前）
| Skill | 功能 |
|-------|------|
| `/office-hours` | YC 式产品质询（6 个核心问题验证 Problem-Solution Fit） |
| `/plan-ceo-review` | 战略范围挑战（4 模式：扩大/选择性扩大/保持/缩减） |
| `/plan-eng-review` | 工程架构审查（技术选型、单点故障、6 个月可扩展性） |
| `/plan-design-review` | UI/UX QA（修复 AI 生成的"slop"不一致样式） |
| `/autoplan` | 从功能描述自动生成优先级任务列表 |

### B. 执行与开发（编码阶段）
| Skill | 功能 |
|-------|------|
| `/review` | 偏执代码审查（发现生产关键 bug：竞态条件、注入风险、未处理错误） |
| `/careful` | 高风险修改保护（核心重构、DB 迁移逐步确认） |
| `/freeze` / `/unfreeze` | 锁定/解锁代码段防止意外修改 |
| `/guard` | 范围蠕变防护（警告超出范围的功能添加） |

### C. 质量与测试
| Skill | 功能 |
|-------|------|
| `/qa` | 完整 E2E 浏览器测试（打开 Chrome，测试 URL，检查控制台错误，移动适配） |
| `/qa-only` | 仅测试，不修改代码 |
| `/benchmark` | 性能基准测试 + 优化建议 |
| `/cso` | OWASP Top 10 安全审计（不自动修复以避免新 bug） |

### D. 发布与部署
| Skill | 功能 |
|-------|------|
| `/ship` | 发布准备（审查 + 变更日志 + 发布检查清单） |
| `/land-and-deploy` | 合并 PR + 触发部署 |
| `/canary` | 金丝雀发布配置（流量分割，自动回滚） |
| `/document-release` | 自动生成变更日志和用户发布说明 |

### E. 复盘与研究
| Skill | 功能 |
|-------|------|
| `/retro` | 周度结构化复盘 |
| `/investigate` | 4 步事件/bug 调查（观察 → 假设 → 验证 → 根因） |
| `/learn` | 引导式技术学习框架 |

### F. 浏览器与跨 Agent 协作
| Skill | 功能 |
|-------|------|
| `/browse` | 安全网页浏览 agent（替代原生 Chrome 工具，4 层安全过滤） |
| `/pair-agent` | 跨 agent 任务协调（将长期规划和短期执行拆分到不同 agent） |
| `/connect-chrome` / `/setup-browser-cookies` | Chrome 连接和安全 cookie 管理 |

---

## 三、安全机制（4 层防护）

gstack 为浏览器 agent 提供 prompt injection 防护：

| 层 | 机制 |
|----|------|
| L1-L3 | 内容安全过滤（数据标记、隐藏元素剥离、ARIA 正则检查、URL 黑名单、信任边界信封） |
| L4 | 本地 ML 分类器（22MB BERT-small ONNX 模型，int8 量化，无需联网） |
| L4b | 对话级审查（Claude Haiku 对完整对话上下文二次审查） |
| 阻断规则 | 仅当两个分类器都标记问题时才阻断（减少误报） |

**可选高精度模型**：
```bash
GSTACK_SECURITY_ENSEMBLE=deberta  # 721MB DeBERTa-v3
```

**紧急熔断**：`GSTACK_SECURITY_OFF=1`

**CAPTCHA/MFA 交接**：`$B handoff` 打开可见 Chrome 窗口手动处理 → `$B resume` 继续

---

## 四、OpenClaw × gstack 集成（4 种方法）

### 方法 1：自动安装
```
告诉 OpenClaw agent: install gstack for openclaw
```

### 方法 2：AGENTS.md 配置
在项目的 `AGENTS.md` 中添加：
```markdown
## Coding Tasks
When spawning Claude Code sessions for coding work, tell the session to use gstack skills.
Examples:
- Security audit: "Load gstack. Run /cso"
- Code review: "Load gstack. Run /review"
- QA test a URL: "Load gstack. Run /qa https://your-url.com"
```

### 方法 3：ClawHub 原生技能（无需 Claude Code）
```bash
clawhub install gstack-openclaw-office-hours
clawhub install gstack-openclaw-ceo-review
clawhub install gstack-openclaw-investigate
clawhub install gstack-openclaw-retro
```

### 方法 4：直接引用 GitHub Raw 链接（自动更新）
```
https://raw.githubusercontent.com/garrytan/gstack/main/skills/office-hours.md
```

---

## 五、Hermes × gstack 集成

Hermes 使用与 OpenClaw 相同的底层模型，集成方式几乎相同：

```bash
# 自动安装
tell Hermes agent: install gstack for hermes

# 或手动
cd ~/.claude/skills/gstack && ./setup --host hermes
```

**关键文件**：
- `AGENTS.md` / `RESOLVER.md`（Hermes v0.19+ 支持两者）
- `hermes claw migrate`：从 OpenClaw 迁移 gstack 配置

**gbrain + gstack 组合**：
- gstack 处理编码任务
- gbrain（Garry Tan 伴侣项目）处理非编码任务

---

## 六、安装步骤

### 前置条件
```bash
npm install -g @anthropic-ai/claude-code
claude --version  # 验证安装
```

### 个人全局安装
```bash
git clone --single-branch --depth 1 https://github.com/garrytan/gstack.git ~/.claude/skills/gstack \
  && cd ~/.claude/skills/gstack \
  && ./setup
```

### 团队项目安装（强制所有贡献者使用 gstack）
```bash
cd <project-root>
~/.claude/skills/gstack/bin/gstack-team-init required
git add .claude/ CLAUDE.md
git commit -m "require gstack for AI-assisted work"
```

### 避免命令冲突（添加 `gstack-` 前缀）
```bash
cd ~/.claude/skills/gstack && ./setup --prefix
# 命令变为 /gstack-review 而非 /review
```

---

## 七、维护

| 操作 | 命令 |
|------|------|
| 更新 | 在 Claude Code 中运行 `/gstack-upgrade`，或手动： |
|      | `cd ~/.claude/skills/gstack && git pull && ./setup` |
| 卸载 | 提供 6 步脚本（注意：卸载后需手动从 `CLAUDE.md` 移除 gstack 配置） |
| 命令冲突 | `./setup --prefix` 添加 `gstack-` 命名空间前缀 |

---

## 八、推荐工作流

```
OpenClaw/Hermes 规划（/office-hours 验证想法）
        ↓
持久化计划到内存/脑库
        ↓
Spawn Claude Code session（执行）
        ↓
/guard（防止范围蠕变）+ /freeze（锁定关键代码）
        ↓
/review（代码审查）+ /cso（安全审计）
        ↓
/qa（E2E 测试）
        ↓
/document-release（自动生成变更日志）+ /ship（发布）
```

---

## 九、关键环境变量

| 变量 | 用途 |
|----------|---------|
| `OPENCLAW_SESSION` | OpenClaw spawn Claude Code session 时自动设置；gstack 检测此变量调整行为 |
| `GSTACK_SECURITY_ENSEMBLE=deberta` | 启用高精度 DeBERTa 安全模型 |
| `GSTACK_SECURITY_OFF=1` | 紧急禁用安全过滤器 |

---

## 十、核心价值

> gstack 的核心价值在于其**规划阶段 Skills**（`/office-hours` 和 `/plan-ceo-review`），它们编码了 Garry Tan 评估数千个 YC 初创公司的框架。

当与 OpenClaw/Hermes 配对时，开发者获得清晰的角色分离：
- **OpenClaw/Hermes**：处理对话和记忆
- **gstack**：处理开发流程质量和控制

---

## 十一、故障排查

| 问题 | 解决方案 |
|------|------------|
| `/office-hours` 跳过问题直接写代码 | 检查 `~/.claude/CLAUDE.md` 有 gstack 配置段，重新运行 `./setup` |
| `/browse` 错误 | 确保 Chrome 已安装，运行 `/connect-chrome` 初始设置，允许 macOS Keychain 权限 |
| ClawHub 安装失败 | 更新 `clawhub`，检查 OpenClaw 正在运行，手动复制 gstack 的 `openclaw/skills/` 目录到 `~/.openclaw/skills/` |
| Skill 名称冲突 | 运行 `./setup --prefix` 添加 `gstack-` 命名空间前缀 |
| 迁移后 Hermes Skills 不工作 | 需要新 session 加载迁移的 Skills；重启 Hermes 对话并运行 `hermes status` 验证 |

---

---

## 十二、gbrain + gstack 组合

Garry Tan 的另一个开源项目，专注于**非编码任务**：

| 工具 | 职责 | 场景 |
|------|------|------|
| **gstack** | 编码相关 skill | review、qa、ship、cso |
| **gbrain** | 其它一切 | brain管理、信号检测、数据摄入、知识富化、定时任务、报告、身份管理 |

```
gstack skillpack install  # 同时安装 gstack + gbrain
```

---

## 十三、完整工作流演示（想法 → 上线）

**场景：给项目加一个"用户导出数据"功能**

| Step | 操作 | Skill | 说明 |
|------|------|-------|------|
| 1 | 产品追问 | `/office-hours` | 搞清楚功能给谁用、怎么导出、GDPR合规、最小版本 |
| 2 | 存计划到 memory | — | 标记为 `feature-export-plan` |
| 3 | Spawn Claude Code | `/autoplan` | 加载计划，拆解任务 |
| 4 | 开发中防护 | `/guard` + `/freeze` | 防止 scope 膨胀 + 锁定关键代码 |
| 5 | 发布前审查 | `/review` + `/cso` | 代码审查 + 安全审计 |
| 6 | E2E 测试 | `/qa https://localhost:3000/export` | 打开 Chrome 测试 |
| 7 | 发布文档 | `/document-release` + `/ship` | 生成 changelog + 发布 |

---

## 十四、在 OPC 社区运营中的应用

gstack 的方法论可以应用于政府公共服务的方案策划和执行审查：

### `/office-hours` → 方案评审追问法

| YC 追问 | OPC 场景应用 |
|---------|--------------|
| 功能给谁用？ | 这个服务包谁最需要？A轨（萌芽期）还是B轨（落地期）？ |
| 他们现在怎么解决？ | 这些人之前怎么创业？街道有替代方案吗？ |
| 你的方案比现状好在哪？ | 综合体比去区政务中心好在哪？差异化在哪？ |
| 哪个假设最容易被证伪？ | "AI培训能变现"这个假设成立吗？有没有数据支撑？ |
| 最小可用版本是什么？ | 先开业还是先建完所有服务？哪些是核心功能？ |
| 怎么定义成功？ | "200人次服务"怎么衡量？有没有可量化的指标？ |

### `/cso` → 风险审计清单

| OWASP 类比 | OPC 风险点 |
|-----------|-----------|
| 注入风险 | 政策申报信息填错导致补贴落空 |
| 敏感数据暴露 | 创业者隐私信息（收入、联系方式）保护 |
| 权限提升 | 第三方运营方（蒂湾创业）越权操作 |
| 安全日志缺失 | 服务记录无台账，考核无依据 |

### `/investigate` → 问题调查四步法

适用于：培训没人来、创业者咨询转化率低、第三方运营出问题

```
Step 1 现象：AI培训报名人数低于预期
Step 2 假设：宣传渠道不对 / 内容不贴合需求 / 时间安排冲突
Step 3 验证：查看报名渠道数据 / 访谈已报名者 / 对比同类培训
Step 4 根因：决定下一步行动
```

---

## 相关链接

- GitHub：https://github.com/garrytan/gstack
- gbrain：https://github.com/garrytan/gbrain（Garry Tan 的伴侣项目）
- YC：https://www.ycombinator.com/
