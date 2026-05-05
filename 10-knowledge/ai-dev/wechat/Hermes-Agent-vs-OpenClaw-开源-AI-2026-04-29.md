---
title: wechat Hermes Agent vs OpenClaw 开源 AI 2026 04 29
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: comparison
tags: [AI-Agent]
---

﻿---
title: Hermes Agent vs OpenClaw：开源 AI Agent 框架技术对决
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: summary
tags: [wechat, Agent, Hermes, OpenClaw, Claude, Skill]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777424653&ver=6689&signature=*v-ajZeICk2xwa3ehFVbHi4YfJqSCoX2Rx2w*eTYG-sESI7PjCLgzxihUPXRXMemzZKDDiRpFf8RTTE1W9fEAUu5Zqdp3z841AUk52CGNn2CulGEMExtvHuIYxM-ocV1&new=1
account: 程序改变世界
pubTime: 2026年4月28日 17:36
---

## 摘要

title: "Hermes Agent vs OpenClaw ：开源 AI Agent 框架技术对决" 当 Claude Code 成了 AI 编程助手的代名词，另一件事正在安静地发生：开源社区正在用两条完全不同的路径，试图重新定义「 AI Agent 」这件事应该怎么做。 本文不聊概念，直接拆开看——Hermes Agent 和 OpenClaw 的架构设计、记忆模型、 Skill 生态和实际场景表现各有什么长短。 一、定位：从第一天就不同的设计假设 两个项目的起点就决定了它们走向何方。 Hermes Agent 来自 Nous Research （翠鸟/Kingdial 模型系列的研究...

---

## 核心要点

（待整理）

---

## 原文（来源：程序改变世界）

