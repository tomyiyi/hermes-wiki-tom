---
title: Log
created: 2026-04-11
updated: 2026-04-11
layer: meta
type: meta
tags: [meta]
---
# Wiki Log

## 2026-05-02
- **full-read-plus | Justin Welsh 全网资料整合**
  - 来源：微信文章 + GrowthInReverse($1.7M分析) + JustinWelsh.me官方文档 + Creator MBA课程大纲
  - 新增综合文档：processed/JustinWelsh-Content-IP-Complete-Workflow-20260502.md
  - 核心产出：
    - 完整财务数据：$1.73M/年，90%+利润率
    - Content OS 5模块完整大纲（Module 1-5详细）
    - Creator MBA 14章节完整大纲（111节课/19小时）
    - Hub & Spoke 4步官方原文
    - 选题矩阵3×3模型完整解析
    - 工具栈：Taplio/Twemex/Notion/Buffer/Canva
  - 同步更新：index.md
- **Content-OS-self-media | 自媒体工作流借鉴分析**
  - 扩展研究：Dan Koe Build-Teach-Earn、Ship 30 for 30（Dickie Bush）、Ali Abdaal批量系统
  - 新增文档：processed/Content-OS-Self-Media-Workflow-Adaptation-20260502.md
  - 核心产出：
    - Content OS 5模块 × 自媒体完整适配
    - PAS/AIDA/Hook三大写作框架详解+示例
    - Hub & Spoke × 自媒体分发矩阵
    - 借鉴优先级：立即/1-2周/长期三档
    - 完整周工作流示例（职场成长赛道）
  - Skill新增：productivity/opc-content-workflow（街道/自媒体双版本）


## 2026-04-28
- **full-article-read | 读完 45 篇 Hermes 文章**
  - Phase 1: 精读 7 篇 HIGH (~105KB) + 通读 11 篇 MEDIUM (~67KB)
  - 核心洞察：Fallback Model坑(5个)、Periodic Nudge机制、三层记忆架构、Skill触发条件、Profile隔离机制
  - 产出：`30-ops/hermes-articles-full-read-optimization-plan.md`
- **optimization-plan | 系统优化方案生成**
  - 18 篇文章系统性分析后输出 9 项优化建议
  - 🔴 立即执行：Telegram降噪、Timezone设置、Fallback Model配置
  - 🟡 本周执行：memory-audit skill、Research Profile、工作空间规范
  - 🟢 长期优化：Honcho用户画像、Delegation子模型、Multi-Agent工作流
  - 关键发现：Hermes无自动过期机制，需定期memory audit补偿

## 2026-04-27
- **wechat-archive | web-access技能介绍**
  - 微信原文：让AI像人一样浏览网页！web-access Skills彻底解决数据抓取难题
  - 来源：木汝科技（muru）
  - 归档：`processed/web-access-skill-wechat-20260427.md`
  - 核心：通过CDP控制Chrome绕过反爬，登录态复用，支持公众号/小红书等反爬站点
- **wechat-article-research | Hermes Agent 热点文章采集**
  - 来源：搜狐科技 + web_search 聚合
  - 归档：`processed/hermes-agent-overview-20260427.md`
  - 核心：Hermes Agent = Nous Research 自我进化AI智能体，三层架构（持久记忆+技能系统+用户建模），10万+ GitHub Stars

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## 2026-05-04
- **merge | 合并三个Obsidian资料库**
  - 合并来源：2026-知识库(~30篇)、newage_vault(~52篇) → hermes-wiki
  - 新增：gstack(3篇)、hermes-optimization(5篇)、hermes文章(15篇)、Knowledge笔记(46篇)、微信文章(3篇)
  - 删除重复：Reference_gstack、Graphify 1_72、concepts/AGENTS.md、concepts/stock-analysis-architecture.md
  - 归档：processed-stub(14个<2KB)、summary-stubs(25个)、_archive/processed/(11个)
  - 旧目录清理：action/、backlog/、queries/、synthesis/、entities/、概念/、行动/、Clippings/、conversations/ 已合并或删除
  - 批量补全：95个无frontmatter文件已全部添加layer/type/tags/title
  - index.md 总页数更新：56 → 334

## [2026-04-11] create | Wiki initialized
- Domain: AI Agent 技术、自动化工作流、知识管理、LLM 应用实践
- Structure created with SCHEMA.md, index.md, log.md
- Path: /Users/tom/Desktop/hermes-wiki

