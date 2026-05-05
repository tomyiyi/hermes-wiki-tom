---
title: wechat Hermes Agent 命令完全指南 80 条命令 这一 2026 04 29
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: query
tags: [AI-Agent]
---

﻿---
title: Hermes Agent 命令完全指南：80+ 条命令，这一篇够了
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: summary
tags: [wechat, hermes, profile, NAME, Hermes, API]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777424653&ver=6689&signature=NaQp5rIgV3fyl7T7PBVC8WZHKjaO4bhbWBd89iy5hvnbotzRCTGb1GenZODJBOy6VikfeEL5EGrIWAzU*PcoIbmzqpYrzSAp8ppM*JGawYFX1PpXndSzOH6pYO0a6T2m&new=1
account: 虾看虾说
pubTime: 2026年4月28日 09:59
---

## 摘要

Hermes Agent 命令分类总览 GitHub 118k Star 的 Hermes Agent，最近更新了一个大版本。 上个月刚装完还在想"这东西好像有点意思"，转眼间 v0.11.0 已经发布，官方称之为"The Interface Release"——整个交互界面用 React 和 Ink 重写了，还顺手加入了 5 个新的推理路径、17 个消息平台支持，以及 GPT-5.5。 趁着这次更新，我把它所有的命令和用法系统梳理了一遍，按「你想做什么」分成 7 大类。不需要全记，收藏备查就好。 先装好 curl -fsSL https://raw.githubusercontent.com...

---

## 核心要点

（待整理）

---

## 原文（来源：虾看虾说）

