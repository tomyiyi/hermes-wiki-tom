---
title: "Hermes Agent 保姆级安装教程（超详细踩坑指南）"
created: 2026-04-12
updated: 2026-04-12
layer: raw
type: summary
tags: [AI-Agent, hermes, installation, tutorial]
source_domain: 微信公众号
source_author: 陈虾仁
source_published: 2026-04-12
original_length: 9KB
archived: false
note: "与 doc_6abf1692d7f7 内容相同，去重保留此版本"
---

# Hermes Agent 保姆级安装教程（超详细踩坑指南）

> 作者：陈虾仁 | 发布：2026-04-12 | 来源：微信公众号

## 摘要简报（150字）

Hermes Agent 官方安装方式有 Docker 和源码两种。Docker 方案适合追求快速体验的用户，源码方案适合需要深度定制的开发者。全文覆盖环境准备→安装步骤→基础配置→平台接入→常见问题排查，并包含大量踩坑记录。

## 关键步骤索引

1. **前置要求**：5美元 VPS 或更高，Git/Docker/Node.js 环境
2. **Docker 安装**：`docker run -d ...` 一行命令完成基础部署
3. **源码安装**：适合深度定制和二次开发
4. **必做配置**：API Key 配置、平台 Webhook 接入、记忆系统初始化
5. **多平台接入**：飞书/微信/Telegram/Discord 等 15+ 平台

## 踩坑重点
- 网络问题：部分海外服务器需配置代理
- 权限问题：Docker 容器内用户权限与宿主机差异
- 首次启动失败常见原因及解决方案

## 关联
- [[hermes-vs-openclaw-vs-claude-code]]（产品选择参考）
