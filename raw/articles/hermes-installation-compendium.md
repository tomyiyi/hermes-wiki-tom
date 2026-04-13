---
title: "Hermes Agent 安装配置合集（去重版）"
created: 2026-04-12
updated: 2026-04-13
layer: raw
type: summary
tags: [AI-Agent, hermes, installation, configuration, tutorial]
source_domain: 微信公众号
source_authors: [陈虾仁, 流年Agent, 沉默王二, Dockercore]
source_published: 2026-04-08 ~ 2026-04-12
original_length: 100KB (合并5篇去重)
archived: false
note: "去重合并版，保留最长/最详细版本"
---

# Hermes Agent 安装配置合集（去重版）

> 来源: 陈虾仁(保姆级)、流年Agent(必做配置)、沉默王二(保姆教程)、Dockercore(Docker部署)

## 摘要简报（150字）

安装路径：Docker（推荐新手）/ 源码（深度定制）。必做配置：API Key、平台Webhook、记忆初始化。多平台接入：飞书/微信/Telegram/Discord等15+平台。常见坑：网络问题、权限错误、首次启动失败。

## 安装路径选择

| 方式 | 适合人群 | 优点 | 缺点 |
|------|---------|------|------|
| Docker | 新手/快速体验 | 一行命令、数据持久化 | 需Docker基础 |
| 源码 | 深度定制开发者 | 完全可控 | 需配置环境 |

## 必做配置清单

1. **API Key 配置**（.env）
2. **模型选择**（config.yaml → model.default）
3. **平台 Webhook 接入**（飞书/微信/Telegram）
4. **记忆系统初始化**（首次启动自动）
5. **双模型 fallback 架构**（主流+备用）

## 踩坑记录

- 网络问题：海外服务器需配置代理
- 权限：Docker 容器用户权限与宿主机差异
- 首次启动：必须先 setup，不能直接后台化
- API Key：不要混用 .env 和 config.yaml

## 关联
- [[hermes-docker-deployment-guide-dockercore]]（Docker 详细部署）
