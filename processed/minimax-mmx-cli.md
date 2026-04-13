---
title: MiniMax MMX-CLI 评测笔记
created: 2026-04-11
updated: 2026-04-11
layer: processed
type: entity
tags: [minimax, mmx-cli, agent, cli, multimodal, tool]
sources: [raw/articles/minimax-mmx-cli-20260411.md]
derived_from: []
---

# MiniMax MMX-CLI 评测笔记

> 原文：《MiniMax 发布 MMX-CLI：为 Agent 设计的全模态命令行工具》| MiniMax 官方

## 核心要点

### 是什么
MMX-CLI = MiniMax 命令行工具，面向 AI Agent，让 Agent 可以在 Claude Code / OpenClaw 等环境中原生调用全模态模型。

### 支持的模态
- `mmx image generate` — 图片生成
- `mmx video generate` — 视频生成
- `mmx tts` — 语音合成
- `mmx music generate` — 音乐创作
- `mmx vision describe` — 图像理解
- `mmx search` — 信息搜索

### Agent 专用设计
| 问题 | 解决方案 |
|------|---------|
| 输出混进度条/颜色字符 | stdout 纯数据，stderr 放人类友好信息 |
| 错误只能读英文 | 语义化 Exit Code（鉴权失败/超时/参数错误各有独立代号）|
| 参数不全时挂起等待 | 参数缺失直接报错退出，不傻等 |
| 长任务阻塞 | `--async` 异步模式，一键后台 |

### 安装
```bash
npx skills add MiniMax-AI/cli -y -g
npm install -g mmx-cli
```

### Token Plan 接入
MMX-CLI 无缝接入 MiniMax Token Plan，Agent 调用走用户已有配额，无额外费用。

## 与 Hermes 的关系
- Hermes 已有 `minimax-cn` provider，vision 已走 mmx CLI
- MMX-CLI 可以扩展：mmx music / mmx tts / mmx video
- `mmx vision describe` 已集成在 Hermes vision_tools.py（minimax-cn provider 专用）
