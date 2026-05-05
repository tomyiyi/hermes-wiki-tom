---
title: Karpathy LLM Wiki
created: 2026-04-11
updated: 2026-04-11
layer: summary
type: concept
tags: [knowledge-base, wiki, rag-alternative, karpathy, compounding-knowledge]
sources: [raw/articles/karpathy-llm-wiki-personal-knowledge-base.md]
---

# Karpathy LLM Wiki

## 是什么
Andrej Karpathy 提出的个人知识库模式：让 LLM 把每次对话中产生的知识沉淀成 Markdown 文件，下次查询时 AI 先翻已有笔记再推导。

核心理念：**知识要滚雪球，不要每次从零开始。**

## 三层架构
1. **Raw Sources**：原始资料，只读不改
2. **The Wiki**：LLM 生成的知识产物（摘要、概念页、对比页）
3. **The Schema**：规则文件，LLM 和人共管

## 三个核心动作

### Ingest（入库）
新资料 → AI 读 → 写摘要 → 判断位置 → 更新链接 → 追加索引

### Query（查询）
查 Wiki → 综合回答 → 发现新关联 → 反哺写回 Wiki

### Lint（健康检查）
- 孤立页面
- 过时内容（>90天）
- 矛盾检测
- 缺失引用

## 与 [[graphify]] 的关系
同属 Karpathy"知识编译"理论：
- [[graphify]] → 代码领域
- 本概念 → 文档/知识领域

## 扩展：五层架构（内容创作者版）
```
Notes/ → Knowledge/ → Software/ → LifeOS/ → Writing/
输入层   知识层     技能层     行动层     产出层
```

## 关键设计原则
- AI 建议，人确认（不搞全权自治）
- 链接宜少不宜多（只建最强关联）
- 对话本身是知识（存进 Notes/Conversation）

## 详见
- [[knowledge-management-principles]]
