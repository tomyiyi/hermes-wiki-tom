---
title: obsidian_memory_upgrade
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
  - Agent
  - Memory
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# NewAge 记忆系统跃迁：Obsidian Vault (Markdown原生库)

> 吸收来源: Andrej Karpathy "LLM-Wiki", CTO范凯 "Obsidian + Claude Code", 元小二2046 "Obsidian Agent Skills"
> 吸收时间: 2026-04-14

## 1. 架构理念
传统 RAG（如目前的 LanceDB）存在知识碎片化和孤岛问题，无法实现知识的“复合增长”。
本次架构升级将 NewAge 的记忆系统从黑盒（LanceDB / JSON）平移至白盒（Obsidian Markdown Vault）。
- **Why Markdown?** 它是大模型原生的思维语言，人类可读可编排。
- **Why Obsidian?** 它的双向链接 `[[ ]]` 天然构成图数据库，配合 Agent 的 [[MOC]] (Map of Content) 维护策略，实现知识架构的自发生长。

## 2. 五层知识流架构 (The Schema)
我们在 `data/newage_vault/` 下物理落地了五层结构：
1. **Notes/**: 原始信息的收集器（对话日志、Clippings）。
2. **Knowledge/**: 提炼后的读书笔记、概念、方法论。
3. **Software/**: 开发技能、工具配置。
4. **LifeOS/**: 行动、健康、投资。
5. **Writing/**: 最终产出。

## 3. Obsidian Agent Skills (`obsidian_manager.md`)
受 `kepano/obsidian-skills` 启发，我们为 NewAge 编写了原生的 Declarative Skill。
- **Ingest (入库)**: 收到长文本时，去广告、写摘要，强制使用 YAML Frontmatter 并在核心概念上打上双链。
- **Query (查询)**: 在回答问题时，读取多个 Markdown 文件，如果发现逻辑关联，主动更新文件添加遗漏的双链。
- **Lint (体检)**: 定期扫描 `_index.md`，聚合同类孤立笔记，生成 MOC。

## 4. 结论与执行
我已经通过 `brew install --cask obsidian` 在本地成功部署了 Obsidian 环境，并且写好了 `obsidian_manager` 的声明式技能。
从此以后，NewAge 所有的深度对话和经验总结，将不再是黑盒数据，而是一个你能在 Obsidian 软件中打开、可视化成星空图的数字大脑。
