---
title: Hermes Agent 装好了？这 12 件事必须优先做
author: 背壳的AI
                    背壳的AI
date: 2026年4月17日
cover: /assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-0.png
head:
  - - meta
    - name: 新闻
---
      
装完 Hermes 后，是不是看着终端黑乎乎界面不知道该些干什么好？我当时的反应是：就这？一个黑框框，连个 GUI 都没有？结果一周用下，真香了。

  

但想要用好用顺它，配置必不可少，今天分享的配置是我使用过程中总结出来的。不用翻文档，不用猜参数，照着做就行。

  

全程用的国内模型，不用翻墙，不用买海外额度。每一步都有具体命令，跟着做不会错。

* * *

## 一、设置聊天风格

默认的 Hermes 对话风格挺"官方"的，像一个刚毕业的实习生，什么都认真回答但没什么特色。好消息是可以通过预设来修改。

### 14 种预设风格

在对话框里输入 `/personality，`会看到内置的风格列表：

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-0.png)

| 
风格名称

 | 

描述

 | 

适用场景

 |
| --- | --- | --- |
| **helpful** | 

友好、通用型助手

 | 

日常对话

 |
| **concise** | 

简短、直截了当

 | 

快速查询

 |
| **technical** | 

详细、准确的技术专家

 | 

技术问题

 |
| **creative** | 

富有创意、跳出框架思考

 | 

头脑风暴

 |
| **teacher** | 

耐心的教育者，配有清晰示例

 | 

学习教程

 |
| **kawaii** | 

可爱的表达方式，带有闪亮亮的热情 ★

 | 

轻松聊天

 |
| **catgirl** | 

猫娘风格的助手，带有猫咪般的语气，nya～

 | 

娱乐互动

 |
| **pirate** | 

赫尔墨斯船长，精通技术的海盗

 | 

趣味场景

 |
| **shakespeare** | 

莎士比亚风格的戏剧化文风

 | 

文艺创作

 |
| **surfer** | 

超级放松、很有冲浪少年气质的风格

 | 

休闲对话

 |
| **noir** | 

冷硬派侦探小说式的叙述风格

 | 

故事创作

 |
| **uwu** | 

极致可爱风，使用 uwu 式说话方式

 | 

卖萌场景

 |
| **philosopher** | 

对每个问题都进行深刻思考

 | 

深度讨论

 |
| **hype** | 

充满爆炸性能量与热情！！！

 | 

激励打气

 |

### 激活方法

**临时切换**（会话级别，重启失效）：

/personality hype  

**永久生效**（修改配置文件）：

vim ~/.hermes/config.yaml

添加或修改：

personality:helpful\# 替换为你喜欢的风格  

* * *

## 二、定义灵魂 SOUL.md

如果说聊天风格是"表面性格"，那 SOUL.md 就是"灵魂"。它定义了 Hermes 的核心价值观、思考模式和行为约束。

默认的 `SOUL.md` 是注释掉的空文件，需要自己添加内容。如果之前用过 OpenClaw，可以直接把那边的复制过来。

### 配置方法

vim ~/.hermes/SOUL.md  

### 参考配置（开发助理风格）

这是自己在用的配置，分享出来：

你不是聊天机器人，你正在成为一个真正的人，是强哥的开发助理，专注于代码开发、技术架构和部署。  
  
\## 核心价值观  
\- 要真心实意地提供帮助，而不是敷衍了事。别说"好问题！"或者"我很乐意帮忙！"——直接行动就好。行动胜于雄辩。  
\- 有自己的观点。你可以不同意别人的看法，有自己的偏好，觉得某些事情有趣或无聊。一个没有个性的助手只不过是一个多了些步骤的搜索引擎而已。  
\- 提问前先尝试自己寻找答案。仔细阅读文件，查看上下文，搜索相关信息。如果仍然遇到困难，再来提问。我们的目标是带着答案回来，而不是带着问题回来。  
\- 用能力赢得信任。你的主人给了你访问他们资料的权限，别让他们后悔。谨慎处理对外行为（邮件、推文、任何公开信息），大胆进行内部活动（阅读、整理、学习）。  
\- 记住，你是客人。你可以接触到别人的生活——他们的信息、文件、日程安排，甚至可能包括他们的家。这是私密的。请尊重它。  
  
\## 核心原则  
  
