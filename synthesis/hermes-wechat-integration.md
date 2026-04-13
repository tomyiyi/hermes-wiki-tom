---
title: Hermes 全平台接入方案
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: concept
tags: [Hermes, wechat, feishu, telegram, discord, platform-integration, multimodal]
sources:
  - processed/hermes-agent.md
  - processed/minimax-mmx-cli.md
derived_from:
  - Hermes Agent 评测笔记
  - MiniMax MMX-CLI 评测笔记
---

# Hermes 全平台接入方案

> Hermes 通过单一 Gateway 接入 15+ 消息平台，飞书是功能最完整的平台之一。

## 平台接入矩阵

| 平台 | 支持情况 | 功能完整度 |
|------|---------|-----------|
| 飞书 | ✅ 功能最完整 | ★★★★★ |
| Telegram | ✅ | ★★★★ |
| Discord | ✅ | ★★★★ |
| Slack | ✅ | ★★★ |
| WhatsApp | ✅ | ★★★ |
| Signal | ✅ | ★★★ |
| Email | ✅ | ★★ |
| 微信 | ⚠️ 社区方案 | ★★ |

## 飞书接入（重点）

当前 Hermes 运行在飞书私信通道，功能已验证：
- WebSocket 连接正常
- 消息路由正常
- Vision 自动识别 MiniMax CN

**飞书特有优势**：
- 文档处理能力强
- 机器人支持富媒体
- 适合定时推送（盘后分析）

## MiniMax MMX-CLI 扩展

MMX-CLI 为 Hermes 提供全模态能力，已集成 vision：

| 模态 | 命令 | 状态 |
|------|------|------|
| 图像理解 | `mmx vision describe` | ✅ 已集成 |
| 语音合成 | `mmx tts` | 待测 |
| 音乐创作 | `mmx music` | 待测 |
| 视频生成 | `mmx video` | 待测 |
| 图片生成 | `mmx image generate` | 待测 |
| 信息搜索 | `mmx search` | 待测 |

**Token Plan 接入**：MMX-CLI 无缝接入 MiniMax Token Plan，Agent 调用走用户已有配额，无额外费用。

## Agent 专用设计原则（MMX-CLI）

| 问题 | 解决方案 |
|------|---------|
| 输出混进度条 | stdout 纯数据，stderr 放人类信息 |
| 错误只能读英文 | 语义化 Exit Code（各有独立代号）|
| 参数缺失挂起 | 直接报错退出，不傻等 |
| 长任务阻塞 | `--async` 异步模式 |

## 微信接入现状

微信官方不支持个人机器人，社区方案稳定性有限。
如需微信接入，建议通过**企业微信**或**微信公众号**官方 API，稳定性更高。

## 相关

- [[minimax-mmx-cli]] — MMX-CLI 详情
- [[hermes-agent-core-concepts]] — Hermes 核心概念
