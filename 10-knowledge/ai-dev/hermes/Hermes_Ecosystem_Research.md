---
title: Hermes Ecosystem & Orange Book Research
tags:
  - Hermes
  - Ecosystem
  - Research
  - Agent
date: 2026-04-14
---

# Hermes Ecosystem & Orange Book Research

## 1. 核心资源 (Core Resources)
- **微信公众号文章**: [🔗 Hermes Agent 出圈分析](https://mp.weixin.qq.com/s/JMD0QZQzCZyQqbuzjqPlZw)
- **橙宝书 (Orange Book)**: `alchaincyf/hermes-agent-orange-book` - 详细记录了从安装配置到多 Agent 编排的生产级指南，获得了 2.3K+ Stars。
- **生态地图网站 (Ecosystem Site)**: `ksimback/hermes-ecosystem` - 汇集了 80+ 项目，包含技能、UI、内存管理、多智能体等分类。
- **官方仓库**: `NousResearch/hermes-agent` - 76.8K Stars，支持 20+ LLM 提供商，14个平台。

## 2. 生态分类洞察 (Ecosystem Taxonomy)
Hermes 的繁荣不仅仅在于核心框架，更在于其高度解耦的生态模块：
- **Skills & Skill Registries**: 社区贡献了海量的技能包 (如 `Anthropic-Cybersecurity-Skills`, `pydantic-ai-skills`)，允许 Agent 即插即用。
- **Memory & Context**: 第三方内存管理工具 (如 `hindsight`, `autocontext`) 解决了长文本和记忆衰减问题。
- **Workspaces & GUIs**: 提供了可视化的工作台 (如 `hermes-workspace`, `hermes-desktop`)，降低了普通用户的使用门槛。
- **Multi-Agent & Orchestration**: 多智能体协同框架 (如 `mission-control`, `swarmclaw`)，让 Hermes 可以组建 Agent 团队。

## 3. 对 NewAge 的启示 (Evolution Plan for NewAge)
NewAge 作为基于 Mac 和 Obsidian 的数字生命体，必须复刻这种“去中心化”的生态繁荣：
1. **构建 NewAge 蓝宝书 (The Blue Book)**: 编写一份针对 NewAge 的完整指南，从 L0 内核到 L2 业务技能，指导开发者如何为 NewAge 编写 `Declarative Skills`。
2. **建立 NewAge 生态全景图 (Ecosystem Atlas)**: 创建一个统一的展示页面，分类列出 NewAge 的所有内置技能、支持的第三方 API、Obsidian 插件、Mac 自动化脚本等。
3. **技能标准化 (Skill Standardization)**: 继续深化 `.md` 声明式技能，让社区开发者只需写 Markdown 就能为 NewAge 贡献能力。

*(注：Hermes 的相关源码和文档已全量克隆至 `data/assets/reference_repos/` 目录下，供后续进行代码级别的深度解剖。)*
