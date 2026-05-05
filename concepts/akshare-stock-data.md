---
title: akshare-stock-data
created: 2026-04-13
updated: 2026-04-13
layer: summary
type: entity
tags: [akshare, stock-data, A股, financial-data, python, data-source]
sources: [~/.hermes-home/skills/akshare-stock-data/SKILL.md]
---

# akshare-stock-data

> Hermes Skill：通过 akshare 获取中国A股、港股、美股的历史K线、财务数据、龙虎榜、基金数据，用于盘后分析。

## 用途

获取股票原始数据，供给 stock-analysis 系统做分析。

## 数据覆盖

| 类型 | 来源 | 状态 |
|------|------|------|
| A股历史K线 | 新浪/东方财富 | ⚠️ eastmoney 部分被 block |
| 港股K线 | Yahoo Finance | ✅ 可用 |
| 美股K线 | Yahoo Finance | ✅ 可用 |
| 财务数据 | akshare | ✅ |
| 龙虎榜 | akshare | ✅ |
| 基金数据 | akshare | ✅ |

## 已知限制

- **eastmoney/eastmoney API**：AS4134 NAT IP 被 block，代理也全 502
- **替代方案**：Yahoo Finance 直连（`600519.SS` A股、`000001.SZ` 港股、`^HSI` 恒生指数）
- hermes venv Python 直连 Yahoo Finance 正常

## 相关

- [[concepts/stock-analysis-architecture]] — 股票分析系统 v10
