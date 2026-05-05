---
title: lark-cli版本v1.0.9发布，三天发两版：自更新命令来了，幻灯片也能创建了
author: 元进式
                        元进式
date: 2026年4月13日
cover: /assets/img/news/-0.png
head:
  - - meta
    - name: 新闻
---
      
      大家好，我是Ryan![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_04.png#imgIndex=0)，欢迎来到MetaRyse-元进式认知提升系列探索新知~今天是2026年4月12日，星期日。今天跟大家一起探讨下：**lark-cli 又更新了，而且一次发了两个版本。**

> 从 1.0.7 到 1.0.9，仅用了 **3 天**，跨越了两个版本。

> 这迭代速度，说实话，有点疯狂。

lark-cli 是飞书官方开源的命令行工具，从 3 月 28 日首次发布到现在，**15 天已经发布了 10 个版本**。平均 1.5 天一个版本，这在开源项目里已经是"日更"级别的节奏了。

这次跨越的两个版本——1.0.8 和 1.0.9——带来了几个重量级功能：**自更新命令、幻灯片创建、Base 大幅增强**。今天咱们就来详细拆解。

## 一、版本时间线：15天10版本

##   

先看数据，数据不会骗人：

| 
版本

 | 

发布日期

 | 

间隔

 | 

核心更新

 |
| --- | --- | --- | --- |
| 

1.0.0

 | 

2026-03-28

 | 

\-

 | 

首次开源发布，20个 Skills，跨平台支持

 |
| 

1.0.1

 | 

2026-03-31

 | 

3天

 | 

自动更新检测、消息分页、API 错误输出修复

 |
| 

1.0.2

 | 

2026-04-01

 | 

1天

 | 

macOS keychain/DPAPI 沙盒兼容、mail 本地图片解析

 |
| 

1.0.3

 | 

2026-04-02

 | 

1天

 | 

\--jq flag、drive shortcuts、代理支持、妙记下载

 |
| 

1.0.4

 | 

2026-04-03

 | 

1天

 | 

MITM 安全修复、用户身份支持 im +chat-create

 |
| 

1.0.5

 | 

2026-04-07

 | 

4天

 | 

20MB+ 大文件分片上传、严格模式身份过滤

 |
| 

1.0.6

 | 

2026-04-08

 | 

1天

 | 

RuntimeContext 并发修复、docs 媒体分片、vc 录制 shortcut

 |
| 

1.0.7

 | 

2026-04-09

 | 

1天

 | 

Bot 自动授权、Windows stdin 修复、mail 别名支持

 |
| 

1.0.8

 | 

2026-04-10

 | 

1天

 | 

**自更新命令、Base 大幅增强、whiteboard Mermaid**

 |
| 

1.0.9

 | 

2026-04-11

 | 

1天

 | 

**幻灯片创建、sheets 行列操作、minutes search**

 |

15 天、10 个版本、累计 **80+ 个** **PR**。这节奏已经超过了大多数开源项目的迭代频率。

## 二、v1.0.8：自更新命令终于来了

##   

### 2.1 之前的痛点

###   

之前更新 lark-cli，需要用 npm，一套流程下来至少 3 步操作。而且 npm 在 Windows 上经常遇到文件占用问题，更新失败。

### 2.2 现在的方式

###   

1.0.8 版本新增了 **update 命令**（PR [#391](javascript:;)）：

lark-cli update

**更厉害的是**，这个命令还支持：

| 
功能

 | 

说明

 |
| --- | --- |
| 

自更新

 | 

检测并安装最新版本

 |
| 

验证

 | 

安装后自动验证是否成功

 |
| 

回滚

 | 

如果更新失败，自动回滚到旧版本

 |

这意味着以后更新 lark-cli，不用再折腾 npm了。

### 2.3 `--file` flag：文件上传更方便

###   

PR [#395](javascript:;) 新增了 **\--file flag**，支持 multipart/form-data 文件上传，简化需要上传文件的 API 调用。

## 三、v1.0.8：Base（多维表格）大幅增强

##   

这是 1.0.8 版本最大的功能模块更新，一口气新增了 **7 个 Base 相关功能**：

### 3.1 dashboard-arrange：自动排列仪表盘

PR [#388](javascript:;) 新增了 `+dashboard-arrange` 命令，自动排列多维表格仪表盘中的区块布局。

### 3.2 record batch +add / +set：批量操作记录

PR [#277](javascript:;) 新增了批量添加和设置记录的快捷方式，之前需要逐条操作，现在可以批量处理。

### 3.3 +record-search：关键词搜索记录

PR [#328](javascript:;) 新增了关键词搜索记录，在多维表格中搜索包含关键词的记录。

### 3.4 view visible fields：查询/设置视图可见字段

PR [#326](javascript:;) 新增了两个快捷方式，控制视图中显示哪些字段。

### 3.5 Base 新功能汇总

| 
功能

 | 

PR

 | 

用途

 |
| --- | --- | --- |
| 

`+dashboard-arrange`

 | 

[#388](javascript:;)

 | 

自动排列仪表盘布局

 |
| 

`+add` / `+set`

 | 

[#277](javascript:;)

 | 

批量添加/设置记录

 |
| 

`+record-search`

 | 

[#328](javascript:;)

 | 

关键词搜索记录

 |
| 

`view visible-fields`

 | 

[#326](javascript:;)

 | 

查询/设置视图可见字段

 |

##   

## 四、v1.0.8：whiteboard 支持 Mermaid 和 PlantUML

##   

PR [#382](javascript:;) 大幅增强了画板功能：

*   **+****query**：查询画板内容信息
    
*   **+update 支持 Mermaid/PlantUML**：用 Mermaid 或 PlantUML 语法更新画板内容，不用手动绘图
    

这对需要绘制流程图、架构图的用户来说，是个巨大的便利。

## 五、v1.0.8：其他重要更新

##   

| 
功能

 | 

PR

 | 

说明

 |
| --- | --- | --- |
| 

calendar room find

 | 

[#403](javascript:;)

 | 

查找指定时间段可用的会议室

 |
| 

mail +triage 分页

 | 

[#301](javascript:;)

 | 

分页获取邮件分类结果

 |
| 

沙盒/初始化错误提示

 | 

[#384](javascript:;)

 | 

错误信息更清晰

 |
| 

Markdown 换行支持

 | 

[#338](javascript:;)

 | 

修复换行被忽略的问题

 |

##   

## 六、v1.0.9：幻灯片终于能创建了

##   

### 6.1 slides +create

PR [#389](javascript:;) 和 [#425](javascript:;) 新增了幻灯片创建命令：

lark-cli slides +create --title "产品演示" --folder-token "fldcnxxx"

**用途：** 终于可以通过 CLI 创建飞书幻灯片了！

### 6.2 slides 创建的意义

###   

| 
对比

 | 

之前

 | 

现在

 |
| --- | --- | --- |
| 

docs

 | 

✅ 支持创建

 | 

✅

 |
| 

sheets

 | 

✅ 支持创建

 | 

✅

 |
| 

slides

 | 

❌ 不支持

 | 

✅ **支持了！**

 |

这意味着飞书三大文档类型（文档、表格、幻灯片）全部支持通过 CLI 创建。

## 七、v1.0.9：sheets 行列和单元格操作

##   

### 7.1 dimension shortcuts：行列操作

PR [#413](javascript:;) 新增了行列操作快捷方式：插入行、删除行、插入列、删除列。

### 7.2 cell shortcuts：单元格操作

PR [#412](javascript:;) 新增了单元格操作快捷方式：

| 
功能

 | 

命令示例

 |
| --- | --- |
| 

合并单元格

 | 

`sheets +merge --range "A1:B2"`

 |
| 

替换内容

 | 

`sheets +replace --range "A1:A10"`

 |
| 

设置样式

 | 

`sheets +style --range "A1:A10"`

 |

##   

## 八、v1.0.9：其他重要更新

##   

| 
功能

 | 

PR

 | 

说明

 |
| --- | --- | --- |
| 

minutes search

 | 

[#359](javascript:;)

 | 

在妙记中搜索关键词

 |
| 

drive folder delete

 | 

[#415](javascript:;)

 | 

删除文件夹，支持异步任务轮询

 |
| 

attendance

 | 

[#405](javascript:;)

 | 

查询用户考勤记录

 |

##   

## 九、自然语言操作：AI Agent 的正确用法

##   

很多人看到这些命令会觉得复杂，但实际上在 Claude Code、Trae、Cursor 这些 AI Agent 工具中，你根本不需要记命令。

### 9.1 幻灯片创建：一句话搞定

###   

**你只需要说：**

> "帮我创建一个幻灯片，标题是「产品演示」，放在我的云空间根目录"

AI Agent 会自动理解需求、执行命令、返回结果。你完全不需要知道参数。

### 9.2 更多自然语言示例

###   

| 
你说的话

 | 

AI Agent 做的事

 |
| --- | --- |
| 

"帮我更新一下 lark-cli"

 | 

执行 `lark-cli update`

 |
| 

"创建一个幻灯片，标题叫周报"

 | 

执行 `slides +create`

 |
| 

"搜索会议妙记里提到「需求」的地方"

 | 

执行 `minutes +search`

 |
| 

"帮我画一个流程图"

 | 

调用 whiteboard +update，生成 Mermaid

 |
| 

"批量添加10条记录"

 | 

执行 `base +add`

 |

###   

### 9.3 这才是 Skills 的真正价值

###   

Skills 的本质不是让你学命令，而是：**让 AI Agent 理解****飞书****API****，你只需要说自然语言。**

这才是飞书开源 lark-cli 的真正意图：把飞书 API 变成 AI Agent 可理解的语言。

## 十、v1.0.8 + v1.0.9 新功能汇总

##   

| 
功能模块

 | 

新功能

 | 

版本

 | 

自然语言示例

 |
| --- | --- | --- | --- |
| 

CLI 核心

 | 

`update` 自更新命令

 | 

1.0.8

 | 

"帮我更新 lark-cli"

 |
| 

slides

 | 

`+create` 创建幻灯片

 | 

1.0.9

 | 

"创建一个幻灯片"

 |
| 

sheets

 | 

dimension shortcuts（行列操作）

 | 

1.0.9

 | 

"在表格里插入5行"

 |
| 

sheets

 | 

cell shortcuts（合并、替换、样式）

 | 

1.0.9

 | 

"合并 A1 到 B2 单元格"

 |
| 

base

 | 

`+dashboard-arrange` 仪表盘排列

 | 

1.0.8

 | 

"排列仪表盘布局"

 |
| 

base

 | 

`+add` / `+set` 批量记录操作

 | 

1.0.8

 | 

"批量添加10条记录"

 |
| 

base

 | 

`+record-search` 记录搜索

 | 

1.0.8

 | 

"搜索包含张三的记录"

 |
| 

whiteboard

 | 

Mermaid/PlantUML 支持

 | 

1.0.8

 | 

"帮我画一个流程图"

 |
| 

calendar

 | 

`+room-find` 会议室查找

 | 

1.0.8

 | 

"找一个空闲会议室"

 |
| 

minutes

 | 

`+search` 搜索

 | 

1.0.9

 | 

"搜索会议里提到需求的地方"

 |
| 

drive

 | 

`+delete-folder` 删除文件夹

 | 

1.0.9

 | 

"删除这个文件夹"

 |

##   

## 十一、如何更新

##   

### 方式一：让 AI Agent 帮你（推荐）

###   

**直接说一句话：** "帮我更新一下 lark-cli 到最新版本"

### 方式二：新的自更新命令

lark-cli updatenpx skills add larksuite/cli -y -g

### 方式三：传统 npm 方式

```
npm update -g @larksuite/cli
```

### 必须做的事👇

**重启****你的 AI Agent 工具**，才能加载最新的 Skills。

## 十二、从版本演进看飞书的开发者策略

##   

15天10版本分析：

| 
阶段

 | 

版本

 | 

重点

 |
| --- | --- | --- |
| 

基础建设

 | 

1.0.0-1.0.3

 | 

核心功能、跨平台支持

 |
| 

安全加固

 | 

1.0.4

 | 

MITM 安全修复

 |
| 

功能补齐

 | 

1.0.5-1.0.6

 | 

大文件上传、并发修复

 |
| 

体验优化

 | 

1.0.7

 | 

Bot 授权、Windows 修复

 |
| 

功能爆发

 | 

1.0.8-1.0.9

 | 

自更新、幻灯片、Base 增强

 |

这个演进路径反映了：**先稳地基，再补功能，最后爆发式增强。**

## 十三、写在最后

##   

lark-cli 这波更新，给我的感觉是：**飞书团队在认真补齐功能短板。**

*   自更新命令解决了长期痛点
    
*   幻灯片创建补齐了三大文档类型
    
*   Base 大幅增强让多维表格操作更完整
    
*   whiteboard Mermaid 支持让绘图更便捷
    
      
    

对于飞书开发者来说，现在 CLI 的功能已经相当完善。但 15 天 10 版本的节奏，也提醒我们：开源项目迭代太快，要跟上节奏需要持续关注。

* * *

**⭐⭐⭐评论区聊聊：**

你最期待哪个新功能？自更新命令、幻灯片创建，还是 Base 的批量操作？欢迎在评论区分享你的使用体验~

![](/assets/img/news/-0.png)

* * *

**MetaRyse | 元进式**

记录一个普通人的认知系统升级实验

每周更新 | 硬核坦诚 | 行动优先

（本文耗时60分钟完成，是对"设定个人时薪"原则的实践坚持。）