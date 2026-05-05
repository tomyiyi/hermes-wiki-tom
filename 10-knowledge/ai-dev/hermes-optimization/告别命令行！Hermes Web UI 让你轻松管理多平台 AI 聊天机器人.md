---
title: 告别命令行！Hermes Web UI 让你轻松管理多平台 AI 聊天机器人
author: 阿志
                    阿志
date: 2026年4月19日
cover: /assets/img/news/告别命令行！Hermes Web UI 让你轻松管理多平台 AI 聊天机器人-0.png
head:
  - - meta
    - name: 新闻
---
      
![](/assets/img/news/告别命令行！Hermes Web UI 让你轻松管理多平台 AI 聊天机器人-0.gif)

在 AI 聊天机器人日益普及的今天，很多开发者和技术爱好者都在使用 **Hermes Agent** 这个强大的多平台 AI 聊天机器人框架。它支持 Telegram、Discord、Slack、WhatsApp 等 8 个主流平台，可以让你的 AI 助手无处不在。

但是，管理这样一个多平台的 AI 机器人，通常需要频繁使用命令行，配置各种复杂的设置。有没有更简单、更直观的方式呢？答案就是 **Hermes Web UI**！

### 什么是 Hermes Web UI？

**Hermes Web UI** 是 Hermes Agent 的Web 管理界面，它提供了一个美观、易用的仪表盘，让你可以通过浏览器轻松管理你的 AI 聊天机器人。

**项目地址：** https://github.com/EKKOLearnAI/hermes-web-ui

这个项目目前已经有 **798 个 Star**，支持 **8 个主流聊天平台**，是 Hermes Agent 用户必备的管理工具。

核心功能一览

#### 1\. AI 聊天管理

  • **实时流式对话**：通过 SSE 技术实现真正的实时对话体验

  • **多会话管理**：创建、重命名、删除、切换不同的聊天会话

  • **会话分组**：按平台来源（Telegram、Discord 等）分组显示，支持折叠展开

  • **Markdown 渲染**：支持代码高亮、代码复制，完美展示 AI 的回复

  • **工具调用详情**：查看 AI 调用的工具参数和结果

  • **文件上传支持**：直接上传文件给 AI 处理

  • **模型选择器**：自动发现可用的 AI 模型，支持切换

#### 2\. 多平台频道配置

这是最实用的功能之一！你可以在一个页面上配置所有 8 个平台的频道：

 平台主要功能 

**Telegram**

机器人令牌、提及控制、表情反应 

**Discord**

机器人令牌、自动线程、频道过滤 

**Slack**

机器人令牌、提及控制、机器人消息处理 

**WhatsApp**

启用/禁用、提及控制、提及模式 

**Matrix**

访问令牌、家庭服务器、自动线程 

**飞书 (Lark)**

应用 ID/Secret、提及控制 

**微信**

扫码登录（在浏览器中扫描，自动保存凭证） 

**企业微信**

机器人 ID/Secret 

所有配置都会自动写入 `~/.hermes/.env` 和 `~/.hermes/config.yaml`，修改后自动重启网关。

#### 3\. 使用分析

想要了解你的 AI 机器人使用情况？Hermes Web UI 提供了详细的分析功能：

  • **总 Token 使用量**：输入/输出分开统计

  • **会话数量**：每日平均会话数

  • **成本估算**：跟踪你的 AI 使用成本

  • **缓存命中率**：了解性能优化情况

  • **模型使用分布**：查看哪个模型最受欢迎

  • **30 天趋势**：柱状图 + 数据表格

#### 4\. 定时任务管理

  • 创建、编辑、暂停、恢复、删除定时任务

  • 支持立即触发执行

  • 提供 Cron 表达式快速预设

#### 5\. 模型管理

  • 自动从凭证池发现可用模型

  • 支持切换不同模型

  • 实时显示当前会话使用的模型

### 快速安装教程

也可以把 github 地址直接给你的hermes让他去给你安装这个 webui 界面

#### 方法一：npm 安装（推荐）

这是传统最简单的方式，只需要两行命令：

 # 1. 全局安装  
 npm install -g hermes-web-ui  
 # 2. 启动服务  
 hermes-web-ui start  
 # 3. 打开浏览器访问  
 # http://localhost:8648

#### 方法二：一键安装脚本

