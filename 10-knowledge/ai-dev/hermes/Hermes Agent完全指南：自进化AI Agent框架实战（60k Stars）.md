---
title: Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）
author: 忠言
                    忠言
date: 2026年4月12日
cover: /assets/img/news/Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）-0.png
head:
  - - meta
    - name: 新闻
---
      
# Hermes Agent完全指南

  

## 一、项目概览

| 
指标

 | 

数值

 |
| --- | --- |
| 

GitHub

 | 

NousResearch/hermes-agent

 |
| 

Stars

 | 

60,098

 |
| 

定位

 | 

自进化AI Agent框架

 |
| 

开发方

 | 

Nous Research（羊驼系列模型开源方）

 |
| 

许可证

 | 

MIT

 |
| 

语言

 | 

Python

 |

**核心差异点**：唯一一个内置"学习循环"的AI Agent——能自创技能、自优化、自记忆，跨session持续进化。

* * *

## 二、核心特性解析

### 

  

2.1 内置学习循环（Built-in Learning Loop）

这是Hermes区别于其他Agent的根本特性：

任务执行 → 经验积累 → 技能自创 → 技能自优化 → 持久化记忆  
     ↑                                            ↓  
     └──────────── 下一个任务 ←─────────────────────┘  

其他Agent：每次session从零开始。 Hermes：每次任务都在丰富自己的技能库和记忆。

### 

  

2.2 三层记忆系统

| 
层级

 | 

内容

 | 

说明

 |
| --- | --- | --- |
| **会话记忆** | 

当前对话上下文

 | 

流式输出，实时更新

 |
| **技能记忆（Skills）** | 

AI从经验中自创的技能

 | 

可跨session复用，可分享

 |
| **用户模型** | 

持续积累的用户偏好/风格

 | 

基于Honcho dialectic框架

 |

### 

  

2.3 多平台接入

支持从单一Gateway接入多个消息平台：

*   **即时通讯**
    
    ：Telegram、Discord、Slack、WhatsApp、Signal
    
*   **邮件**
    
    ：Email
    
*   **智能家居**
    
    ：Home Assistant
    
*   **CLI**
    
    ：本地Terminal
    

架构示例：Telegram发指令 → 云端VM执行 → 结果推送回Telegram

### 

  

2.4 任意模型支持

# 切换模型  
hermes model sonnet                    # Claude  
hermes model gpt-4o                    # OpenAI  
hermes model deepseek-chat             # DeepSeek  
hermes model ollama/llama3             # 本地模型  
  
# 支持的提供商  
# Nous Portal / OpenRouter (200+模型) / z.ai / Kimi / MiniMax / OpenAI / Anthropic  

### 

  

2.5 多后端部署

| 
后端

 | 

适用场景

 | 

成本

 |
| --- | --- | --- |
| 

本地

 | 

开发测试

 | 

免费

 |
| 

Docker

 | 

一键部署

 | 

$5-10/月VPS

 |
| 

SSH

 | 

远程服务器

 | 

按需

 |
| 

Daytona/Singular

 | 

服务器less，冷启动按需

 | 

几乎为零

 |
| 

Modal

 | 

GPU集群

 | 

按调用计费

 |

* * *

## 三、安装与快速开始

### 

  

3.1 一键安装

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash  
source ~/.bashrc  # 或 source ~/.zshrc  
hermes            # 启动！  

### 

  

3.2 平台支持

*   **Linux**
    
     ✅
    
*   **macOS**
    
     ✅
    
*   **WSL2**
    
     ✅
    
*   **Android (Termux)**
    
     ✅
    
*   **Windows**
    
     ❌（需装WSL2）
    

### 

  

3.3 初始配置

hermes setup        # 全配置向导  
hermes model        # 选择LLM提供商和模型  
hermes tools        # 配置启用的工具  
hermes config set   # 设置单个配置项  

* * *

## 四、常用命令

### 

  

4.1 CLI命令

| 
命令

 | 

功能

 |
| --- | --- |
| `hermes` | 

启动交互式CLI

 |
| `/new`

 或 `/reset`

 | 

开始新对话

 |
| `/model [provider:model]` | 

切换模型

 |
| `/personality [name]` | 

设置人格

 |
| `/retry` | 

重试上一轮

 |
| `/undo` | 

撤销上一轮

 |
| `/compress` | 

