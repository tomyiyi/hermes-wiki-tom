---
type: card
deck: Hermes核心
---

# WAL 协议是什么？

WAL（Write-Ahead Logging）协议是 Hermes Agent 的核心记忆架构，采用 L1-L5 五层分层记忆系统：
- L1：即时上下文（当前对话）
- L2：会话记忆（近期对话摘要）
- L3：项目记忆（项目相关持久上下文）
- L4：领域记忆（跨项目领域知识）
- L5：核心记忆（永久核心知识）

---

# Hermes 工作流的 8 个阶段是什么？

Think → Plan → Build → Review → Ship → Deploy → QA → Reflect（8阶段完整环），另有 Hotfix 分支可在任意阶段触发快速闭环。

---

# Hermes Vault 中 hermes-wiki 的定位是什么？

个人知识库 + OPC社区项目执行沉淀，约 255 篇文件，目录包括：00-inbox / 10-knowledge / 20-projects / 30-ops / concepts / conversations / entities / opc / processed / raw

---

# Hermes 的三大核心模块是什么？

memoryManager（记忆管理）、feedbackLearner（反馈学习）、selfLearn（自主学习）

---

# Obsidian frontmatter 的双维分类是什么？

Layer × Type 双维分类：
- Layer：raw / processed / summary / synthesis / action / conversations
- Type：concept / entity / comparison / query / summary
