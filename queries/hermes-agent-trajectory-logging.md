---
title: "Learning Loop与四层记忆的协同机制"
created: 2026-04-13
updated: 2026-04-13
layer: queries
type: query
tags: [hermes, memory, learning-loop, trajectory, agent, four-layer-memory]
summary_only: false
archived: false
---

# Learning Loop与四层记忆的协同机制

## 核心问题

Learning Loop 产生的 Skills 和四层记忆系统如何协同？轨迹日志的记录路径是什么？

## 四层记忆架构（已验证）

### 第一层：常驻提示记忆
- 文件：`MEMORY.md` + `USER.md`
- 作用：每次会话开始自动加载的上下文
- 容量上限：3575 字符（故意收窄，强迫筛选）
- 原则：只放每次对话都必须出现的内容

### 第二层：会话归档
- 存储：SQLite 数据库，全文索引检索
- 机制：需要历史上下文时，主动查询 → LLM 摘要 → 只注入相关部分
- 原则：只在特定话题出现时有用

### 第三层：技能文件（Learning Loop 产出）
- 存储：`~/.hermes/skills/`
- 特点：默认只加载名称和描述，全文按需调入
- 扩展性：从 40 个增长到 200 个，上下文成本几乎不变
- 这是 Learning Loop 的直接产物

### 第四层：Honcho（用户建模层）
- 作用：跨会话积累用户偏好、沟通风格、领域知识
- 适合：把 Hermes 当日常个人助理长期使用
- 原则：用户长期画像

## Learning Loop × 四层记忆的协同流程

```
任务执行 → 触发条件满足 → Skill 生成 → 写入第三层
                              ↓
Periodic Nudge → 回顾最近操作 → 判断值得记忆的内容 → 写入对应层
```

## 关键洞察

1. **各层职责清晰**：不是把所有东西放第一层，而是按使用频率和范围分层
2. **上下文成本可控**：第三层按需加载，避免上下文膨胀
3. **Periodic Nudge 是粘合剂**：在没有用户输入时主动整理，防止记忆流失

## 待验证

- [ ] Periodic Nudge 实际多久触发一次？
- [ ] 多层记忆之间有没有冲突或冗余？
- [ ] Honcho 层的偏好积累速度是否够用？

## 关联文章

- [[raw/articles/hermes-agent-wechat-20260411]]
- [[raw/articles/simin-hermes-architecture-business-model]]

## 相关 Queries
- [[queries/hermes-skills-auto-evolution-verification]] — Skills 是 Learning Loop 的直接产物
- [[queries/hermes-wiki-compounding-knowledge]] — 四层记忆协同决定复利效应质量
