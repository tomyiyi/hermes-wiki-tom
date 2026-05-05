---
title: agency_agents_analysis
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
  - Agent
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# 🎭 The Agency: AI Specialists (msitarzewski/agency-agents) 知识分析与 NewAge 融合计划

## 📋 Step 1：提取内容 + 独立观点
### 核心提取
* **项目本质**：`msitarzewski/agency-agents` 并不是一个执行框架代码，而是一个庞大且结构化极好的 **AI 专家 Prompt (Persona) 集合**（"The Agency"）。在 GitHub 上有高达 ~79k Stars。
* **文件形式**：纯 Markdown 文件，通过各种终端自动化脚本 (`install.sh`, `convert.sh`) 注入到不同 AI 辅助编程工具的配置中（如 [[Claude Code]] `~/.claude/agents/`, Copilot, Cursor `.cursor/rules/`, OpenClaw 等）。
* **角色拆分 (Division)**：
  * **Engineering (工程)**：Frontend Developer, Backend Architect, Mobile App Builder, AI Engineer, DevOps Automator...
  * **Marketing (营销)**：SEO, Copywriting, China Market Localization...
  * **Design, Academic, Game Development, Paid-media** 等多领域的角色。
* **特点**：每个 Agent 有独立的 Identity (身份), Personality (性格), Core mission (核心任务), Workflow (工作流), Deliverable-focused (交付标准)。

### 独立观点 (Trae Solo's View)
* **优劣势**：这种以 `.md` 或系统规则形式存在的 Prompt 库非常容易被复用，但它**缺乏真正的自动化协作能力**。在原生生态中，它们仅仅是被动地被工具加载（比如 Cursor 看到规则后改变对话口吻）。
* **化学反应**：如果将这种极具深度的“角色设定”与 **NewAge** 强大的底层执行引擎（特别是我们刚刚写的跨主机控制 `ssh_remote_operator.py` 和自动任务流）结合，就会产生真正的 **Agentic Workflow**。不再是“人切换角色跟 AI 聊天”，而是 NewAge 在接到复杂任务时，**自己化身为 Backend Architect 思考，化身为 DevOps Automator 执行跨主机部署**。

---

## 📋 Step 2：归档 + 模式识别
### 归档标签
* `Persona-Library` (角色库)
* `Prompt-Engineering` (提示词工程)
* `Multi-Agent-Collaboration` (多智能体协作)

### 模式识别 (Pattern Recognition)
* **模式 1：垂直细分胜过全能大模型**。让一个大模型去解决所有问题，效果往往不如把大模型“降维”限制在某个具体的专家身份中（比如强制它只按 DevOps 的思维和检查清单输出）。
* **模式 2：工作流标准化 (SOP)**。Agency Agents 之所以火爆，是因为它把每个角色的最佳实践固化成了 Checklist。
* **模式 3：跨平台兼容设计**。项目自带脚本，将一种 Markdown 转化为多种平台格式（Cursor Rules, Claude Agents等）。这提醒我们，NewAge 的输出也可以通过转换器兼容其他系统。

---

## 📋 Step 3：系统优化建议 + 收益对比
### 给 NewAge 的优化建议：动态人格加载器 (Dynamic Persona Loader)
目前 NewAge 的 `system_prompt.md` 可能是固定的全局人设。我们需要开发一个 `Persona Manager`，允许 NewAge 在执行不同任务时，从 `agency-agents` 库中动态抽取并挂载特定的人设规则。

### 收益对比 (Before vs After)
| 维度 | Before (当前 NewAge) | After (吸收 Agency Agents 后) |
| --- | --- | --- |
| **思维深度** | 全局通用大模型思维，解决细分领域容易泛泛而谈 | 化身垂直领域专家，强制遵循该领域的专家 Checklist |
| **任务分发** | 线性思维执行任务 | “虚拟项目组”模式：前端部分套用 Frontend 人格，运维部分套用 DevOps 人格 |
| **代码风格** | 依赖大模型的随机发挥 | 强制对齐各个角色的输出标准 (Deliverable-focused) |
| **知识广度** | 依赖自带系统提示词和短期记忆 | 坐拥 79k+ Star 开源社区不断迭代的百种专家级 SOP |

---

## 📋 Step 4：计划执行 (Plan for NewAge)
1. **获取源数据**：编写一个技能 `fetch_agency_agents.py`，让 NewAge 自动拉取 `msitarzewski/agency-agents` 仓库。
2. **提取核心记忆**：将所有 `.md` 中的专家角色数据进行清洗。
3. **入库 MemPalace**：将这些角色和对应的工作流 (Workflow) 存入 NewAge 的 `LanceDBPalace`，分类为 `semantic` (语义记忆) 和 `procedural` (程序记忆)。
4. **引擎重构 (可选)**：在 NewAge 的 Orchestrator 中加入 **"Persona Switcher"** 机制，遇到写代码任务时自动通过 LanceDB 检索出对应的工程师 SOP 挂载到 Context 中。

---

## 📋 Step 5：沉淀到记忆系统
（此文档将直接送入 NewAge 的知识库中，供其长期检索与自我进化。）