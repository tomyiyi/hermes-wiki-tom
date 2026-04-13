---
title: "Hermes Agent 深度解析"
created: 2026-04-11
updated: 2026-04-13
layer: raw
type: article
tags: ['AI-Agent', 'hermes', ' Nous Research']
source_url: ""
source_domain: ""
archived: false
---


# Hermes Agent 深度解析

## 概述

Hermes Agent 由 **Nous Research** 团队开发，名字来源于古希腊神话中的神祇 Hermes，以及古希腊语中"直接感知真理、理性以及神圣现实的能力"—— Nous。

> 核心理念：不是更聪明的聊天框，而是一套部署在服务器上、持续运转、会从执行经验里自动沉淀能力的**自主智能体框架**。

## 快速成绩单

| 指标 | 数据 |
|------|------|
| OpenRouter 全球排名 | 第二（每日） |
| 编程 Agent/CLI Agent 排名 | 第一 |
| 过去一个月调用量 | 超过 1.6 万亿 Token |
| GitHub 星标 | 近 6 万（两个月达成） |
| 达到 4 万星速度 | 45 天（OpenClaw 用 61 天） |
| 版本迭代 | V0.8.0（高频更新） |

## 三层记忆系统

### 第一层：会话记忆
- 每轮对话内容、工具调用、返回结果全部记录
- 按需检索：FTS5 全文索引，上下文占用恒定

### 第二层：持久记忆
- 存储编码偏好、项目习惯、常用工具链
- 跨会话保持，不丢失

### 第三层：Skill 记忆
- 方法论和操作规范存在 ~/.hermes/skills/ 的 markdown 文件
- 从经验中自主创建，可读可编辑

## 闭合学习循环

策划记忆 → 自主创建 Skill → Skill 自改进，越用越精准。

## 核心定位

唯一解决的核心问题：让 Agent 不再是用完归零的一次性工具，而是一个能从失败里学到东西、能把经验沉淀成能力、会随着使用时间变得越来越懂你的长期搭档。