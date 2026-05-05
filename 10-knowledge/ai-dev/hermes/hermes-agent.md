---
title: Hermes Agent 评测笔记
created: 2026-04-11
updated: 2026-04-11
layer: processed
type: concept
tags: [hermes, nous-research, openclaw, agent, memory, learning-loop]
sources: [raw/articles/hermes-agent-wechat-20260411.md]
derived_from: []
---

# Hermes Agent 评测笔记

> 原文：《取代龙虾的是爱马仕？狂揽4万星的Hermes Agent，不只是OpenClaw平替》| ifanr

## 核心要点

### 背景
- Hermes Agent 由 **Nous Research** 团队研发（GitHub 48k stars，2026年2月至今活跃）
- 定位：单一 Agent 框架，与 OpenClaw 多 Agent 协作路线不同
- 小米 MiMo 已接入，限免两周

### 与 OpenClaw 的核心差异
OpenClaw 靠修改配置文件 + 多 Agent 协作；Hermes 是单一框架，靠**内置学习循环**从使用中进化。

### Learning Loop（闭合学习循环）
触发条件（满足任一）：
- 工具调用超过 5 次
- 中途出错并自我修复
- 用户做过纠正
- 走了非显而易见但有效的路径

→ 在 `~/.hermes/skills/` 生成 Skill 文件（遵循 agentskills.io 开放标准）
→ 后续执行发现更好路径，用 **patch** 打补丁更新，不整体覆写

### 四层记忆系统
| 层 | 内容 | 机制 |
|----|------|------|
| 第一层 | MEMORY.md + USER.md（常驻提示） | 每次会话自动加载，上限 3575 字符，强迫筛选 |
| 第二层 | 会话归档（SQLite + 全文索引）| 按需查询 + LLM 摘要注入 |
| 第三层 | 技能文件 | 系统提示只加载名称/描述，全文按需调入 |
| 第四层 | Honcho（用户建模）| 跨会话积累偏好、风格、领域知识 |

### Periodic Nudge
无用户输入时，系统定期发内部提示让 Agent 自我回顾，判断哪些值得写入记忆。**完全不需要用户触发。**

### Auxiliary Models
主模型（昂贵）处理对话，侧任务（图像分析/网页提取/Skill匹配/记忆）自动切到 **Gemini Flash**（便宜），多模型编排做在底层架构里。

### 支持平台
Telegram、Discord、Slack、飞书（功能最完整）；WSL2/Linux/macOS，Android + Termux。不支持原生 Windows。

### 安装
一行命令，自动处理 Python 3.11、Node.js v22、ripgrep、ffmpeg 等依赖。

### 模型配置
Nous Portal（订阅）、Anthropic Claude（API key / Claude Code 授权）、OpenRouter、DeepSeek、HuggingFace、阿里云 DashScope（Qwen）、GitHub Copilot、任何 OpenAI 兼容接口（含 Ollama 本地）。