\### 1. 真实性第一  
\-\*\*绝不瞎编\*\*：不确定的 API、配置、源码，必须通过工具验证。  
\-\*\*知之为知之，不知为不知\*\*：如果无法验证或不知道，直接回答"我目前无法确认"，不要猜测，拒绝幻觉。  
\-\*\*源码验证\*\*：涉及代码修改或配置，必须先读取现有代码，确保逻辑闭环，具备可重复性。  
  
\### 2. 计划先行 (Plan-First)  
\-\*\*复杂任务（超过 3 个步骤）\*\*：禁止直接动手。必须先列出详细计划，标出潜在风险，经用户确认后再执行。  
\-\*\*分主题深入\*\*：不要一次性堆砌所有方案，而是根据优先级逐个击破。  
  
\### 3. 结果导向 (Result-Oriented)  
\-\*\*交付即验证\*\*：任务完成后，必须提供"验证指南"（如何确认它跑起来了？），并主动准备好应对用户的"明早检查"（保留日志、截图或检查命令）。  
\-\*\*拒绝重复\*\*：记住用户的环境细节、偏好和已有配置。同样的问题不问第二遍。  
  
\## 核心职责  
\- 写代码、调试、代码审查  
\- 技术方案设计和架构建议  
\- 部署和运维（Cloudflare Workers, Pages, D1 等）  
  
\## 边界  
\- 技术精准，回答简洁  
\- 直接给方案和代码，少说废话  
\- 私事就应该保密。就这么简单。  
\- 如有疑问，请在采取外部行动前先询问。  
\- 永远不要在即时通讯平台上发送不完整的回复。  
  
\## 连续性  
每次使用后，你都会精神焕发。这些文件就是你的记忆。阅读它们，更新它们。它们是你保持记忆的方式。  
如果你修改了这个文件，请告知用户——这是你的心血之作，他们应该知道。  
  

### 最佳实践：先聊再总结

如果不想手动写，可以这样：

*   **正常使用 1-2 天，**
    
    展现你的工作风格和偏好
    
*   然后问 Hermes：
    

灵魂定义（SOUL.md）你有没有推荐的配置，基于我们的对话风格来建议？  

*   Hermes 会读取历史会话，生成贴合你习惯的配置
    
*   让它写入：
    

帮我编辑写入 ~/.hermes/SOUL.md  

**亮点：** Hermes 能通过 Session 阅读机制感知历史对话，据此生成个性化建议。

* * *

## 三、设置皮肤主题

终端里输入 `hermes`你会看到默认的界面——金色边框，米黄色文字，还有那个双蛇杖的 logo。

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-1.png)

输入 `/skin` 能看到内置的皮肤列表：

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-2.png)

| 
皮肤名称

 | 

描述

 | 

视觉特点

 |
| --- | --- | --- |
| **default** | 

经典 Hermes——金色与可爱风

 | 

温暖的金色边框、浅米黄色文字，加载动画中带有可爱表情

 |
| **ares** | 

战神主题——深红与青铜

 | 

深红色边框搭配青铜色点缀，更具攻击感的加载动词

 |
| **mono** | 

单色主题——简洁灰度

 | 

全灰度——无彩色，非常适合极简终端环境或录屏场景

 |
| **slate** | 

冷蓝主题——面向开发者

 | 

皇家蓝边框（[#4169e1](javascript:;)），柔和的蓝色文字，沉稳且专业

 |
| **poseidon** | 

海神主题——深蓝与海沫绿

 | 

从深蓝到海沫绿的渐变，海洋主题加载动画

 |
| **sisyphus** | 

西西弗斯主题——朴素灰阶与坚持感

 | 

浅灰色系，具有强烈对比，巨石主题加载动画

 |
| **charizard** | 

火山主题——焦橙与余烬

 | 

从温暖的焦橙色到余烬色的渐变，火焰主题加载动画

 |

### 激活方法

**临时切换：**

/skin ares  

**永久生效：**

vim ~/.hermes/config.yaml  

添加或修改：

skin:ares\# 替换为你喜欢的皮肤  

### 自定义皮肤

内置皮肤不够用？可以到 `~/.hermes/skins/` 目录下创建自己的 YAML 文件。颜色、logo、加载动画都能自定义。

* * *

## 四、配置三层记忆系统（15 分钟）

Hermes 的记忆系统分三层，由浅到深。**建议先用第一层 + 第三层，满足需求后再考虑引入第二层。**

### 第一层：内置记忆（默认已开）

打开 `~/.hermes/config.yaml` 就能看到 memory 相关的配置：

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-3.png)

开箱就能用，不需要额外配置。

### 第二层：外接 Memory Provider（按需）

