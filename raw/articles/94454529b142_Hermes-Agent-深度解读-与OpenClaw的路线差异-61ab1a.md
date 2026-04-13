---
title: "Hermes Agent 深度解读，与OpenClaw的路线差异"
created: 2026-04-11
updated: 2026-04-13
layer: raw
type: article
tags: ['AI-Agent', 'hermes', 'OpenClaw', ' Nous Research', '架构分析']
source_url: ""
source_domain: ""
archived: false
---


---
layer: raw
title: Hermes Agent 深度解读, 与OpenClaw的路线差异
layer: raw
author: A不AI
layer: raw
                    A不AI
layer: raw
date: 2026年4月12日
layer: raw
cover: /assets/img/news/Hermes Agent 深度解读, 与OpenClaw的路线差异-0.png
layer: raw
head:
layer: raw
  - - meta
layer: raw
    - name: 新闻
---
      
Hermes Agent要解决的不是“这一轮怎么把任务做完”，而是另外五个更难、也更接近真实使用的问题：

第一，Agent 不应该只活在本地终端里，它应该可以长期跑在云上，被 Telegram、Discord、Slack、WhatsApp、Email 等不同入口随时唤起。

第二，Agent 不应该每次开新会话都失忆，它需要有受控的长期记忆、跨会话检索，以及对用户的持续建模。

第三，Agent 不应该只会临时完成任务，它还应该把有效做法沉淀成 skill，形成可复用的程序性记忆。

第四，Agent 不应该只会串行思考，它应该能把部分任务拆给隔离的 subagent，并用更低的上下文成本并行推进。

第五，Agent 不应该只是“产品前端”，它还应该反过来为下一代 tool-calling 模型提供轨迹数据、评测环境和训练接口。

把这些目标放在一起看，Hermes Agent 的定位就变了。

它不是单点能力型产品，而是一个把“交互入口、执行环境、工具系统、调度系统、记忆系统、技能系统、训练数据闭环”揉成一体的 agent runtime。

