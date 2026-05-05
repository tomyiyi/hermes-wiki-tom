---
title: wechat Hermes Agent 周报 3 2026 04 28
created: 2026-04-28
updated: 2026-04-28
layer: processed
type: comparison
tags: [AI-Agent]
---

﻿---
title: Hermes Agent 周报#3
created: 2026-04-28
updated: 2026-04-28
layer: processed
type: summary
tags: [wechat, hermes, TUI, Hermes, Agent, Slack]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777345020&ver=6687&signature=*4-khTFI20t6BS2UslExNqGkbPNOGEZB9Hq5lAM4rhyruj3wVwif*-Rp388BjmL9lSD8hi1CpxVqOPCAYMhGL4hoUIk26wAboGX*6Vi36oKc5S9H9L5aWNWGo-9NFSoC&new=1
account: 小星AI技术笔记
pubTime: 2026年4月27日 14:26
---

## 摘要

> 📢 这是「Hermes Agent 周报」第 3 期，记录 4月20日-4月26日的项目动态。 > 每周一更新，帮你省下刷 GitHub 的时间。 > 觉得有用就收藏+关注，不错过每周更新 👋 --- 📊 本周速览 这周的数据离谱到我要确认一下是不是脚本写错了。 | 指标 | 数据 | |------|------| | 提交数 | 1,151 个 | | 新功能 | 150 个 | | Bug修复 | 595 个 | | 贡献者 | 260 人 | | 当前版本 | v2026.4.23 (v0.11.0) | 一句话：Hermes Agent 发了 v0.11.0 大版本，代号"...

---

## 核心要点

（待整理）

---

## 原文（来源：小星AI技术笔记）

