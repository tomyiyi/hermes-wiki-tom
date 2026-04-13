---
title: "Wiki知识复利效应的量化验证"
created: 2026-04-13
updated: 2026-04-13
layer: queries
type: query
tags: [hermes-wiki, knowledge-management, compounding, metrics, knowledge-base]
summary_only: false
archived: false
---

# Wiki知识复利效应的量化验证

## 核心问题

Hermes Wiki 的知识复利效应如何量化？随着页面数量增长，跨文章洞察的质量是否提升？

## 复利机制

### 信息层级的复利
```
raw/articles/  →  processed/  →  synthesis/  →  action/
  (原始摄取)       (提炼加工)      (跨文综合)      (执行落地)
```

每上一层，抽象程度提高，但信息损耗存在。

### Wiki Link 网络效应
- inbound links 越多，页面"被发现"的概率越高
- 同一主题的页面互相引用 → 形成知识簇
- 知识簇之间的跨界连接 → 产生新洞察

## 可量化指标

### 数量指标
| 指标 | 当前值 | 目标 |
|------|--------|------|
| 总页面数 | 44 | 100+ |
| queries/ 页数 | 5 | 20+ |
| inbound links 覆盖率 | ~30% | >60% |
| 无 orphan 页面比例 | ~0% | >80% |

### 质量指标
- **观点密度**：每篇 summary 页的"独立观点"数量
- **跨文章引用率**：同一 synthesis 页引用多少篇 raw 文章
- **行动转化率**：queries → action 的转化比例
- **复盘频率**：Skills 自我迭代的实际频率

## 当前缺口

1. **Inbound links 覆盖率低**：46个孤儿页，大多是 action/backlog/conversations 目录页
2. **Queries 页质量参差**：部分只有框架无实质内容
3. **无量化看板**：没有 Dashboard 展示复利效应进展

## 迭代方案

### 短期（本周）
- [ ] 完善5个 queries 页的"待验证假设"清单
- [ ] 给每个 queries 页补充关联文章的 actual links

### 中期（本月）
- [ ] 建立 Wiki Dashboard（Obsidian Dashboard 插件）
- [ ] 追踪 inbound links 覆盖率变化
- [ ] 建立"每周摄取报告"自动化

### 长期
- [ ] 复利效应可视化：随时间推移，跨文章洞察占比增长曲线
- [ ] 评估知识管理 ROI：投入时间 vs 解决实际问题数量

## 关联文章

- [[raw/articles/simin-hermes-architecture-business-model]]
- [[raw/articles/Alan-hsu-hermes-advanced-play-review]]

## 相关 Queries
- [[queries/hermes-agent-trajectory-logging]] — 记忆协同机制是复利的基础设施
- [[queries/hermes-skills-auto-evolution-verification]] — Skills 进化率是复利的加速因子
