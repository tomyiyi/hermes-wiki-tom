---
title: Hermes Agent 安装与部署
created: 2026-04-13
updated: 2026-04-13
layer: synthesis
type: concept
tags: [Hermes, AI-Agent, installation, docker, deployment, Nous-Research, configuration]
sources:
  - processed/hermes-docker-deployment-guide-dockercore.md
  - processed/2957d41fbf15_Hermes-Agent-保姆级安装教程-超详细踩坑指南-852844.md
derived_from:
  - Hermes Docker 部署完全指南
  - Hermes Agent 保姆级安装教程
---

# Hermes Agent 安装与部署

> Hermes Agent 可通过 Docker 或直接安装运行，核心原则：数据在宿主机，不在镜像层。

## 两种运行方式

| 方式 | 命令 | 适用场景 |
|------|------|---------|
| **Docker（推荐）** | `docker run -d --name hermes ...` | 生产环境、跨平台 |
| **直接安装** | `pip install hermes-agent` | 开发调试 |

## Docker 部署三种模式

| 模式 | 命令 | 适用场景 |
|------|------|---------|
| 临时CLI | `docker run -it --rm -v ~/.hermes:/opt/data ...` | 偶尔测试 |
| 后台常驻Gateway | `docker run -d --name hermes --restart unless-stopped ... gateway run` | 日常使用（推荐）|
| Docker Compose | `docker compose up -d` | 生产环境/团队协作 |

## 核心架构

```
宿主机 ~/.hermes ──挂载──→ 容器内 /opt/data（HERMES_HOME）
                                │
                    ┌───────────┴────────────┐
                    │  .env（密钥）          │
                    │  config.yaml（行为）    │
                    │  sessions/（会话）     │
                    │  skills/（技能）        │
                    │  memory/（记忆）        │
                    └───────────────────────┘
```

**关键原则**：数据存在宿主机，不在镜像层。升级镜像不会丢失数据。

## 配置边界

| 配置项 | 放哪里 | 说明 |
|--------|--------|------|
| API密钥（OPENAI_API_KEY等）| `~/.hermes/.env` | 密钥类 |
| 默认模型、provider | `~/.hermes/config.yaml` | 行为类 |
| 模型选择 | `hermes model` / `hermes config set` | 官方推荐方式 |

> **警告**：不要把模型名写进 `.env` 的 `LLM_MODEL`——官方已明确 CLI 不再读取该变量。

## 常见安装坑

| 坑 | 原因 | 解决方案 |
|----|------|---------|
| 网络问题 | 国内访问 GitHub/Docker Hub 受限 | 使用代理或镜像 |
| Windows 需 WSL2 | 原生 Windows 支持不完整 | 安装 WSL2 后运行 |
| Nous Portal 免费陷阱 | MiMo 免费套餐实为 Nous Portal 订阅 | 订阅 Nous Portal 才能正常使用 |
| setup 未完成 | 首次启动未交互式 setup | `docker exec -it hermes setup` |

## 排障四层验证

1. **进程层**：`docker ps` 容器正常 Up
2. **日志层**：`docker logs -f hermes` 无异常
3. **网络层**：`docker exec -it hermes curl https://api.openai.com` 可达
4. **功能层**：`docker exec -it hermes hermes doctor` 完整检查

## 相关

- [[hermes-agent-core-concepts]] — Hermes 核心概念（记忆系统、学习循环）
- [[hermes-vs-openclaw-vs-claude-code]] — Hermes vs OpenClaw vs Claude Code 对比
