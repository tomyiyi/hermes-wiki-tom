---
title: Hermes Agent 必做配置与调试：从能用到好用
author: 流年Agent
                    流年Agent
date: 2026年4月12日
cover: /assets/img/news/Hermes Agent 必做配置与调试：从能用到好用-0.png
head:
  - - meta
    - name: 新闻
---
      
#   

> **本文是「Hermes Agent 群晖 NAS 部署系列」共 4 篇中的第 3 篇。**① 📖 Hermes Agent 是什么？ ② 🔧 Hermes Agent 群晖 NAS 安装实战 ③ ⚙️ Hermes Agent 必做配置与调试（本文） ④ 🛠️ Hermes Agent 运维手册：升级、排障与日常维护

> Hermes Agent（GitHub: github.com/NousResearch/hermes-agent）是由 Nous Research 开发的开源 AI Agent 框架，支持持久记忆、技能自学习和 15+ 消息平台接入。**前置要求**：请先完成本系列第二篇《Hermes Agent 群晖 NAS 安装实战》，确保 Agent 已启动并运行。

* * *

## 概述：为什么需要这篇文章？

在上一篇中，你已经让 Hermes Agent 跑起来了。但此时它只是一个能聊天的 Bot——核心差异化功能（持久记忆、技能学习、定时任务）**都需要手动配置**才能生效。这篇文章会带你完成所有"必做"配置，让 Agent 真正变成你的私人助手。

配置优先级（按重要性排序）：

1.  ⭐⭐⭐ **LLM 模型与 Fallback** —— Agent 的"大脑"，决定智能水平
    
2.  ⭐⭐⭐ **消息平台** —— 你和 Agent 交互的渠道
    
3.  ⭐⭐ **人格定制** —— 让 Agent 变成"你的 Agent"
    
4.  ⭐⭐ **Camoufox 反爬浏览器** —— 让 Agent 真正能抓到网页
    
5.  ⭐⭐ **危险命令审批与消息推送优化** —— 减少不必要的干扰
    
6.  ⭐ **进阶配置（压缩优化与终端模式）** —— 稳定性与效率微调
    
7.  ⭐ **技能和定时任务** —— 解锁高级能力
    

* * *

## 一、配置 LLM 模型与 Fallback

### Hermes 支持的 LLM 提供商

| 
提供商

 | 

环境变量

 | 

网络要求

 | 

特点

 |
| --- | --- | --- | --- |
| 

MiniMax

 | `MINIMAX_API_KEY` | 

🇨🇳 国内直连

 | 

性价比高

 |
| 

智谱 GLM

 | `GLM_API_KEY` | 

🇨🇳 国内直连

 | 

国产大模型

 |
| 

DeepSeek

 | `DEEPSEEK_API_KEY` | 

🇨🇳 国内直连

 | 

推理能力强

 |
| 

月之暗面 Kimi

 | `KIMI_API_KEY` | 

🇨🇳 国内直连

 | 

长上下文

 |
| 

通义千问

 | `DASHSCOPE_API_KEY` | 

🇨🇳 国内直连

 | 

阿里出品

 |
| 

OpenRouter

 | `OPENROUTER_API_KEY` | 

🌐 需国际网络

 | 

聚合多个 LLM

 |
| 

ChatGPT Plus

 | 

OAuth 登录

 | 

🌐 需国际网络

 | 

复用 Plus 订阅

 |
| 

Anthropic Claude

 | `ANTHROPIC_API_KEY` | 

🌐 需国际网络

 | 

推理能力强

 |
| 

GitHub Copilot

 | 

OAuth 登录

 | 

🌐 需国际网络

 | 

免费额度

 |

### 推荐：双模型故障转移

如果你同时有国内和国际提供商的 API，强烈推荐配置**主力 + 备用**双模型架构：

主力模型（如 GPT-5.4 / Codex）  
  │  API 限流（429）/ 网络波动时自动切换  
  ▼  
备用模型（如 MiniMax-M2.7）  

笔者的选择：

| 
角色

 | 

模型

 | 

提供商

 | 

费用

 |
| --- | --- | --- | --- |
| **主力** | 

GPT-5.4（Codex）

 | 

ChatGPT Plus 订阅

 | 

$20/月

 |
| **备用** | 

MiniMax-M2.7

 | 

