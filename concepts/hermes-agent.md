---
title: Hermes Agent 评测总结
created: 2026-04-11
updated: 2026-04-11
layer: summary
type: concept
tags: [hermes, nous-research, openclaw, agent, memory, learning-loop]
sources: [raw/articles/hermes-agent-wechat-20260411.md, processed/hermes-agent.md]
derived_from: []
---

# Hermes Agent 评测总结

## 一句话总结
> Hermes Agent 是一个能从使用中"越用越懂你"的单一 Agent 框架，通过内置 Learning Loop 和四层记忆系统，解决了 OpenClaw"用完归零"的根本缺陷。

## 核心判断
Hermes 最大的创新不是某个功能，而是**把"越用越进化"做进了底层架构**：
- OpenClaw：记忆是静态配置文件 → 每次从零读取 → 不会自我进化
- Hermes：记忆是动态学习循环 → 每次执行后自检 → 发现有效路径自动写 Skill → Periodic Nudge 定期主动整理

## 关键机制

### Learning Loop
任务完成 → 自检是否值得记录 → 生成/更新 Skill 文件（patch 方式，非覆写）
Skill 遵循 agentskills.io 开放标准，可跨 Agent（OpenClaw / Claude Code / Cursor）复用

### 四层记忆
```
第一层 常驻提示（MEMORY.md + USER.md） → 每次会话必加载，3575 字符上限
第二层 会话归档（SQLite） → 按需查询 + LLM 摘要注入
第三层 技能文件 → 按需加载，库从 40 增到 200 上下文成本几乎不变
第四层 Honcho → 跨会话用户画像
```

### Auxiliary Models
多模型编排做在底层：图像/网页提取/Skill匹配/记忆 → 自动切 Gemini Flash，主模型只处理对话。

## 与 Hermes 本 Workspace 的关系
- Hermes（这个 AI）≠ Hermes Agent（Nous Research 的开源项目）
- Hermes Wiki 用的是 Hermes（workspace） + Obsidian 的知识管理思路
- Hermes Agent 的 Learning Loop 思路值得借鉴：可以给 Hermes Wiki 增加"对话沉淀"自动写入 conversations/ 的机制

## 开放问题
- Hermes Agent 的 Patch 写入和 agentskills.io 标准，能否直接被 Hermes（这个工具）调用？
- 小米 MiMo + Hermes Agent 的合作模式是否可复制到其他国产模型？
