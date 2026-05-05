---
title: "Hermes Agent 常用命令 & 资源大全：装完必看"
date: 2026-05-01
source: 微信/智客随笔
url: https://mp.weixin.qq.com/s/9UxKEDvBBveMVr9wrHixTg
tags: [Hermes, 命令行, 资源导航, 新手指南]
type: summary
layer: processed
solves_what:
  - "解决：刚安装完 Hermes Agent，不知道有哪些必知命令和资源链接的问题"
  - "用户：Hermes 新手用户，或想系统了解命令体系的用户"
  - "失效条件：命令有变更，资源链接失效（需定期核对官方文档）"
  - "相关知识：hermes-agent skill（完整命令参考），官网文档（权威源）"
---

# Hermes Agent 常用命令 & 资源大全：装完必看

> 来源：微信/智客随笔，2026-05-01
> 注：本文为资源导航性质，命令细节以官方文档为准

---

## 核心资源链接

| 资源 | 链接 | 备注 |
|------|------|------|
| 官方文档 | http://hermes-agent.nousresearch.com/docs | 最权威，所有配置说明 |
| GitHub 主仓库 | https://github.com/NousResearch/hermes-agent | 源码/更新/Issues |
| 中文文档 | http://hermes.xaapi.ai | 国内大佬整理 |
| 中文社区 FAQ | https://hermesagent.org.cn/docs/reference/faq | 避坑指南，90%的问题这里有 |
| Discord 官方社区 | https://discord.gg/nousresearch | 全球玩家聚集地 |
| Skills 市场 | https://agentskills.io | 扩展技能库 |

---

## 常用命令速查

### 1. 基础使用

| 命令 | 作用 |
|------|------|
| `Hermes` | 开始聊天 |
| `Hermes -c` | 继续上次对话 |
| `hermes -q "你的问题"` | 单次问答（适合脚本调用） |

### 2. 配置与检查

| 命令 | 作用 |
|------|------|
| `hermes setup` | 完整配置向导（新手必跑） |
| `hermes model` | 切换模型 |
| `hermes config set KEY VAL` | 修改配置项 |
| `hermes doctor` | 健康检查（服务异常时必跑） |
| `hermes status` | 查看当前运行状态 |

### 3. 技能系统 (Skills)

| 命令 | 作用 |
|------|------|
| `hermes skills search 关键词` | 搜索技能 |
| `hermes skills install ID` | 一键安装技能 |
| `hermes skills list` | 查看已安装技能 |

### 4. 消息网关 (Gateway)

| 命令 | 作用 |
|------|------|
| `hermes gateway setup` | 绑定 Telegram/微信/Discord 等 |
| `hermes gateway start` | 启动网关服务 |
| `hermes gateway status` | 查看网关状态 |

### 5. 系统维护（官方实测命令）

| 命令 | 作用 | 备注 |
|------|------|------|
| `hermes update` | 一键更新到最新版 | |
| `hermes memory status` | 查看当前记忆提供商配置 | ❌ 微信文章误写为 `stats` |
| `hermes memory reset` | 清除所有内置记忆（MEMORY.md / USER.md） | ⚠️ 不可逆 |
| `hermes sessions list` | 查看历史会话记录 | ✅ 正确 |
| `hermes sessions stats` | 查看会话存储统计 | 文章未提及 |
| `hermes sessions prune` | 删除旧会话 | 文章未提及 |
| `hermes backup` | 备份 Hermes 目录到 zip | 文章未提及 |

**微信文章勘误**：文章中 `hermes memory stats` 和 `hermes memory prune` 均不存在，已纠正为上述官方实测命令。

---

## 文章背景

本文是智客随笔发布的 Hermes 入门实操指南，整理了社区流传的"工具包"。文章定位是"新手入门速查"，内容不涉及深度技术，主要价值在于：
1. 提供了中文资源入口（避开了英文文档的语言障碍）
2. 汇总了常用命令的分类速查表

**局限性**：
- 命令内容较浅，未涉及进阶用法（多 Agent/Cron/MCP 等）
- 链接需定期核对官方文档（Web UI 等新功能文章未收录）

---

## Deep Compression Results

### 沉默的维度
作者为什么写这篇而不是更深入的技术分析？因为社区里大量新手"装好了但不知道能干什么"——这个痛点是信息过载时代的典型症状：工具在手，地图缺失。

### 可证伪性
如果 Hermes 的命令体系在后续版本中大幅重构（如全面迁移到 MCP 架构），本文的命令速查表将失效。验证方式：对比官方文档的 Commands Reference。

### 隐藏推论
本文反映了一个更深层的趋势：**AI Agent 的竞争已从"能力"转向"易用性"**。Hermes 社区在大力补齐中文文档和 FAQ，说明降低使用门槛正在成为差异化竞争点。这也意味着：谁的入门体验更好，谁就能获得更多的自然增长。
