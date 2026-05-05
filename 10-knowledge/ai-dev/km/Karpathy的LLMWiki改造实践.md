---
title: Karpathy的LLMWiki改造实践
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# Karpathy 的 LLM Wiki 火了，我改造了一下，比原版更好用

## 核心痛点
别让 AI 每次都从零开始帮你想，让它帮你把知识攒起来。换 session 问 AI，上下文容易丢。

## 三个核心动作
1. **Ingest（入库）**: 新资料进来，AI 读一遍，写摘要，判断放哪，更新链接。
2. **Query（查询）**: 问 AI 问题，它在 Wiki 里搜内容综合回答，并反哺发现的新关联。
3. **Lint（健康检查）**: 定期扫一遍，找孤立页面、过时内容、矛盾概念。

## 范凯的五层架构实践
- Notes/（输入层）：统一入口（网页剪藏、想法、AI 对话）
- Knowledge/（知识层）：方法论、读书笔记
- Software/（技能层）：工具技巧
- LifeOS/（行动层）：投资、健康
- Writing/（产出层）：输出内容

## 人机协作原则
- AI 列出分发方案，人类确认后再动手。
- 只建最强关联，不追求覆盖率。