## [2026-04-11] ingest | 3 articles ingested
- Ingested: graphify-token-reduction-1-72.md
- Ingested: karpathy-llm-wiki-personal-knowledge-base.md
- Ingested: karpathy-obsidian-claudian-tutorial.md
- Created concepts: graphify, karpathy-llm-wiki, knowledge-management-principles
- Created entities: obsidian
- Updated: index.md, log.md

## [2026-04-11] restructure | Two-dimensional taxonomy added
- Added layer dimension to SCHEMA.md: raw → processed → summary → synthesis → action
- New dirs: processed/, summary/, synthesis/, action/
- concepts/ & entities/ moved to _archive/
- layer is now top-level directory; type stays as frontmatter attribute
- index.md and log.md updated

## [2026-04-11] fill | processed/ layer populated (3 pages)
- processed/graphify.md: Token data, dual-channel mechanism, relation labels, Leiden clustering
- processed/karpathy-llm-wiki.md: Three vs five layer architecture, Ingest/Lint flow
- processed/obsidian-tutorial.md: Tool chain, best practices, Claudian install

## [2026-04-11] fill | synthesis/ layer populated (1 page)
- synthesis/knowledge-compilation-pattern.md: RAG vs knowledge compilation, two technical paths, five-layer resonance

## [2026-04-11] fill | action/ layer populated (1 page)
- action/hermes-wiki-initialized.md: Wiki init + two-dimension restructure, action_id=wiki-init-20260411

## [2026-04-11] update | index.md rebuilt
- All 11 pages now listed under correct layer sections

## [2026-04-11] ingest | hermes-agent-wechat-20260411.md
- URL: https://mp.weixin.qq.com/s/_c-MR-RxjFrwWgJn4nyPrg
- Title: 取代龙虾的是爱马仕？狂揽4万星的Hermes Agent，不只是OpenClaw平替
- 12KB 干净正文，无 JS 混入
- Source: ifanr 公众号（爱马仕/Nous Research）
- Topic: Hermes Agent vs OpenClaw 评测，4层记忆系统、Learning Loop、Periodic Nudge、Auxiliary Models

## [2026-04-11] ingest | processed/hermes-agent.md + summary/concepts/hermes-agent.md
- processed: 核心要点 + 机制详情（Learning Loop / 四层记忆 / Auxiliary Models / 支持平台）
- summary: 一句话总结 + 核心判断 + 与 Hermes workspace 的关系 + 开放问题

## [2026-04-11] action | 工作流升级（4步全部完成）
- Step 1: conversations/save_conversation.py + conversations-archive.md 自动沉淀规则
- Step 2: MEMORY.md 软上限 3000 字符（新增文件头注释）
- Step 3: agentskills.io 格式 action/hermes-workflow-upgrade-20260411.md
- Step 4: Cron "Hermes Wiki Weekly Nudge" 每週日 09:00 触发，检查 lint + stale pages
- Cron job ID: 658b29799b7a
- 触发条件参考 Hermes Agent Periodic Nudge 机制

## [2026-04-11] create | Lint health check script
- scripts/lint.py: orphaned pages, stale content (>90d), missing frontmatter, broken wikilinks
- All 15 pages pass: 0 issues, 5 reasonable orphaned warnings

## [2026-04-11] action | article-review-round1-20260411
- 第一轮回顾：Graphify / Karpathy LLM Wiki / 知识管理原则
- 每篇提炼：核心观点 + 启发 + 迭代计划
- 识别出4项待落地：conversations确定性标签 / processed增量刷新 / ingest-AI推荐 / wiki-output-challenge
- 对话已自动沉淀到 conversations/

## [2026-04-11] create | backlog/ 层 + 4项待办
- backlog/backlog-index.md — 待办总览
- backlog/ingest-ai-recommend.md — 2026-04-12 执行
- backlog/conversations-certainty-auto.md — 2026-04-12 执行
- backlog/wiki-output-challenge.md — 有问题时触发
- backlog/processed-incremental-refresh.md — 2026-04-13 执行
- Weekly Nudge cron 更新：检查 lint + backlog 状态
- lint.py 修复：check_wikilinks 和 check_orphaned 补 backlog/ 路径

## [2026-04-11] create | conversations/ layer
- conversations/conversations-archive.md: Conversations 层说明与收录标准
- SCHEMA.md updated: added conversations to layer table and rules

