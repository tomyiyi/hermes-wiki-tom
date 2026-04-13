---
title: 知识管理方法论
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: concept
tags: [knowledge-management, wiki, rag, graphify, karpathy, llm, compounding-knowledge]
sources:
  - processed/karpathy-llm-wiki.md
  - processed/graphify.md
derived_from:
  - Karpathy LLM Wiki Processed Notes
  - Graphify Processed Notes
---

# 知识管理方法论

> Wiki vs RAG vs Graphify：三条知识管理路线的本质对比。

## 核心问题

**别让 AI 每次从零开始，让知识滚雪球。**

| 方案 | 积累性 | Token消耗 | 适用场景 |
|------|--------|---------|---------|
| RAG | 无积累，每次从零检索 | 高 | 一次性查询 |
| Wiki | 有积累，复利效应 | 低 | 长期知识体系 |
| Graphify | 部分积累（代码结构）| 极低 | 代码理解 |

## RAG vs Wiki 本质差异

| | RAG | Wiki（Karpathy）|
|--|-----|----------------|
| 检索方式 | 向量相似度 | 链接导航 |
| 积累 | 无 | 有（知识复利）|
| Token 效率 | 每次全量 | 编译后极低 |
| 维护成本 | 低（自动）| 高（需人工）|

## Karpathy LLM Wiki 架构

**三层（技术版）**：
```
Raw Sources → The Wiki → The Schema
（存档）     （LLM编译）  （规则）
```

**五层（内容创作者版）**：
```
Notes/（输入）
  ├── Clippings/   网页剪藏
  ├── Inbox/       碎片想法
  └── Conversation/ 有价值对话
        ↓
Knowledge/（方法论、读书笔记）
Software/（工具技巧、开发）
LifeOS/（投资、健康、生活）
        ↓
Writing/（视频、文章、SOP）
```

## Graphify 方案

**核心创新：双通道提取**
- 通道一：AST 解析（零 Token，Tree-sitter）
- 通道二：Claude Vision 多模态（PDF、截图）

**Token 降低数据**：
- 52 文件混合语料：降至 1/72
- 极小项目：收益不明显

**三种关系标签**：
| 标签 | 性质 | 置信度 |
|------|------|--------|
| EXTRACTED | AST 解析 | 100% 事实 |
| INFERRED | LLM 推断 | 概率性 |
| AMBIGUOUS | 证据不足 | 需人工 |

## Ingest 流程（Wiki 标准）

```
新资料 → AI 读 → 写摘要 → 判断位置 → 更新链接 → 追加索引
```

→ AI 全程主导，人只确认

## Lint 四项检查

1. **孤立页面**：无任何链接指向 → 降低系统性
2. **过时内容**：>90 天未更新 → 知识腐烂
3. **矛盾检测**：同主题两个相反结论
4. **缺失引用**：声称引用了但不存在的链接

## 适合当前 hermes-wiki 的原则

| 原则 | 应用 |
|------|------|
| 知识复利 | processed → synthesis 层层沉淀 |
| AI 主导 | ingest 流程让 AI 主导判断 |
| Lint 护航 | 定期检查孤立/过时/矛盾 |
| 晋升机制 | Queries 积累够多 → 升格为概念页 |

## 相关

- [[karpathy-llm-wiki-methodology]] — LLM Wiki 方法论详述
- `scripts/query.py` — wiki 关键词检索工具