title: "Hermes Agent vs OpenClaw ：开源 AI Agent 框架技术对决" 当 Claude Code 成了 AI 编程助手的代名词，另一件事正在安静地发生：开源社区正在用两条完全不同的路径，试图重新定义「 AI Agent 」这件事应该怎么做。 本文不聊概念，直接拆开看——Hermes Agent 和 OpenClaw 的架构设计、记忆模型、 Skill 生态和实际场景表现各有什么长短。 一、定位：从第一天就不同的设计假设 两个项目的起点就决定了它们走向何方。 Hermes Agent 来自 Nous Research （翠鸟/Kingdial 模型系列的研究团队），从一开始就把「全平台 AI 操作系统」当作目标。它的核心假设是：未来的 AI Agent 不是某个聊天窗口里的工具，而是渗透到工作流各处的智能体，所以需要同时对接消息平台、代码执行环境、定时任务系统。 OpenClaw 来自 sparklab.ai ，定位是 Claude Code 的开源对标。它的核心假设更聚焦：开发者需要一个能在本地跑起来的、行为和 Claude Code 一致的 Agent，所以优先保证 skill 格式兼容和 IDE 集成（ ACP 协议）。 这两个起点不一样——一个是操作系统思维，一个是工具思维。 二、 Agent 核心架构：循环模型 vs 上下文窗口 两者都采用标准的 Tool-Calling Agent 循环：接收消息 → 调用 LLM → LLM 返回 tool_calls → 执行工具 → 结果写回 context → 循环直到输出文本。 但内部实现有显著差异： Hermes Agent 的核心循环 (run_conversation)： 1. Build system prompt（加载 memory、skill context、用户 profile） 2. while iterations < max_turns(90): a. Call LLM（OpenAI-compatible message format + tool schemas） b. if tool_calls → handle_function_call() → append results → continue c. if text → return 3. 上下文压缩触发（自动）near token limit 关键特点：Tool Router 和 Skill Dispatcher 是独立模块，不是写死在主循环里的。这意味你可以注入自定义的工具发现逻辑。 Session 数据走 SQLite 持久化，hermes sessions list 可以随时回溯任何一次对话。 OpenClaw 的核心循环 更接近 Claude Code 的实现： context window 管理更紧， skill 以插件形式挂载在 ~/.openclaw/skills/ 下。 Honcho 作为记忆层通过文件 IO 读写历史。 架构差异直接影响的是：长时间任务的稳定性。 Hermes 的 90 轮 max_turns 配合自动压缩，比 OpenClaw 更适合跑需要几十步的复杂任务。 三、记忆系统：内置持久化 vs 插件扩展 这是两个框架实际体验拉开差距最明显的地方。 Hermes Agent 的记忆是系统级内置的： hermes memory status 它用 SQLite 存 session transcript ，用 memory tool 读写结构化记忆，用 session_search 跨会话搜索。记忆数据在 ~/.hermes/sessions/ 和 ~/.hermes/memory.jsonl 里，不依赖任何外部服务。 更关键的是记忆的来源多样性：不只是对话内容，还包括工具执行结果（tool_use 日志）、用户纠正（memory tool 的 add action ）、甚至 cron 任务的输出。这让 Hermes 能建立真正跨任务的项目模型。 OpenClaw 的记忆依赖 Honcho ： Honcho （也是 Nous Research 的项目）做得相当成熟，支持会话摘要、记忆向量化和召回。但它是独立安装的插件，需要额外的配置流程。对于不需要长期 Agent 的用户这是优点（更轻），但对于想把 Agent 当作固定工作搭档的用户，这增加了上手成本。 四、 Provider 体系：开放生态 vs 深度绑定 Hermes 支持 20+ LLM provider ： 类型 Provider 通用 OpenRouter, Anthropic, OpenAI, DeepSeek 国产 MiniMax, Kimi/Moonshot, DashScope, Qwen, GLM, Xiaomi MiMo 其他 xAI/Grok, Google Gemini, Hugging Face, Copilot, Vercel AI Gateway Credential Pool 是 Hermes 独有设计：同一 provider 可以配置多个 API Key ，轮询使用，单个 key 耗尽时自动切换。对于日均调用量大的用户，这不只是省钱的问题——它意味着Hermes 的 Agent 不会因为模型 API 限流而中断。 OpenClaw 目前更偏重 Claude 系列，对 Anthropic API 的集成最深。如果你的工作流强依赖 Claude 3.5 Sonnet 或 Opus ， OpenClaw 的体验更无缝。 五、 Gateway 架构：跨平台工具调用 这是 Hermes 最具差异化的部分，也是 OpenClaw 完全没有对标的功能。 Hermes Gateway = 多平台消息路由 + 工具调用代理： User(WeChat) → Gateway → Hermes Core → Terminal Tool → 执行 uptime ↑ ↓ User(Telegram) ← Gateway ← 结果处理 ←─────────────────────┘ 你在微信里说「帮我看看服务器负载」， Gateway 接收消息、转给 Agent Core 、执行 uptime、结果通过 Gateway 推送回微信——整个链路是闭环的，而且每一步都有完整的权限控制和操作日志。 支持的平台： Telegram / Discord / Slack / WhatsApp / Signal / Matrix / Email / SMS / Mattermost / DingTalk / Feishu / WeCom / Home Assistant / WeChat / API Server / Webhooks Gateway 还支持 /webhook subscribe 接收外部事件触发 agent 任务，以及原生 Cron 调度。这意味着你可以建一个「每天早上 9 点查 GitHub issues 、汇总发给 Slack 」的自动化工作流，完全不需要写服务器代码。 OpenClaw 没有 Gateway。它的设计哲学是「你在哪个环境用，就专注那个环境」——CLI 用户用 CLI ， IDE 用户用 IDE 。 六、 Skill 系统：同源但分化 两个框架 Skill 格式完全兼容（都是 SKILL.md + YAML frontmatter ），但社区走向已经开始分化： Hermes Skill 生态的特点： - 按领域分类（ autonomous-ai-agents 、 content-generation 、 mlops 、 research...） - Skill 可以携带完整的工作流：参考文档 + 模板 + 脚本 + 依赖说明 - 支持 hermes skills tap add <github-repo> 直接从 GitHub 安装 - 社区 registry ：hermes skills browse OpenClaw Skill 生态的特点： - 聚焦开发工作流（代码审查、测试、 CI/CD...） - 与 Claude Code 官方 skill 完全互换 - 社区更小但更专注编程场景 说到这里必须提一句： WeWrite （本文写作用的 Skill ）同时支持 Hermes 和 OpenClaw ，格式完全兼容。 Skill 格式的统一是这两个项目对社区最实在的贡献之一。 七、实际场景：谁更好用？ 场景 1 ：跨国团队协作（多语言、多时区） Hermes ：把同一个 Agent 同时接入 Slack （美国团队）和 DingTalk （国内团队），用中文在美国团队的 channel 里推任务进度。 OpenClaw ：本地开发机跑，处理 PR review ，更专注。 场景 2 ： 24/7 自动化监控 Hermes ：配置 cron job ，每小时抓一次服务器 metrics ，异常时发微信告警。 OpenClaw ：不擅长这个场景——它设计上是按需触发的，不是守望型的。 场景 3 ：日常编码助手 两者都很强。 OpenClaw 的 IDE 集成（ ACP 协议）略好； Hermes 的记忆让你在项目里切来切去时不用每次重新解释项目结构。 八、技术规格一览 Hermes Agent OpenClaw License MIT MIT 开发者 Nous Research sparklab.ai 主要语言 Python Python 配置文件 ~/.hermes/config.yaml ~/.openclaw/config.yaml Session 存储 SQLite 文件（ Honcho 可选） 工具集 20+ toolsets （ terminal/file/web/vision...） 基础 toolsets MCP 支持 ✅ 原生 ✅ 基础 ACP/IDE 集成 ✅ ✅ 深度 定时任务 原生 cron 需插件 消息平台 15+ 无 Provider 数 20+ 以 Claude 为主 Skill 格式 SKILL.md SKILL.md （兼容） 九、怎么选？ 选 Hermes Agent ，如果： - 你需要跨平台 Agent （微信/Telegram/邮件同时在线） - 你的团队或工作流涉及多个 LLM provider - 你需要长期记忆、项目级上下文积累 - 你在树莓派、 NAS 或自建服务器上跑 Agent - 你需要定时任务 + webhook 的自动化能力 选 OpenClaw ，如果： - 你的核心场景是 IDE 编程助手 - 你高度绑定 Anthropic Claude 系列 - 你喜欢更轻量的上手体验 - 你主要在本地 Mac/Linux 机器上工作 - 你需要与 Claude Code 格式完全兼容的 skill 两者都试一下也是合理答案——hermes claw migrate 可以把你 OpenClaw 的配置一键迁过去，成本很低。