Hermes Agent 命令分类总览 GitHub 118k Star 的 Hermes Agent，最近更新了一个大版本。 上个月刚装完还在想"这东西好像有点意思"，转眼间 v0.11.0 已经发布，官方称之为"The Interface Release"——整个交互界面用 React 和 Ink 重写了，还顺手加入了 5 个新的推理路径、17 个消息平台支持，以及 GPT-5.5。 趁着这次更新，我把它所有的命令和用法系统梳理了一遍，按「你想做什么」分成 7 大类。不需要全记，收藏备查就好。 先装好 curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh |bash source ~/.bashrc # 或 source ~/.zshrc hermes update Windows 用户注意 必须先装 WSL2，在 PowerShell 里运行 wsl --install，重启后打开 Ubuntu 终端操作。 一、基础启动和会话管理 启动相关 hermes # 进入聊天 hermes chat # 同上 hermes -c # 继续上次会话（--continue） hermes --resume 会话名 # 恢复指定会话 会话管理 hermes sessions list # 列出所有历史会话 hermes sessions browse # 交互式翻找 hermes sessions rename ID 新名 # 重命名 hermes sessions export 文件名 # 导出 JSONL hermes sessions delete ID # 删除会话 hermes sessions prune # 批量清理旧会话 hermes sessions stats # 存储统计 小细节 对话自动双份存储（SQLite + Markdown），不会丢失。另外，会话可以用自然语言描述恢复，比如 hermes --resume "昨天调 API 那个"。 聊天界面里的斜杠指令 进入 hermes 之后，按 / 会弹出自动补全菜单，关键命令有： /new # 开新会话（alias: /reset） /title 我的标题 # 给会话起名 /clear # 清屏开新会话 /history # 查看当前对话历史 /save # 保存当前对话 /retry # 重试上一条 /undo # 撤销上一轮对话 /rollback [N] # 恢复文件系统检查点 /compress # 手动压缩上下文 /status # 当前会话状态 /agents # 查看后台运行的任务 /bg <prompt> # 后台跑任务，不阻塞当前对话 /q <prompt> # 队列下一轮提示词 /btw <问题> # 临时问一句，不存档 /branch [名字] # 分叉当前会话，探索不同方向 二、模型切换和配置 随时换模型 hermes model # 交互式菜单，上下键选，回车确认 在聊天里也可以直接打： /model claude-sonnet-4 /model deepseek/deepseek-v4/model custom:name:model # 自定义端点 加 --global 参数可以持久化这个选择。 国内模型配置 提供商环境变量DeepSeekDEEPSEEK_API_KEYKimi / MoonshotKIMI_API_KEY通义千问DASHSCOPE_API_KEY智谱 GLMGLM_API_KEYMiniMaxMINIMAX_API_KEY / MINIMAX_CN_API_KEY 国外模型配置 提供商说明Nous Portal订阅制，零配置，hermes loginAnthropic Claudehermes model 或直接配 API KeyOpenAI / Codex设备码认证OpenRouter200+ 模型路由Hugging Face20+ 开源模型，HF_TOKENGitHub CopilotOAuth 或 COPILOT_GITHUB_TOKEN 本地模型（Ollama、vLLM、SGLang 等 OpenAI 兼容 API），通过 hermes model →「Custom Endpoint」配置。 配置文件管理 hermes config # 查看当前配置 hermes config edit # 用编辑器打开 config.yaml hermes config set 键 值 # 单独改一项 hermes config path # 配置文件路径 hermes config check # 检查配置 hermes config migrate # 升级配置格式 hermes setup # 完整配置向导 hermes setup model # 只配模型 hermes setup gateway # 只配消息网关 hermes setup tools # 只配工具集 凭证池（多账号轮换） hermes auth add # 交互式添加凭证 hermes auth list # 查看凭证池 hermes auth remove 提供商 INDEX # 删除 hermes auth reset 提供商 # 重置"配额耗尽"状态 环境诊断 hermes doctor # 检查环境问题 hermes doctor --fix # 自动修复 三、工具集和 MCP 工具管理 hermes tools # 查看可用工具集 聊天界面里： /tools list # 列出所有工具 /tools disable 工具名 # 禁用某个工具 /tools enable 工具名 # 启用某个工具 MCP 服务器管理 hermes mcp add NAME --url URL # 添加 HTTP 类型 MCP Server hermes mcp add NAME --command CMD # 添加命令行类型 hermes mcp list # 查看已配置 hermes mcp test NAME # 测试连接 hermes mcp configure NAME # 配置工具 hermes mcp remove NAME # 删除 hermes mcp serve # 把 Hermes 作为 MCP Server 运行 配置文件示例 在 config.yaml 里写好 MCP Server 配置，格式统一，不需要在每个工具里单独配认证信息。 聊天内重载 /reload # 重载 .env（不重启，新 API Key 立即生效） /reload-mcp # 重载 config.yaml 里的 MCP 服务器 四、技能商店 什么是技能 技能是 Markdown 文件，写着"遇到这类任务，按这个流程做"。Hermes 会自动加载对应技能，不需要每次重新解释。 自动创建技能：用 5+ 工具调用完成一个复杂任务后，Hermes 会自动保存成技能，下次遇到类似任务自动调用。 条件激活：可以按平台或文件存在条件触发，比如「检测到 vercel.json 就激活 Vercel 部署技能」。 技能命令 /skills browse # 翻找技能 /skills install 名字 # 安装技能 /skills audit # 检查技能健康状态 常用内置技能 /plan # 加载 plan 技能，制定执行计划 /github-pr-workflow # GitHub PR 工作流 /architecture-diagram # 生成架构图 /excalidraw # 手绘风格图表 内置 73 个 + 可选 59 个技能，覆盖 Web 开发、健康、资讯、机器学习等方向。 五、多实例隔离（Profiles） Profiles 是 Hermes 最被低估的功能之一。它让你在同一台机器上跑多个完全隔离的 Hermes 实例——独立配置、独立记忆、独立技能、独立 cron。 hermes profile list # 查看所有 profile hermes profile create NAME # 创建空白 profile hermes profile create NAME --clone # 复制当前配置 hermes profile create NAME --clone-all # 复制所有内容 hermes profile use NAME # 设为默认 hermes profile show NAME # 查看详情 hermes profile rename A B # 重命名 hermes profile delete NAME # 删除 hermes profile export NAME # 导出 tar.gz hermes profile import FILE # 导入 创建完会生成一个 shell alias，比如 hermes profile create work 之后会多一个 work 命令，直接进入 work 隔离环境。 六、消息网关和自动化 Hermes 不只是一个终端工具，它内置了消息网关，可以连接到 17 个平台：Telegram、Discord、Slack、WhatsApp、Signal、Email、飞书、微信……以及刚加入的 QQBot。 网关命令 hermes gateway # 启动网关 hermes platforms # 查看平台状态（alias: /platforms） 定时任务（Cron） /cron # 管理定时任务 创建新任务时会问你要投递到哪里：origin — 回到当前对话local — 保存到本地文件 telegram、discord、feishu 等 — 直接发到对应平台 自然语言配置，比如"每天早上 9 点给我发一份 GitHub Trending 总结"，设置一次，之后自动跑。 七、其他有用的命令 hermes status # 组件运行状态 hermes version # 版本号 hermes update # 更新 Hermes hermes logs # 查看日志 hermes dump # 导出安装摘要（排错用） hermes insights # 使用统计 hermes insights --days 7 # 最近 7 天统计 # Shell 自动补全 hermes completion bash >> ~/.bashrc # Linux/WSL2 hermes completion zsh >> ~/.zshrc # Mac # 从 OpenClaw 迁移 hermes claw migrate # 卸载 hermes uninstall 快捷键Alt + Enter — 多行输入，粘贴代码或写长提示词时用Ctrl + C — 中断当前任务Ctrl + Z — 挂起后台任务 v0.11.0 新特性，重点说一下 最近这次更新（2026.4.23）改动很大，官方称之为"The Interface Release"：整个 TUI 用 React + Ink 重写，界面更好看，也更容易扩展传输层架构可插拔，接新模型更方便新增 5 个推理路径：NVIDIA NIM、Arcee、Step Plan、Gemini CLI OAuth、ai-gateway原生 AWS Bedrock 支持GPT-5.5 通过 Codex OAuth 接入Dashboard 插件系统，支持主题实时切换 /steer 指令，可以在任务中途干预 AI 的思考方向Shell hooks 和 Webhook 直接投递QQBot 加入（第 17 个消息平台） Hermes Agent 命令分类总览 最后 Hermes 不是一个聊天框，是一个9 个模块拼起来的完整系统。 它能跑在 6 种终端后端（本地、Docker、SSH、Daytona、Singularity、Modal），接 20+ 模型，自动创建技能记住你教它的东西，还能定时自动执行任务。 把这些命令收藏好，慢慢试，你会发现它跟普通的 AI 聊天工具完全不是一个物种。 GitHub：https://github.com/NousResearch/hermes-agent 文档：https://hermes-agent.nousresearch.com/docs 觉得有用，欢迎转发。