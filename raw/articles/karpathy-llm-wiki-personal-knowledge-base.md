---
title: Karpathy 的 LLM Wiki 火了，我改造了一下，比原版更好用
author: (internal)
date: 2026-04-11
source: 用户分享文章
url: (internal document)
created: 2026-04-11
updated: 2026-04-11
layer: raw
type: summary
tags: [knowledge-base, wiki, karpathy]
archived: false
---

# Karpathy LLM Wiki 个人知识库方法论

## 核心理念
**别让 AI 每次都从零开始，让知识滚雪球。**

## Karpathy 三层架构

| 层 | 干什么 | 谁管 |
|----|--------|------|
| Raw Sources | 原始资料丢进来，只读不改 | 人选材料 |
| The Wiki | LLM 生成的知识产物 | LLM 维护 |
| The Schema | 规则文件，告诉 LLM 该怎么干活 | 人和 LLM 共管 |

## 三个核心动作

### Ingest（入库）
- AI 读一遍新资料
- 写摘要
- 判断该放哪
- 更新相关页面链接
- 追加到索引

### Query（查询）
- 在 Wiki 里搜相关内容
- 综合回答
- 发现新关联时会写回 Wiki（反哺）

### Lint（健康检查）
- 孤立页面检测
- 过时内容检测
- 矛盾检测
- 缺失引用检测

## 作者的五层扩展

从三层变成五层（适合内容创作者）：

```
Notes/（输入层）
  ├── Clippings/    网页剪藏
  ├── Inbox/        碎片想法
  └── Conversation/ 跟 AI 的有价值对话
        ↓
Knowledge/（知识层）    方法论、读书笔记、原创思考
Software/（技能层）     工具技巧、开发思考、产品研发计划
LifeOS/（行动层）       投资、健康、保险、联系人
        ↓
Writing/（产出层）      视频脚本、文章、运营 SOP
```

关键设计：
- **确认机制**：AI 先列方案，人确认后再执行
- **Notes/Conversation**：存跟 AI 的深度讨论，对话本身就在生产知识
- **链接宜少不宜多**：只建最强关联，不追求覆盖率

## 八大分类
- AI & 技术
- 内容创作 & IP
- 投资 & 财经
- 管理 & 领导力
- 创业
- 个人成长
- 生活管理
- 教育 & 回忆

## 关键原则
1. 一个入口，多个终点
2. 结构够用就行
3. AI 建议，你拍板
4. 链接宜少不宜多
5. 对话也是知识
6. 存着不用等于没有
7. 索引到目录，不到文件
8. 不绑定工具
