---
title: Hermes Agent从0-1搭建部署和配置
created: 2026-04-28
updated: 2026-04-28
layer: processed
type: summary
tags: [Hermes-Agent, Nous-Research, 安装指南, AI-Agent]
source: https://mp.weixin.qq.com/s/RTir4iDyiIRvdyIMwbxgZQ
---

## 核心要点

来自微信公众号文章，Hermes Agent 完整安装指南。覆盖 Linux/macOS/Windows (WSL2)。

---

## 安装前置要求

| 工具 | 命令 | 说明 |
|------|------|------|
| Python | `python --version` | 3.11+ |
| Git | `git --version` | 任意版本 |
| uv | 自动处理 | 一键安装脚本时自动处理 |

---

## Linux / macOS 安装

### 方式一：一键安装（推荐）
```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

### 方式二：手动安装

1. **克隆仓库**（必须加 `--recurse-submodules`）
   ```bash
   git clone --recurse-submodules https://github.com/NousResearch/hermes-agent.git
   cd hermes-agent
   ```
   如已克隆但忘记加参数，补救：
   ```bash
   git submodule update --init --recursive
   ```

2. **安装 uv 并创建虚拟环境**
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv venv venv --python 3.11
   ```

3. **安装依赖**
   ```bash
   export VIRTUAL_ENV="$(pwd)/venv"
   # 全部功能（含 Discord/Telegram/cron）
   uv pip install -e ".[all]"
   # 仅核心功能
   uv pip install -e "."
   ```

4. **启动 Hermes**
   ```bash
   ./hermes
   ```

---

## Windows 用户（必须用 WSL2）

1. 以管理员身份打开终端，执行 `wsl --install`
2. 进入 WSL 后创建用户名和密码
3. 在 WSL 内执行一键安装命令

---

## 启动后配置

- 选择模型：国外用 OpenAI GPT-4 / Anthropic Claude，国内用 Qwen
- **要求：模型必须支持至少 64K context**
- 完成后保存配置

---

## Discord 接入步骤

1. 在 Discord Developer Portal 创建 Application → Bot
2. 开启 **Privileged Gateway Intents**：
   - Server Members Intent
   - **Message Content Intent**（最重要，不开则 bot 读不到消息）
3. 复制 Bot Token（不要泄露）
4. 生成邀请链接把 bot 拉进服务器
5. 把 token 和权限配置到 Hermes，启动 gateway

---

## 常见问题

| 问题 | 解决 |
|------|------|
| bot 能拉进群但私信不回复 | 确认已打开 Message Content Intent |
| 提示 User not allowed | Discord 用户 ID 没写进 `DISCORD_ALLOWED_USERS` |
| Bot 一直离线 | 检查 `hermes gateway` 是否启动成功，`DISCORD_BOT_TOKEN` 是否正确 |

---

## 来源

微信公众号：飞牛 OS 与 AI 自动化
（发布日期：2天前）
