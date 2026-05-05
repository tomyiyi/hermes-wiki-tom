---
title: "股票系统迁移路径"
created: 2026-04-13
updated: 2026-04-13
layer: queries
type: query
tags: [stock-analysis, hermes, migration, pending]
summary_only: false
archived: false
---

# 股票系统迁移路径（暂停）

## 当前状态

**用户指令：先不做 stock 相关，等进一步通知。**

## 原计划（记录待用）

### stock-analysis v6 迁移要素

1. **数据源层**
   - AkShare eastmoney API（当前 AS4134 NAT IP 被 block，代理全 502）
   - 替代方案：Yahoo Finance 直连（`600519.SS`、`000001.SZ`、`^HSI`）
   - hermes venv Python 直连 Yahoo Finance 正常

2. **Hermes 集成**
   - 复用 hermes-wiki 的知识管理框架
   - 盘后分析优先，需要数据全面性而非实时性
   - A股金融专家是长期主轴

3. **现有资产**
   - `stock-analysis/` 目录已有初始化结构
   - `hermes-experiments/` 已建仓 GitHub 仓库
   - AkShare 已安装在 hermes venv

### 迁移前提
- [ ] 等用户确认恢复时间
- [ ] 验证 Yahoo Finance 数据完整性（财务数据、公告）
- [ ] 确认 hermes-wiki 的 Query 机制稳定后对接 stock queries

## 关联文档

- [[raw/articles/股票分析系统架构文档-318982]]

## 相关 Queries
- [[queries/hermes-wiki-compounding-knowledge]] — Wiki 知识管理是股票分析以外的基础设施
- [[queries/wechat-article-ingest-automation]] — 微信文章摄取是金融知识入口
