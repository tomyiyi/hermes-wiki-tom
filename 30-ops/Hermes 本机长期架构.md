---
title: Hermes 本机长期架构
created: 2026-04-24
updated: 2026-04-24
layer: action
type: summary
tags: [AI-Agent]
---

# Hermes 本机长期架构

## 当前机器

- 主机：MacBook Air（24G 内存）
- Hermes 主仓库：`~/Desktop/hermes`
- Hermes 主数据目录：`~/.hermes`
- 主知识库：`~/Desktop/hermes-wiki`
- 主消息入口：飞书 Bot `hermes-tangyi`

## 设计原则

1. 内置 Memory 只保存稳定事实，不保存长文章和大段背景。
2. 长期知识、调研、SOP、项目资料统一写入 `hermes-wiki`。
3. 日常使用按角色拆分 profile，避免一个实例什么都做。
4. 飞书适合日常对话；本机终端适合修复、重启、结构化维护。

## Profile 分工

### 默认主实例（default / ~/.hermes）

- 用途：日常飞书对话、轻量执行、快速问答
- 特点：上下文更轻，提示更克制

### research（~/.hermes/profiles/research）

- 默认工作目录：`~/Desktop/hermes-wiki`
- 用途：微信文章采集、总结、知识沉淀、Obsidian/llm-wiki 写入
- 适合任务：
  - 抓取文章并归档
  - 生成总结与标签
  - 补充知识节点与项目背景

### ops（~/.hermes/profiles/ops）

- 默认工作目录：`~/Desktop/hermes`
- 用途：Hermes 本机维护、日志排查、配置修复、重启网关
- 适合任务：
  - 检查 gateway 状态
  - 看日志
  - 调整 config / memory / skills
  - 修复本机问题

## Hermes-Wiki 目录建议

现有 `raw / processed / summary / action` 继续保留给 llm-wiki 流程使用。

新增的四层目录用于人工和 Agent 协作：

- `00-inbox/`：临时待整理材料
- `10-knowledge/`：长期有效的知识结论
- `20-projects/`：项目级文档与推进记录
- `30-ops/`：系统说明、SOP、排障、安装规范

## 写入规则

### 应该写进内置 Memory 的内容

- 用户偏好
- 本机固定路径
- 主模型/provider 约束
- 飞书/知识库的固定入口
- 运行约束与维护规则

### 不应该写进内置 Memory 的内容

- 长篇微信文章全文
- 调研汇总大段正文
- 一次性项目背景
- 可放入 wiki 的 SOP、总结、流程说明

## 常用维护命令

检查 Hermes：

```bash
launchctl print gui/$(id -u)/ai.hermes.gateway | head -40
```

重启 Hermes：

```bash
launchctl kickstart -k gui/$(id -u)/ai.hermes.gateway
```

查看最近日志：

```bash
tail -n 80 ~/.hermes/logs/agent.log
```

## 运行建议

- 飞书里遇到“要改本机配置/目录/代码”的任务，优先交给 `ops` 思路处理。
- 长任务按主题分 session，不要无限续在一个线程里。
- 如果是文章、资料、案例，优先进入 `research` 工作流，而不是塞进 Memory。

## 最小常驻模式

长期常驻时，只保留 `gateway`。

- 保持运行：`ai.hermes.gateway`
- 按需启动：dashboard、web-ui
- 默认关闭：api_server（除非明确需要本地 API 接入）

这样可以减少后台进程、降低暴露面，也更符合本机飞书主入口的使用方式。