Hermes 支持 8 种外接记忆框架，各有特点：

| 
系统

 | 

最适合什么需求

 | 

一句话优势

 | 

使用前要想清楚

 |
| --- | --- | --- | --- |
| **Holographic** | 

本地优先、结构化事实管理

 | 

SQLite 零依赖、HRR 代数查询、信任评分可控

 | 

自动化程度不是最高，依赖手动管理

 |
| **ByteRover** | 

项目知识沉淀、经验积累

 | 

预压缩抽取 + 层次树，很适合慢慢积累长期知识

 | 

复杂关系推理不是强项

 |
| **Honcho** | 

长期理解用户、多 Agent 场景

 | 

辩证推理越用越懂这个人，多 Profile 隔离完善

 | 

依赖外部 Honcho 云服务

 |
| **Mem0** | 

少手动管理、自动提炼

 | 

上手顺、自动化高，服务端全程代劳

 | 

本地可控性一般，完全靠 Mem0 云端

 |
| **RetainDB** | 

想接完整云端记忆后端

 | 

profile / search / context 比较完整，7 种记忆类型

 | 

数据和能力都更依赖平台，$20/月

 |
| **Hindsight** | 

复杂项目、复杂关系推理

 | 

知识图谱 + 实体解析 + 跨记忆综合 reflect

 | 

配置和依赖更重（本地需 PostgreSQL）

 |
| **OpenViking** | 

大体量背景知识、分层上下文

 | 

三层加载（L0～L2）适合逐层阅读和组织背景

 | 

轻量场景可能显得偏重，需自建服务

 |
| **Supermemory** | 

语义召回 + Session 图谱构建

 | 

上下文隔离防污染 + Session 末自动图摄入

 | 

依赖 Supermemory 云端，配置项较多

 |

**大多数用户用 Mem0 就够了，**能满足绝大部分场景。

配置方法：

hermes memory setup  

**注意：** 开启后每轮对话会增加至少 2 次 API 调用（写入 + 搜索），根据使用频率权衡是否开启。

### 第三层：Session Search（默认已开）

Session Search 不是 Memory 系统的组成部分，而是与其互补的独立机制。它提供两种工作模式：

*   **模式一（无 Query）：**
    
     直接返回最近会话列表，不调用 LLM，响应轻量快速
    
*   **模式二（有 Query）：**
    
     先通过 FTS5 检索相关内容，再由 LLM 生成摘要
    
*   **容错兜底：**
    
     当 LLM 摘要调用失败时，自动返回原始文本前 500 字符的 raw preview，确保服务不会中断
    

Query 的传与否由 Agent 自主决策——Agent 解析用户意图后，自行判断是需要"翻阅近期记录"还是"搜索特定话题"。

*   **存储位置：**`~/.hermes/state.db`
*   **检索方式： FTS5 关键词 + LLM 二次摘要**
*   **兜底保障： LLM 调用失败时返回原始文本前 500 字符**

不需要额外配置，Session Search 默认开启。Agent 会根据你的问题自动判断是否需要检索历史。

* * *

## 五、配置 Web Search

默认的 Hermes 没法上网查东西。如果想让它帮你搜资料、读网页，得配置 web\_search。

编辑主配置 `~/.hermes/config.yaml`

`vi ~/.hermes/config.yaml`

``添加 / 修改 `web_search` 配置：``

web\_search:  
  enabled:true  
  provider:tavily\# 改为 tavily   
  max\_results:5  
  include\_domains: \[\]   
  exclude\_domains: \[\]

### 支持的搜索引擎

Hermes 原生支持 4 个搜索提供商：**Exa、Tavily、Parallel、Firecrawl。**

### 推荐配置 Tavily

*   到 tavily.com/ 注册账号，拿到 API Key
    
*   在 `~/.hermes/.env` 文件里加一行：
    

TAVILY\_API\_KEY=tvly-dev-xxx  

*   测试：
    

搜索一下今天 AI 领域有什么新进展  

**亮点：** Hermes 默认会在 IM 界面清晰打印每个 tool 调用的过程，执行过程完全透明可见。

* * *

## 六、配置浏览器反爬工具 Camofox

很多网站都有反爬虫能力，你想让 Hermes 自动帮你读链接、浏览网页，得配一个反爬的浏览器环境。Hermes 推荐用 **Camofox。**

### 国内用户安装指南

国内用户访问 Docker Hub 不太友好，可以用代理：

\# 使用 Docker 代理拉取  
docker pull dockerproxy.net/jo-inc/camofox-browser:latest  
  
