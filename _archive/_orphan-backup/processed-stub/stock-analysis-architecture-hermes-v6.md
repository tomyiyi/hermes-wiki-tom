---
title: "股票分析系统架构文档 v6"
created: 2026-04-12
updated: 2026-04-13
layer: processed
type: entity
tags: [stock-analysis, A股, akshare, financial-analysis, system-architecture, python]
source_domain: 本地
source_author: 用户（陈涛）
source_published: 2026-04-12
derived_from: 用户自建
action_id: null
action_outcome: pending
---

# 股票分析系统架构文档 v6

> 版本：v6.0 | 创建：2026-04-12 | 更新：2026-04-13
> 状态：⚠️ 待迁移（当前为 OpenClaw 版，需迁移至 Hermes）

## 系统架构

```
用户输入 → OpenClaw → Skill Layer → Script Layer → Data Layer → Output Layer
```

### Skills（当前 OpenClaw 版）
| Skill | 功能 | 触发词 |
|-------|------|--------|
| stock-analysis | A股全维度盘后分析 v6 | `分析股票 300436` |
| a-stock-market | 实时行情查询 | `600519现在多少钱` |
| eastmoney-stock | 东方财富数据 | `东方财富 300059` |
| stock-recommend | 新闻选股推荐 | `/stock-news-picker A股` |

### Scripts
| 脚本 | 用途 |
|------|------|
| stock-report-v6.py | 数据采集核心 |
| stock-daily-report.py | 每日推送 |
| stock-backtest.py | 回测引擎 |
| stock-sina.py | 新浪实时行情 |

### 数据源
- 新浪财经 API（K线/实时）
- 东方财富 API（资金流向）
- akshare（财务数据）
- Prophet（价格预测）

### v6 分析报告10章节
1. 核心定位与基本盘
2. MyTT技术指标全景
3. 主力资金深度拆解
4. 财务三表诊断
5. Prophet趋势预测
6. 回测验证
7. 次日情景演练
8. 操作建议
9. 风险提示
10. 综合评级

## 待优化项
- [ ] Hermes Two 长任务反馈机制
- [ ] 财务三表完整性
- [ ] 多股票批量分析
- [ ] 每日自动推送功能
- [ ] 迁移至 Hermes Agent

## 关联
- akshare-stock-data skill（数据获取方法，参见 ~/.hermes-home/skills/akshare-stock-data/）
- A股分析流程（待创建）