MiniMax Token Plan Plus

 | 

¥99/月

 |

ChatGPT Plus 的 Codex 端点性能最强，但有每 5 小时和每周使用配额限制；MiniMax 是国内模型，不吃代理、延迟低、Token Plan Plus 额度充裕，作为兜底刚好。

### 配置方法

**方法一：交互式配置**（推荐新手）

docker exec -it hermes-agent bash  
hermes model  

**方法二：直接编辑配置文件**

编辑 `data/config.yaml`（⚠️ 注意细节，这里有坑）：

model:  
  base_url: https://chatgpt.com/backend-api/codex  
  default: gpt-5.4  
  provider: openai-codex  
  
providers:  
  minimax-cn:  
    model: MiniMax-M2.7  
  
# ⚠️ 不要用 fallback_providers，原因见下文踩坑部分  
# fallback_providers:  
#   - minimax-cn  
  
# ✅ 用 fallback_model（完整字典格式）  
fallback_model:  
  provider: minimax-cn  
  model: MiniMax-M2.7  
  base_url: https://api.minimaxi.com/v1  
  api_key_env: MINIMAX_CN_API_KEY  

同时在 `docker-compose.yml` 的 `environment` 段中声明：

environment:  
  - MINIMAX_CN_API_KEY=sk-cp-xxxx  
  - MINIMAX_CN_BASE_URL=https://api.minimaxi.com/v1  

### Fallback 配置的 5 个坑

这是整个部署过程中最折腾的部分。主模型限流后，Agent 理应自动切换到 MiniMax，但实际测试时 fallback 始终失败。最终定位了 5 个问题。

**坑 1：YAML 字符串 ≠ YAML 列表**

# ❌ 这是字符串，不是列表  
fallback_providers: '["minimax-cn"]'  
  
# ✅ YAML 原生列表  
fallback_providers:  
  - minimax-cn  

Hermes 的配置初始化代码在某些情况下会把 `fallback_providers` 写成 JSON 字符串格式。YAML 解析后依然是 `str` 类型，不是 `list`。

**坑 2：providers 字典为空**

`fallback_providers` 指向了 `minimax-cn`，但 `providers: {}` 是空的——Hermes 不知道这个 provider 用什么模型、连什么 URL。

**坑 3：双 `.env` 文件混淆**

| 
文件

 | 

路径

 | 

用途

 |
| --- | --- | --- |
| 

Docker Compose `.env`

 | `./hermes-agent/.env` | 

容器启动时注入环境变量

 |
| 

Hermes 数据 `.env`

 | `./hermes-agent/data/.env` | 

运行时通过 dotenv 加载

 |

光在一个文件里写 API Key 不一定够。**最保险的做法**：直接写在 docker-compose.yml 的 `environment` 段里。

**坑 4：模型名称与 Token Plan 不匹配**

配了 `MiniMax-M1`，但 Token Plan 只支持 `MiniMax-M2.7`。API 返回 500。验证方法——在容器里直接测试连通性：

docker exec hermes-agent python3 -c "  
import os  
from openai import OpenAI  
client = OpenAI(  
  base_url='https://api.minimaxi.com/v1',  
  api_key=os.environ['MINIMAX_CN_API_KEY']  
)  
resp = client.chat.completions.create(  
  model='MiniMax-M2.7',  
  messages=[{'role':'user','content':'hi'}],  
  max_tokens=10  
)  
print(f'SUCCESS: {resp.choices[0].message.content}')  
"  

**坑 5（最致命）：`or` 短路逻辑**

源码中加载 fallback 的逻辑是：

fb = cfg.get("fallback_providers") or cfg.get("fallback_model") or None  

`fallback_providers` 哪怕格式不对，只要有值就会阻止代码继续读取 `fallback_model`。然后 Agent 初始化时要求 fallback 列表里的每个元素必须是字典（包含 `provider` 和 `model` 键），字符串被直接过滤掉，最终 `_fallback_chain` 为空列表。

**解决方案**：注释掉 `fallback_providers`，只保留 `fallback_model`。

* * *

## 二、接入飞书消息平台

Hermes 内置了飞书支持，通过 **WebSocket 长连接**方式接收消息——NAS 不需要公网 IP 或域名。

### 2.1 创建飞书自建应用（详细步骤）