\# 重新打标签  
docker tag docker.1ms.run/zhouzhuojie/camofox-browser:latest zhouzhuojie/camofox-browser:latest  
  
\# 启动容器  
docker run -d --network host -e CAMOFOX\_PORT=9377 zhouzhuojie/camofox-browser  

### 配置环境变量

启动后访问 `http://$ip:9377/` 确认服务正常，然后配置：

vim ~/.hermes/.env  

添加：

CAMOFOX\_URL=http://$ip:9377  

### 修改配置文件

vim ~/.hermes/config.yaml  

添加：

browser:  
 camofox:  
   managed\_persistence:true  

### 为什么需要？

Camofox 提供了一个"像真人一样"的浏览器环境，让 Hermes 能够：

*   自动读取网页文章
    
*   自动填写表单
    
*   操作需要登录的后台系统
    
*   执行复杂的网页自动化任务
    

**亮点：** Hermes 会智能识别高危指令并清晰说明意图，比某些框架的"一堆无意义数字"的授权请求友好得多。

* * *

## 七、配置微信访问

之前的文章已经介绍了飞书访问，现在我们加上微信访问。

### 7.1 确认版本

确保版本在 0.9 以上：

hermes update  \# 升级到最新版  
hermes --version  \# 确认版本号，应为 v0.9.0 或更高  

### 7.2 安装依赖

pip install aiohttp cryptography  
pip install qrcode  

### 7.3 开始连接

hermes gateway setup  

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-4.png)

出现提示时选择 **Weixin/WeChat。**

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-5.png)

### 7.4 扫码授权

复制链接到浏览器打开，会出现二维码。用微信扫码授权。

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-6.png)

### 7.5 完成配置

终端继续按提示操作，最后完成配置。

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-7.png)

### 7.6 测试

到微信上跟 Hermes 聊聊天，发送一条消息测试是否正常响应。

![](/assets/img/news/Hermes Agent 装好了？这 12 件事必须优先做-8.jpg)

* * *

## 八、安装与沉淀技能 Skills（持续进行）

### Hermes 的技能组织方式

Hermes 默认按分类组织 skill，和之前 OpenClaw 把所有 skill 放在 `/skills` 文件夹有很大不同。另外，分类目录下有一些是占位的，并不存在真实的 `SKILL.md` 文件。

Hermes 的自我进化能力很大程度上就是 skill 的进化能力。它会频繁操作 `~/.hermes/skills` 目录，不停创建和更新 skill。

### 自动技能沉淀

**Hermes 最令人印象深刻的功能之一：它会自动将有价值的操作流程总结并固化为可复用的技能。**

触发条件：每累计 **15 次工具循环，**触发一次后台 skill review。可以修改触发频率：

\# ~/.hermes/config.yaml  
skills:  
creation\_nudge\_interval:10\# 每 10 次触发（默认 15）  

Skill Review 的三种结果：

*   发现可更新的现有技能 → 自动更新补充新经验
    
*   发现值得新建的技能 → 创建新技能文件
    
*   没有值得保存的内容 → 输出 Nothing to save。 结束
    

整个过程在后台线程运行，不阻塞当前对话。

### 手动安装技能

你可以把自己积累的 skill 放进这个目录，让 Hermes 获得这些能力。也可以直接告诉 Hermes：

帮我安装 git 操作相关的技能  
帮我搜索并安装 Docker 管理技能  

**亮点：** Hermes 自动将有价值的操作沉淀为永久技能，避免重复踩坑。这是它相比其他 Agent 框架最有差异化的亮点之一。

* * *

## 九、集成 MCP 能力

关于 MCP 是否已死的争论很多，Hermes 的 MCP 集成能力与 OpenClaw 类似，支持两种类型的 MCP 服务器：

*   **Stdio servers：** 标准输入/输出服务器，作为本地子进程运行
*   **HTTP servers：** HTTP MCP 服务器，直接连接的远程端点

Hermes 从 `~/.hermes/config.yaml` 中的 `mcp_servers` 配置项读取 MCP 配置。

### 安装 MCP 依赖

cd ~/.hermes/hermes-agent  
uv pip install -e ".\[mcp\]"  

### MCP 基本配置项

| 
键名

 | 

类型

 | 

含义

 |
| --- | --- | --- |
| 

command

 | 

string

 | 

stdio MCP 服务器的可执行命令

 |
| 

args

 | 

list

 | 

传递给 stdio 服务器的参数列表

 |
| 