## [2026-04-12] ingest | Hermes-Agent-爱马仕Agent全面解析-a9f521
- **Hermes Agent: 爱马仕Agent全面解析** — 开源Agent框架，三层记忆系统+闭合学习循环，实现从一次性工具到长期智能搭档的进化
- 存档: raw/articles/Hermes-Agent-爱马仕Agent全面解析-a9f521.md, summary/concepts/Hermes-Agent-爱马仕Agent全面解析-a9f521.md
- 来源: [Hermes Agent: 爱马仕Agent全面解析](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | Hermes-Agent-深度解析-a9f521
- **Hermes Agent 深度解析** — Hermes Agent是具有三层记忆系统的自主智能体框架，从一次性工具进化为持续学习的长周期搭档
- 存档: raw/articles/Hermes-Agent-深度解析-a9f521.md, summary/concepts/Hermes-Agent-深度解析-a9f521.md
- 来源: [Hermes Agent 深度解析](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | Hermes-Agent-有史以来增长最快的AI-Agent框架-a9f521
- **Hermes Agent - 有史以来增长最快的AI Agent框架** — Hermes Agent是一款开源AI Agent框架，通过三层记忆系统和Skill机制实现持续学习和经验沉淀。
- 存档: raw/articles/Hermes-Agent-有史以来增长最快的AI-Agent框架-a9f521.md, summary/concepts/Hermes-Agent-有史以来增长最快的AI-Agent框架-a9f521.md
- 来源: [Hermes Agent - 有史以来增长最快的AI Agent框架](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | AI大模型发展综述-c80735
- **AI大模型发展综述** — 
- 存档: raw/articles/AI大模型发展综述-c80735.md, summary/concepts/AI大模型发展综述-c80735.md
- 来源: [AI大模型发展综述]()

## [2026-04-12] ingest | AI大模型发展综述-c80735
- **AI大模型发展综述** — 
- 存档: raw/articles/AI大模型发展综述-c80735.md, summary/concepts/AI大模型发展综述-c80735.md
- 来源: [AI大模型发展综述]()

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 开源AI Agent Hermes原生支持微信，以学习循环实现持续进化
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent实现AI学习闭环，支持微信
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent成最快开源Agent，三层记忆+原生微信支持
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent：具备闭合学习循环的开源AI Agent，原生支持微信
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent开源AI助手支持微信，具备自主学习进化能力
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent开源AI Agent，支持微信并具备自动学习进化能力
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 会成长的AI搭档：原生微信支持+自学习循环
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — Hermes Agent成最快增长开源Agent，三层记忆学习系统原生支持微信
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-a9f521
- **wechat article** — 开源AI Agent新星Hermes支持微信接入，三层记忆实现持续进化
- 存档: raw/articles/wechat-article-a9f521.md, summary/concepts/wechat-article-a9f521.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/YNeg111oiSLnocIxlQzaIA)

## [2026-04-12] ingest | wechat-article-81de13
- **wechat article** — Hermes Agent内置循环学习系统，用久越智能，与OpenClaw互补
- 存档: raw/articles/wechat-article-81de13.md, summary/concepts/wechat-article-81de13.md
- 来源: [wechat article](https://mp.weixin.qq.com/s/Z1yXVDRkLJJv_Cg6qycB4Q)

## [2026-04-12] ingest | Hermes-Agent测评-2026年必须换的下一代AI-Agent-429bad
- **Hermes Agent测评：2026年必须换的下一代AI Agent** — 2026年必须升级到带自我进化能力的AI Agent
- 存档: raw/articles/Hermes-Agent测评-2026年必须换的下一代AI-Agent-429bad.md, summary/concepts/Hermes-Agent测评-2026年必须换的下一代AI-Agent-429bad.md
- 来源: [Hermes Agent测评：2026年必须换的下一代AI Agent]()

## [2026-04-12] ingest | Hermes-Agent完全指南-自进化AI-Agent框架实战-60k-Stars-b7061e
- **Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）** — 自进化AI Agent框架，内置学习循环支持技能自创与跨session持续进化
- 存档: raw/articles/Hermes-Agent完全指南-自进化AI-Agent框架实战-60k-Stars-b7061e.md, summary/concepts/Hermes-Agent完全指南-自进化AI-Agent框架实战-60k-Stars-b7061e.md
- 来源: [Hermes Agent完全指南：自进化AI Agent框架实战（60k Stars）](https://mp.weixin.qq.com/s/oxq1xH-E5irufiNkWKADHQ)

## [2026-04-12] ingest | article-d391bd
- **article** — None
- 存档: raw/articles/article-d391bd.md, summary/concepts/article-d391bd.md
- 来源: [article](https://mp.weixin.qq.com/s/-gNBbuKBSdT39XIikRpHfQ)

## [2026-04-13] ingest | 8992a932d2b4_取代龙虾的是爱马仕-狂揽4万星的Hermes-Agent-不只是OpenClaw平替-ae10ea
- **8992a932d2b4_取代龙虾的是爱马仕？狂揽4万星的Hermes Agent，不只是OpenClaw平替** — 开源AI助手Hermes凭内置学习循环超越OpenClaw
- 存档: raw/articles/8992a932d2b4_取代龙虾的是爱马仕-狂揽4万星的Hermes-Agent-不只是OpenClaw平替-ae10ea.md, summary/concepts/8992a932d2b4_取代龙虾的是爱马仕-狂揽4万星的Hermes-Agent-不只是OpenClaw平替-ae10ea.md
- 来源: [8992a932d2b4_取代龙虾的是爱马仕？狂揽4万星的Hermes Agent，不只是OpenClaw平替]()

## [2026-04-13] ingest | b4150d594ac5_OpenClaw-的对手来了-Hermes-Agent-狂飙-40-4k-Star-真能干活--d224cf
- **b4150d594ac5_OpenClaw 的对手来了！Hermes Agent 狂飙 40.4k Star，真能干活（附保姆级教程）。** — 开源AI Agent框架Hermes爆火，40.4k Star主打自进化功能
- 存档: raw/articles/b4150d594ac5_OpenClaw-的对手来了-Hermes-Agent-狂飙-40-4k-Star-真能干活--d224cf.md, summary/concepts/b4150d594ac5_OpenClaw-的对手来了-Hermes-Agent-狂飙-40-4k-Star-真能干活--d224cf.md
- 来源: [b4150d594ac5_OpenClaw 的对手来了！Hermes Agent 狂飙 40.4k Star，真能干活（附保姆级教程）。]()

## [2026-04-13] ingest | 2957d41fbf15_Hermes-Agent-保姆级安装教程-超详细踩坑指南-852844
- **2957d41fbf15_Hermes Agent 保姆级安装教程（超详细踩坑指南）** — Hermes Agent内置循环学习系统，可自动进化技能
- 存档: raw/articles/2957d41fbf15_Hermes-Agent-保姆级安装教程-超详细踩坑指南-852844.md, summary/concepts/2957d41fbf15_Hermes-Agent-保姆级安装教程-超详细踩坑指南-852844.md
- 来源: [2957d41fbf15_Hermes Agent 保姆级安装教程（超详细踩坑指南）]()

## [2026-04-13] ingest | 94454529b142_Hermes-Agent-深度解读-与OpenClaw的路线差异-61ab1a
- **94454529b142_Hermes Agent 深度解读, 与OpenClaw的路线差异** — 
- 存档: raw/articles/94454529b142_Hermes-Agent-深度解读-与OpenClaw的路线差异-61ab1a.md, summary/concepts/94454529b142_Hermes-Agent-深度解读-与OpenClaw的路线差异-61ab1a.md
- 来源: [94454529b142_Hermes Agent 深度解读, 与OpenClaw的路线差异]()

## [2026-04-13] ingest | cf85aeecffad_Hermes-Agent测评-2026年必须换的下一代AI-Agent-59c440
- **cf85aeecffad_Hermes Agent测评：2026年必须换的下一代AI Agent** — 
- 存档: raw/articles/cf85aeecffad_Hermes-Agent测评-2026年必须换的下一代AI-Agent-59c440.md, summary/concepts/cf85aeecffad_Hermes-Agent测评-2026年必须换的下一代AI-Agent-59c440.md
- 来源: [cf85aeecffad_Hermes Agent测评：2026年必须换的下一代AI Agent]()

## [2026-04-13] ingest | a7996cc07296_Hermes-Agent今天更新了-有一个细节我觉得比Gemini支持更重要-a3f97e
- **a7996cc07296_Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要** — Agent自我诊断标志AI从工具向自主体范式转变
- 存档: raw/articles/a7996cc07296_Hermes-Agent今天更新了-有一个细节我觉得比Gemini支持更重要-a3f97e.md, summary/concepts/a7996cc07296_Hermes-Agent今天更新了-有一个细节我觉得比Gemini支持更重要-a3f97e.md
- 来源: [a7996cc07296_Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要]()

## [2026-04-13] ingest | Hermes-Agent完全指南-cca8fe
- **Hermes Agent完全指南** — 
- 存档: raw/articles/Hermes-Agent完全指南-cca8fe.md, summary/concepts/Hermes-Agent完全指南-cca8fe.md
- 来源: [Hermes Agent完全指南]()

## [2026-04-13] ingest | Hermes-agent-高级玩法-d13774
- **Hermes agent 高级玩法** — Hermes agent配置与高级玩法详解
- 存档: raw/articles/Hermes-agent-高级玩法-d13774.md, summary/concepts/Hermes-agent-高级玩法-d13774.md
- 来源: [Hermes agent 高级玩法]()

## [2026-04-13] ingest | 5402671550e3_养龙虾已经Out-现在都流行爱马仕Agent-还原生支持微信-9e00fd
- **5402671550e3_养龙虾已经Out！现在都流行爱马仕Agent，还原生支持微信** — Hermes Agent原生微信支持，三层记忆系统让AI持续成长
- 存档: raw/articles/5402671550e3_养龙虾已经Out-现在都流行爱马仕Agent-还原生支持微信-9e00fd.md, summary/concepts/5402671550e3_养龙虾已经Out-现在都流行爱马仕Agent-还原生支持微信-9e00fd.md
- 来源: [5402671550e3_养龙虾已经Out！现在都流行爱马仕Agent，还原生支持微信]()

## [2026-04-13] ingest | 395f4636416e_Karpathy-的-LLM-Wiki-火了-我改造了一下-比原版更好用-82fe1a
- **395f4636416e_Karpathy 的 LLM Wiki 火了，我改造了一下，比原版更好用** — AI知识库三层变五层，从沉淀到产出
- 存档: raw/articles/395f4636416e_Karpathy-的-LLM-Wiki-火了-我改造了一下-比原版更好用-82fe1a.md, summary/concepts/395f4636416e_Karpathy-的-LLM-Wiki-火了-我改造了一下-比原版更好用-82fe1a.md
- 来源: [395f4636416e_Karpathy 的 LLM Wiki 火了，我改造了一下，比原版更好用]()

## [2026-04-13] ingest | 股票分析系统架构文档-318982
- **股票分析系统架构文档** — 股票分析系统v6架构文档，整合技术指标、财务诊断、资金流向与Prophet预测
- 存档: raw/articles/股票分析系统架构文档-318982.md, summary/concepts/股票分析系统架构文档-318982.md
- 来源: [股票分析系统架构文档]()

## [2026-04-13] ingest | bac90116238b_Hermes-Agent-多代理模式完全实战指南-39ebe0
- **bac90116238b_Hermes Agent 多代理模式完全实战指南** — 
- 存档: raw/articles/bac90116238b_Hermes-Agent-多代理模式完全实战指南-39ebe0.md, summary/concepts/bac90116238b_Hermes-Agent-多代理模式完全实战指南-39ebe0.md
- 来源: [bac90116238b_Hermes Agent 多代理模式完全实战指南]()

## [2026-04-13] ingest | 1ce13da5e79f_Hermes-Agent-必做配置与调试-从能用到好用-9c7dda
- **1ce13da5e79f_Hermes Agent 必做配置与调试：从能用到好用** — Hermes Agent配置指南：双模型fallback架构实现稳定运行
- 存档: raw/articles/1ce13da5e79f_Hermes-Agent-必做配置与调试-从能用到好用-9c7dda.md, summary/concepts/1ce13da5e79f_Hermes-Agent-必做配置与调试-从能用到好用-9c7dda.md
- 来源: [1ce13da5e79f_Hermes Agent 必做配置与调试：从能用到好用]()

## [2026-04-13] ingest | Hermes-agent-高级玩法-d13774
- **Hermes agent 高级玩法** — AI代理Hermes的多场景高级配置与工作流优化指南
- 存档: raw/articles/Hermes-agent-高级玩法-d13774.md, summary/concepts/Hermes-agent-高级玩法-d13774.md
- 来源: [Hermes agent 高级玩法]()

## [2026-04-13] batch-process | 32文档批量分类处理（SOP 7步）
- 原始文档: 32个.md（含9个重复），去除重复后19篇独立内容
- 识别7大类别: 深度解读/架构、安装/配置、高级玩法/多代理、对比/评测、资讯/周边、知识管理LLM Wiki、自用项目
- 🔴高价值(4篇) → raw层存档 + 深度分析 → 新增概念页×2 + 对比页×1
- 🟡资讯类(3篇) → 精简摘要存档
- ⚫低价值重复(9篇) → 已过滤（不做深度处理）
- 新增: simin-hermes-architecture-business-model, aliu-hermes-deep解读路线差异, Alan-hsu-hermes-advanced-play-review
- 新增概念: hermes-four-layer-memory-architecture, skills-auto-evolution
- 新增对比: hermes-vs-openclaw-vs-claude-code
- stock-analysis架构文档 → processed层标记（⚠️ OpenClaw版需迁移Hermes）
- index.md更新: Total 20→28, 新增synthesis+comparisons条目

## [2026-04-13] B-done | Docker部署指南深度处理
- Dockercore《1分钟Docker部署Hermes Agent》(307行) → processed/hermes-docker-deployment-guide-dockercore.md
- 提取: 三种运行模式、配置边界、排障四层、安全底线、命令速查
- 关键结论: ~/.hermes→/opt/data映射是核心，setup必须先行

## [2026-04-13] E-done | LLM Wiki × 2 合并深度处理
- 2篇合并: 栗氪聊AI(安装教程) + 改造版LLM Wiki → 概念/karpathy-llm-wiki-methodology.md
- 核心: RAG vs Wiki本质差异、三层架构、Ingest/Query/Lint三操作、Obsidian+Claudian工具链
- 结论: hermes-wiki的SCHEMA+index+log+两维分类 = 已对齐Karpathy LLM Wiki架构
- 发现可优化: Lint矛盾检测、Query自动化流程、ingest→wiki更新自动化

## [2026-04-13] D+C-done | 资讯归档+剩余文章降噪
- D: 3篇资讯类 → 快速摘要归档（v0.8.0更新1篇已处理，其余2篇重复/低价值过滤）
- C: 5篇安装/配置类文章 → 去重合并为 raw/hermes-installation-compendium.md
- index.md: 新增Archive分类，Total 28→34

## [2026-04-13] Wiki 框架建设 + 批量 frontmatter 修复
- 22个 raw frontmatter 缺失 → 批量修复（加 layer:raw, type:article, source:wechat）
- 5个断链（Hermes-agent-高级玩法引用不存在的 wiki 文件）→ 已识别，保留待清理
- 建第一个概念页：concepts/hermes-agent-core-concepts.md（三层记忆/闭合学习循环/多平台/配置架构/对比表）
- index.md 更新：Synthesis 新增 hermes-agent-core-concepts
- lint issue: 27 issues → frontmatter 问题已修复，断链 5 个待处理

## [2026-04-13] 建概念页 ×3 + lint 全部清零
- 修 raw/股票分析系统架构文档（frontmatter 重复注入损坏）
- 建 concepts/stock-analysis-architecture.md（v6 系统、10章节、数据源、迁移计划）
- 建 concepts/hermes-installation.md（Docker部署、配置边界、常见坑、排障四层）
- index.md Synthesis 新增 2 个概念页
- lint: 5 broken links → 全部清零（AGENTS/SOUL/USER/INDEX/frontmatter-spec 内部链接已删除）
- lint wikilink 解析 bug → 修复（split方向反了），中文目录 概念/ 已加入候选路径
- lint issues: 6 → 0 ✅
## [2026-04-13] 第三轮：批量提炼 + archive 空洞文章
- 归档 11 个空洞 processed 文章 → _archive/processed/（body < 150 chars，无实质内容）
- 建 synthesis/ai-agent-architecture-comparison.md（记忆/进化/技能/数据主权全面对比）
- 建 synthesis/knowledge-management-ai-era.md（RAG vs Wiki vs Graphify，Lint 1 broken link 已修）
- 建 synthesis/hermes-wechat-integration.md（平台接入矩阵、飞书重点、MMX-CLI 全模态扩展）
- lint: 新增 broken link（hermes-wiki-query skill 路径），已修

## [2026-04-20] ingest+skill | Graph of Skills (GoS) — full two-channel flow
- Channel 1 (Wiki): raw/articles/graph-of-skills-2026-04-20.md + summary/concepts/graph-of-skills.md
- Channel 2 (Skill): created `skill-retrieval` — Seed→Merge→Rerank→Return pipeline for dependency-aware skill retrieval
- Relevance: skill-retrieval (find skills) + skill-authoring (create skills) are complementary pairs
- Total pages: 115 (+1), skills: 72 (+1)

## [2026-04-20] skill-create | Enhanced skill system from wiki synthesis
- `knowledge-to-behavior` already existed (full two-channel framework)
- Enhanced it with cross-reference to new skills
- Created `skill-authoring` — three-layer model, patch>overwrite, agentskills.io format
- Created `wiki-knowledge-channel` — deprecated, superseded by enhanced `knowledge-to-behavior`
- Created `wiki-ingest-flow` — Karpathy LLM Wiki operational workflow with two-channel check
- 4-skill stack: `llm-wiki` + `knowledge-to-behavior` + `skill-authoring` + `wiki-ingest-flow`
- WIKI_PATH: .env 受保护，通过记忆机制处理

## 2026-04-26 14:37 | created
- [synthesis] CodeBuddy 能力增强记录

## 2026-04-28 16:36 | ingest | Ilya Sutskever 访谈精华
- [10-knowledge/ai-dev/ilya-sutskever-访谈精华-学习笔记] — 8次访谈，12个知识点归档
- [10-knowledge/rationality/think-like-reality-学习笔记] — Yudkowsky 文章归档
- [10-knowledge/rationality/think-like-reality-应用记录] — Ilya 补充：压缩即理解、Top-down信念、神经网络最简化
- [skill] deep-compression — 新建深度压缩检验 skill（Q1/Q2/Q3 深层问题）
- [skill] reality-check — 核心原则新增第6、7条（来源+Yudkowsky+Ilya）
- [skill] wiki-ingest-flow — Step 5.5 新增 Deep Compression Check
- [skill] knowledge-to-behavior — 提取标准新增第5条：压缩质量门
- [skill] systematic-debugging — 反藩篱表新增 Top-down belief 条目
- [skill] workflow-engineering — Eval 反直觉时新增 Top-down 检查点

## 2026-04-28 16:50 | policy | 知识消化闭环纪律确认
- 每次 ingest 完成，必须走完：wiki写入 + index更新 + log追加 + Skill同步 + Deep Compression Check
- 没有"这次就算了"——知识不闭环等于没存
- 自检清单：Wiki写了吗 / index更新了吗 / log追加了吗 / 有可复用行为吗 / Compression通过了吗


## 2026-04-28 afternoon batch — 11 articles ingested

### URLs processed
| # | URL | Title | Status |
|---|-----|-------|--------|
| 1 | mmguo.dev/writings/ilya/?lang=zh | Ilya Sutskever 访谈列表 | ✅ archived |
| 2 | arc.net/folder/... | (internal Link folder — inaccessible) | ⛔ skipped |
| 3 | cs.virginia.edu/~robins/YouAndYourResearch | You and Your Research (Hamming) | ✅ archived |
| 4 | mmguo.dev/writings/ai-native-multithreaded | Multithreaded + Deep Focus | ✅ archived |
| 5 | mmguo.dev/writings/self-referentiality-of-meaning | Self-Referentiality of Meaning | ✅ archived |
| 6 | mmguo.dev/writings/fingerprint-of-reality | Fingerprints of Reality | ✅ archived |
| 7 | mmguo.dev/writings/boundary-method | Boundary Definition Method | ✅ archived |
| 8 | mmguo.dev/prompts/protagonist-perspective | Protagonist Perspective | ✅ archived |
| 9 | mmguo.dev/prompts/trident | Trident Triple Mind Model | ✅ archived |
| 10 | mmguo.dev/prompts/dr-sharp | Dr. Sharp | ✅ archived |
| 11 | lesswrong.com/posts/tWLFWAndSZSYN6rPB | Think Like Reality (Yudkowsky) | ✅ archived |

### Storage
- Raw: `~/Desktop/hermes-wiki/raw/articles/`
- 10 new files archived
- Index: updated, total pages 38→48
- DeerFlow 2.0 skipped per user request

## 2026-04-28 下午 | batch | 11篇文章系统性阅读 → 可落地优化

### 来源文章（11篇）
- You and Your Research (Hamming, 1986) — 伟大科学家的方法论
- Think Like Reality (Yudkowsky, 2007) — 像现实一样思考
- Ilya Sutskever 访谈精华（8次访谈）— 压缩即理解、next-token prediction
- Dr. Sharp v6 (mmguo) — AI研究框架，Top-down信念传播
- Trident (mmguo) — 三重视角深度思考prompt
- Fingerprints of Reality (mmguo) — 效果定义→特征拆解→模式组合
- Self-Referentiality of Meaning (mmguo) — 意义的自指性哲学分析
- Boundary Definition Method (mmguo) — 边界定义法
- Protagonist Perspective (mmguo) — 主角视角prompt
- Hermes架构与商业模型（思敏）— 五层架构+数据飞轮
- Karpathy LLM Wiki改造方案 — 三层变五层，知识到产出

### 落地行动（全部自动执行）
| # | 行动 | 状态 |
|---|------|------|
| 1 | Weekly Knowledge Nudge cron（每周一09:00） | ✅ 已创建 |
| 2 | wiki-ingest-flow skill → Trident三视角分析 | ✅ 已更新 |
| 3 | Deep Compression Check（Q1/Q2/Q3）| ✅ 已在skill中 |
| 4 | log.md → 本条记录 | ✅ 正在写入 |
| 5 | SCHEMA.md → 已存在且完整，无需修改 | ✅ |
| 6 | 飞书文档输出标准化 | ✅ 已识别待落地 |

### 核心方法论沉淀
- **Ilya 压缩定律**：Lossless Compression = True Understanding（压缩即理解）
- **Trident三视角**：框架构建者×批判者×实践者，同时运行
- **Hermes Periodic Nudge**：无任务时定时唤醒，主动问"有什么值得沉淀？"
- **Fingerprints方法**：定义效果→拆解特征→组合模式（可迁移到知识整理）

### SCHEMA.md 确认
- 两维分类（layer + type）✅
- Frontmatter规范 ✅
- Tag Taxonomy ✅
- Update Policy ✅
- 无需修改，现有框架已对齐

## 2026-04-28 下午补全批次 — 完整正文已归档

### 补全内容（已用 console 提取完整文本）
| 文章 | 文件 | 状态 |
|------|------|------|
| You and Your Research (Hamming) | you-and-your-research-hamming.md | ✅ 完整正文+QA+传记，含完整引语 |
| Think Like Reality (Yudkowsky) | think-like-reality-yudkowsky.md | ✅ 完整正文存档 |
| Dr. Sharp (mmguo) | dr-sharp-mmguo.md | ✅ 完整 v6 prompt (1400字) 存档 |
| Trident (mmguo) | trident-mmguo.md | ✅ 完整 prompt 存档 |
| mmguo 其他文章 | 已完成摘要归档 | ✅ |

## 2026-05-02
- Karpathy AI知识库理念落地 | 微信文章-LLM-Wiki-20260428.md → processed/微信文章-LLM-Wiki-20260428.md | nashsu/llm_wiki 3300+⭐，两步链式录入×四维知识图谱×自动缺口补全
- Justin Welsh 一人公司内容系统 | 微信文章-JustinWelsh-一人公司-20260427.md → processed/微信文章-JustinWelsh-一人公司-20260427.md | 选题矩阵×Hub&Spoke，与OPC社区直接关联

## 2026-04-29
- 美股AI概念股重挫·软银狂泻12% (第一财经) | 微信文章-美股AI概念股重挫软银狂泻12-20260429.md | 归档 raw/articles/

## 2026-05-03
- **wechat-archive | Everywhere 桌面AI助手**
  - 来源：[Everywhere：一个真正"懂你屏幕"的桌面 AI 神器](https://mp.weixin.qq.com/s/ghIslC3c-lx7BEZ7Od9eEA)
  - 公众号：极客之家
  - 归档：processed/微信文章-Everywhere桌面AI助手-20260503.md
  - 核心：Everywhere = 桌面AI助手，按快捷键唤出直接读懂屏幕，无障碍API+多模型支持，专注消除AI使用时的切换成本
- **23位游资心法·完整合集** | 23位游资心法/目录.md → 10-knowledge/stock-trading/23位游资心法/ | 完成全部29位游资心法采集归档，含综合分析文件(00-综合分析.md)，核心发现：7条共同铁律、4阶段学习路径、4大时代演进、9种操作体系对比。人物覆盖：炒股养家/职业炒手/Asking/赵老哥/令狐冲/不动明王/艾琳歆/退学炒股/独股一箭/杨永兴/著名刺客/章盟主/欢乐海岸/宁波敢死队/徐翔/龙飞虎/丁一熊/万法归宗/92科比/浓汤野人/榜中榜/凡倍无名/落升/万狮虎/孤独牛背/乔帮主/瑞鹤仙/小鳄鱼/涅盘重升