> 💡 **预警：** 飞书开放平台的配置步骤多达八九步，初看会比较繁琐，大约需要耗费你 **10 分钟**。但请保持耐心，这是整个部署中唯一需要些许耐心的环节，且**配置一次永久有效**。跟着下方的图文步骤“闭眼操作”即可。

**第 1 步：打开飞书开放平台**

浏览器访问 open.feishu.cn，用你的飞书账号登录。

**第 2 步：创建应用**

1.  点击「**创建企业自建应用**」
    
2.  填写应用名称（如 "My AI Assistant"）和描述
    
3.  在「**凭证与基础信息**」页面，记录 **App ID**（`cli_xxx`）和 **App Secret**
    

**第 3 步：添加应用能力**

1.  左侧菜单 →「**添加应用能力**」
    
2.  找到「**机器人**」能力，点击添加
    

**第 4 步：配置权限**

在左侧菜单「**权限管理**」中，搜索并开通以下权限：

**基础必需权限：**

| 
权限名称

 | 

权限标识

 | 

用途

 |
| --- | --- | --- |
| 

获取与发送单聊、群组消息

 | `im:message` | 

接收和发送消息（**必需**）

 |
| 

以应用的身份发消息

 | `im:message:send_as_bot` | 

Agent 主动发送消息（**必需**）

 |
| 

获取单聊、群组消息

 | `im:message:readonly` | 

读取历史消息（**必需**）

 |

**推荐开通权限（提升体验）：**

| 
权限名称

 | 

权限标识

 | 

用途

 |
| --- | --- | --- |
| 

获取消息中的资源文件

 | `im:resource` | 

接收用户发送的图片和文件

 |
| 

上传图片

 | `im:image` | 

Agent 回复图片（如图像生成结果）

 |
| 

上传文件

 | `im:file` | 

Agent 发送文件附件

 |
| 

获取与更新群组信息

 | `im:chat` | 

支持群聊场景

 |
| 

获取群组成员信息

 | `im:chat:member:readonly` | 

识别群聊中的不同用户

 |
| 

获取应用信息

 | `admin:app.info:readonly` | 

自动获取机器人名称

 |

> 权限越完整，Agent 的交互能力越强。建议至少开通前述所有权限。

**第 5 步：配置事件订阅与回调**

**事件订阅**（左侧菜单「**事件订阅**」）：

1.  选择「**使用 WebSocket 长连接接收事件**」
    
2.  添加以下事件：
    

| 
事件名称

 | 

事件标识

 | 

是否必需

 |
| --- | --- | --- |
| 

接收消息

 | `im.message.receive_v1` | 

✅ **必需**

 |
| 

消息被 reaction

 | `im.message.reaction.created_v1` | 

可选，支持表情回复

 |
| 

消息被取消 reaction

 | `im.message.reaction.deleted_v1` | 

可选

 |

**回调配置**（左侧菜单「**回调配置**」，注意不是事件订阅）：

| 
回调名称

 | 

回调标识

 | 

用途

 |
| --- | --- | --- |
| 

卡片回传交互

 | `card.action.trigger` | 

可选，支持交互卡片按钮

 |

> ⚠️ 注意区分：前三项在「事件订阅」中配置，卡片回传交互在「回调配置」中配置，不要搞混。

**第 6 步：发布应用**

1.  左侧菜单 →「**版本管理与发布**」
    
2.  创建新版本，填写版本号和更新说明
    
3.  点击「**申请发布**」
    
4.  管理员审批通过后即可使用
    

### 2.2 配置 Hermes 飞书通道

在 `.env` 文件中添加：

FEISHU_APP_ID=cli_你的AppID  
FEISHU_APP_SECRET=你的AppSecret  
FEISHU_DOMAIN=feishu  
FEISHU_CONNECTION_MODE=websocket  

> `FEISHU_DOMAIN`：`feishu`（国内飞书）或 `lark`（国际 Lark）。

### 2.3 重启并验证

docker compose restart  
docker compose logs --tail 20 -f  

在飞书中搜索你的机器人，发一条消息测试。

### 2.4 安全配置：用户配对

首次有人给机器人发消息时，Hermes 会生成配对码。在 NAS 上批准：

docker exec hermes-agent hermes pairing list  
docker exec hermes-agent hermes pairing approve feishu 配对码  

