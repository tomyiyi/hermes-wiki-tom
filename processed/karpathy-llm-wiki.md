---
title: Karpathy LLM Wiki — Processed Notes
created: 2026-04-11
updated: 2026-04-11
layer: processed
type: concept
tags: [knowledge-base, wiki, rag-alternative, karpathy, compounding-knowledge]
sources: [raw/articles/karpathy-llm-wiki-personal-knowledge-base.md]
derived_from: []
---

# Karpathy LLM Wiki Processed Notes

## 划重点

### 核心理念
**别让 AI 每次从零开始，让知识滚雪球。**

RAG 的问题：每次查询从零检索，无积累，Token 消耗高。
Wiki 的优势：先查已编译知识，有复利，Token 低。

### 三层架构 vs 五层架构

**Karpathy 原版三层：**
| 层 | 职责 |
|----|------|
| Raw Sources | 只读存档 |
| The Wiki | LLM 生成和维护 |
| The Schema | 规则，人+LLM 共管 |

**作者扩展五层（内容创作者版）：**
```
Notes/（输入层）
  ├── Clippings/    网页剪藏
  ├── Inbox/        碎片想法
  └── Conversation/ 有价值的 AI 对话
        ↓
Knowledge/（知识层）  方法论、读书笔记
Software/（技能层）   工具技巧、开发
LifeOS/（行动层）     投资、健康、生活
        ↓
Writing/（产出层）     视频、文章、SOP
```

→ 五层更适合个人创作者，三层适合纯技术场景

### Ingest 流程（关键）
```
新资料 → AI 读 → 写摘要 → 判断位置 → 更新链接 → 追加索引
```
→ AI 全程主导，人只确认

### Lint 四项检查
1. 孤立页面（无任何链接指向）
2. 过时内容（>90 天未更新）
3. 矛盾检测（同主题两个相反结论）
4. 缺失引用（声称引用了但不存在的链接）

### 八大分类（来自文章）
AI & 技术、内容创作 & IP、投资 & 财经、管理 & 领导力、创业、个人成长、生活管理、教育 & 回忆

## 与 Hermes Wiki 的映射
- Raw Sources → `raw/articles/`
- The Wiki → `summary/`（单篇总结）、`synthesis/`（综合）
- The Schema → `SCHEMA.md`
- Inbox → `queries/`
- Conversation → 尚未建立（可考虑新增）

## 待讨论
- 对话存档策略：哪些对话值得存？当前 Hermes 没有 Conversation/ 目录