如果你使用的是 Debian/Ubuntu/macOS，可以使用官方提供的一键安装脚本，它会自动安装 Node.js（如果缺失）和 hermes-web-ui：

 bash <(curl -fsSL https://raw.githubusercontent.com/EKKOLearnAI/hermes-web-ui/main/scripts/setup.sh)

#### 方法三：WSL 用户

如果你使用 Windows 的 WSL（Windows Subsystem for Linux），同样可以使用一键安装脚本：

 bash <(curl -fsSL https://raw.githubusercontent.com/EKKOLearnAI/hermes-web-ui/main/scripts/setup.sh)  
 hermes-web-ui start

#### 方法四：Docker Compose

对于喜欢容器化部署的用户，项目也提供了 Docker Compose 配置。

### 常用命令

安装完成后，你可以使用以下命令管理 hermes-web-ui：

 # 前台运行（调试模式）  
 hermes-web-ui start --foreground  
 # 指定端口启动  
 hermes-web-ui start --port 9000  
 # 停止服务  
 hermes-web-ui stop  
 # 重启服务  
 hermes-web-ui restart  
 # 查看状态  
 hermes-web-ui status  
 # 更新到最新版本  
 hermes-web-ui update  
 # 查看版本  
 hermes-web-ui -v  
 # 查看帮助  
 hermes-web-ui -h

### 自动配置功能

Hermes Web UI 在启动时会自动完成以下配置：

1. **验证配置文件**：检查 `~/.hermes/config.yaml` 并填充缺失的 `api_server` 字段

2. **备份原配置**：如果修改了配置，会备份到 `config.yaml.bak`

3. **检测并启动网关**：自动检测并启动 Hermes 网关（如果需要）

4. **解决端口冲突**：自动清理占用端口的残留进程

5. **自动打开浏览器**：启动成功后自动打开浏览器

### 技术架构

Hermes Web UI 采用了现代化的技术栈：

**前端：**

  • Vue 3 + TypeScript

  • Vite 构建工具

  • Naive UI 组件库

  • Pinia 状态管理

  • Vue Router 路由

  • vue-i18n 国际化

  • SCSS 样式

  • markdown-it + highlight.js 代码高亮

**后端：**

  • Koa 2（BFF 服务器）

  • node-pty（Web 终端）

**架构图：**

 浏览器 → BFF (Koa, :8648) → Hermes Gateway (:8642)  
 ↓  
 Hermes CLI（会话、日志、版本）  
 ↓  
 ~/.hermes/config.yaml（频道行为）  
 ~/.hermes/auth.json（凭证池）  
 腾讯 iLink API（微信扫码登录）

### 为什么选择 Hermes Web UI？

1. **告别命令行**：通过直观的 Web 界面管理所有配置

2. **多平台统一管理**：一个界面管理 8 个聊天平台

3. **实时监控**：随时了解 AI 机器人的使用情况

4. **简单易用**：npm 一键安装，开箱即用

5. **完全开源**：MIT 许可证，可以自由使用和修改

6. **活跃维护**：项目更新频繁，社区活跃

### 实际使用场景

  • **个人 AI 助手**：管理自己的 Telegram/Discord AI 机器人

  • **团队协作**：为团队配置多个平台的 AI 助手

  • **客户服务**：部署多平台的 AI 客服机器人

  • **开发测试**：快速测试和调试 AI 聊天功能

  • **数据分析**：监控 AI 使用情况和成本

### 总结

**Hermes Web UI** 是一个真正实用的开源项目，它让管理多平台 AI 聊天机器人变得前所未有的简单。无论你是个人开发者还是企业用户，都可以通过这个工具轻松管理你的 AI 助手。

**项目地址：** https://github.com/EKKOLearnAI/hermes-web-ui

**快速开始：**

 npm install -g hermes-web-ui  
 hermes-web-ui start

**访问地址：** http://localhost:8648

如果你正在使用 Hermes Agent，强烈建议你试试这个 Web 管理界面，它会让你的 AI 机器人管理体验提升一个档次！

\---

**💡 小贴士：** 项目完全开源，欢迎 Star、Fork 和贡献代码！如果你在使用过程中遇到问题，可以在 GitHub 上提交 Issue。

**🔗 相关链接：**

  • Hermes Agent 主项目：https://github.com/NousResearch/hermes-agent

  • Hermes Web UI：https://github.com/EKKOLearnAI/hermes-web-ui

  • npm 包：https://www.npmjs.com/package/hermes-web-ui

\---