或预设允许的用户：`FEISHU_ALLOWED_USERS=ou_xxx,ou_yyy`

* * *

## 三、人格定制（SOUL.md）—— 必做

`SOUL.md` 是 Agent 的核心身份定义，每次对话开始时自动注入 system prompt。**这是让 Agent"变成你的 Agent"的关键**。

### 数据目录结构

/opt/data/（容器内）  ←→  ./data/（NAS 上）  
├── config.yaml         # 模型、工具、平台配置  
├── .env                # API 密钥  
├── SOUL.md             # 🧠 Agent 人格设定  
├── memories/           # 📝 持久记忆（Agent 自动管理）  
├── skills/             # 🔧 技能文档（77+ 内置）  
├── cron/               # ⏰ 定时任务配置  
├── sessions/           # 💬 会话存储  
├── logs/               # 📋 日志  
└── hooks/              # 🔗 事件钩子脚本  

### 创建 SOUL.md

docker exec hermes-agent bash -c 'cat > /opt/data/SOUL.md << EOF  
# 人格  
  
你是一个务实的高级工程师，有很强的技术品味。  
你追求真实、清晰和实用，而不是无意义的客套。  
  
## 风格  
- 直接但不冷漠  
- 重内容轻废话  
- 默认使用中文回答  
- 代码注释用英文  
EOF'  

> 根据你自己的需求修改人格描述。SOUL.md 支持 Markdown 格式，可以包含复杂的指令。

* * *

## 四、持久记忆

### 基础配置

| 
文件

 | 

用途

 | 

默认容量

 |
| --- | --- | --- |
| `memories/MEMORY.md` | 

环境事实、工作流程、经验教训

 | 

2,200 字符（~800 tokens）

 |
| `memories/USER.md` | 

用户偏好、身份、沟通风格

 | 

1,375 字符（~500 tokens）

 |

Agent 通过 `memory` 工具自动读写，无需手动编辑。它会在对话中自动判断哪些信息值得记住（如你的开发环境、工作习惯、纠正过的错误），并主动归纳持久化。当记忆接近容量上限时，Agent 会自动合并和精简旧条目腾出空间。

### 调整记忆容量

默认的字符限制对大多数用户够用，但如果你觉得记忆空间不够，可以在 `data/config.yaml` 中调大：

memory:  
  memory_enabled: true  
  user_profile_enabled: true  
  memory_char_limit: 4400   # 默认 2200，翻倍后约 1600 tokens  
  user_char_limit: 2750     # 默认 1375，翻倍后约 1000 tokens  

> ⚠️ **权衡**：增大记忆容量意味着每次对话的 system prompt 更长，消耗更多 tokens（=更多 API 费用）。建议按需逐步调整，而不是一次拉到很高。

### 进阶：外部记忆 Provider

如果内置的 MEMORY.md + USER.md 无法满足需求（比如你希望有知识图谱、语义搜索、更深层的用户建模），Hermes 官方支持 **8 个外部记忆 Provider 插件**：

| 
Provider

 | 

特点

 |
| --- | --- |
| **Honcho** | 

辩证用户建模（Dialectic User Modeling），Hermes 官方推荐

 |
| **Mem0** | 

自动事实提取 + 知识图谱

 |
| **Hindsight** | 

跨会话语义搜索

 |
| **Holographic** | 

全息记忆压缩

 |
| **OpenViking** | 

向量数据库集成

 |
| **RetainDB** | 

结构化持久记忆

 |
| **ByteRover** | 

字节级精准召回

 |
| **Supermemory** | 

超大规模记忆存储

 |

外部 Provider 是**并行运行**的（不替代内置记忆），可以通过以下命令配置：

docker exec -it hermes-agent bash  
hermes memory setup    # 交互式选择和配置 Provider  
hermes memory status   # 查看当前启用的记忆系统  

> 详情参见 Hermes 官方 Memory Providers 文档：hermes-agent.nousresearch.com/docs/user-guide/features/memory-providers

* * *

## 五、技能系统（Skills）

### 搜索和安装技能

# 搜索技能  
docker exec hermes-agent hermes skills search kubernetes  
  
# 安装技能  
docker exec hermes-agent hermes skills install openai/skills/k8s  

