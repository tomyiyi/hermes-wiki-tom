---
title: "2026年4月最火的开源AI Agent【hermes-agent】，我从架构拆到商业模型"
created: 2026-04-12
updated: 2026-04-12
layer: raw
type: summary
tags: [AI-Agent, hermes, 架构分析, 商业模型, Nous-Research, memory, skills, agent-loop]
source_domain: 微信公众号
source_author: 思敏
source_published: 2026-04-12
original_length: 562 lines
archived: false
---

# 2026年4月最火的开源AI Agent【hermes-agent】，我从架构拆到商业模型

> 作者：思敏 | 发布：2026-04-12 | 来源：微信公众号

## 独立观点（作者非共识核心论点）

1. **Skills 自动生成 + 自我迭代构成正反馈飞轮**，这是 Hermes 区别于所有竞品的核心差异——其他 Agent 的 Skills 靠人写，Hermes 的 Skills 由 Agent 从执行经验中自生成、自迭代
2. **数据飞轮是开源动机的真正逻辑**：开源 Agent 是获客手段，轨迹数据训练模型，Nous Portal 付费平台才是利润中心——这与 Meta 开源 LLaMA 的逻辑一脉相承
3. **产品形态正在从工具转向基础设施**：能 7×24 自主运行、在用户不在时继续工作，才是真正的 Agent，否则只是"加了个界面的大型语言模型"

## 核心骨架

### 五层架构
- **接入层（Gateway）**：连接 15+ 平台
- **Agent Core**：思考与执行循环的大脑
- **Memory + Skills + Tools**：能力基底
- **Terminal Backends**：6种执行环境（本地/Docker/SSH/Daytona/Modal/Singularity）
- **数据飞轮**：用户轨迹反哺模型训练

### 四层记忆架构
1. 会话内上下文（上下文压缩）
2. 跨会话持久记忆（主动沉淀机制，非被动等待）
3. 历史会话全文检索（SQLite FTS5）
4. 辩证式用户心智建模（Honcho 集成，记行为模式而非静态标签）

### Skills 系统三层模型
| 层级 | 编写者 | 内容 |
|------|--------|------|
| 方法论层 | 人工 | 价值判断、质量标准 |
| 流程层 | 人工+Agent | 大框架人定，细节 Agent 优化 |
| 执行层 | Agent 自动 | 工具选择、参数配置、错误处理 |

### 商业飞轮
```
开源Agent获取用户 → 轨迹数据 → RL训练更强工具调用模型 
→ Nous Portal付费推理平台(400+模型) → Agent更好用 → 更多用户
```

### 与 OpenClaw 的核心分歧
OpenClaw 技能靠人写，Hermes 技能靠 Agent 从经验中学。初期 OpenClaw 体验更好，但"用久了 Hermes 会变好，OpenClaw 原地踏步"。

## 关键数据
- 两个月 58k stars，382 贡献者
- Daytona/Modal Serverless 月成本 < $1
- 3 个 Skills 积累后重复研究任务速度提升 40%
- Nous Portal 支持 400+ 模型
