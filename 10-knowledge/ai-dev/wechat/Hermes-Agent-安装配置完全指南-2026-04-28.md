---
title: wechat Hermes Agent 安装配置完全指南 2026 04 28
created: 2026-04-28
updated: 2026-04-28
layer: processed
type: query
tags: [AI-Agent]
---

﻿---
title: Hermes Agent 安装配置完全指南
created: 2026-04-28
updated: 2026-04-28
layer: processed
type: summary
tags: [wechat, hermes, Hermes, Agent, config, gateway]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777345020&ver=6687&signature=F8PWyOdXD216uskGh2l2kpnGGU*0dTMGrJ-dLo02x*K4BKPgtl8z*aFiS*nouEyiY9UPYRprl6PwholVFL-SNESH3v9JC0fdVb1ziZm-m0fY-Mo5BCerS0ytky7JCZYQ&new=1
account: 查令十街84号
pubTime: 2026年4月27日 15:23
---

## 摘要

引言如果你用过各种 AI 助手，一定有过这种体验：每次对话都像是第一次认识——它不记得你上周的需求，不理解你习惯的工作方式，更谈不上"越用越顺手"。Hermes Agent 要解决的就是这个问题。它不只是又一个命令行工具，而是一套能长期学习、持续进化的 Agent 运行时。用官方的话说："用得越多，它越强。"这篇文章带你从零开始，把它装起来、配好、跑通。一、Hermes Agent 是什么Hermes Agent 由 Nous Research（开源模型圈的老熟人，Hermes、Nomos 系列模型就是他们训练的）开发，核心定位是"介于 coding agent 与 generalist ag...

---

## 核心要点

（待整理）

---

## 原文（来源：查令十街84号）

引言如果你用过各种 AI 助手，一定有过这种体验：每次对话都像是第一次认识——它不记得你上周的需求，不理解你习惯的工作方式，更谈不上"越用越顺手"。Hermes Agent 要解决的就是这个问题。它不只是又一个命令行工具，而是一套能长期学习、持续进化的 Agent 运行时。用官方的话说："用得越多，它越强。"这篇文章带你从零开始，把它装起来、配好、跑通。一、Hermes Agent 是什么Hermes Agent 由 Nous Research（开源模型圈的老熟人，Hermes、Nomos 系列模型就是他们训练的）开发，核心定位是"介于 coding agent 与 generalist agent 之间的混合体"。跟大多数 Agent 最大的区别：它不是无状态的。普通 Agent：你配好什么能力，它就什么能力；问完即忘，下次从零开始。Hermes：自带闭环学习系统，能从交互中学习，自动沉淀技能，跨会话记忆，持续改进自己的行为。简单说——它会越用越懂你。二、安装前准备系统要求操作系统：Linux（推荐）、macOS、Windows WSL2、Android TermuxPython：3.10+内存：建议 4GB+（本地跑模型需 16GB+）网络：能访问 GitHub 和你选的 LLM 提供商 API需要提前准备LLM API Key：推荐 DeepSeek、OpenRouter（支持 200+ 模型）、Anthropic Claude 或 OpenAIGitHub 账号：安装脚本从 GitHub 拉取代码三、安装：一行命令搞定方式一：一键安装脚本（推荐）curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh|bash安装完成后加载环境变量：source~/.bashrc&&hermes预期输出：hermes v0.8.0 (v2026.4.8)方式二：手动安装如果脚本下载失败（国内网络你懂的），手动来：git clone --depth=1https://github.com/NousResearch/hermes-agent.git ~/.hermes/hermes-agentcd ~/.hermes/hermes-agent python -m venv venv source venv/bin/activateUV_HTTP_TIMEOUT=300 uv pip install -e ".[messaging,cron,cli,mcp,pty]"ln-sf ~/.hermes/hermes-agent/hermes ~/.local/bin/hermesecho'export PATH="$HOME/.local/bin:$PATH"'>>~/.bashrcsource~/.bashrc herme sversion四、配置 LLM 模型首次运行会进入交互式配置向导：hermes setup或者在已安装后切换模型：hermes model以 DeepSeek 为例选择More providers...选择Custom endpoint (enter URL manually)填入：-API base URL：https://api.deepseek.com/v1-API key：你的sk-xxx-Model name：deepseek-chat-Context length：65536（Hermes 要求最低 64K）以 Ollama 本地模型为例（Windows WSL2）先确保 Windows 端 Ollama 已启动，然后在 WSL2 里：HOST_IP=$(iproute|grepdefault|awk'{print $3}')hermesconfigsetmodel.base_url"http://$HOST_IP:11434/v1"hermesconfigsetmodel.name"qwen2.5:7b"hermesconfigsetmodel.api_key""五、核心功能配置5.1 工具模块管理Hermes 内置了 40+ 工具，按需启用：hermes tools list hermes tools enable shell browser files search hermes tools disable visiontts常用工具说明：-shell：终端命令执行-browser：浏览器自动化-files：文件读写操作-search：网络搜索（默认 Firecrawl）5.2 记忆系统配置Hermes 的三层记忆架构会自动工作，但你可以调整压缩策略：hermes config get memory hermes config set MEMORY_COMPRESSION_RATIO 0.55.3 定时任务（Cron）用自然语言设置定时任务：hermes schedule "每天早上 8 点，检查我的项目目录并生成昨日代码统计"hermes schedule list hermes schedule remove <task-id>六、对接消息平台Hermes 支持 7+ 平台，配置方式统一：hermes gateway setup6.1 Telegram 对接找 @BotFather 创建 Bot，拿到 Token运行hermes gateway setup，选择 Telegram填入 Token，启动：hermes start6.2 飞书/Lark 对接访问 https://open.feishu.cn 创建应用开启 Bot 能力，拿到 App ID 和 App Secret配置环境变量：hermes config set gateway.feishu.app_id "cli_xxx"hermes config set gateway.feishu.app_secret "your_secret"hermes config set gateway.feishu.connection_mode "websocket"启动网关：hermes gateway start feishu七、日常使用命令速查命令作用hermes chat进入交互式对话hermes "任务描述"直接执行单次任务hermes setup重新运行配置向导hermes model切换 LLM 模型hermes config set <key> <value>修改配置项hermes doctor诊断环境问题hermes skills list查看已沉淀的技能hermes schedule "..."创建定时任务hermes gateway setup配置消息平台hermes start启动后台服务八、常见问题与解决Q：安装后找不到hermes命令？A：执行source ~/.bashrc，或检查~/.local/bin是否在 PATH 中。Q：提示 "Model has a context window of 32,768 tokens, which is below the minimum 64,000"？A：直接覆盖配置hermes config set model.context_length 65536，或换支持更长上下文的模型。Q：Windows 能用吗？A：原生不支持，必须走 WSL2。这是官方明确说的，别挣扎。Q：必须用它自家的 Hermes 模型吗？A：不必须。支持 OpenRouter 200+ 模型、Claude、GPT-4o、DeepSeek 等。只有 function-calling 子框架对 Hermes 模型有优化。总结Hermes Agent 的核心价值不在于"能做什么"，而在于"越用越会做"。它的闭环学习系统、跨会话记忆和技能沉淀，让它从一个"执行命令的工具"变成了"能记住你习惯的协作者"。现在开源 Agent 框架竞争激烈，Hermes、OpenClaw 各有所长。但如果你想找一个能长期陪伴、持续进化的 Agent，Hermes 值得认真试试。官方仓库：https://github.com/NousResearch/hermes-agent文档：https://hermesagent.org