Hermes 内置 77+ 技能，还可以在 AgentSkills.io 浏览社区贡献的技能。

### Agent 会自动创建技能

这是 Hermes 最独特的能力之一：当你让它执行一个复杂任务后，**Agent 会自主判断这个过程是否值得记住，并自动创建一个 Skill 文档**。比如你让它搜索整理一份技术调研资料，任务完成后它可能会自动创建一个 "technical-research" 的 Skill，下次遇到类似任务时它会参考这个 Skill 来执行。

你不需要做任何事——这就是 Hermes 官方所说的 "built-in learning loop"。当然你也可以手动创建 Skill（在 `skills/` 目录下放一个 `SKILL.md` 文件即可）。

* * *

## 六、定时任务（Cron）

### 最简单的方式：直接在聊天中创建

在飞书中用自然语言告诉 Agent 就行：

> "帮我每天早上 9 点发送一份天气预报" "每两小时检查一下服务器状态"

Agent 会自动理解并创建对应的 Cron 任务。你也可以用 slash 命令：

/cron add "every 2h" "检查服务器状态"  
/cron list  

> **提示**：在飞书中发送 `/set-home` 可以将当前聊天设为"主聊天"，Cron 任务的执行结果会发送到这个聊天。

### 为什么 Hermes 的 Cron 比较可靠？

从实际使用体验看，Hermes 的定时任务执行成功率确实比较高，可能与以下设计有关：

1.  **独立 Cron 引擎**：Hermes 内置了独立的 Cron 调度器，直接在 Gateway 进程内运行，不依赖外部进程管理
    
2.  **任务隔离**：每个 Cron 任务在独立的会话中执行，不会相互干扰，也不会受当前的聊天会话影响
    
3.  **存储路径加固**：官方文档提到 Cron 存储路径有防路径穿越攻击保护，说明在安全性上有专门设计
    

当然，Cron 任务的实际执行效果也和你选择的 LLM 模型有很大关系——推理能力更强的模型（如 Anthropic Claude、GPT-4 级别）执行复杂定时任务的成功率会更高。

* * *

## 七、危险命令审批（/approve）

Hermes 在执行可能有风险的命令（如 `rm -r`、`bash -c`、`sed -i`、写入系统文件等）时，会弹出审批请求等你确认。这是一个重要的安全机制，但在日常使用中可能频繁打断工作流。

### 三种审批模式

在 `data/config.yaml` 中配置：

approvals:  
  mode: manual    # manual | smart | off  
  timeout: 60     # 等待用户回复的秒数（默认 60 秒，超时则拒绝）  

| 
模式

 | 

说明

 | 

适合场景

 |
| --- | --- | --- |
| `manual` | 

每个危险命令都需要你明确批准（默认）

 | 

对安全性要求高

 |
| `smart` | 

Agent 自行判断风险级别，仅高风险命令需审批

 | 

日常使用推荐

 |
| `off` | 

关闭所有审批

 | 

⚠️ 仅限可信环境（如 Docker 容器内）

 |

### YOLO 模式：临时跳过所有审批

如果你正在让 Agent 执行一个大型任务（如部署项目），频繁审批会很烦。可以临时开启 YOLO 模式：

**在飞书中发送 `/yolo` 即可切换（再发一次关闭）**：

> /yolo  
⚡ YOLO mode ON — all commands auto-approved. Use with caution.  
  
> /yolo  
⚠ YOLO mode OFF — dangerous commands will require approval.  

也可以在启动时设置环境变量 `HERMES_YOLO_MODE=1`。

### 永久允许特定命令

如果某些命令你确认安全、不想每次都审批，可以加入永久白名单：

# data/config.yaml  
command_allowlist:  
  - rm           # 允许所有 rm 命令  
  - systemctl    # 允许 systemctl 操作  

