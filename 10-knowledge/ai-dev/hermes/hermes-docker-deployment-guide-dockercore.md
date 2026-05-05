---
title: "Hermes Docker 部署完全指南"
created: 2026-04-12
updated: 2026-04-13
layer: processed
type: summary
tags: [AI-Agent, hermes, docker, deployment, installation, configuration]
source_domain: 微信公众号
source_author: Dockercore
source_published: 2026-04-08
original_length: 307 lines
archived: false
---

# Hermes Docker 部署完全指南

> 作者：Dockercore | 发布：2026-04-08 | 来源：微信公众号

## 独立观点

1. **两种 Docker 角色完全不是一回事**：把 Hermes 跑进容器 ≠ 让 Hermes 使用 Docker 沙箱执行命令。新手最常混这两层
2. **数据在宿主机，不在镜像层**：核心设计原则——`~/.hermes` → 容器内 `/opt/data`，所有配置、会话、记忆都存在宿主机
3. **setup 先行，后台化**：官方推荐的首次启动必须先交互式 setup，否则会得到"容器在跑但无法服务"的半成品

## 核心架构

```
宿主机 ~/.hermes ──挂载──→ 容器内 /opt/data（HERMES_HOME）
                                │
                    ┌───────────┴────────────┐
                    │  .env（密钥）          │
                    │  config.yaml（行为）   │
                    │  sessions/（会话）     │
                    │  skills/（技能）        │
                    │  memory/（记忆）       │
                    └───────────────────────┘
```

## 三种运行方式

| 模式 | 命令 | 适用场景 |
|------|------|---------|
| 临时CLI | `docker run -it --rm -v ~/.hermes:/opt/data nousresearch/hermes-agent` | 偶尔测试 |
| 后台常驻Gateway | `docker run -d --name hermes --restart unless-stopped -v ~/.hermes:/opt/data nousresearch/hermes-agent gateway run` | 日常使用（推荐）|
| Docker Compose | `docker compose up -d` | 生产环境/团队协作 |

## 配置边界（关键）

| 配置项 | 放哪里 | 说明 |
|--------|--------|------|
| API密钥（OPENAI_API_KEY等）| ~/.hermes/.env | 密钥类 |
| 默认模型、provider | ~/.hermes/config.yaml | 行为类 |
| 模型选择 | `hermes model` / `hermes config set` | 官方推荐方式 |

> **警告**：不要把模型名也写进 .env 的 LLM_MODEL——官方已明确 CLI 不再读取该变量

## 排障四层验证

1. **进程层**：`docker ps` 容器正常 Up
2. **日志层**：`docker logs -f hermes` 无异常
3. **CLI层**：`docker exec -it hermes hermes doctor` 正常返回
4. **业务层**：实际发消息验证，不只看容器在线

## 安全底线

- 消息平台配置 allowlist（如 `TELEGRAM_ALLOWED_USERS`）
- API Server 必须设置 `API_SERVER_KEY`
- `chmod 600 ~/.hermes/.env`
- 不要让两个容器并发写同一 ~/.hermes

## 重要命令速查

```bash
# 首次初始化（必须先跑这个）
mkdir -p ~/.hermes
docker run -it --rm -v ~/.hermes:/opt/data nousresearch/hermes-agent setup

# 后台常驻
docker run -d --name hermes --restart unless-stopped \
  -v ~/.hermes:/opt/data nousresearch/hermes-agent gateway run

# 升级
docker pull nousresearch/hermes-agent:latest
docker rm -f hermes && docker run -d ... (同上)

# 备份
tar -czf hermes-backup-$(date +%F).tar.gz ~/.hermes

# 排障
docker logs -f hermes
docker exec -it hermes hermes doctor
```

## 关联
- [[hermes-vs-openclaw-vs-claude-code]]（产品选型）
- [[skills-auto-evolution]]（Skills 系统）
- [[stock-analysis-hermes-migration-20260413]]（stock-analysis 迁移 Action）
