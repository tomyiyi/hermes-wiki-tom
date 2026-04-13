---
layer: raw
title: Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）
layer: raw
url: https://mp.weixin.qq.com/s/oxq1xH-E5irufiNkWKADHQ
layer: raw
type: article
layer: raw
created: 2026-04-12
---

# Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）

Original  忠言 忠言    [码农知道的事](javascript:void(0);)

# Hermes Agent完全指南

## 一、项目概览

|  |  |
| --- | --- |
|  |  |
|  |  |
|  | 自进化AI Agent框架 |
|  | Nous Research（羊驼系列模型开源方） |
|  |  |
| 语言 | Python |

**核心差异点**：唯一一个内置"学习循环"的AI Agent——能自创技能、自优化、自记忆，跨session持续进化。

---

layer: raw
## 二、核心特性解析

layer: raw
### 2.1 内置学习循环（Built-in Learning Loop）

layer: raw
这是Hermes区别于其他Agent的根本特性：

layer: raw
```
layer: raw
任务执行 → 经验积累 → 技能自创 → 技能自优化 → 持久化记忆      ↑                                            ↓      └──────────── 下一个任务 ←─────────────────────┘
layer: raw
```

layer: raw
其他Agent：每次session从零开始。 Hermes：每次任务都在丰富自己的技能库和记忆。

layer: raw
### 2.2 三层记忆系统

layer: raw
| 层级 | 内容 | 说明 |
layer: raw
| --- | --- | --- |
layer: raw
| **会话记忆** | 当前对话上下文 | 流式输出，实时更新 |
layer: raw
| **技能记忆（Skills）** | AI从经验中自创的技能 | 可跨session复用，可分享 |
layer: raw
| **用户模型** | 持续积累的用户偏好/风格 | 基于Honcho dialectic框架 |

layer: raw
### 2.3 多平台接入

layer: raw
支持从单一Gateway接入多个消息平台：

layer: raw
* **即时通讯**

layer: raw
  ：Telegram、Discord、Slack、WhatsApp、Signal
layer: raw
* **邮件**

layer: raw
  ：Email
layer: raw
* **智能家居**

layer: raw
  ：Home Assistant
layer: raw
* **CLI**

layer: raw
  ：本地Terminal

layer: raw
架构示例：Telegram发指令 → 云端VM执行 → 结果推送回Telegram

layer: raw
### 2.4 任意模型支持

layer: raw
```
layer: raw
# 切换模型 # 切换模型 hermes model sonnet                     # Claude # Claudehermes model gpt-4o                     # OpenAI # OpenAIhermes model deepseek-chat              # DeepSeek # DeepSeekhermes model ollama/llama3              # 本地模型 # 本地模型 # 支持的提供商 # 支持的提供商# Nous Portal / OpenRouter (200+模型) / z.ai / Kimi / MiniMax / OpenAI / Anthropic# Nous Portal / OpenRouter (200+模型) / z.ai / Kimi / MiniMax / OpenAI / Anthropic
layer: raw
```

layer: raw
### 2.5 多后端部署

layer: raw
| 后端 | 适用场景 | 成本 |
layer: raw
| --- | --- | --- |
layer: raw
| 本地 | 开发测试 | 免费 |
layer: raw
| Docker | 一键部署 | $5-10/月VPS |
layer: raw
| SSH | 远程服务器 | 按需 |
layer: raw
| Daytona/Singular | 服务器less，冷启动按需 | 几乎为零 |
layer: raw
| Modal | GPU集群 | 按调用计费 |

---

## 三、安装与快速开始

### 3.1 一键安装

```
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash source source ~/.bashrc  # 或 source ~/.zshrc# 或 source ~/.zshrc hermes             # 启动！ # 启动！
```

### 3.2 平台支持

* **Linux**

  ✅
* **macOS**

  ✅
* **WSL2**

  ✅
* **Android (Termux)**

  ✅
* **Windows**

  ❌（需装WSL2）

### 3.3 初始配置

```
hermes setup         # 全配置向导 # 全配置向导 hermes model         # 选择LLM提供商和模型 # 选择LLM提供商和模型 hermes tools         # 配置启用的工具 # 配置启用的工具 hermes config  set set     # 设置单个配置项 # 设置单个配置项
```

---

layer: raw
## 四、常用命令

layer: raw
### 4.1 CLI命令

