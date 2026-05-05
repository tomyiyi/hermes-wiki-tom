---
title: gstack 是什么？顺便把 BMad、Superpowers、GSD 一起摆上桌比一比
author: 巾山
                        巾山
date: 2026年4月13日
cover: /assets/img/news/gstack 是什么？顺便把 BMad、Superpowers、GSD 一起摆上桌比一比-0.png
head:
  - - meta
    - name: 新闻
---
      
YC 总裁 Garry Tan 前阵子把自己用的一整套 Claude Code 配置开源了，叫 gstack。上线 48 小时破万 star，现在已经爬到 5 万。

一句话讲 gstack 在干嘛：**把 Claude Code 调教成一个虚拟创业团队**。你一个人写代码，但它给你配了 CEO、设计师、工程经理、代码审查员、QA、安全官、发布工程师。每个角色都是一个 slash command，背后是一段精心写的 Markdown prompt。

听起来是不是很熟悉？对，这个思路跟国内开发圈聊得比较多的 BMad 方法非常像。但两者味道完全不同。这篇文章把 gstack 讲清楚，再顺手把 BMad、Superpowers、GSD 这些同类框架一起摆上桌比一比。

## gstack 到底是怎么运作的

核心机制其实很朴素：一个 `CLAUDE.md` 文件 + 23 个 slash command + 8 个 power tool，全部 Markdown，MIT 协议。

`CLAUDE.md` 是 Claude Code 每次启动都会自动读的文件，Garry 把他对创业公司开发流程的理解写进去了。23 个 skill 按冲刺阶段排列：

```
Think → Plan → Build → Review → Test → Ship → Reflect
```

每个阶段有一个或多个角色接手，串行喂数据，前一步的产出直接是后一步的输入：

| 
阶段

 | 

主角

 | 

干什么

 |
| --- | --- | --- |
| 

Think

 | 

CEO

 | 

重新审视产品方向，砍掉不该做的

 |
| 

Plan

 | 

工程经理

 | 

锁定架构、拆任务

 |
| 

Build

 | 

开发

 | 

写代码

 |
| 

Review

 | 

代码审查员

 | 

按生产级标准挑毛病

 |
| 

Test

 | 

QA 主管

 | 

开真实浏览器点一遍

 |
| 

Ship

 | 

发布工程师

 | 

推 PR、发布

 |
| 

Reflect

 | 

CEO

 | 

复盘，沉淀经验

 |

中间还穿插设计师（挑 UI slop）、安全官（跑 OWASP + STRIDE 审计）、文档工程师等角色，总共 23 个 skill + 8 个 power tool。

为什么这套东西能火？我觉得有两个原因：

一是它是 Garry Tan 本人在用的配置，不是哪个理论派写的。他见过几千家 YC 公司，知道创业早期哪些事情必须做、哪些可以跳。这种"浓缩的经验"比任何方法论都值钱。

二是它足够轻。纯 Markdown，没有任何依赖，clone 下来就能用。跟那种动辄要装一整套工具链的方案比，心理门槛低得多。

## 类似思路的还有哪几个

gstack 不是孤品，2026 年这个赛道至少有四个玩家在跑。先用一张表看全景：

| 
框架

 | 

GitHub Stars

 | 

核心解决

 | 

一句话概括

 |
| --- | --- | --- | --- |
| 

Superpowers

 | 

~94k

 | 

能力扩展

 | 

给 Claude 装一堆"手"，能连 MCP、调 API、操作第三方系统

 |
| 

gstack

 | 

~50k

 | 

项目结构

 | 

把 Claude 编成一个虚拟创业团队，按冲刺流程干活

 |
| 

GSD

 | 

~35k

 | 

任务执行

 | 

不讲角色扮演，把活儿拆细、一条一条干完

 |
| 

BMad Method

 | 

—

 | 

敏捷全流程

 | 

按敏捷研发生命周期铺开的拟人化 agent 团队

 |

**Superpowers** 跟 gstack 的角色化思路是正交的，能叠着用。

**BMad Method**，全称 Breakthrough Method for Agile AI-Driven Development，是最像 gstack 但气质完全不同的那个。它也是"虚拟团队"，但按敏捷研发生命周期铺开，角色还起了拟人化名字：

| 
角色

 | 

名字

 | 

职责

 |
| --- | --- | --- |
| 

Business Analyst

 | 

Mary

 | 

市场/领域研究、Project Brief

 |
| 

Product Manager

 | 

John

 | 

PRD、需求拆解

 |
| 

Architect

 | 

Winston

 | 

架构设计、技术选型

 |
| 

UX Designer

 | 

Sally

 | 

UX 方案、界面规范

 |
| 

