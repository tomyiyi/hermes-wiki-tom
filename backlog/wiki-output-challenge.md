---
title: "[challenge] wiki-output-challenge — 用 wiki 知识回答真实问题"
created: 2026-04-11
updated: 2026-04-11
layer: backlog
type: action
status: pending
priority: high
owner: human
execution_target: "when-needed"
tags: [backlog, wiki-value, validation]
sources: [summary/concepts/knowledge-management-principles.md]
---

# [Backlog] wiki-output-challenge

## 做什么
当用户提出真实问题时，Hermes 先查 wiki，再用 wiki 知识回答，最后记录回答质量。

## 什么时候做
用户提出问题时（非简单命令），自动触发

## 执行条件（满足任一）
1. 用户问了一个开放性问题（why / how / what is / compare）
2. 用户提到的话题在 wiki 中有相关页面
3. 用户说"你知道吗..."

## 怎么做
1. 查 wiki 相关页面（grep 或人工定位）
2. 用 wiki 知识组合回答
3. 在当前对话末尾追加：
```
## Wiki 知识支撑

- 来源页面：[[pagename]]
- 确定性：confirmed / inferred / speculative
- 回答覆盖率：完整 / 部分 / 无直接支撑
```
4. 标记本次回答的正向/负向反馈

## 反馈要求
每次执行后记录：
- wiki 是否有直接支撑（yes / partial / no）
- 用户是否有后续追问（判断回答质量）
- 是否有新的知识沉淀到 wiki

## 备注
这个需要你配合——当你问问题或讨论话题时，我说"正在用 wiki 回答"，你告诉我回答得怎么样（有用/不对/不够）
