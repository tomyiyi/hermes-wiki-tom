---
title: HKUDS/DeepTutor 调研
created: 2026-05-01
updated: 2026-05-01
layer: processed
type: entity
tags: [AI-Agent, knowledge-management, AI-Agent]
---

# HKUDS/DeepTutor 调研

**星标：+4.5K（截至 2026-05-01）**
**最新版本：v1.3.3（2026-04-30）**
**定位：原生 AI 智能体个性化学习助手**

---

## 核心定位

> *"Agent-Native Personalized Tutoring"*

不是通用 AI 助手，而是专为**个性化学习辅导**设计的智能体系统。核心差异：
- 学习场景专属：知识库问答、Quiz 生成、数学动画、研究报告
- 多入口并行：CLI、WebSocket API、Python SDK、Web UI

---

## 架构：两层插件模型

```
Entry Points:  CLI (Typer)  |  WebSocket /api/v1/ws  |  Python SDK
                    ↓                   ↓                   ↓
              ┌─────────────────────────────────────────────────┐
              │              ChatOrchestrator                    │
              │   routes to ChatCapability (default)           │
              │   or a selected deep Capability                 │
              └──────────┬──────────────┬───────────────────────┘
                       │              │
           ┌──────────▼──┐  ┌────────▼──────────┐
           │ ToolRegistry │  │ CapabilityRegistry │
           │  (Level 1)  │  │   (Level 2)       │
           └──────────────┘  └────────────────────┘
```

### Level 1 — Tools（轻量级单功能工具）

| Tool | 说明 |
|------|------|
| `rag` | 知识库检索（RAG） |
| `web_search` | 带引用的网络搜索 |
| `code_execution` | 沙箱 Python 执行 |
| `reason` | 专用深度推理 LLM 调用 |
| `brainstorm` | 广度优先创意探索 |
| `paper_search` | arXiv 学术论文搜索 |
| `geogebra_analysis` | 图像 → GeoGebra 命令（4 阶段视觉管道）|

### Level 2 — Capabilities（多步骤智能体管道）

| Capability | 阶段 |
|-----------|------|
| `chat` | responding（默认，工具增强）|
| `deep_solve` | planning → reasoning → writing |
| `deep_question` | ideation → evaluation → generation → validation |

---

## 核心能力矩阵

| 能力 | 说明 | 典型场景 |
|------|------|---------|
| **Chat** | 通用对话，工具增强 | 日常问答 |
| **Deep Solve** | 多阶段数学/科学问题求解 | 证明、定理推导 |
| **Quiz Generation** | 自动化试题生成 | 学习自测 |
| **Deep Research** | 多智能体研究 + 报告生成 | 学术调研 |
| **Math Animator** | Manim 动画生成 | 数学可视化 |
| **Visualize** | Chart.js/SVG 可视化 | 数据图表 |
| **Co-Writer** | 多文档 Markdown 协作 | 写作辅助 |
| **Book Engine** | "活书"编译，14 种区块类型 | 知识整理 |

---

## 内存系统：双文件模型

```
Memory/
├── SUMMARY.md   # 运行摘要（自动更新）
└── PROFILE.md   # 用户画像（偏好、知识水平）
```

**关键设计**：
- 每 Bot 有独立 SOUL.md / TOOLS.md / USER.md（位于各自 workspace）
- 跨 Bot 共享 SUMMARY + PROFILE（shared_memory_dir）
- 内存更新由 LLM 自动触发，存储为自然语言而非结构化 JSON

---

## TutorBot：多平台持久智能体

支持 13 个平台同时接入（Discord/Telegram/WhatsApp/MoChat/飞书等），每个平台独立 Bot 实例，共享统一内存层。

**心跳机制**：`HEARTBEAT.md` 定时任务，支持 cron 工具创建/删除定时任务。

---

## Skills 系统

内置 Skills：
- `deep-solve` / `deep-question` / `deep-research`
- `summarize` / `knowledge-base` / `notebook`
- `cron` / `tmux` / `weather` / `github`
- `skill-creator`（用户可自建 Skill）
- `memory` / `clawhub`

**Skill Creator 核心原则**：
1. **Concise is Key**：上下文窗口是公共资源，只添加模型真的不知道的内容
2. **Degrees of Freedom**：高自由（文本指令）→ 低自由（具体脚本）按任务脆弱性匹配
3. **自验证**：每个 Skill 可附带测试脚本

---

## 发布节奏（2026）

| 版本 | 日期 | 关键词 |
|------|------|--------|
| v1.3.3 | 04-30 | NVIDIA NIM + Gemini embedding、Space 统一上下文 |
| v1.3.2 | 04-29 | 透明 embedding URL、RAG 重建韧性 |
| v1.3.0 | 04-27 | 版本化 KB 索引、Space hub |
| v1.2.0 | 04-20 | Book Engine"活书"编译器 |
| v1.1.0 | 04-15 | LaTeX 块数学重构、LLM 诊断探测 |
| v1.0.0 | 04-04 | Agent-native 架构重写（~200k 行）|
| v0.6.0 | 01-23 | Session 持久化、增量文档上传 |

---

## 对 Hermes 的可借鉴点

### 1. 双文件内存模型 → 可吸收
- `SUMMARY.md` + `PROFILE.md` 比当前 Hermes 的 MEMORY 更结构化
- 自动 LLM 触发的内存更新 vs 手动 memory 工具调用

### 2. Capability 协议 → 可借鉴
- `BaseCapability` 抽象类定义 manifest + stages
- 能力可注册、可发现、有静态元数据
- Hermes 的 Skill 系统可以向 Capability 协议靠拢

### 3. Space 统一上下文 → 设计参考
- 把历史会话、Notebook、Question Bank、Skills、Memory 统一到"Space"概念
- 用户选择什么上下文，精确传递给后端（`memory_references`）

### 4. 多平台 Bot 架构 → TutorBot 设计
- 共享内存层 + 平台隔离 Bot 配置
- 对应 Hermes 的多平台接入（飞书/微信/Telegram）

### 5. Skill Creator 自举 → Meta-Skill
- 用 Skill Creator 创建新 Skill，实现自举
- DeepTutor 的 skill-creator 是真正的"做事前先建工具"思维

---

## 源码文件索引

```
deeptutor/
├── core/
│   ├── context.py          # UnifiedContext 数据结构
│   └── capability_protocol.py  # BaseCapability 抽象层
├── tutorbot/
│   ├── agent/
│   │   ├── context.py      # ContextBuilder（组装系统提示）
│   │   ├── memory.py       # MemoryStore（内存读写）
│   │   ├── loop.py        # AgentLoop（核心处理引擎）
│   │   └── skills.py      # SkillsLoader
│   ├── templates/
│   │   ├── SOUL.md        # Bot 身份定义
│   │   └── AGENTS.md     # 调度指令
│   └── skills/
│       ├── deep-solve/SKILL.md
│       └── skill-creator/SKILL.md
└── services/memory/service.py  # SUMMARY+PROFILE 内存服务
```

---

**归档时间**：2026-05-01
**源码版本**：v1.3.3（2026-04-30）