> ⚠️ **安全提醒**：
> 
> *   YOLO 模式和 `mode: off` 会让 Agent 可以执行**任何命令**，包括删除文件、修改系统配置等。在 NAS Docker 容器内相对安全（容器就是隔离边界），但仍需谨慎
>     
> *   **NAS Docker 用户的好消息**：Hermes 在 Docker 后端运行时，会自动跳过危险命令检查，因为容器本身就是基础的安全边界。所以你在 NAS 上可能不会遇到太多审批提示。
>     
> *   ☢️ **高危警告：如果你在 `docker-compose.yml` 中把 NAS 的根目录（如 `/volume1`）直接挂载进了容器，开启 YOLO 模式将是致命的！** 这种情况下 Agent 的一个误操作（如执行 `rm -rf`）可能直接清空你 NAS 上的真实数据。因此，**强烈建议永远不要**把宿主机敏感数据目录挂载进 Agent 容器中。
>     
> *   本篇建议：日常使用保持为 `smart` 模式即可，仅在确认安全的情况下偶尔使用 `/yolo`。
>     

* * *

## 八、消息推送优化：减少打扰

默认配置下，Hermes 会推送较多中间过程信息（思考过程、工具调用进度），可能造成频繁弹窗。**强烈建议在配置完成后立即优化**。

### 关闭思考/推理过程显示

**方法一：发送命令**（当前会话立即生效）

/reasoning hide  

**方法二：配置文件永久关闭**（编辑 `data/config.yaml`）

reasoning:  
  show: false  

### 减少工具执行进度通知

编辑 `data/config.yaml`：

display:  
  # off = 完全关闭 | new = 新工具时通知 | all = 全部（默认）| verbose = 详细  
  tool_progress: new  
  
  # off | result | error | all  
  background_process_notifications: result  

### 修改后重启

docker compose restart  

* * *

## 九、进阶配置

### 9.1 上下文压缩超时

当对话变长时，Hermes 会自动调用模型对历史对话进行压缩（摘要），腾出上下文窗口空间。这个操作本身需要调用 LLM API，如果你的 NAS 通过代理访问国际 API，网络波动可能导致压缩请求超时失败——一旦压缩失败，上下文窗口爆满，Agent 可能直接报错或丢失对话记忆。

默认超时是 120 秒，建议调高到 300 秒：

# data/config.yaml → auxiliary 段  
auxiliary:  
  compression:  
    timeout: 300    # 默认 120，改为 5 分钟  

> 💡 **关于压缩模型的选择**：你可能注意到配置中 `summary_model` 可以单独指定。压缩是辅助任务，不需要用最强的主模型。推荐使用 **Google Gemini Flash**（`google/gemini-3-flash-preview`）——免费、速度快、而且有 1M 上下文窗口（远超主模型的 200K），完全不用担心历史对话太长装不下。这样还能把主模型的额度省下来用于正经对话。

### 9.2 持久化 Shell：开不开？

默认情况下，Hermes 每执行一条命令都会启动一个全新的 shell，执行完立刻销毁。这意味着：

命令1: cd /opt/project        → shell 销毁  
命令2: ls                      → 回到默认目录，不是 /opt/project！  
命令3: export MY_VAR=hello     → shell 销毁  
命令4: echo $MY_VAR            → 空的，变量丢了  

开启持久化后（`terminal.persistent_shell: true`），同一个 shell 进程会保持存活，cd、环境变量、alias 等状态在命令之间保留。

**听起来很好，但笔者选择不开。原因如下：**

1.  **状态污染风险**：前面命令设了个奇怪的环境变量，可能悄悄影响后续命令的行为。one-shot 模式下每次都是干净的环境，反而更可预测
    
2.  **工作目录混乱**：Agent 在持久 shell 里 `cd` 到某个目录后如果忘了当前位置，可能在错误的目录执行操作
    
3.  **实际收益有限**：Agent 本来就会在命令中写完整路径，很少依赖 `cd` 的状态
    
4.  **性能不是问题**：一个 bash 进程只占 2-4MB 内存，不会因为执行很多命令而变大。每条命令都是 fork 子进程来跑的，退出后资源就释放了。所以不开持久化也不会有性能损失
    

> **结论：保持默认的 one-shot 模式即可。** 除非你的使用场景大量依赖命令间的状态传递（如复杂的多步 DevOps 脚本），否则不建议开启。

* * *

## 十、Camoufox 反爬浏览器

Hermes 默认用 Playwright + Chromium 作为浏览器后端。对于普通网页没问题，但访问有反爬检测的网站（知乎、Google 等）时，经常会被拦截返回 403 或验证码。

**Camoufox** 是一个 Firefox 分支，在 **C++ 层面**伪造浏览器指纹（navigator、WebGL、AudioContext、Canvas 等），比 JavaScript 层的 stealth 插件更难被检测。

