---
title: Hermes 工作流升级 — conversations 沉淀 + MEMORY 上限
created: 2026-04-11
updated: 2026-04-11
layer: action
type: summary
tags: [hermes, workflow, conversations, memory, learning-loop]
sources: [raw/articles/hermes-agent-wechat-20260411.md, processed/hermes-agent.md, summary/concepts/hermes-agent.md]
derived_from: [hermes-agent]
action_id: workflow-upgrade-20260411
action_outcome: success
---

# Action: Hermes 工作流升级

## 背景
读了 Hermes Agent 评测文章后，决定把"越用越懂你"的思路落地到 Hermes workspace。

## 做了什么

### Step 1: conversations/ 自动沉淀机制 ✓
- 新增 `conversations/save_conversation.py`
- 规则：有价值对话 → 自动判断是否值得沉淀 → 写入 conversations/
- 触发条件：实质性推理/新关联/解决技术问题/配置修改/用户说"记住"
- 同步更新 `conversations-archive.md`，加入"自动沉淀规则"说明

### Step 2: MEMORY.md 3000 字符软上限 ✓
- 新增文件头注释说明上限（参考 Hermes Agent 3575 字符设计）
- 现有内容 2042 字符，在限制内

### Step 3: agentskills.io 兼容格式 ✓
- 新增 `action/hermes-workflow-upgrade-20260411.md`
- frontmatter 遵循 agentskills.io 结构：action_id / outcome / summary / sources

### Step 4: Periodic Nudge cron 方案
- 方案已定：每周自动检查 wiki 哪些页面过时、哪些可以合并
- 待落地：需要 cron job 配合

## agentskills.io 格式参考
```yaml
action_id: unique-id          # 唯一标识，格式: [action]-[date]
action_outcome: success|failure|partial
sources: [相关来源页面]       # 引用上游 wiki 页面
derived_from: [父 action]     # 溯源
```

## 待落地
- Step 4: 周期性 wiki 整理 cron job（建议每周日凌晨触发）
