---
title: Hermes Agent日常使用技巧与配置：让AI伙伴真正好用起来
author: 静远AI实战
                        静远AI实战
date: 2026年4月18日
cover: /assets/img/news/Hermes Agent日常使用技巧与配置：让AI伙伴真正好用起来-0.png
head:
  - - meta
    - name: 新闻
---
      
# Hermes Agent日常使用技巧与配置：让AI伙伴真正好用起来

前两篇我们装好了Hermes，也搞懂了它的架构。但装好不等于好用——默认配置只是"能跑"，改几个配置才能"好跑"。

这篇是实操向的保姆级配置指南，涵盖飞书对接、人设定制、体验优化、定时任务、浏览器操作等核心场景。看完照着改，你的Hermes会好用一个量级。

## 一、飞书对接：让Hermes住在你的飞书里

Hermes可以通过飞书机器人跟你聊天，收发消息、图片、文件。配置好之后，你在飞书里直接跟AI对话，定时任务的结果也自动发到指定群。

### 1.1 创建飞书应用

最简单的方式是一条命令搞定：

```
hermes gateway setup
```

选择 Feishu / Lark，用飞书App扫码，Hermes会自动创建机器人应用并保存凭证。

如果扫码不可用，就手动创建：打开 https://open.feishu.cn\[1\] → 创建新应用 → 复制 App ID 和 App Secret → 启用机器人能力。

### 1.2 配置文件在哪？

所有飞书相关配置在两个文件里：

*   **`~/.hermes/.env`** — 存放密钥和连接配置
    
*   **`~/.hermes/config.yaml`** — 存放行为配置
    

### 1.3 核心配置项

在 `~/.hermes/.env` 中添加：

```
# 必填：飞书应用凭证
FEISHU_APP_ID=cli_xxxx
FEISHU_APP_SECRET=xxxx

# 推荐：连接模式（websocket免公网IP，推荐）
FEISHU_CONNECTION_MODE=websocket

# 强烈推荐：允许使用的用户（不设则所有人可用）
FEISHU_ALLOWED_USERS=ou_xxxx,ou_yyyy

# 推荐：定时任务结果发到哪个群
FEISHU_HOME_CHANNEL=oc_xxxx

# 群聊策略：open=所有人可用 / allowlist=仅白名单用户 / disabled=不响应群消息
FEISHU_GROUP_POLICY=allowlist
```

**怎么获取这些ID？**

*   `ou_xxx`（用户open\_id）：在飞书开放平台的API调试器里查，或者让Hermes帮你查
    
*   `oc_xxx`（群chat\_id）：在群里输入 `/set-home`，Hermes会自动记录
    

### 1.4 重点：群聊不响应消息的解决方法

这是最常见的问题——群里@了机器人，但没反应。**90%的原因是权限没配对**。

登录 https://open.feishu.cn\[2\] → 你的应用 → 权限管理，确保开了以下权限：

**消息接收权限：**

*   `im:message` — 获取与发送单聊、群组消息
    
*   `im:message.group_at_msg` — 接收群聊中@机器人的消息
    
*   `im:message.group_msg` — 接收群聊中所有消息（如果需要不@也能响应）
    

**群组相关权限：**

*   `im:chat` — 获取群信息
    
*   `im:chat:readonly` — 获取群基本信息
    

**应用自管理权限（关键！很多人漏这个）：**

*   `application:application:self_manage` — 应用自管理
    
*   `admin:app.info:readonly` — 读取应用信息（用于自动发现机器人身份）
    

> ⚠️ 修改权限后需要在应用发布页面**创建版本并发布**，权限才生效。光保存不够！

### 1.5 关于群聊必须@的问题

默认情况下，群聊中**必须@机器人才会响应**，这是飞书平台的安全策略。

如果你想在特定群里不@也能响应（比如专用的工作群），需要修改源代码。这不是配置项能解决的——飞书API本身就要求群消息必须@才能推送给机器人。

如果你有这个需求，可以私信联系我获取修改方案。

### 1.6 建议：创建多个群隔离不同类型的任务

推荐创建以下群：

| 群 | 用途 | FEISHU\_HOME\_CHANNEL |
| --- | --- | --- |
| AI助手-日常 | 日常对话、临时问题 | 不设为home |
| AI助手-定时任务 | 定时任务结果汇总 | ✅ 设为home |
| AI助手-内容运营 | 内容生产相关任务 | 按需配置 |

这样定时任务的结果不会淹没在日常对话里，各司其职。

* * *

## 二、人设与身份：让Hermes成为"你的"Hermes

### 2.1 SOUL.md — 定义Hermes的性格

文件位置：`~/.hermes/SOUL.md`

这是Hermes的"灵魂"文件，定义它的性格、说话风格、价值观。你可以直接编辑这个文件，也可以**在对话中让Hermes自己改**。

比如你可以在聊天中说：

> "以后你跟我说话要简洁一点，不要废话" "你的名字叫小赫，是一个温和耐心的技术助手" "回答问题时优先给出结论，再解释原因"

Hermes会自动把这些偏好写入SOUL.md。

### 2.2 USER.md — 告诉Hermes你是谁

文件位置：`~/.hermes/memories/USER.md`

这里面存放关于你的信息：你的职业、技术栈、偏好、常用工具等。Hermes会在每次对话时读取这些信息，让回答更贴合你的需求。

同样，你可以在对话中自然地告诉它：

> "我是后端程序员，主要用Python和Go" "我不喜欢用vim，编辑器用VS Code" "我在运营一个AI自媒体账号"

Hermes会自动记录。

* * *

## 三、config.yaml：几个提升体验的关键配置

文件位置：`~/.hermes/config.yaml`

