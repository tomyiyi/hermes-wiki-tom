---
title: "Skills 自动进化的实际效果验证"
created: 2026-04-13
updated: 2026-04-13
layer: query
type: query
tags: [AI-Agent, hermes, skills, self-evolution]
sources: [概念/skills-auto-evolution.md]
status: open
priority: high
owner: hermes
---

# Skills 自动进化的实际效果验证

## 核心问题

Skills 自动进化机制的理论框架已建立，但**实际运行效果尚未验证**。

## 具体验证问题

### Q1: 轨迹记录是否完整？
- 什么触发一次"轨迹记录"写入？
- 轨迹数据存在哪里？格式是什么？
- 如何区分成功轨迹和失败轨迹？

### Q2: 经验沉淀的触发条件是否合理？
- 文档说"调用 3+ 工具，经历 2+ 步骤"触发
- 这个阈值是配置项还是硬编码？
- 用户能否自定义触发阈值？

### Q3: Skill 生成质量如何？
- 自动生成的 Skill 与人工编写的差距有多大？
- 有没有出现过生成错误/误导性的 Skill？
- 如何回滚/删除错误的自动生成 Skill？

### Q4: 进化闭环是否真正闭合？
- Skill 更新后，下次调用是否真的用了新版本？
- 版本控制机制是什么？
- 多个 Skills 之间的调用顺序如何确定？

## 验证方法

1. **看**：检查 hermes 代码中 trajectory 写入逻辑
2. **试**：执行一个 3+ 工具调用任务，看是否生成新 Skill
3. **查**：检查 `~/.hermes/skills/` 是否有 auto-generated 内容

## 相关
- [[概念/skills-auto-evolution]] — Skills 三层模型和进化闭环理论
- [[stock-analysis-architecture]] — 待迁移股票系统，其中涉及 Skills 设计
