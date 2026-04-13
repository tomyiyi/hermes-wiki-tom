---
title: 股票分析系统架构
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: entity
tags: [stock-analysis, A股, akshare, 量化交易, MyTT, Prophet, 财务分析, system-architecture]
sources:
  - processed/stock-analysis-architecture-hermes-v6.md
  - action/stock-analysis-hermes-migration-20260413.md
derived_from:
  - 股票分析系统架构文档 v6
  - stock-analysis 迁移至 Hermes
---

# 股票分析系统架构

> 用户自建的 A股全维度盘后分析系统，v6 版本完整，当前运行于 OpenClaw，待迁移至 Hermes。

## 系统架构

```
用户输入：「分析股票 300436」
        ↓
    OpenClaw / Hermes
        ↓
┌─────────────────────────────────┐
│  Skill Layer（调度层）           │
│  stock-analysis（v6分析）       │
│  a-stock-market（实时行情）      │
│  eastmoney-stock（东方财富）     │
│  stock-recommend（选股推荐）     │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│  Script Layer（执行层）          │
│  stock-report-v6.py（核心）     │
│  stock-daily-report.py（推送）  │
│  stock-backtest.py（回测）      │
│  stock-sina.py（新浪实时）      │
└─────────────────────────────────┘
        ↓
┌─────────────────────────────────┐
│  Data Layer（数据层）            │
│  新浪财经 API（K线/实时）        │
│  东方财富 API（资金流向）        │
│  akshare（财务数据）             │
│  Prophet（价格预测）             │
└─────────────────────────────────┘
```

## v6 报告10章节

| 章节 | 内容 |
|------|------|
| 1. 核心定位与基本盘 | 股票定位、行业、估值 |
| 2. MyTT技术指标全景 | MACD/KDJ/RSI/布林带等 |
| 3. 主力资金深度拆解 | 资金流向、主力动向 |
| 4. 财务三表诊断 | 资产负债表、利润表、现金流量表 |
| 5. Prophet趋势预测 | 时间序列预测 |
| 6. 回测验证 | 策略回测收益 |
| 7. 次日情景演练 | 涨/跌/平情景推演 |
| 8. 操作建议 | 具体买卖点建议 |
| 9. 风险提示 | 风险等级与黑天鹅预警 |
| 10. 综合评级 | 机构评级+综合评分 |

## 数据源

| 数据源 | 用途 | 状态 |
|--------|------|------|
| 新浪财经 API | K线、实时行情 | ✅ 可用 |
| 东方财富 API | 资金流向 | ⚠️ 曾被 block |
| akshare | 财务数据、龙虎榜 | ⚠️ eastmoney 部分失效，可用 Yahoo Finance 替代 |
| Prophet | 价格预测 | ✅ |

## 当前状态

- **运行环境**：OpenClaw
- **迁移目标**：Hermes Agent
- **迁移优先级**：高（用户明确方向）

## 待迁移任务

- [ ] 将 stock-report-v6.py 封装为 Hermes Skill
- [ ] 配置 Hermes Cron：收盘后 15:30 自动分析
- [ ] 适配 Hermes Feishu 集成（推送）
- [ ] 验证 akshare 数据源连通性
- [ ] 测试 Gemini/港股/指数分析

## 相关

- [[action/stock-analysis-hermes-migration-20260413]] — 迁移行动计划
- [[akshare-stock-data]] — akshare 数据获取 skill