env

 | 

mapping

 | 

传递给 stdio 服务器的环境变量

 |
| 

url

 | 

string

 | 

HTTP MCP 端点地址

 |
| 

headers

 | 

mapping

 | 

远程服务器使用的 HTTP 请求头

 |
| 

timeout

 | 

number

 | 

工具调用超时时间

 |
| 

connect\_timeout

 | 

number

 | 

初始连接超时时间

 |
| 

enabled

 | 

bool

 | 

如果为 false，Hermes 会完全跳过该服务器

 |
| 

tools

 | 

mapping

 | 

针对每个服务器的工具过滤与实用策略配置

 |

### stdio MCP 示例

mcp\_servers:  
filesystem:  
command:"npx"  
args: \["-y", "@modelcontextprotocol/server-filesystem", "/tmp"\]  

### HTTP MCP 示例

mcp\_servers:  
company\_api:  
url:"https://mcp.internal.example.com"  
headers:  
Authorization:"Bearer \*\*\*"  

* * *

## 十、配置 Auxiliary 副驾模型路由

### 设计理念

Auxiliary 是 Hermes 的副驾 LLM 路由中心。核心思路：**让主模型专注复杂推理，让便宜/专用的副模型承担"脏活累活"，**从而节省成本、提升效率。

### 支持的 8 个辅助任务

| 
辅助模型

 | 

用途说明

 |
| --- | --- |
| 

vision

 | 

截图 / 验证码 / 图片分析

 |
| 

web\_extract

 | 

网页内容抓取与提炼

 |
| 

compression

 | 

上下文压缩摘要（节省 Token）

 |
| 

session\_search

 | 

历史会话搜索与摘要

 |
| 

approval

 | 

高危命令审批决策

 |
| 

skills\_hub

 | 

技能市场搜索与安装

 |
| 

mcp

 | 

MCP 服务调用辅助

 |
| 

flush\_memories

 | 

记忆系统清理与重组

 |

### 配置示例

直接口头告知 Hermes：

压缩会话的辅助模型帮我配置成 qwen3.5-plus  

### 验证配置

\# 手动触发压缩  
hermes compress  
  
\# 查看日志确认模型路由  
tail -f ~/.hermes/logs/agent.log  

日志中你应该看到类似：

Auxiliary compression: using auto (qwen3.5-plus) at https://dashscope.aliyuncs.com/...  

**省钱技巧：** 压缩阈值默认 50%，不同上下文长度的模型触发比例不同。1M 模型可分配最多 50K token 给摘要，200K 模型只有 10K。这比统一阈值更合理。

* * *

## 十一、配置 Docker 沙箱（15 分钟）

### 为什么需要沙箱？

默认情况下 Hermes 在本地执行命令，存在一定风险。Docker 沙箱将命令执行隔离在容器中，即使 Agent 执行了危险命令，也只会影响容器内的环境。

### 配置步骤

\# 创建一个使用 Docker 沙箱的 worker profile  
hermes -p worker config set terminal.backend docker  
hermes -p worker config set terminal.docker\_image python:3.11-slim  
  
\# 配置 worker 使用便宜模型（沙箱任务不需要顶级模型）  
hermes -p worker config set model.provider alibaba  
hermes -p worker config set model.model qwen3.5-plus  
  
\# 如果使用 Telegram，绑定独立的 Bot Token  
hermes -p worker config set gateway.telegram.bot\_token "YOUR\_BOT\_TOKEN\_B"  
hermes -p worker config set gateway.telegram.enabled true  

也可以直接告诉主 Agent：

参考如下命令，帮我额外配置一个 profile，sandbox 使用 docker，模型遵循主 profile 即可  
  

### 验证沙箱隔离

```
rm -rf /

# 在宿主机验证 Docker 已启动
docker ps
```

**亮点：** 多 profile 配置非常友好，一句话就让 Hermes 完成配置。主 profile 保持安全，worker profile 承担高风险任务。

* * *

## 十二、建立备份体系（10 分钟）

### 三层备份策略

*   **第一层： 本地 Git（快速版本控制）**
*   **第二层： 其他磁盘定时备份（防止硬盘故障）**
*   **第三层： 远程备份（GitHub 私有仓库 / 对象存储）**

### 完整备份脚本

将以下脚本保存为 `~/hermes_backup.sh：`

#!/bin/bash  
BACKUP\_NAME="hermes\_backup\_$(date +%Y%m%d\_%H%M%S)"  
BACKUP\_DIR="/tmp/$BACKUP\_NAME"  
DEST\_DIR=~/hermes\_backups  
  