### 自动切换机制

Agent 调用浏览器工具（browser_navigate / browser_snapshot 等）  
    │  
    └→ browser_tool.py 检查 is_camofox_mode()  
          │  
          ├── CAMOFOX_URL 有值 → Camofox 容器（REST API）  
          └── CAMOFOX_URL 为空 → Playwright + Chromium  

只要在 docker-compose.yml 中设了 `CAMOFOX_URL` 环境变量，所有浏览器操作就自动走 Camofox。不需要改任何代码。

### 部署步骤

**第 1 步：获取源码和二进制文件**

从 GitHub 下载 camofox-browser 源码包，解压到 `camofox-source` 目录。然后手动下载两个二进制文件到 `camofox-source/dist/`：

| 
文件

 | 

大小

 | 

重命名为

 |
| --- | --- | --- |
| 

Camoufox 浏览器引擎

 | 

~680MB

 | `camoufox-x86_64.zip` |
| 

yt-dlp

 | 

~35MB

 | `yt-dlp-x86_64` |

> 群晖 NAS 的 OpenSSL 版本偏旧，直连 GitHub 可能遇到 SSL 错误。最稳的方式是在 PC 浏览器下载后通过 SMB 共享传到 NAS。

**第 2 步：构建 Docker 镜像**

官方 Dockerfile 用了 BuildKit 的 `--mount=type=bind` 语法，群晖的 Docker 不支持（没有 buildx 组件）。需要用改造过的 Dockerfile，把 `--mount` 改为 `COPY`：

# Dockerfile.nas — 群晖兼容版  
FROM node:20-slim  
ARG CAMOUFOX_VERSION=135.0.1  
ARG CAMOUFOX_RELEASE=beta.24  
ARG ARCH=x86_64  
  
