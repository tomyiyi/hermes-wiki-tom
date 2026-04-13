---
title: "stock-analysis 迁移至 Hermes"
created: 2026-04-13
updated: 2026-04-13
layer: action
type: action
tags: [stock-analysis, hermes, A股, migration, python]
sources: [processed/stock-analysis-architecture-hermes-v6.md]
action_id: stock-analysis-hermes-migrate-20260413
action_outcome: pending
action_summary: "将现有 OpenClaw 版 stock-analysis 系统迁移至 Hermes Agent，适配 Skills + cron 架构"
---

# stock-analysis 迁移至 Hermes

## 背景
当前 stock-analysis 系统运行在 OpenClaw 上，v6 架构完整，10章节报告体系成熟。需要迁移至 Hermes 以利用：
- Hermes Skills 自动进化（股票分析经验可持续沉淀）
- Hermes 四层记忆（避免每次对话丢失分析上下文）
- Hermes Cron 定时任务（盘后自动分析+推送）
- Hermes 数据飞轮（分析轨迹反哺模型）

## 待执行任务

- [ ] 调研 Hermes Agent Skills 格式（agentskills.io 标准）
- [ ] 将 stock-report-v6.py 封装为 Hermes Tool/Skill
- [ ] 设计 stock-analysis Hermes Skill（触发词、数据流程、输出格式）
- [ ] 配置 Hermes Cron：收盘后 15:30 自动运行分析
- [ ] 迁移飞书文档写入到 Hermes Feishu 集成
- [ ] 配置 akshare 数据源（中国A股，需验证网络连通性）
- [ ] 测试 Gemini/港股/指数分析功能
- [ ] 验证 v6 报告10章节在 Hermes 下的完整输出

## 预期收益对比

| | 当前 OpenClaw 版 | 迁移后 Hermes 版 |
|--|----------------|----------------|
| 记忆 | 无跨会话积累 | 四层记忆+心智建模 |
| 技能进化 | 手动维护 | 自动沉淀分析经验 |
| 定时任务 | 需外部 cron | 内置 Cron |
| 多平台 | 依赖 OpenClaw | 15+ 平台 |
| 成本 | OpenClaw 托管费 | < $1/月（Serverless）|

## 风险提示
- akshare eastmoney API 此前有被 block 记录（AS4134 NAT IP），Yahoo Finance 可作为替代
- Hermes盘后分析优先，需要数据全面性而非实时性
