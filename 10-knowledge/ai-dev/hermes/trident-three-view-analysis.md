---
title: Trident 三视角分析
created: 2026-04-28
updated: 2026-04-28
layer: 10-knowledge
type: concept
tags: [prompt-engineering, llm, deep-thinking, triple-mind, framework-architect, critical-thinking, practitioner]
sources: [raw/articles/trident-mmguo.md, raw/articles/dr-sharp-mmguo.md]
derived_from: [trident-mmguo.md, dr-sharp-mmguo.md]
archived: false
---

# Trident 三视角分析

> **来源：** Trident + Dr. Sharp（Lingbo Guo / mmguo.dev）  
> **核心方法：** 让 LLM 同时以三个身份思考同一个问题

## 核心定义

**Trident Triple Mind Model**：一个 prompt 框架，强制 LLM 同时从三个正交视角分析任何内容：

| 视角 | 身份 | 职责 |
|------|------|------|
| 🔭 Framework Architect | 框架构建者 | 扩展、延伸、找因果结构 |
| ⚔️ Critical Thinker | 批判者 | 找弱点、找漏洞、找未声明的假设 |
| 🔧 Practitioner | 实践者 | 落地行动、具体步骤、可操作性 |

## 使用方式

1. 开启新对话，先发 Trident prompt
2. AI 回复后，粘贴要分析的文章
3. AI 同时以三身份输出分析

## 为什么有效

**单一身份的问题是**：LLM 训练时倾向于"取悦用户"，会顺着你的思路走。三身份强制它同时既是检察官又是辩护人又是顾问。

**关键技巧**："让 LLM 思考自己的思考"（Metacognition）——mmguo 最常用这个技巧来解锁 LLM 的创造力。

## 在 Hermes 的应用

### Ingest 流程中的应用

每次消化文章时，用三视角替代单一摘要：

**Framework Architect 视角**：
- 这篇文章的核心理论框架是什么？
- 能延伸到哪些其他领域？
- 作者在建模什么因果结构？

**Critical Thinker 视角**：
- 这篇文章最薄弱的环节在哪里？
- 什么证据可以证伪这个论点？
- 作者没有处理或一笔带过的是什么？
- 什么假设没有被明确声明？

**Practitioner 视角**：
- 这个可以怎么应用到真实场景？
- 触发什么具体行动？
- 实施起来是什么样？
- 具体下一步是什么？

## 与其他方法论的关系

- **Deep Compression（Ilya）**：在批判者视角里自然包含了"证伪"检查
- **Fingerprints of Reality**：定义效果→拆解特征→组合模式，可作为Practitioner的工具
- **Dr. Sharp**：Top-down信念传播 = Framework Architect的认知层操作

## 相关文件

- `[[trident-mmguo.md]]` — Trident prompt 原文
- `[[dr-sharp-mmguo.md]]` — Dr. Sharp v6 prompt 原文
- `[[deep-compression]]` — Ilya 压缩即理解
- `[[wiki-ingest-flow]]` — 已将三视角整合入ingest流程