压缩上下文

 |
| `/usage` | 

查看使用统计

 |
| `/skills` | 

浏览已有技能

 |
| `/skills [name]` | 

使用特定技能

 |
| `Ctrl+C` | 

中断当前工作

 |

### 

  

4.2 消息平台命令

在Telegram/Discord等平台使用，同样支持`/model`、`/skills`、\`\`/new\`等命令。

### 

  

4.3 定时任务（Cron）

# 自然语言描述定时任务  
"每天早上9点给我发个工作报告"  
"每周日晚上备份一次代码"  

* * *

## 五、Skills系统详解

### 

  

5.1 什么是Skills？

Skills是Hermes的自进化核心——AI从复杂任务中自动提取、可复用、可分享的技能模块。

对比：

| 
  


 | 

其他Agent

 | 

Hermes Skills

 |
| --- | --- | --- |
| 

代码审查

 | 

每次都要描述流程

 | 

AI自动学会流程，一句话调用

 |
| 

Bug修复

 | 

每次都要说明上下文

 | 

AI积累修复模式，下次更快

 |
| 

文档生成

 | 

每次描述格式要求

 | 

AI学会偏好，下次直接生成

 |

### 

  

5.2 Skills生态

*   **Skills Hub**
    
    : agentskills.io，技能市场
    
*   **开放标准**
    
    : 兼容agentskills.io开放标准
    
*   **自创技能**
    
    : AI自动从任务中创建
    
*   **技能进化**
    
    : 每次使用都在优化已有技能
    

### 

  

5.3 MCP扩展

# 连接任意MCP服务器  
hermes tools --add mcp --server your-mcp-server  

可接入任何符合MCP协议的工具扩展。

* * *

## 六、从OpenClaw迁移

如果你已经在用OpenClaw，可以零成本迁移：

hermes claw migrate              # 交互式完整迁移  
hermes claw migrate --dry-run    # 预览迁移内容  
hermes claw migrate --preset user-data  # 仅迁移用户数据  

**迁移内容**：

*   SOUL.md（人格配置）
    
*   Memories（记忆文件）
    
*   Skills（用户创建的技能）
    
*   API Keys（加密存储）
    
*   消息平台配置
    
*   命令白名单
    

* * *

## 七、技术架构

### 

  

7.1 Agent循环

用户输入 → 理解 → 规划 → 工具调用 → 执行 → 反思 → 记忆更新 → 响应  
                                                              ↓  
                                              技能自创 / 技能优化 / 记忆持久化  

### 

  

7.2 与其他Agent对比

| 
维度

 | 

Hermes

 | 

Claude Code

 | 

OpenClaw

 |
| --- | --- | --- | --- |
| 

自进化技能

 | 

✅

 | 

❌

 | 

❌

 |
| 

三层记忆

 | 

✅

 | 

简单

 | 

简单

 |
| 

多消息平台

 | 

✅

 | 

❌

 | 

部分

 |
| 

Skills市场

 | 

✅

 | 

❌

 | 

❌

 |
| 

Any模型

 | 

✅

 | 

Claude系

 | 

多

 |
| 

服务器less

 | 

✅

 | 

❌

 | 

❌

 |
| 

Stars

 | 

60k

 | 

\-

 | 

355k

 |

* * *

## 八、适用场景

**推荐用Hermes，如果你：**

*   需要跨session持续记忆的AI搭档
    
*   想在手机端发指令、云端跑任务
    
*   希望AI能从错误中自我优化
    
*   需要多平台统一的AI入口（Telegram管理所有任务）
    
*   想构建自己的AI技能库
    

**不太适合，如果你：**

*   只需要简单的代码补全（用Copilot/Cursor）
    
*   完全不熟悉命令行
    
*   项目极小，几句话搞定不需要Agent
    

* * *

## 九、资源链接

*   官方文档：https://hermes-agent.nousresearch.com/docs/
    
*   Skills市场：https://agentskills.io
    
*   橙皮书中文指南：https://github.com/alchaincyf/hermes-agent-orange-book
    
*   Discord社区：https://discord.gg/NousResearch
    

* * *

**总结**：Hermes Agent代表了AI Agent的一个新方向——不是"问答工具"，而是"会进化的搭档"。其内置学习循环和Skills系统，让AI从"执行一次忘一次"进化到"越用越强"。60k Stars不是偶然。