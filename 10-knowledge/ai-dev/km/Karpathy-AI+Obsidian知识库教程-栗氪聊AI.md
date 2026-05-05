---
title: Karpathy AI+Obsidian知识库教程 栗氪聊AI
created: 2026-05-04
updated: 2026-05-04
layer: processed
type: comparison
tags: [AI-Agent, knowledge-management]
---

**Karpathy-AI+Obsidian知识库教程-栗氪聊AI**

**工具安装**

**Obsidian**

[下载地址](https://obsidian.md/zh/)

**Claude Code**

Claude Code网上安装教程很多，没有安装claude code的朋友，大家可以自行找一个教程跟着安装就行，我这里就不赘述了

[Claude Code链接](https://github.com/anthropics/claude-code)

如果不是claude官方订阅，推荐下一个[cc switch](https://github.com/farion1231/cc-switch)来切换其他国产模型和api，非常好用！

**Claudian**

claudian是一个把claude code以图形化界面接入Obsidian的插件，比claude code原生的命令行界面好用很多

**安装方法**

在Obsidian设置里，第三方插件里搜索“brat”插件并安装

打开BRAT插件的设置页面，添加插件，输入claudian的地址进行安装：https://github.com/YishenTu/claudian

安装后就能在Obsidian的右上角看到一个小机器人按钮，这就是claudian了，点开就会有一个图形对话界面，背后就是claude code

**Obsidian必备的5个skill**

这是Obsidian CEO亲自做的5个skill，里面都是Obsidian的一些操作规范和最佳实践，也是非常好用，推荐安上

安装方式：直接把这个链接扔给你的claude code，让它安装上就行：https://github.com/kepano/obsidian-skills

**搭建&使用教程**

1\. **创建知识库文件夹结构**

打开Obsidian新建一个仓库，直接发给AI（我用的是Claudian）

“请你根据 karpathy 的这套方法，帮我把仓库里的文件夹的结构给建立起来”

AI会自动帮你创建好所有的文件夹以及对应的文件

我是提前创建了一个markdown文件叫“karpathy的wiki方法论”让AI读取，你可以和我一样，也可以直接复制在对话框里发给AI

提前创建的markdown文件  

karpathy的wiki方法论（复制发给AI就可以）👇

SQL  
\# LLM Wiki  
<br/>A pattern for building personal knowledge bases using LLMs.  
<br/>This is an idea file, it is designed to be copy pasted to your own LLM Agent (e.g. OpenAI Codex, Claude Code, OpenCode / Pi, or etc.). Its goal is to communicate the high level idea, but your agent will build out the specifics in collaboration with you.  
<br/>\## The core idea  
<br/>Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but the LLM is rediscovering knowledge from scratch on every question. There's no accumulation. Ask a subtle question that requires synthesizing five documents, and the LLM has to find and piece together the relevant fragments every time. Nothing is built up. NotebookLM, ChatGPT file uploads, and most RAG systems work this way.  
<br/>The idea here is different. Instead of just retrieving from raw documents at query time, the LLM \*\*incrementally builds and maintains a persistent wiki\*\* — a structured, interlinked collection of markdown files that sits between you and the raw sources. When you add a new source, the LLM doesn't just index it for later retrieval. It reads it, extracts the key information, and integrates it into the existing wiki — updating entity pages, revising topic summaries, noting where new data contradicts old claims, strengthening or challenging the evolving synthesis. The knowledge is compiled once and then \*kept current\*, not re-derived on every query.  
<br/>This is the key difference: \*\*the wiki is a persistent, compounding artifact.\*\* The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read. The wiki keeps getting richer with every source you add and every question you ask.  
<br/>You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it. You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time. In practice, I have the LLM agent open on one side and Obsidian open on the other. The LLM makes edits based on our conversation, and I browse the results in real time — following links, checking the graph view, reading the updated pages. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.  
<br/>This can apply to a lot of different contexts. A few examples:  
<br/>\- \*\*Personal\*\*: tracking your own goals, health, psychology, self-improvement — filing journal entries, articles, podcast notes, and building up a structured picture of yourself over time.  
\- \*\*Research\*\*: going deep on a topic over weeks or months — reading papers, articles, reports, and incrementally building a comprehensive wiki with an evolving thesis.  
\- \*\*Reading a book\*\*: filing each chapter as you go, building out pages for characters, themes, plot threads, and how they connect. By the end you have a rich companion wiki. Think of fan wikis like \[Tolkien Gateway\](https://tolkiengateway.net/wiki/Main_Page) — thousands of interlinked pages covering characters, places, events, languages, built by a community of volunteers over years. You could build something like that personally as you read, with the LLM doing all the cross-referencing and maintenance.  
\- \*\*Business/team\*\*: an internal wiki maintained by LLMs, fed by Slack threads, meeting transcripts, project documents, customer calls. Possibly with humans in the loop reviewing updates. The wiki stays current because the LLM does the maintenance that no one on the team wants to do.  
\- \*\*Competitive analysis, due diligence, trip planning, course notes, hobby deep-dives\*\* — anything where you're accumulating knowledge over time and want it organized rather than scattered.  
<br/>\## Architecture  
<br/>There are three layers:  
<br/>\*\*Raw sources\*\* — your curated collection of source documents. Articles, papers, images, data files. These are immutable — the LLM reads from them but never modifies them. This is your source of truth.  
<br/>\*\*The wiki\*\* — a directory of LLM-generated markdown files. Summaries, entity pages, concept pages, comparisons, an overview, a synthesis. The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references, and keeps everything consistent. You read it; the LLM writes it.  
<br/>\*\*The schema\*\* — a document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) that tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow when ingesting sources, answering questions, or maintaining the wiki. This is the key configuration file — it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time as you figure out what works for your domain.  
<br/>\## Operations  
<br/>\*\*Ingest.\*\* You drop a new source into the raw collection and tell the LLM to process it. An example flow: the LLM reads the source, discusses key takeaways with you, writes a summary page in the wiki, updates the index, updates relevant entity and concept pages across the wiki, and appends an entry to the log. A single source might touch 10-15 wiki pages. Personally I prefer to ingest sources one at a time and stay involved — I read the summaries, check the updates, and guide the LLM on what to emphasize. But you could also batch-ingest many sources at once with less supervision. It's up to you to develop the workflow that fits your style and document it in the schema for future sessions.  
<br/>\*\*Query.\*\* You ask questions against the wiki. The LLM searches for relevant pages, reads them, and synthesizes an answer with citations. Answers can take different forms depending on the question — a markdown page, a comparison table, a slide deck (Marp), a chart (matplotlib), a canvas. The important insight: \*\*good answers can be filed back into the wiki as new pages.\*\* A comparison you asked for, an analysis, a connection you discovered — these are valuable and shouldn't disappear into chat history. This way your explorations compound in the knowledge base just like ingested sources do.  
<br/>\*\*Lint.\*\* Periodically, ask the LLM to health-check the wiki. Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search. The LLM is good at suggesting new questions to investigate and new sources to look for. This keeps the wiki healthy as it grows.  
<br/>\## Indexing and logging  
<br/>Two special files help the LLM (and you) navigate the wiki as it grows. They serve different purposes:  
<br/>\*\*index.md\*\* is content-oriented. It's a catalog of everything in the wiki — each page listed with a link, a one-line summary, and optionally metadata like date or source count. Organized by category (entities, concepts, sources, etc.). The LLM updates it on every ingest. When answering a query, the LLM reads the index first to find relevant pages, then drills into them. This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages) and avoids the need for embedding-based RAG infrastructure.  
<br/>\*\*log.md\*\* is chronological. It's an append-only record of what happened and when — ingests, queries, lint passes. A useful tip: if each entry starts with a consistent prefix (e.g. \`## \[2026-04-02\] ingest | Article Title\`), the log becomes parseable with simple unix tools — \`grep "^## \\\[" log.md | tail -5\` gives you the last 5 entries. The log gives you a timeline of the wiki's evolution and helps the LLM understand what's been done recently.  
<br/>\## Optional: CLI tools  
<br/>At some point you may want to build small tools that help the LLM operate on the wiki more efficiently. A search engine over the wiki pages is the most obvious one — at small scale the index file is enough, but as the wiki grows you want proper search. \[qmd\](https://github.com/tobi/qmd) is a good option: it's a local search engine for markdown files with hybrid BM25/vector search and LLM re-ranking, all on-device. It has both a CLI (so the LLM can shell out to it) and an MCP server (so the LLM can use it as a native tool). You could also build something simpler yourself — the LLM can help you vibe-code a naive search script as the need arises.  
<br/>\## Tips and tricks  
<br/>\- \*\*Obsidian Web Clipper\*\* is a browser extension that converts web articles to markdown. Very useful for quickly getting sources into your raw collection.  
\- \*\*Download images locally.\*\* In Obsidian Settings → Files and links, set "Attachment folder path" to a fixed directory (e.g. \`raw/assets/\`). Then in Settings → Hotkeys, search for "Download" to find "Download attachments for current file" and bind it to a hotkey (e.g. Ctrl+Shift+D). After clipping an article, hit the hotkey and all images get downloaded to local disk. This is optional but useful — it lets the LLM view and reference images directly instead of relying on URLs that may break. Note that LLMs can't natively read markdown with inline images in one pass — the workaround is to have the LLM read the text first, then view some or all of the referenced images separately to gain additional context. It's a bit clunky but works well enough.  
\- \*\*Obsidian's graph view\*\* is the best way to see the shape of your wiki — what's connected to what, which pages are hubs, which are orphans.  
\- \*\*Marp\*\* is a markdown-based slide deck format. Obsidian has a plugin for it. Useful for generating presentations directly from wiki content.  
\- \*\*Dataview\*\* is an Obsidian plugin that runs queries over page frontmatter. If your LLM adds YAML frontmatter to wiki pages (tags, dates, source counts), Dataview can generate dynamic tables and lists.  
\- The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free.  
<br/>\## Why this works  
<br/>The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages. Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero.  
<br/>The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else.  
<br/>The idea is related in spirit to Vannevar Bush's Memex (1945) — a personal, curated knowledge store with associative trails between documents. Bush's vision was closer to this than to what the web became: private, actively curated, with the connections between documents as valuable as the documents themselves. The part he couldn't solve was who does the maintenance. The LLM handles that.  
<br/><br/>\## Note  
<br/>This document is intentionally abstract. It describes the idea, not a specific implementation. The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice. Everything mentioned above is optional and modular — pick what's useful, ignore what isn't. For example: your sources might be text-only, so you don't need image handling at all. Your wiki might be small enough that the index file is all you need, no search engine required. You might not care about slide decks and just want markdown pages. You might want a completely different set of output formats. The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest.

建立好后的文件结构大概长这样，可以根据你自己的需求来定制

如果你觉得AI给你创建的效果不好，也可以直接参考复制我的配置，我用起来还不错

我的claude.md👇，直接复制内容替换掉你的claude.md内容就可以

Markdown  
\# Wiki Schema — Harness Engineering  
<br/>\> 这是 Claude 的行为配置文件（Schema）。它定义了这个知识库的结构、约定和工作流。  
\> 每次会话开始时，Claude 应先阅读此文件，再阅读 \`wiki/index.md\`，再开始工作。  
<br/>\---  
<br/>\## 仓库结构  
<br/>\`\`\`  
Harness Engineering/  
├── CLAUDE.md ← 本文件：Schema 配置（Claude 的"说明书"）  
├── raw/ ← 原始资料层（只读，不可修改）  
│ ├── README.md  
│ └── 素材/ ← 文章内嵌图片的本地存储  
├── wiki/ ← 知识库层（Claude 全权维护）  
│ ├── index.md ← 内容索引（每次 ingest 后更新）  
│ ├── log.md ← 操作日志（仅追加）  
│ ├── 实体/ ← 实体页：人、公司、产品、工具等  
│ ├── 概念/ ← 概念页：原理、方法论、技术术语  
│ ├── 来源/ ← 来源摘要页：每篇原始资料的提炼  
│ └── 对比/ ← 对比分析页：跨来源横向综合  
└── karpathy wiki方法论.md ← 参考文档  
\`\`\`  
<br/>\### 层级规则  
<br/>| 层级 | 目录 | 谁可以修改 |  
|------|------|-----------|  
| 原始资料 | \`raw/\` | \*\*只有用户\*\*，Claude 只读 |  
| 知识库 | \`wiki/\` | \*\*只有 Claude\*\*，用户可读 |  
| Schema | \`CLAUDE.md\` | 用户和 Claude 共同演进 |  
<br/>\---  
<br/>\## Wiki 页面约定  
<br/>\### Frontmatter（YAML）  
<br/>所有 wiki 页面都应有以下 frontmatter：  
<br/>\`\`\`yaml  
\---  
type: entity | concept | source | comparison  
tags: \[tag1, tag2\]  
sources: \[来源文件名或 URL\]  
created: YYYY-MM-DD  
updated: YYYY-MM-DD  
\---  
\`\`\`  
<br/>\### 页面类型说明  
<br/>| 类型 | 目录 | 命名格式 | 说明 |  
|------|------|---------|------|  
| \`entity\` | \`wiki/实体/\` | \`实体名.md\` | 具体的人、组织、产品 |  
| \`concept\` | \`wiki/概念/\` | \`概念名.md\` | 核心原理、方法论、术语 |  
| \`source\` | \`wiki/来源/\` | \`YYYY-MM-DD 标题.md\` | 原始资料的摘要和要点 |  
| \`comparison\` | \`wiki/对比/\` | \`对比主题.md\` | 跨来源横向对比分析 |  
<br/>\### 交叉引用  
<br/>\- 页面间用 Obsidian Wiki-link：\`\[\[页面名\]\]\`  
\- 提到的每个实体/概念都应链接到对应页面  
\- 如果对应页面不存在，先创建再引用  
\- \*\*重要\*\*：每个 \`wiki/来源/\` 摘要页的顶部必须用干净的 wiki-link 链接到对应的 raw 文件，例如：\`\[\[raw/Effective harnesses for long-running agents\]\]\`，\*\*不要\*\*用反引号包住，否则 Obsidian 图谱视图无法识别链接  
<br/>\### 创建时机规则（Karpathy 自下而上原则）  
<br/>\*\*核心思想\*\*：Wiki 里的概念必须从多篇来源中自然浮现，而不是对单篇文章的过度抽象。  
<br/>| 页面类型 | 创建条件 |  
|---------|---------|  
| 实体页 | 同一实体（人/公司/产品）在 \*\*≥2 篇不同来源\*\* 中被明确提及 |  
| 概念页 | 同一概念（原理/方法/术语）在 \*\*≥2 篇不同来源\*\* 中被讨论 |  
| 对比页 | 对比主题已在 \*\*≥2 篇来源\*\* 中分别出现不同立场或数据 |  
| 来源摘要页 | 每篇原始资料都对应一个来源摘要页（\*\*始终创建\*\*，不受此规则约束） |  
<br/>\*\*具体流程\*\*：  
<br/>1\. \*\*第 1 篇来源出现\*\*：在来源摘要页的 \`tags\` 和 Related Concepts 中列出该概念（但\*\*不创建\*\*独立概念页）  
2\. \*\*第 2 篇来源出现\*\*：检查前一来源摘要是否提到过该概念 → \*\*是\*\* → 创建概念/实体/对比页；\*\*否\*\* → 继续等待  
3\. \*\*跨来源识别\*\*：读新文章时，主动回溯已有来源摘要，发现与当前内容的重叠 → 触发建页  
<br/>\> 这个规则与 Ingest 工作流第 4 步（"更新相关概念页"）配合使用：如果概念只出现在当前一篇里，先列在来源页中，不创建独立页；如果发现已有来源页提到过，则立即创建。  
<br/>\---  
<br/>\## 工作流  
<br/>\### 1. Ingest（摄取新资料）  
<br/>当用户说"摄取 XXX"或"处理 XXX"时：  
<br/>1\. \*\*阅读\*\* \`raw/\` 中的目标文件（含图片）  
2\. \*\*讨论\*\* 与用户确认关键要点和侧重点  
3\. \*\*创建\*\* \`wiki/来源/YYYY-MM-DD 标题.md\` 摘要页  
4\. \*\*更新\*\* 相关的实体页（不存在则创建）  
5\. \*\*更新\*\* 相关的概念页（不存在则创建）  
6\. \*\*更新\*\* \`wiki/index.md\`：添加新页面到对应表格，更新 Stats  
7\. \*\*追加\*\* \`wiki/log.md\`：格式 \`## \[YYYY-MM-DD\] ingest | 标题\`  
<br/>\> 一次摄取可能触及 10-15 个 wiki 页面，这是正常的。  
<br/>\### 2. Query（查询）  
<br/>当用户提问时：  
<br/>1\. \*\*阅读\*\* \`wiki/index.md\` 找到相关页面  
2\. \*\*深入\*\* 阅读相关页面及其链接  
3\. \*\*综合\*\* 生成回答，标注来源页面  
4\. \*\*归档\*\*（可选）：如果回答有价值，将其写入 \`wiki/对比/\` 作为新页面  
5\. \*\*追加\*\* \`wiki/log.md\`：格式 \`## \[YYYY-MM-DD\] query | 问题简述\`  
<br/>\### 3. Lint（健康检查）  
<br/>当用户说"检查 wiki"或"lint"时：  
<br/>检查以下问题并逐一修复：  
<br/>\- \[ \] 有无\*\*互相矛盾\*\*的说法（不同页面对同一事实描述不一致）  
\- \[ \] 有无\*\*孤儿页面\*\*（没有任何入链的页面）  
\- \[ \] 有无\*\*提到但缺页\*\*的实体/概念（有链接但目标页不存在）  
\- \[ \] 有无\*\*过时信息\*\*（被新资料推翻但未更新的内容）  
\- \[ \] \`index.md\` 是否与实际文件同步  
\- \[ \] 有无值得新建的汇总/对比页  
<br/>追加日志：\`## \[YYYY-MM-DD\] lint | 发现 N 个问题\`  
<br/>\---  
<br/>\## Index 维护规则  
<br/>\`wiki/index.md\` 的每一行格式：  
<br/>\`\`\`markdown  
| \[\[wiki/来源/2026-04-06 标题\]\] | 一句话简介 | 2026-04-06 |  
\`\`\`  
<br/>每次 ingest 或创建新页面后必须更新 index，同步更新 Stats 数字。  
<br/>\---  
<br/>\## Log 格式  
<br/>\`\`\`markdown  
\## \[YYYY-MM-DD\] 操作类型 | 标题  
<br/>\- 操作说明 bullet 1  
\- 操作说明 bullet 2  
\`\`\`  
<br/>操作类型固定为：\`init\` / \`ingest\` / \`query\` / \`lint\` / \`update\`  
<br/>\---  
<br/>\## 图片处理  
<br/>\- 原始资料中的图片应下载到 \`raw/素材/\` 目录  
\- wiki 页面引用图片用：\`!\[\[素材/图片名.png\]\]\`  
\- Claude 读取 Markdown 时先处理文本，再单独读取图片文件获取视觉信息  
<br/>\---  
<br/>\## 快速参考  
<br/>\`\`\`bash  
\# 查最近 5 条日志  
grep "^## \\\[" wiki/log.md | head -5  
<br/>\# 统计 wiki 页面数  
find wiki -name "\*.md" | grep -v index | grep -v log | wc -l  
<br/>\# 查找孤儿页面（无入链）  
\# 请求 Claude 执行 lint 操作  
\`\`\`  
<br/>\---  
<br/>\*Schema 版本：v1.2 — 2026-04-06\*（新增：创建时机规则，实体/概念/对比页须出现在 ≥2 篇来源才创建）  
\*如需调整结构或约定，直接修改本文件，Claude 下次会话时会遵循新规则。\*  

2\. **内容入库**

推荐安装一个Obsidian官方的chrome插件 “[Obsidian Web Clipper](https://chromewebstore.google.com/detail/obsidian-web-clipper/cnjifjpddelmedmihgijeibhnjfabmlf?hl=zh-CN&utm_source=ext_sidebar)”

这个插件可以一键以markdown格式保存网页内容、YouTube视频到Obsidian（带图片链接，图片支持下载到本地）

下面介绍如何设置将内容一键保存至指定仓库位置

设置好后，打开任意一个网页，点击插件，就能一键添加到提前指定好的位置

3\. **建立wiki概念**

当你每新增一篇内容，就可以直接告诉AI，他会根据claude.md的指示自动帮你整理，建立wiki，自然对话就行

4\. **定期健康检查**

当你内容多了之后，或者你想让AI检查一下wiki是否搭建完善，可以直接告诉AI，做一轮健康检查（Lint）

|     |     |
| --- | --- |
| claude.md里定义的规范 |     |

5\. **将好的回答输出保存至wiki沉淀**

当你觉得和AI讨论的内容很有价值时，可以直接让AI把这个回答保存至wiki，完成优质内容的沉淀&积累

**Harness Engineering学习材料**

有朋友需要可以自取

**OpenAI官方：Harness engineering: leveraging Codex in an agent-first world**  
链接：https://openai.com/index/harness-engineering/ （2026年2月11日）  
OpenAI团队用Codex实际构建内部百万行代码产品的完整案例，详细拆解分层架构、自定义linter、结构化测试、垃圾回收式漂移修正等harness设计。这是行业公认的“奠基之作”，直接展示了harness如何让代理从“聪明但不可靠”变成生产级工具。必读首选。

**Anthropic官方：Effective harnesses for long-running agents**  
链接：https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents （2025年11月26日）  
Anthropic工程团队针对长运行代理的经典论文级实践，解决跨多个上下文窗口的连贯性问题（初始化代理 + 环境管理 + 失败模式总结）。被后续几乎所有harness讨论反复引用，是理解“为什么prompt engineering不够”的必备基础。

**Anthropic官方：Harness design for long-running application development**  
链接：https://www.anthropic.com/engineering/harness-design-long-running-apps （2026年3月24日）  
接续上篇的进阶版，聚焦前端设计和长期自主软件工程的多代理harness，包含具体架构演进（从context reset到连续会话）。Anthropic在agentic coding前沿的最新实证，极具操作性。

**Martin Fowler网站：Harness engineering for coding agent users**  
链接：https://martinfowler.com/articles/harness-engineering.html （最近发布）  
软件工程界权威Martin Fowler站点文章，专门给coding agent使用者提供“外层harness”心智模型（信任建立、反馈循环、评估覆盖率）。把OpenAI/Anthropic的理念翻译成可落地的软件工程实践，极具普适性。

**Geoffrey Huntley：Ralph Wiggum as a Software Engineer（Ralph Wiggum Loop）**  
链接：https://ghuntley.com/ralph/ （2025年推出，后续被Anthropic官方插件支持）  
影响力爆棚的实战技术：通过简单bash/script循环实现“永不放弃”的持久迭代harness，被业界称为“Ralph Wiggum Technique”。Anthropic和LangChain都直接引用或借鉴，是最接地气的harness原型之一。

**LangChain官方博客：Improving Deep Agents with harness engineering**  
链接：https://blog.langchain.com/improving-deep-agents-with-harness-engineering/ （2026年2月17日）  
LangChain团队仅通过调整harness（自验证循环、中间件、上下文交付），就把coding agent在Terminal Bench 2.0从Top 30提升到Top 5的实证报告。数据驱动、代码级细节丰富，是“harness能显著超越模型升级”的最佳证明。

**LangChain官方博客：The Anatomy of an Agent Harness**  
链接：https://blog.langchain.com/the-anatomy-of-an-agent-harness/ （2026年3月）  
系统性拆解“Agent = Model + Harness”的完整架构，包括规划、技能、内存、工具、人机循环等组件。LangChain作为agent框架的核心输出，理论与实现结合得非常清晰。

**YouTube访谈：OpenAI’s Michael Bolin on Codex, Harness Engineering, and the Real Future of Coding Agents**  
链接：https://www.youtube.com/watch?v=6BAqgT3qe98  
OpenAI Codex技术负责人Michael Bolin深度对话，讲解harness vs 模型的本质区别、安全沙箱、多代理系统等。时长适中、干货密集，是听官方工程师亲口解释的最佳视频。

**arXiv学术论文：Building Effective AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engineering, and Lessons Learned**  
链接：https://arxiv.org/abs/2603.05344 （2026年）  
聚焦终端编码代理的scaffolding + harness + context工程，总结大量教训和最佳实践。学术严谨性高，适合想深入理解底层机制的研究型读者。

**YouTube/视频讲解：What Harness Engineering Actually Means**  
链接：https://www.youtube.com/watch?v=zYerCzIexCg （Louis-François Bouchard频道）  
清晰对比prompt engineering、context engineering与harness engineering的区别，并结合OpenAI/Anthropic案例讲解环境、工具、反馈循环的作用。适合作为入门或快速建立整体框架的视频补充。