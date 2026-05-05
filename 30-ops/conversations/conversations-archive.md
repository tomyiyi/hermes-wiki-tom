---
title: Conversations Archive
created: 2026-04-11
updated: 2026-04-11
layer: conversations
type: query
tags: [meta, conversations, notes]
sources: []
derived_from: []
---

# Conversations Archive

> Karpathy 五层架构中，`Notes/Conversation/` 层用于存储与 AI 的有价值的对话记录。对话本身即知识。

## 目的
记录 Hermes 对话中产生的有价值的推理、决策、解决方案。对话结束知识随之沉淀，下次同类问题直接查这里。

## 自动沉淀规则

Hermes 对话后自动判断是否值得写入 conversations/，规则：

**触发条件（满足任一即沉淀）：**
1. 产生了实质性的推理、决策或新结论
2. 发现跨文章/跨话题的新关联
3. 解决了非平凡的技术问题
4. 对 Hermes 配置、工作流或 Wiki 结构做了修改
5. 用户明确说"记住这个"

**触发后的动作：**
```bash
python3 /Users/tom/Desktop/hermes-wiki/conversations/save_conversation.py \
  "<话题>" "<洞察1>" "<洞察2>" "<行动结果>"
```

## 最近对话

- [[第一轮文章回顾-graphify-karpathy-llm-wiki-知识管理原则-2026-04-11]] — 2026-04-11: 第一轮文章回顾 — Graphify / Karpathy LLM Wiki / 知识管理原则

## 最近对话

- [[minimax-mmx-cli-全模态工具接入-2026-04-11]] — 2026-04-11: MiniMax MMX-CLI 全模态工具接入 [inferred]

## 收录标准
- 有深度的技术推理（不是简单问答）
- 发现新关联或产生了新结论
- 解决了非平凡的问题
- 对 Hermes 配置或工作流的修改决策

## 不收录
- 简单命令执行
- 一次性查询无后续价值
- 用户私人信息

## 格式
每篇对话存档包含：
- `title`: 对话主题
- `date`: 对话日期
- `certainty`: 确定性标签（见下）
- `participants`: 谁参与了（human / Hermes / 其他）
- `outcome`: 对话产生了什么（决策/代码/知识/行动）
- `key_insights`: 核心结论

### 确定性标签（certainty）
- `confirmed` — 有明确事实/文档支撑，非争议
- `inferred` — 由已知信息合理推断，未直接验证
- `speculative` — 大胆假设，结论不确定，需要后续验证

标签意义：后续查 wiki 时，知道哪些可以直接用，哪些还要再验证。
