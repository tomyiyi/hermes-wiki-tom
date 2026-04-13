---
title: Obsidian Tutorial — Processed Notes
created: 2026-04-11
updated: 2026-04-11
layer: processed
type: concept
tags: [tools, obsidian, notes, knowledge-base, vault]
sources: [raw/articles/karpathy-obsidian-claudian-tutorial.md]
derived_from: []
---

# Obsidian Tutorial Processed Notes

## 划重点

### 工具链
- **Obsidian** → 笔记软件，本地 Markdown
- **Claude Code** → AI 编码助手
- **Claudian** → Obsidian 插件，接入 Claude Code 图形界面

→ Claudian 是可选的，Hermes 用户不一定需要

### 安装关键点
1. Obsidian → 官网下载
2. Claude Code → 网上教程多
3. Claudian → BRAT 插件安装，URL：`https://github.com/YishenTu/claudian`
4. 5 个必备 Skill → `https://github.com/kepano/obsidian-skills`（Obsidian CEO 制作）

### Workflow
1. Obsidian 新建 vault
2. 把 Karpathy 方法论文档发给 AI
3. AI 自动创建文件夹结构和文件
4. 人确认方案

→ **AI 负责结构，人负责确认**，不搞全权自治

### 关键插件
- **Claudian**：Claude Code ↔ Obsidian 图形界面（不是所有人需要）
- **BRAT**：安装第三方插件
- **Dataview**：查询笔记数据库
- **5 Skills（CEO 亲做）**：最佳实践

## 对 Hermes Wiki 的意义
- Hermes wiki 输出的目录 = Obsidian vault
- 直接用 Obsidian 打开 `/Users/tom/Desktop/hermes-wiki` 即可
- 不需要 Claudian，因为 Hermes 本身已经是 AI 交互界面

## 局限性
- Claudian 要求 Claude Code CLI（Hermes 用户不适用）
- 5 Skills 安装链接需要 Claude Code 执行
- 教程内容较浅，缺少实际使用案例