layer: raw
| 命令 | 功能 |
layer: raw
| --- | --- |
layer: raw
| `hermes` | 启动交互式CLI |
layer: raw
| `/new` 或 `/reset` | 开始新对话 |
layer: raw
| `/model [provider:model]` | 切换模型 |
layer: raw
| `/personality [name]` | 设置人格 |
layer: raw
| `/retry` | 重试上一轮 |
layer: raw
| `/undo` | 撤销上一轮 |
layer: raw
| `/compress` | 压缩上下文 |
layer: raw
| `/usage` | 查看使用统计 |
layer: raw
| `/skills` | 浏览已有技能 |
layer: raw
| `/skills [name]` | 使用特定技能 |
layer: raw
| `Ctrl+C` | 中断当前工作 |

layer: raw
### 4.2 消息平台命令

layer: raw
在Telegram/Discord等平台使用，同样支持`/model`、`/skills`、``/new`等命令。

layer: raw
### 4.3 定时任务（Cron）

layer: raw
```
layer: raw
# 自然语言描述定时任务 # 自然语言描述定时任务 "每天早上9点给我发个工作报告" "每天早上9点给我发个工作报告" "每周日晚上备份一次代码" "每周日晚上备份一次代码"
layer: raw
```

---

## 五、Skills系统详解

### 5.1 什么是Skills？

Skills是Hermes的自进化核心——AI从复杂任务中自动提取、可复用、可分享的技能模块。

对比：

| 其他Agent | Hermes Skills |
| --- | --- |
| 代码审查 | 每次都要描述流程 | AI自动学会流程，一句话调用 |
| Bug修复 | 每次都要说明上下文 | AI积累修复模式，下次更快 |
| 文档生成 | 每次描述格式要求 | AI学会偏好，下次直接生成 |

### 5.2 Skills生态

* **Skills Hub**

  : agentskills.io，技能市场
* **开放标准**

  : 兼容agentskills.io开放标准
* **自创技能**

  : AI自动从任务中创建
* **技能进化**

  : 每次使用都在优化已有技能

### 5.3 MCP扩展

```
# 连接任意MCP服务器 # 连接任意MCP服务器hermes tools --add mcp --server your-mcp-server
```

可接入任何符合MCP协议的工具扩展。

---

layer: raw
## 六、从OpenClaw迁移

layer: raw
如果你已经在用OpenClaw，可以零成本迁移：

layer: raw
```
layer: raw
hermes claw migrate               # 交互式完整迁移 # 交互式完整迁移hermes claw migrate --dry-run     # 预览迁移内容 # 预览迁移内容hermes claw migrate --preset user-data   # 仅迁移用户数据 # 仅迁移用户数据
layer: raw
```

layer: raw
**迁移内容**：

layer: raw
* SOUL.md（人格配置）
layer: raw
* Memories（记忆文件）
layer: raw
* Skills（用户创建的技能）
layer: raw
* API Keys（加密存储）
layer: raw
* 消息平台配置
layer: raw
* 命令白名单

---

## 七、技术架构

### 7.1 Agent循环

```
用户输入 → 理解 → 规划 → 工具调用 → 执行 → 反思 → 记忆更新 → 响应                                                               ↓                                              技能自创 / 技能优化 / 记忆持久化
```

### 7.2 与其他Agent对比

| 维度 | Hermes | Claude Code | OpenClaw |
| --- | --- | --- | --- |
| 自进化技能 | ✅ | ❌ | ❌ |
| 三层记忆 | ✅ | 简单 | 简单 |
| 多消息平台 | ✅ | ❌ | 部分 |
| Skills市场 | ✅ | ❌ | ❌ |
| Any模型 | ✅ | Claude系 | 多 |
| 服务器less | ✅ | ❌ | ❌ |
| Stars | 60k | - | 355k |

---

layer: raw
## 八、适用场景

layer: raw
**推荐用Hermes，如果你：**

layer: raw
* 需要跨session持续记忆的AI搭档
layer: raw
* 想在手机端发指令、云端跑任务
layer: raw
* 希望AI能从错误中自我优化
layer: raw
* 需要多平台统一的AI入口（Telegram管理所有任务）
layer: raw
* 想构建自己的AI技能库



---

## 九、资源链接



---

layer: raw
**总结**：Hermes Agent代表了AI Agent的一个新方向——不是"问答工具"，而是"会进化的搭档"。其内置学习循环和Skills系统，让AI从"执行一次忘一次"进化到"越用越强"。60k Stars不是偶然。

layer: raw
Scan to Follow

layer: raw
[Got It](javascript:;)

layer: raw
Scan with Weixin to   
layer: raw
use this Mini Program

layer: raw
[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

layer: raw
[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

layer: raw
[Cancel](javascript:void(0);) [Allow](javascript:void(0);)

layer: raw
微信扫一扫可打开此内容，  
layer: raw
使用完整服务

layer: raw
:  ， ， ， ， ， ， ， ， ， ， ， ， .   Video Mini Program Like ，轻点两下取消赞 Wow ，轻点两下取消在看 Share Comment Favorite 听过  