Scrum Master

 | 

Bob

 | 

Epic 拆 Story、Sprint 规划

 |
| 

Developer

 | 

Amelia

 | 

Story 驱动开发

 |
| 

QA

 | 

Quinn

 | 

测试策略、质量门禁

 |

最有意思的是 **Party Mode**，能把多个 agent 拉进同一个会话里讨论问题——比如把 Architect + PM + Dev 同时拽过来对一个技术决策开会。

**GSD**（Get Shit Done）定位最朴素，不搞花活，就是帮你把事情做完。

这四个基本覆盖了"让 Claude Code 干活更靠谱"这件事的主流路径。

## 把它们摆一起看

最直观的差别不是功能列表，而是**约束了什么**。一张表横向对比：

| 
维度

 | 

gstack

 | 

BMad

 | 

Superpowers

 | 

GSD

 |
| --- | --- | --- | --- | --- |
| 

约束什么

 | 

项目结构一致性

 | 

敏捷流程完整性

 | 

外部能力边界

 | 

执行闭环

 |
| 

流程粒度

 | 

重执行（Think/Plan 快过）

 | 

重前期（PRD 没写完不让动代码）

 | 

跟流程无关

 | 

只有执行

 |
| 

文档产出

 | 

仅 CLAUDE.md，其他在代码/PR

 | 

大量 Markdown，PRD+Story 是核心资产

 | 

基本无

 | 

基本无

 |
| 

项目阶段

 | 

偏 Greenfield

 | 

Greenfield + Brownfield 都覆盖

 | 

不挑

 | 

不挑

 |
| 

角色数量

 | 

23 skill + 8 power tool

 | 

12+ 拟人化 agent，多 pack

 | 

按工具数算

 | 

少

 |
| 

产出物

 | 

代码、PR

 | 

PRD、架构、Epic、Story、代码

 | 

集成能力

 | 

代码

 |
| 

组合性

 | 

可叠 Superpowers

 | 

可叠 Superpowers

 | 

可叠任意框架

 | 

可叠任意框架

 |
| 

学习曲线

 | 

低

 | 

中高

 | 

中

 | 

低

 |

一句话读懂这张表：**gstack 告诉你怎么干，BMad 告诉你该干什么，Superpowers 让你能干，GSD 保证干完。**

## 什么情况用哪个

先上决策表，再细说：

| 
你的情况

 | 

推荐

 | 

原因

 |
| --- | --- | --- |
| 

Solo 全栈，从零开始，想快

 | 

gstack

 | 

角色切换成本低，流程短

 |
| 

中大型项目，需要文档留存

 | 

BMad

 | 

PRD + Story 是一等公民，半年后还能看懂

 |
| 

有遗留代码库，要加功能或重构

 | 

BMad

 | 

自带 `document-project` 做棕地梳理

 |
| 

需要对接 Slack / Linear / Figma / 数据库

 | 

Superpowers

 | 

专治外部集成

 |
| 

需求已想清楚，只要 Claude 写代码

 | 

GSD

 | 

其他都是噪音

 |
| 

什么都想要

 | 

gstack + Superpowers + GSD 叠用

 | 

注意 skill 可能冲突

 |

**从零开始做一个 solo 全栈项目**，用 gstack。一个人开 7 个马甲自己跟自己吵架，Garry 自己就是这么用的。

**项目有规模、未来要交接**，用 BMad。我自己手上的 QualityHub 走的就是这条路——前期花时间把 PRD、架构文档写扎实，后期 Story 驱动开发非常顺，半年后回来看，还知道当时为什么这么决策。这是 gstack 给不了的。

**需要大量外部集成**，用 Superpowers，或把它叠在别的框架上。它跟 gstack、BMad 不冲突，可以同装。

**需求清晰，只要执行**，GSD 够用。

有开发者写过 Superpowers + gstack + GSD 叠加用的方案，思路是：gstack 管结构、Superpowers 补能力、GSD 保证事情真的被做完。注意 skill 之间可能冲突，调用时明确指定。

## 最后

回到 gstack 本身。它最大的贡献不是那 23 个 skill，而是证明了一件事：**Claude Code 这种 agentic CLI 工具，真正的差距不在模型，而在你怎么给它写规则**。同样一个 Claude，gstack 用户和裸用户产出的代码质量能差一个量级。

这也解释了为什么 BMad、Superpowers 这些框架都能火——大家都在摸索同一件事：怎么把一个通用 AI，变成一个符合自己工作方式的专属工具。

gstack 给了一个答案，BMad 给了另一个答案。没有谁对谁错，看你想做什么样的项目、想留下什么样的产出。

选一个上手，比纠结哪个更好强得多。