以下是我强烈建议修改的几个配置项：

### 3.1 输入模式：避免消息互相打断

```
display:
  busy_input_mode: queue   # 默认是 interrupt
```

**默认行为**（interrupt）：你发一条新消息，Hermes会立刻中断正在执行的任务来回复你。

**建议改为**（queue）：新消息排队等待，等当前任务完成后再处理。如果确实需要打断，用 `/stop` 手动终止。

原因：Hermes执行复杂任务时可能要跑几十秒甚至几分钟，如果随便发条消息就打断，前面的工作全白费了。

### 3.2 命令审批：关掉频繁确认

```
approvals:
  mode: off   # 默认是 ask
```

**默认行为**（ask）：Hermes每次执行终端命令、写文件等操作前，都会弹出来问你"允许吗？"。

**建议改为**（off）：直接执行，不再询问。

原因：Hermes的核心价值就是能自动帮你做事。每次都问，效率还不如自己来。如果你担心安全问题，可以通过 `~/.hermes/config.yaml` 的 `approvals.deny_patterns` 配置禁止某些危险命令。

### 3.3 会话重置：别让它自动清空

```
session_reset:
  mode: idle   # 默认是 daily，每天凌晨4点重置
```

**默认行为**（daily）：每天凌晨4点自动重置会话，清空对话历史。

**建议改为**（idle）：会话闲置超过一定时间后才重置，或者改成 `off` 完全不自动重置，通过对话中 `/reset` 手动重置。

原因：自动重置可能在你不注意的时候清空了重要的对话上下文。手动控制更靠谱。

### 3.4 技能目录：加载你自己的Skills

```
skills:
  external_dirs:
    - ~/my-hermes-skills
```

如果你自己写了一些Hermes技能（Skills），可以通过 `external_dirs` 指定外部目录。Hermes启动时会自动扫描加载。

这样你就可以把自己常用的流程、模板、工具封装成技能，Hermes每次都能直接用。

### 3.5 修改配置后需要重启网关

改完 `config.yaml` 或 `.env` 后，需要重启网关才能生效。

你可以在飞书里直接让Hermes重启自己：

> "重启网关"

Hermes会自己执行 `hermes gateway restart`。

如果AI重启失败，手动在电脑终端执行：

```
hermes gateway restart
```

* * *

## 四、定时任务：让Hermes自己干活

Hermes内置了定时任务系统（Cron），支持通过自然语言创建定时任务。

### 4.1 在对话中创建定时任务

直接跟Hermes说就行：

> "每天早上8点给我发一条今日AI资讯摘要" "每周一上午9点检查一下服务器状态" "每天晚上10点提醒我写日报"

Hermes会自动创建cron任务，执行结果会发到你配置的 `FEISHU_HOME_CHANNEL` 群。

### 4.2 定时任务投递到不同群

每个定时任务可以投递到不同的群。在创建任务时指定，或者后续修改：

```
hermes cron list         # 查看所有定时任务
hermes cron update       # 修改任务配置
```

* * *

## 五、本地浏览器操作

Hermes可以通过CDP（Chrome DevTools Protocol）直接操控你本地的Chrome浏览器——打开网页、点击按钮、填表单、截图。

### 5.1 启用方式

在Chrome启动时加上远程调试参数：

```
# macOS
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222

# 或者用已有的Chrome实例，在终端执行：
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 &
```

然后Hermes就能通过CDP代理操控这个Chrome了。

### 5.2 使用场景

*   登录需要扫码的网站（比如视频号、微信公众号后台）
    
*   操作不提供API的网页系统
    
*   截图分析网页内容
    
*   自动化表单填写
    

> 详细配置参考官方文档：https://hermes-agent.nousresearch.com/docs/user-guide/features/browser#local-chrome-via-cdp-browser-connect\[3\]

* * *

## 六、速查表

**飞书常用操作：**

| 操作 | 方式 |
| --- | --- |
| 设置home群（定时任务投递） | 在群里发 `/set-home` |
| 查看谁在用 | `FEISHU_ALLOWED_USERS` 配置白名单 |
| 群聊策略 | `FEISHU_GROUP_POLICY` 设为 open/allowlist/disabled |

**配置文件位置：**

| 文件 | 作用 |
| --- | --- |
| `~/.hermes/.env` | API密钥、飞书凭证等敏感信息 |
| `~/.hermes/config.yaml` | 行为配置、显示设置、技能目录 |
| `~/.hermes/SOUL.md` | Hermes的性格和说话风格 |
| `~/.hermes/memories/USER.md` | 关于你的信息和偏好 |
| `~/.hermes/memories/MEMORY.md` | Hermes的长期记忆 |

**重启网关：**

*   飞书里说："重启网关"
    
*   终端执行：`hermes gateway restart`
    

* * *

## 写在最后

Hermes的默认配置是"安全优先"的保守设置——权限要确认、群聊要@、会话每天清空。这对初次使用来说没问题，但长期使用会觉得束手束脚。

按照这篇指南改完之后，你会发现Hermes突然"开窍"了：不打断你的工作、不频繁问你要权限、定时任务自动执行、飞书里随叫随到。

这就是一个真正好用的AI伙伴的样子。

官方文档：https://hermes-agent.nousresearch.com/docs/\[4\] 飞书对接文档：https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu\[5\]

### 引用链接

\[1\]_https://open.feishu.cn_

\[2\]_https://open.feishu.cn_

\[3\]_https://hermes-agent.nousresearch.com/docs/user-guide/features/browser#local-chrome-via-cdp-browser-connect_

\[4\]_https://hermes-agent.nousresearch.com/docs/_

\[5\]_https://hermes-agent.nousresearch.com/docs/user-guide/messaging/feishu_