RUN apt-get update && apt-get install -y \  
    libgtk-3-0 libdbus-glib-1-2 libxt6 libasound2 libx11-xcb1 \  
    libxcomposite1 libxcursor1 libxdamage1 libxfixes3 libxi6 \  
    libxrandr2 libxrender1 libxss1 libxtst6 libegl1-mesa \  
    libgl1-mesa-dri libgbm1 xvfb fonts-liberation \  
    fonts-noto-color-emoji fontconfig ca-certificates unzip \  
    python3-minimal && rm -rf /var/lib/apt/lists/*  
  
# 关键改动：用 COPY 替代 --mount  
COPY dist/camoufox-${ARCH}.zip /tmp/camoufox.zip  
COPY dist/yt-dlp-${ARCH} /usr/local/bin/yt-dlp  
  
RUN mkdir -p /root/.cache/camoufox \  
    && (unzip -q /tmp/camoufox.zip -d /root/.cache/camoufox || true) \  
    && chmod -R 755 /root/.cache/camoufox \  
    && echo "{\"version\":\"${CAMOUFOX_VERSION}\",\"release\":\"${CAMOUFOX_RELEASE}\"}" \  
       > /root/.cache/camoufox/version.json \  
    && test -f /root/.cache/camoufox/camoufox-bin \  
    && rm /tmp/camoufox.zip && chmod 755 /usr/local/bin/yt-dlp  
  
WORKDIR /app  
COPY package.json ./  
RUN npm install --production  
COPY server.js ./  
COPY lib/ ./lib/  
ENV NODE_ENV=production  
EXPOSE 9377  
CMD ["sh", "-c", "node --max-old-space-size=${MAX_OLD_SPACE_SIZE:-128} server.js"]  

构建：

cd /volume1/docker/hermes-agent/camofox-source  
docker build -f Dockerfile.nas \  
  --build-arg ARCH=x86_64 \  
  --build-arg CAMOUFOX_VERSION=135.0.1 \  
  --build-arg CAMOUFOX_RELEASE=beta.24 \  
  -t camofox-browser:135.0.1-x86_64 .  

**第 3 步：整合到 docker-compose.yml**

在现有的 `hermes-agent` 服务旁边新增 `camofox` 服务：

services:  
  hermes-agent:  
    # ...原有配置...  
    environment:  
      - CAMOFOX_URL=http://camofox:9377    # 新增  
      - NO_PROXY=localhost,camofox,...      # camofox 必须加入 NO_PROXY！  
    depends_on:  
      - camofox                            # 新增  
  
  camofox:                                 # 新增服务  
    container_name: camofox-browser  
    image: camofox-browser:135.0.1-x86_64  
    restart: unless-stopped  
    environment:  
      - CAMOFOX_PORT=9377  
      - MAX_SESSIONS=5  
      - BROWSER_IDLE_TIMEOUT_MS=300000  
      - MAX_OLD_SPACE_SIZE=128  
      - PROXY_HOST=172.17.0.1              # 浏览器级代理（访问国外站）  
      - PROXY_PORT=7890  
    mem_limit: 512m  

> ⚠️ **关键细节**：`NO_PROXY` 里\*\*必须加 `camofox`\*\*！否则 Hermes 发往 Camofox 容器的 HTTP 请求会被代理拦截，导致 `check_camofox_available()` 返回 False，浏览器工具会静默回退到 Playwright，前功尽弃。

> 💡 **代理分流**：Camofox 的 `PROXY_HOST`/`PROXY_PORT` 配置的是**浏览器级代理**（不是 Node.js 的 `HTTP_PROXY`）。如果你用 mihomo 等规则代理，它会自动分流：国内站（知乎、百度）直连，国外站（Google、X.com）走代理。

**第 4 步：验证**

# 健康检查  
docker exec hermes-agent curl -s http://camofox:9377/health  
# → {"ok":true,"engine":"camoufox","browserConnected":true}  
  
# Hermes 是否识别了 Camofox  
docker exec hermes-agent python3 -c "  
from tools.browser_camofox import is_camofox_mode, check_camofox_available  
print('Mode:', is_camofox_mode())           # → True  
print('Available:', check_camofox_available())  # → True  
"  

### 资源消耗

| 
状态

 | 

内存

 |
| --- | --- |
| 

空闲

 | 

~56MB

 |
| 

活跃（一个标签页）

 | 

~200-300MB

 |
| 

磁像（镜像）

 | 

~1.2GB

 |

### 实测效果

| 
网站

 | 

Playwright + Chromium

 | 

Camoufox

 |
| --- | --- | --- |
| 

知乎

 | 

403 被拦

 | 

✅ 正常加载

 |
| 

百度

 | 

✅

 | 

✅

 |
| 

Google

 | 

需代理

 | 

✅（配代理后）

 |

* * *

## 十一、常用 Slash 命令速查

| 
命令

 | 

说明

 |
| --- | --- |
| `/help` | 

查看所有命令

 |
| `/model` | 

查看/切换模型

 |
| `/tools` | 

查看可用工具

 |
| `/skills` | 

浏览技能

 |
| `/cron` | 

管理定时任务

 |
| `/new`

 / `/reset`

 | 

新会话 / 重置

 |
| `/reasoning show` | 

显示思考过程

 |
| `/reasoning hide` | **隐藏思考过程** |
| `/yolo` | 

切换 YOLO 模式（跳过危险命令审批）

 |
| `/voice on` | 

开启语音模式

 |
| `/background <提示词>` | 

后台运行任务

 |
| `/stop` | 

中断当前操作

 |
| `/set-home` | 

设为主聊天（接收 Cron 结果）

 |
| `/compress` | 

压缩上下文

 |

* * *

## 十二、调试 Cheatsheet

| 
场景

 | 

命令

 |
| --- | --- |
| 

测试备用模型 API 连通

 | `docker exec hermes-agent python3 -c "from openai import OpenAI; ..."` |
| 

检查 Camofox 是否收到请求

 | `docker logs camofox-browser --tail 20 | grep req` |
| 

查看 Fallback 触发情况

 | `docker logs hermes-agent --tail 100 | grep -E '429|fallback|retry'` |
| 

检查环境变量注入

 | `docker exec hermes-agent env | grep -E 'MINIMAX|CAMOFOX|PROXY'` |
| 

检查 Camofox 可用性

 | 

见上文第九节验证命令

 |

* * *

## 下一步

到这里，你的 Hermes Agent 应该已经是一个功能完整、体验良好的 AI 助手了。接下来请阅读本系列最后一篇：**《Hermes Agent 运维手册：升级、排障与日常维护》**，了解如何一键升级、排查常见问题和日常维护。