> 📢 这是「Hermes Agent 周报」第 3 期，记录 4月20日-4月26日的项目动态。 > 每周一更新，帮你省下刷 GitHub 的时间。 > 觉得有用就收藏+关注，不错过每周更新 👋 --- 📊 本周速览 这周的数据离谱到我要确认一下是不是脚本写错了。 | 指标 | 数据 | |------|------| | 提交数 | 1,151 个 | | 新功能 | 150 个 | | Bug修复 | 595 个 | | 贡献者 | 260 人 | | 当前版本 | v2026.4.23 (v0.11.0) | 一句话：Hermes Agent 发了 v0.11.0 大版本，代号"The Interface Release"。TUI 重写、Transport 抽象层、AWS Bedrock、QQBot——这周的量够别的项目肝半年。 --- 🆕 重磅新功能 1. TUI 全面重写：React/Ink 接管终端交互 以前 hermes --tui 的终端界面就是个命令行换皮。这周不一样了——底层全部重写。 > commit cluster by @Brooklyn Nicholson + @Teknium 是什么：TUI 现在基于 React/Ink 构建，Python JSON-RPC 做后端。差不多 310 个提交全砸在这一块。 实际体验上的变化： 底部输入框固定不动（sticky composer），不像以前要滚动找输入位置 直播输出有 OSC-52 剪贴板支持——远程 SSH 也能复制代码了 状态栏显示当前 git 分支 + 本轮耗时 /clear 有确认提示，手残党福音 子任务（subagent）有专用观测层，能看子代理在干啥 暗色/亮色主题切换，对眼睛友好 我的点评：之前我对 TUI 的态度一直是"能用就行"。但这次重写之后，我试了一下……回不去了。特别是那个 sticky composer，以前要 ⌘+↑ 翻到输入框，现在一直就在底部，体验差距巨大。 本周还在继续打磨：FPS 计数器（HERMES_TUI_FPS=1）、todo 面板可以折叠归档、滚轮加速状态机从 Claude Code 搬过来的。对，你给 Claude Code 打赏那套滚轮体验，现在 Hermes 也有了。 # 试试新 TUI hermes --tui 想看实时 FPS？ HERMES_TUI_FPS=1 hermes --tui --- 2. Transport ABC + Native AWS Bedrock 是什么：之前所有模型的 API 调用都挤在 run_agent.py 里，一个大 switch-case 处理各种格式转换。现在拆成了 agent/transports/ 下的插件式结构： AnthropicTransport — Anthropic Messages API ChatCompletionsTransport — OpenAI 兼容 ResponsesApiTransport — OpenAI Responses API BedrockTransport — AWS Bedrock Converse API 每个 transport 自己管格式转换和 API 调用，互不干扰。 > commit: #10549, #13347, #13430 by @kshitijk4poor + Teknium 我的点评：这种重构看着"不性感"，但懂的都懂——之前跑 run_agent.py 的时候加一个新 provider，得改 3 个文件还得祈祷别动到其他逻辑。现在往 transports/ 丢一个类就行了。AWS Bedrock 的用户终于不用自己写适配层了。 --- 3. Kanban 看板：多用户协作白板 说个坑——我之前用 Hermes 做项目管理的时候，每次重启会话状态就没了。想要跨设备同步？想多了。 > commit: 15937a6b by @Teknium 这周上了个 kanban 子命令，支持多用户协作看板。状态是持久的（durable），意味着你关了终端再打开，看板还在。 # 创建看板 hermes kanban create "我的项目" 邀请协作 hermes kanban invite @teammate 我的点评：就……挺需要的。一个 Agent 框架带原生看板，说实话一开始觉得有点怪。但仔细一想，Agent 帮你跑任务，看板帮你跟踪进度，这两个东西放一起挺合理。 --- 4. Slack 原生斜杠命令 + 严格提及模式 > commit: 087e74d4 by @Teknium 之前 Hermes 在 Slack 里的命令是通过消息内容解析的，体验上对比 Discord/Telegram 总差一截。这周把 所有 gateway 命令都注册成原生 Slack 斜杠命令了。 另外加了个 slack.strict_mention 开关，开之后只有 @提到机器人 bot 才会响应——防止你的下班闲聊被 Agent 截胡打断。 > commit: aea4a90f by @Ching --- 5. 浏览器：云模式自动拉起本地 Chromium > commit: 42c076d3 by @Teknium 你在云上跑 Hermes（比如 Modal 或者自己的 VPS），想在浏览器工具里访问 localhost:3000 或者 192.168.1.x？ 之前不行——远程 Chromium 连不到你的本地服务。 现在它会自动检测 LAN/localhost URL，然后在你本机拉起一个本地 Chromium。配置是零的，detect 到了就自动做。 --- 🔧 重要改进 hermes fallback 命令 (1e37ddc9) — 现在可以管理 fallback provider。一个模型挂了，自动切到备胎。 Skills 状态显示 (0e2a53ea) — skills list 现在能看是 enabled 还是 disabled。之前你得自己去翻配置文件才知道哪个技能是开着的。 /queue, /bg, /steer 提示 (eaa7e2db) — Agent 运行中时，placeholder 里会提示你这些命令。新手友好。 首次使用引导 (ffd26210) — 新用户第一次用 TUI 时，会弹出 /busy 和 /verbose 的上下文提示。说实话这个早该有了。 审批黑名单 (eb28145f) — hardline blocklist 可以配置不可恢复的命令（比如 rm -rf /），Agent 想执行也不行。 模型目录远程化 (85536690) — OpenRouter + Nous Portal 的模型清单现在从远程拉取，不用等发布更新就能看到新模型。 Azure Foundry 支持 (731e1ef8) — 自动探测 transport、模型列表和 context length。 hermes update --check (dc5e02ea) — 只想看看有没有新版本，不想真的更新？ hermes update --check 输出: Latest: v2026.4.23, yours: v2026.4.16 — update available --- 🐛 关键 Bug 修复 本周 595 个修复，我挑几个影响面大的说一下： TUI 渲染修复 — 这个系列大概有 20+ 个 commits，重点解决：流式输出时 markdown 渲染错位、todo 面板浮动定位、思考块（thinking）段落格式、工具面板和转录合并问题。如果你这周之前用过 TUI 发现界面偶尔"抽风"，现在应该好了。 CLI -c 修复 (bde89c16) — hermes -c claude-code 会选错会话的问题。现在它选的是你最近用过的那个。 Slack 富文本引用 (6087e040) — Slack 里的引用块和列表现在能正确提取了，之前从 Slack 发的消息里带引用的内容，Hermes 看到的是一堆 JSON。 --- 📦 版本发布 | 版本 | 日期 | 一句话 | |------|------|--------| | v2026.4.23 (v0.11.0) | 2026-04-23 | The Interface Release — TUI 重写 + Transport 抽象 + AWS Bedrock + 5 个新推理路径 + QQBot | 从 v0.9.0 到 v0.11.0 的累积数据： > 1,556 commits · 761 merged PRs · 1,314 files changed · 224,174 insertions · 29 个社区贡献者（含 co-author 共 290 人） 升级： hermes update 或者从 GitHub 下载 pip install --upgrade hermes-agent --- 👀 值得期待 🔜 TUI 性能工具 — Brooklyn 给 profile harness 加了 --loop, --save, --compare，正在系统性地做性能基线 🔜 Hook 系统深化 — Shell hooks + Plugin hooks 刚落地，接下来应该会有更多内置钩子和社区插件 🔜 看板功能扩展 — Kanban 刚发布 v1，后续大概率会加时间线视图和与 todo 面板的同步 --- 💬 本周热议 GitHub 上这个版本讨论最热的是 Transport ABC 架构——社区争论的点是：为什么不直接用现有的 OpenAPI 规范，而要自己搞一套 transport 抽象层？ 项目组回应的大意是：OpenAPI 规范解决的是"API 长什么样"，但他们需要的是"不同的 API 怎么统一塞进同一个 agent loop"。两个维度不同。我觉得这个解释说得过去。 --- 📈 升级建议 > 本周有 重大版本发布。有少量破坏性变更（Transport 层重构可能影响自定义 provider 的配置），但官方已经提供了迁移指南。 > 建议升级——特别是如果你在用 TUI、AWS Bedrock，或者在 Slack 里用 Hermes。 > > 特别注意：如果你之前自定义过 provider 配置，升级后检查一下 config.yaml 中 provider 的 transport 字段是否兼容。 --- 升级后可以试试 几个我觉得值得上手的东西： 1. 打开 TUI：hermes --tui 然后按 ? 看所有快捷键。试试 /steer "说得简短点" 在对话中间打断它 2. 配置 fallback：hermes fallback add openrouter/anthropic/claude-sonnet-4 3. 试试看板：hermes kanban create "本周计划"，然后问它"帮我把这个看板加到 todo 里" 4. 配一个 Slack 斜杠：如果你们团队用 Slack，这个改动很值得试 --- 觉得有用？ 👍 点个赞，让更多人看到 Hermes Agent 在做什么。 有问题？ 💬 评论区聊聊，我每周都会回复。 想第一时间收到？ 🔔 关注专栏，每周一自动推送。 --- > 本文由「小星AI」整理发布，数据来源：NousResearch/hermes-agent > 专栏持续更新中，欢迎订阅 ✨ 📝 每天一篇 AI 实战干货 Cursor · Claude Code · AI Agent · MCP 协议 👆 长按关注「小星AI」，技术路上不迷路