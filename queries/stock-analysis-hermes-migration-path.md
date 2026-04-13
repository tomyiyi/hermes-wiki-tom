---
title: "股票分析系统迁移至 Hermes 的最优路径"
created: 2026-04-13
updated: 2026-04-13
layer: query
type: query
tags: [stock-analysis, A股, akshare, hermes, migration]
sources: [concepts/stock-analysis-architecture.md, action/stock-analysis-hermes-migration-20260413.md]
status: open
priority: medium
owner: human
---

# 股票分析系统迁移至 Hermes 的最优路径

## 背景

用户明确推迟了 stock 相关迁移（"stock 相关先不做"），但这个问题需要长期规划。

## 具体问题

### Q1: 迁移的前提条件
- Hermes 的 Skills 系统是否支持 OpenClaw 的 stock-report-v6.py 全部功能？
- akshare 数据源在 Hermes 环境是否有同样的连接问题（被 block）？
- Yahoo Finance 替代方案能否无缝接入？

### Q2: 迁移的性价比
- 当前 OpenClaw 版本运行稳定，是否值得迁移？
- 迁移后哪些能力会变强？
- 预计迁移工作量多大？

### Q3: v7 规划
- 用户提到"股票分析系统 v6"，v7 的规划方向是什么？
- v7 是否会改变数据源架构？

## 用户明确指令
**暂时不做迁移，保持 OpenClaw 运行。**

## 相关
- [[concepts/stock-analysis-architecture]] — 系统架构详情
- [[action/stock-analysis-hermes-migration-20260413]] — 迁移行动记录
- [[backlog/processed-incremental-refresh]] — processed 层增量刷新待办
