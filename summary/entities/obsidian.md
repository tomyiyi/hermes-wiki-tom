---
title: Obsidian
created: 2026-04-11
updated: 2026-04-11
layer: summary
type: entity
tags: [tools, obsidian, notes, knowledge-base, vault]
sources: [raw/articles/karpathy-obsidian-claudian-tutorial.md]
---

# Obsidian

## 是什么
本地笔记软件，以 Markdown 文件为基础，支持双向链接、图形化知识图谱视图。

## 关键特性
- Wikilinks 双向链接语法
- Graph View 可视化知识网络
- YAML frontmatter 支持 Dataview 查询
- 附件文件夹存放图片

## 与 Hermes Wiki 的关系
Hermes 的 `llm-wiki` skill 输出的目录可直接作为 Obsidian vault 使用：
- Obsidian 打开 `/Users/tom/Desktop/hermes-wiki` 即可
- 自动识别 wikilinks、frontmatter、附件

## 相关插件
- **Claudian**：将 Claude Code 接入 Obsidian（需 Claude Code CLI，Hermes 用户不适用）
- **Dataview**：查询笔记数据库
- **BRAT**：安装第三方插件

## 5 个必备 Skill（Obsidian CEO 亲做）
由 Obsidian CEO 制作的最佳实践 Skill：
安装：https://github.com/kepano/obsidian-skills

## 使用场景
- 知识沉淀（配合 [[karpathy-llm-wiki]]）
- 项目文档
- 任务管理

## 相关概念
- [[knowledge-management-principles]]（待确认是否存在）
