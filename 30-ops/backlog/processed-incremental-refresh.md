---
title: "[processed] processed 层增量刷新机制"
created: 2026-04-11
updated: 2026-04-11
layer: backlog
type: action
status: pending
priority: medium
owner: hermes
execution_target: "2026-04-13"
tags: [backlog, processed, ingest, workflow]
sources: [summary/concepts/graphify.md]
---

# [Backlog] processed 层增量刷新

## 做什么
设计并实现 processed 层的增量刷新逻辑：
- 新文章 ingest 时，processed 层已有页面不覆盖，只标记变更
- 用 diff 思想：新增内容追加，已存在内容比较后选择性更新

## 什么时候做
2026-04-13

## 怎么做
在 `scripts/` 下新建 `processed_refresh.py`：
```
输入：新 article 的 processed 草稿（raw article → 划重点）
输入：已存在的 processed 页面
处理：
  1. 比较新旧 processed 的核心要点列表
  2. 新要点追加，已存在要点保留
  3. 在 updated 字段记录刷新时间和原因
输出：合并后的 processed 页面
```

## 反馈要求
完成后在当前文件记录：
- 增量刷新实际运行了多少次
- 合并质量如何（是否有重复/冲突）
- token 消耗对比（全量重写 vs 增量）

## 备注
低优先级——当前 processed 层规模小，全量重写成本低。先跑通再优化。