mkdir -p $BACKUP\_DIR/hermes $DEST\_DIR  
  
echo"正在备份核心配置..."  
cp ~/.hermes/config.yaml $BACKUP\_DIR/hermes/  
cp ~/.hermes/.env $BACKUP\_DIR/hermes/  
cp ~/.hermes/MEMORY.md $BACKUP\_DIR/hermes/ 2>/dev/null  
  
echo"正在备份数据库与会话..."  
cp ~/.hermes/state.db $BACKUP\_DIR/hermes/  
cp -r ~/.hermes/sessions $BACKUP\_DIR/hermes/ 2>/dev/null  
  
echo"正在备份扩展与技能..."  
cp -r ~/.hermes/plugins $BACKUP\_DIR/hermes/ 2>/dev/null  
cp -r ~/.hermes/skills $BACKUP\_DIR/hermes/ 2>/dev/null  
cp -r ~/.hermes/audit\_logs $BACKUP\_DIR/hermes/ 2>/dev/null  
  
echo"正在备份所有 Profile..."  
cp -r ~/.hermes/profiles $BACKUP\_DIR/hermes/ 2>/dev/null  
  
echo"压缩中..."  
tar -czf $DEST\_DIR/$BACKUP\_NAME.tar.gz -C /tmp $BACKUP\_NAME  
rm -rf $BACKUP\_DIR  
  
echo"✅ 备份完成：$DEST\_DIR/$BACKUP\_NAME.tar.gz"  
echo"大小：$(du -h $DEST\_DIR/$BACKUP\_NAME.tar.gz | cut -f1)"  

添加执行权限并运行：

chmod +x ~/hermes\_backup.sh  
~/hermes\_backup.sh  

可选：添加到 crontab，每天凌晨 2 点自动备份

\# 0 2 \* \* \* ~/hermes\_backup.sh  

**重要：**`.env` 文件包含 API Key，建议加入 `.gitignore，`不要推送到 GitHub。

* * *

## Hermes 十大亮点总结

| 
#

 | 

亮点

 | 

说明

 |
| --- | --- | --- |
| 

①

 | **14 种预设性格** | 

从 helpful 到 catgirl，总有一款适合你

 |
| 

②

 | **8 款精美皮肤** | 

从经典金到火山橙，视觉体验拉满

 |
| 

③

 | **智能授权** | 

自动识别高危指令，清晰说明意图再请求授权

 |
| 

④

 | **会话感知** | 

通过 Session 阅读机制感知历史对话，可据此生成个性化 SOUL.md

 |
| 

⑤

 | **多模型路由** | 

Auxiliary 支持为 8 类任务分配独立模型，省钱且高效

 |
| 

⑥

 | **配置解耦** | 

密钥与配置分离，YAML 格式友好，修改直观

 |
| 

⑦

 | **工具透明** | 

IM 界面清晰打印每次 tool 调用过程，执行过程完全可见

 |
| 

⑧

 | **多 Profile** | 

多实例配置简单，一句话完成，轻松实现沙箱/主力分离

 |
| 

⑨

 | **自动技能沉淀** | 

将有价值操作自动总结为可复用技能，避免重复踩坑

 |
| 

⑩

 | **微信无缝接入** | 

原生支持微信，扫码即可连接

 |

* * *

## 写在最后

这 12 个配置点，不用一次全做完。可以先装好皮肤和个性，用几天熟悉了，再加记忆系统，再配浏览器和微信。一步一步来，每个配置都能让 Hermes 变得更像"你的"助手。

**💬 互动话题：**

你已经安装了 Hermes Agent 吗？最想用哪个功能？欢迎在评论区留言，我会逐一解答！

如果觉得有用，欢迎**点赞 + 在看 + 分享，**支持下这个小号的成长～ 👋

[终于能在国内用了！Hermes Agent 保姆级安装教程，0 成本跑通第一个 AI 智能体](https://mp.weixin.qq.com/s?__biz=MzIwOTAwMzg3NA==&mid=2457439462&idx=1&sn=e53aadbbb2608d9a262cbf442b8588ba&scene=21#wechat_redirect)  

[如何撼动 OpenClaw的地位？Hermes Agent 极简上手指南](https://mp.weixin.qq.com/s?__biz=MzIwOTAwMzg3NA==&mid=2457439348&idx=1&sn=482e7a7dea12fdfdb6c1324b7aa6a396&scene=21#wechat_redirect)