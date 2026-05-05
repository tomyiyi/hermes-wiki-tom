---
title: "mmx-cli 接入 Hermes 全模态工具"
created: 2026-04-11
updated: 2026-04-11
layer: action
type: summary
tags: [hermes, minimax, mmx-cli, integration, multimodal]
sources: [raw/articles/minimax-mmx-cli-20260411.md, processed/minimax-mmx-cli.md, summary/concepts/minimax-mmx-cli.md]
derived_from: []
action_id: mmx-cli-hermes-integration-20260411
action_outcome: pending
---

# Action: mmx-cli 接入 Hermes 全模态工具

## 背景
MMX-CLI 发布，MiniMax 全模态能力（图像/视频/语音/音乐）可以用命令行调用。Hermes 已有 minimax-cn provider，vision 已走 mmx vision describe，可扩展接入更多模态。

## 待落地项

### 高优先级
1. **Hermes 工具错误码标准化** — 当前工具调用失败时 Hermes 如何判断是否重试？是否需要语义化 Exit Code？
2. **mmx vision describe 已集成**（确认现状）— 检查 vision_tools.py 里的 mmx CLI 检测逻辑是否完整

### 中优先级
3. **mmx tts 接入 Hermes** — 利用 text_to_speech 工具走 mmx tts
4. **mmx music 生成 BGM** — 娱乐向，探索用 mmx music 创作 wiki BGM

### 低优先级
5. **--async 异步模式借鉴** — Hermes cron 任务的异步化

## 执行检查清单
- [ ] 确认 vision_tools.py 里 mmx vision describe 路径完整
- [ ] 检查 Hermes 工具调用错误处理逻辑
- [ ] 测试 mmx tts 是否可用
- [ ] 测试 mmx music 是否可用