截至 2026 年 4 月 12 日，这个仓库在 GitHub 上已经有 6.0 万以上 star，并持续霸榜 Github 趋势榜单. 最新 release 是 2026 年 4 月 8 日发布的\`Hermes Agent v0.8.0\`。它的增长速度和更新节奏都说明，这不是一个停留在概念层的实验项目，而是在快速向“可长期使用的 agent 基础设施”收敛。

#   

## 它最值得注意的，不是功能多，而是产品边界变了

今天很多 Agent 产品，核心还是“把模型接进编辑器或网页，再给它几个工具”。

这种做法当然有用，但它的默认假设是：用户和 agent 同时在线，任务主要发生在一个前端里，记忆是短时的，执行是会话内的，任务结束后系统大多也就结束了。

Hermes Agent 的假设不一样。

它把 agent 看成一个持续存在的后台实体。你可以在 CLI 里和它说话，也可以在 Telegram 上给它发一句话，让它去云端机器上干活；你可以让它在夜里跑定时任务，也可以几天后回来继续接着聊；你可以让它保留用户偏好、工程约束、历史会话摘要，还可以把复杂工作流沉淀成技能，下次直接调用。

这意味着 Hermes Agent 的竞争对手，并不只是其他“会调用工具的 agent”。

它更像是在同时和几类东西竞争：

一类是本地编码 agent，比如只在终端或 IDE 内工作的系统；

一类是聊天机器人平台，它们能接 Telegram 或 Slack，但通常没有完整的工具执行和长期记忆闭环；

还有一类是自动化平台，它们能做 cron 和通知，但缺少通用 agent 的推理与工具组合能力。

Hermes Agent 的野心，是把这些层拼起来，变成一个统一系统。

#   

## 从架构上看，Hermes Agent 更像一个 Agent Runtime

Hermes Agent 的源码结构其实已经把这个定位写得很清楚了。

它的核心入口不是单一前端，而是一组入口层：CLI、Messaging Gateway、ACP 编辑器适配、Batch Runner、API Server。无论用户从哪里进入，最后都会落到同一个核心执行引擎 \`AIAgent\`。

按官方架构文档的描述，Hermes 的整体路径大致是：

用户输入先进入 CLI 或 Gateway；

随后进入\`AIAgent\`；

\`AIAgent\`负责拼装系统提示词、解析 provider 与 API 模式、生成工具 schema、发起模型调用、执行工具、写回会话状态；

会话状态落在 SQLite 与 FTS5 上；

终端、浏览器、Web、MCP 等具体能力，则由独立工具后端承接。

这套结构带来两个直接后果。

第一个后果是，Hermes Agent 不是“某个平台的一个壳”，而是有独立中枢的。

第二个后果是，它天然适合被部署成长期运行进程，而不是一次性脚本。

这也是为什么它把 Messaging Gateway 设计成单独常驻进程，并在里面同时管理消息路由、session、cron tick、voice 和平台回传。对于普通聊天机器人来说，这种设计可能显得偏重；但如果你真想让 agent 变成一个随时能被唤起、能跨平台连续工作的数字实体，这反而是更合理的工程组织方式。

#   

## Hermes Agent 真正的核心，不是工具调用，而是“学习闭环”

Hermes Agent 最值得细看的地方，是它反复强调的 built-in learning loop。

这不是一句简单的 marketing slogan。

从文档和代码结构看，它至少由四层组成。

##   

### 第一层：受控的持久记忆

Hermes 没有一上来就做“无限记忆”，而是先做了两个很克制的本地记忆文件：\`MEMORY.md\`和\`USER.md\`。

前者存环境事实、项目约束、工作流经验；后者存用户偏好、沟通方式、长期习惯。

更重要的是，这两个记忆在会话开始时会被冻结成 prompt snapshot，而不是每次写入后立即改写系统提示词。

这个设计背后其实是一个很成熟的工程判断：长期记忆当然重要，但如果每次都动态改 prompt，会破坏 prompt cache 稳定性，也会让系统状态变得难以理解。

Hermes 选择了“写入实时落盘，注入下轮生效”的策略。

这会让记忆系统稍微慢半拍，却换来更稳定的缓存命中、更清晰的系统语义，以及更容易控制的上下文结构。

这比很多“只要用户说了就马上改系统提示”的 agent 设计更像生产系统。

##   

### 第二层：跨会话检索，而不是只靠 prompt 常驻

很多 agent 一说长期记忆，就陷入一个误区：把更多历史内容塞回 prompt。

Hermes 不是这么做的。

它把完整历史会话存进 SQLite，并用 FTS5 做全文检索，再通过\`session\_search\`在需要时回捞过去谈过的内容。

这意味着它把“常驻上下文”和“按需召回”分开了。

常驻上下文只保留最重要、最稳定的信息；

大量历史细节不常驻，只在需要时被搜索和总结。

这个分层非常重要，因为真正可扩展的 agent 记忆，几乎都必须走这条路。否则会话一长，token 成本和上下文污染都会迅速失控。

##   

### 第三层：Skill 作为程序性记忆

Hermes 的 skill 系统不是简单的 prompt 模板库。

它的文档把 skill 明确定义成 procedural memory，也就是“怎么做一类事情”的记忆，而不是“事实是什么”的记忆。

这和\`MEMORY.md\`、\`USER.md\`构成了一个很清晰的分工：

memory 负责记事实；

skill 负责记方法。

而且 Hermes 在 skill 上用了 progressive disclosure 设计。系统不会一口气把所有 skill 全部塞进上下文，而是先给一个压缩的索引，只有当 agent 判断某个 skill 真相关时，才加载对应\`SKILL.md\`，必要时再继续加载 reference、template、script。

Agent 要想真正拥有一个不断增长的 skill 库，前提就是 skill 不会把日常会话的上下文成本炸掉。Hermes 在这里的处理，比很多“把经验都堆进总提示词”的做法成熟得多。

更进一步的是，Hermes 允许 agent 自己用\`skill\_manage\`去创建、修改、删除 skill。

这就让“做完一次复杂任务”不再只产生一个结果，还可能顺手产出一段下次能复用的工作流。

如果说 memory 是 agent 的长期事实记忆，那么 skill 就是它的长期操作记忆。

##   

### 第四层：对用户的更深建模

Hermes 还接入了 Honcho 这类 memory provider。

这部分的意义，不在于“多接了一个插件”，而在于它承认了一件事：用户画像不一定只是一个静态偏好列表，它也可以是对长期行为模式的推断。

Honcho 的思路是，conversation 结束后再去做 dialectic reasoning，提取更深层的 conclusions，比如用户习惯、沟通风格、目标模式，而不是只保留显式说过的话。

这一步让 Hermes 的 memory 体系从“可用”进一步走向“有用户模型”。

当然，这也意味着更高的复杂性和更重的依赖，但从产品方向上看，它说明 Hermes 的目标不是做一个只会记标签的 agent，而是想做一个真的能随着互动变得更懂你的系统。

#   

## Agent 从“本地工具”变成了“可托管服务”

Hermes Agent 在 README 里一直强调一件事：它不绑定你的笔记本。

这句话背后其实有一整套设计。

与OpenClaw相同, 它支持本地、Docker、SSH、Daytona、Singularity、Modal 等多种 terminal backend；支持 Telegram、Discord、Slack、WhatsApp、Signal、Email、Matrix、WeCom、Weixin 等多消息入口；还把 cron 做成第一等能力，而不是外挂脚本。

这些能力组合起来，产生的是一种和主流编码 agent 很不一样的使用方式。

你不一定非要坐在电脑前开一个终端，盯着 agent 一步步跑。

你完全可以把它部署在云端机器上，让它在后台常驻，再通过聊天入口给它下任务、看进度、收结果。

从产品形态上说，这会让 Agent 更接近“个人后端”。

也就是说，它不只是一个交互界面里的智能体，而是一个长期驻留、具备执行权限、可被多入口访问、能自己跑计划任务的服务。

这也是为什么 Hermes 的 cron 不是传统 shell cron，而是“fresh agent session + attached skills + target delivery”。

它调度的不是脚本，而是 agent 本身。

一旦调度对象从 shell task 变成 AI agent，系统设计就不只是“什么时候执行”，还包含“以什么身份、带什么技能、用哪套工具、把结果回投到哪里”。

Hermes 显然在朝这个方向建。

#   

## 把“上下文成本”当成一等问题

这里面有几个很值得注意的设计。

第一，prompt 组装是分层的，而且区分 cached system prompt 和 API-call-time additions。

第二，memory snapshot 是冻结的，不在会话中段乱改。

第三，skill 采用 progressive disclosure，只在相关时展开。

第四，subagent 默认是完全新上下文，只把最终摘要回收到父 agent。

第五，长会话会做 context compression，而且压缩前先 flush memory，避免信息在压缩中丢失。

#   

## Subagent 设计

Hermes 提供\`delegate\_task\`，能把任务交给子代理并行处理，最多 3 个并发。

文档明确强调，subagent 启动时对父上下文一无所知，只知道你显式传给它的\`goal\`和\`context\`；它有自己的终端 session、自己的工具集，而且中间执行细节不会全部回灌到父 agent 的上下文里。

#   

## 为什么说它更像 Agent OS，而不只是 Agent App

如果把今天的大多数 agent 产品看成应用层，那么 Hermes 更像在搭一层 agent runtime 或 agent OS。

它有入口层。

它有统一执行内核。

它有可插拔 provider、toolset、memory provider、plugin。

它有 session store、FTS5 recall、prompt assembly、compression、approval flow。

它有长期后台进程，有 cron，有多平台 delivery。

它还有 batch trajectory generation、Atropos RL environment、训练数据格式压缩这些明显偏“模型基础设施”的模块。

也就是说，Hermes 既在服务最终用户，也在服务下一代 agent 模型的训练与评测。

这点非常像操作系统式产品的特征：它不只承载一个应用，而是在定义一套更底层的运行范式。

#   

## 当然，它也不是没有代价

Hermes Agent 的优势，恰恰也是它的门槛。

第一，它的系统边界很大。

当一个项目同时覆盖 CLI、消息网关、定时任务、工具运行时、长期记忆、技能管理、插件系统、训练轨迹时，复杂度一定会陡增。对普通用户来说，这意味着它很难像单点产品那样“打开即懂”。

第二，它更像一个需要托管和维护的系统。

如果你只想要一个在本地终端里偶尔帮你改代码的 agent，那么 Hermes 的很多能力会显得过重。它真正擅长的，是长期运行、多入口触达、需要记忆和调度的使用场景。

第三，它的很多价值来自系统协同，而不是某一个瞬间惊艳的 feature。

这也是 Hermes Agent 最有意思的地方。

它不像很多 agent 项目那样，重点在证明“模型现在已经能自主做很多事”。

它更像是在回答另一个问题：

如果默认前提是 agent 会长期存在、会跨入口工作、会积累经验、会被调度、会产生训练数据，那么这个系统应该怎样被组织？

  

## 与OpenClaw的路线差异

围绕 Hermes Agent 的公开讨论里，一个非常高频的关键词就是 \`OpenClaw\`。

这不是偶然。

因为 Hermes 官方已经把迁移写成了正式产品路径。README 和官方文档里都直接提供了 \`hermes claw migrate\`，而且迁移范围不是简单导入几个配置项，而是明确覆盖 persona、memory、skills、消息平台设置、命令 allowlist，甚至还包括部分 API key。

一个项目如果把“从另一个 agent 生态迁移过来”做成内建命令，说明它的目标用户并不只是新用户，也包括那些已经在上一代 agent 运行方式里生活过一段时间的人。

但更值得注意的，不是“它能迁移”，而是“迁移文档暴露了两套系统真正不同的地方”。

Hermes 的迁移文档里明确写到，一些 OpenClaw 时代的对象在 Hermes 里并没有直接等价物，比如 \`HEARTBEAT.md\`、\`BOOTSTRAP.md\`、旧 cron 配置、部分插件与 hooks 配置。这些内容不会被原样照搬，而是会被打包进归档目录，提示用户手动转换成 Hermes 的 context files、skills 或新的 cron 任务。

这说明了：它们在很多表层功能上相似，但系统组织方式已经变了。

OpenClaw 语境里的一些能力单元，到了 Hermes 这里，被重新分解进了 skill、memory、context file、gateway、cron 这些新的边界里。

也就是说，这不是简单替代，更像是一次 runtime 重构。

如果再看最近的公开讨论，会发现用户对两者的对比，正在逐渐收敛成几条主线。

第一条主线：可预测性，对上灵活性

OpenClaw 一侧最近公开发布的对比文章，给出的核心表述其实非常直白：Hermes 代表的是最大控制权，OpenClaw 代表的是更高的确定性。

这种说法当然带有明显立场，但它点中的矛盾是真实存在的。

Hermes 的优势，是你几乎可以改任何东西，自己选模型、自己托管、自己配工具、自己接本地推理、自己管理 skill、memory 和 gateway。

代价则是，成本结构、部署复杂度、长期维护压力，也更容易落回用户自己身上。

OpenClaw 那一边更强调的是“拿来就用”和成本可预期。

所以它们真正分开的地方，不只是 feature list，而是用户到底想要一个“自己搭起来的 agent 系统”，还是一个“尽量少操心的 agent 服务”。

  

第二条主线：消息入口时代的 agent，正在分化成两类产品

这也是最近讨论里很明显的一点。

OpenClaw 长期被很多人当成“消息平台里的 AI 助手系统”来使用；而 Hermes 虽然同样重视 Telegram、Discord、Slack、WhatsApp 这些入口，但它在结构上更强调整个统一运行时，尤其是 skill、memory、subagent、cron、provider routing 这些底层能力如何拼到一起。

  

换句话说，两者都重视消息入口，但关注点已经不一样了。

OpenClaw 更像从“可直接使用的 assistant”出发。

Hermes 更像从“可长期托管的 agent runtime”出发。

这个差异，在迁移文档里也能看出来。Hermes 迁移的不只是聊天配置，而是试图把用户原有的 persona、长期记忆、skill 和工作方式都吸纳进自己的系统结构里。

  

第三条主线：最近一波迁移，背后不只是功能比较，也有外部环境变化

在最近的 Reddit 讨论里，已经能看到一些很具体的迁移动机。

例如在 2026 年 4 月的一条帖子里，有用户明确提到，自己从 OpenClaw 切到 Hermes，其中一个触发因素是 2026 年 4 月 4 日前后的 Anthropic 计费与第三方 harness 使用变化。这里需要说明，这个说法来自用户帖子，不是官方迁移公告本身，但它至少说明了一点：这波迁移并不只是“谁功能更强”，也和外部 provider 政策变化有关。

另一类讨论则更朴素。有用户在并行运行 Hermes 和 OpenClaw 时，提到两者在同一台机器、同一个 Telegram 体系下可能出现 gateway 或 pairing 冲突；也有用户直接把自己偏向 Hermes 的原因总结成四个词：skills、memory、updates、day-to-day usability。

这些讨论未必能代表全部用户，但它们共同指向了一个趋势：

Hermes 现在吸引 OpenClaw 用户的地方，越来越不是单一亮点，而是整套系统在长期使用中的连贯性。

也就是你用得越久，越会在意 memory 怎么存、skill 怎么长、session 怎么找回、cron 怎么投递、provider 怎么切换、gateway 怎么稳定，而不只是“第一次演示时能不能自动做一件很酷的事”。

  

所以，Hermes 和 OpenClaw 的真正差异，不该只按功能表来理解

如果只看功能表，很多结论都会很浅。

两边都有消息入口，都能调用模型，都能做自动化，都能承接 agent 工作流。

真正的区别更像是：

OpenClaw 更接近一个偏使用导向、偏助手导向、偏可直接部署体验的产品路径。

Hermes 更接近一个偏系统导向、偏 runtime 导向、偏长期积累与自我组织能力的产品路径。

前者更强调“把 agent 用起来”。

后者更强调“把 agent 养起来”。

这也是为什么 Hermes 在 OpenClaw 语境里显得特别有意思。

它不是在做一次温和优化，而是在试图把 agent 从“会话中可用的助手”，进一步推进成“长期存在的、可调度的、会沉淀经验的系统实体”。

  

  

  

  

  

参考资料

  

Hermes Agent 仓库首页，https://github.com/NousResearch/hermes-agent

Hermes Agent 官方文档首页，https://hermes-agent.nousresearch.com/docs/

Hermes Agent Architecture，https://hermes-agent.nousresearch.com/docs/developer-guide/architecture/

Hermes Agent Agent Loop Internals，https://hermes-agent.nousresearch.com/docs/developer-guide/agent-loop/

Hermes Agent Prompt Assembly，https://hermes-agent.nousresearch.com/docs/developer-guide/prompt-assembly/

Hermes Agent Persistent Memory，https://hermes-agent.nousresearch.com/docs/user-guide/features/memory/

Hermes Agent Skills System，https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/

Hermes Agent Subagent Delegation，https://hermes-agent.nousresearch.com/docs/user-guide/features/delegation/

Hermes Agent Messaging Gateway，https://hermes-agent.nousresearch.com/docs/user-guide/messaging/

Hermes Agent v0.8.0 Release，https://github.com/NousResearch/hermes-agent/releases/tag/v2026.4.8

Migrate from OpenClaw | Hermes Agent，https://hermes-agent.nousresearch.com/docs/guides/migrate-from-openclaw

OpenClaw vs Hermes Agent: The Honest Comparison Nobody Asked For，https://www.getopenclaw.ai/blog/openclaw-vs-hermes-agent

\[Megathread\] Migrating from OpenClaw to Hermes? Read this first.，https://www.reddit.com/r/hermesagent/comments/1sfezio/megathread\_migrating\_from\_openclaw\_to\_hermes\_read/

Moved from OpenClaw to Hermes, now lost on provider choice, what are you using?，https://www.reddit.com/r/hermesagent/comments/1scgv91/moved\_from\_openclaw\_to\_hermes\_now\_lost\_on/

Heads up: running Hermes + OpenClaw on the same server without containers can get messy，https://www.reddit.com/r/hermesagent/comments/1sih7zh/heads\_up\_running\_hermes\_openclaw\_on\_the\_same/