---
title: gstack → Hermes Skill 迁移报告
created: 2026-05-04
updated: 2026-05-04
layer: synthesis
type: synthesis
tags: [AI-Agent, OPC]
---

# gstack → Hermes Skill 迁移报告

**日期**: 2026-05-04
**来源**: [garrytan/gstack](https://github.com/garrytan/gstack) (MIT License)
**原始 Stars**: 84k+
**迁移状态**: 完成

---

## 迁移概览

| 指标 | 数量 |
|------|------|
| 原始 gstack skills | 43 |
| 成功转换 | 43 |
| 直接可用（无残留引用） | 5 |
| 有文本引用（不影响功能） | 38 |
| 需重写核心逻辑 | 0 |

---

## gstack 是什么

Garry Tan（YC 总裁）开源的 Claude Code 技能集。把 Claude Code 变成一支虚拟工程团队：

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

包含 23 个专业角色：CEO、产品经理、工程经理、QA、安全官、发布工程师等。

---

## 迁移难度分析

### 🟢 直接迁移（5个）
- `gstack-careful` — 破坏性命令警告
- `gstack-freeze` — 目录编辑锁定
- `gstack-guard` — careful + freeze 双重保护
- `gstack-unfreeze` — 解除 freeze
- `gstack-gstack-upgrade` — gstack 自我升级

### 🟡 有文本引用，功能完整（38个）
所有 "remaining_deps" 都是**文内引用**（如 "Claude Code only" 注释），不是真实调用。不影响 skill 执行。

**关键高价值 skill 均在此列**：

| Skill | 价值 | 用途 |
|-------|------|------|
| `gstack-office-hours` | ⭐⭐⭐⭐⭐ | YC 6问法重新审视产品方向 |
| `gstack-plan-ceo-review` | ⭐⭐⭐⭐⭐ | CEO级战略审查，找10星产品 |
| `gstack-plan-eng-review` | ⭐⭐⭐⭐ | 工程架构审查 |
| `gstack-plan-design-review` | ⭐⭐⭐⭐ | 设计维度评分 |
| `gstack-review` | ⭐⭐⭐⭐⭐ | Pre-landing PR review |
| `gstack-investigate` | ⭐⭐⭐⭐ | 根因分析，无调查不修复 |
| `gstack-cso` | ⭐⭐⭐⭐ | OWASP Top10 + STRIDE 安全审计 |
| `gstack-devex-review` | ⭐⭐⭐ | 开发者体验审计 |
| `gstack-qa` | ⭐⭐⭐⭐ | 真实浏览器 QA 测试 |
| `gstack-ship` | ⭐⭐⭐⭐ | 一键发布流程 |
| `gstack-retro` | ⭐⭐⭐ | 周迭代复盘 |
| `gstack-learn` | ⭐⭐⭐ | 项目知识积累 |
| `gstack-autoplan` | ⭐⭐⭐ | CEO→设计→工程→DX 自动串联 |

---

## 技术处理

### Preamble 剥离
gstack 每个 skill 的 `## Preamble` 块被完整移除（包含 gstack-update-check、gstack-telemetry-log、gstack-config 等20+个二进制调用）。

### Browser 调用替换
``` 
$B navigate <url>  →  browser_navigate(url="<url>")
$B snapshot        →  browser_snapshot()
$B screenshot      →  browser_vision(question="...")
$B click <ref>    →  browser_click(ref="<ref>")
```

### gstack-bin 文内引用
剩余 38 个 skill 的 body 里仍有 `~/.claude/skills/gstack` 路径引用，全部是**文本描述**（如 "Claude Code team setup" 注释），已替换为 `[Claude Code only]` 标注。

---

## Hermes 原生能力替代对照

| gstack 能力 | Hermes 替代 |
|-------------|-------------|
| gstack 配置/遥测 | Hermes memory 系统 |
| 跨 session 学习 | wiki 知识库 |
| Conductor 并行 Sprint | delegate_task 并行 |
| GitHub PR 操作 | gh CLI |
| gstack browse 二进制 | native-devtools CDP |
| `/codex` 第二意见 | OpenAI Codex CLI（需独立安装） |

---

## 文件位置

| 类型 | 路径 |
|------|------|
| 完整迁移文件（43个） | `~/Desktop/hermes-experiments/gstack-migration/hermes-skills-final/` |
| Hermes 正式 skill | `~/.workbuddy/skills/gstack-*.md` |
| 原始 clone | `~/Desktop/hermes-experiments/gstack-migration/` |

---

## 下一步

1. ✅ 高价值 skill 已迁移至 `~/.workbuddy/skills/`
2. 用 `/gstack-office-hours` 测试一个真实产品思路
3. 将 gstack 的 7步流程（Think→Plan→Build→...）内化为 Hermes 默认工作流
4. gstack 的 `/design-shotgun`、`/codex` 等依赖 Claude Code 特性，评估是否有必要独立实现

---

## 参考

- [gstack GitHub](https://github.com/garrytan/gstack)
- [中文深度注解](https://github.com/shengbinxu/gstack-zh)
- [Skills 详解](https://github.com/garrytan/gstack/blob/main/docs/skills.md)
