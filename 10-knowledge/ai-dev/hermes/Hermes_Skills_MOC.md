---
title: Hermes Master Skills & Ecosystem MOC
tags:
  - MOC
  - Hermes
  - Ecosystem
  - Reference
date: 2026-04-14
---

# Hermes Master Skills & Ecosystem MOC

本节点为所有从 Hermes 生态吸收的外部知识、框架与能力的总索引。
NewAge 必须定期查阅本节点，并根据项目需求从中寻找解决方案。

## 1. 软件开发与自动化控制 (Software & Automation)
- **Claude Code**: [Reference_claude-code.md](./Reference_claude-code.md) - 终端物理接管与 AST 级别沙箱执行理念来源。
- **Browser Use**: [Reference_browser-use.md](./Reference_browser-use.md) - 网页自动化与浏览器交互参考。
- **MCP (Model Context Protocol)**: [Reference_mcp.md](./Reference_mcp.md) - 标准化上下文接入与 `native-mcp`, `mcporter` 技能底层逻辑。

## 2. MLOps 与模型推理 (Model Inference & MLOps)
- **vLLM**: [Reference_vllm.md](./Reference_vllm.md) - 高并发大模型推理后端。
- **Unsloth**: [Reference_unsloth.md](./Reference_unsloth.md) - 极速微调工具。
- **DSPy**: [Reference_dspy.md](./Reference_dspy.md) - 将 Prompt 工程转化为代码编译的革命性框架。
- **Axolotl**: [Reference_axolotl.md](./Reference_axolotl.md) - LLM 训练与对齐平台。

## 3. 已吸收并转化为 Declarative Skills 的项目 (Absorbed Skills)
- `wechat_article_ingest` (衍生自 `wechat-article-ingest`)
- `macmini_openclaw_inspect` (衍生自 `macmini-ssh-openclaw-inspect`)
- `subagent_driven_development` (衍生自 `subagent-driven-development`)

*(以上工具的 README 已被 `ingest_ecosystem.py` 自动化脚本下载入库。)*
