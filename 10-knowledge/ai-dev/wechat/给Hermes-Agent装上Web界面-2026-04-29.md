---
title: wechat 给Hermes Agent装上Web界面 2026 04 29
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: comparison
tags: [AI-Agent]
---

﻿---
title: 给Hermes Agent装上Web界面
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: summary
tags: [wechat, API, open, webui, docker, SERVER]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777424653&ver=6689&signature=7cuX*uUEBYD7R91byl70YwP-51deh9H5k5JmiHO-9Mc3XG8wzTvyPumjsikyDAXHaM1c4SmwLAe5Wdj7eOvMuqmMxwtqWPXqw9Z1-neCu*ulQcDQPKBnseYsYnr4XiZP&new=1
account: 硅基起源
pubTime: 2026年4月28日 19:19
---

## 摘要

导语 Hermes Agent是Nous Research开源的AI智能体框架，原生通过命令行交互。但如果你想在浏览器里使用它，或者让团队成员通过网页访问，就需要给它装上Web界面。本文提供两种经过验证的部署方案，任选一个即可。 前置条件 在开始之前，请确认以下基础环境已经就绪： 操作系统：Linux、macOS或WSL2。原生Windows不支持。Git：用于克隆仓库，执行git --version确认已安装。Hermes Agent：已完成基础安装，CLI可以正常对话。Docker：方案一需要Docker运行Open WebUI。 如果你还没有安装Hermes Agent，先用官方一键脚本...

---

## 核心要点

（待整理）

---

## 原文（来源：硅基起源）

导语 Hermes Agent是Nous Research开源的AI智能体框架，原生通过命令行交互。但如果你想在浏览器里使用它，或者让团队成员通过网页访问，就需要给它装上Web界面。本文提供两种经过验证的部署方案，任选一个即可。 前置条件 在开始之前，请确认以下基础环境已经就绪： 操作系统：Linux、macOS或WSL2。原生Windows不支持。Git：用于克隆仓库，执行git --version确认已安装。Hermes Agent：已完成基础安装，CLI可以正常对话。Docker：方案一需要Docker运行Open WebUI。 如果你还没有安装Hermes Agent，先用官方一键脚本完成安装： # 一键安装（自动处理Python、Node.js等依赖） curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash 方案一：Open WebUI + Hermes API Server（官方推荐） 这是官方文档推荐的方案。Hermes Agent内置了一个兼容OpenAI格式的API Server，Open WebUI作为前端连接它，就像在连接一个OpenAI API一样简单。 第一步：启用API Server 编辑Hermes的配置文件~/.hermes/.env，添加以下两行： API_SERVER_ENABLED=true API_SERVER_KEY=your-secret-key API_SERVER_KEY是你自己设定的密钥，后续Open WebUI连接时需要用到，请妥善保管。 第二步：启动Hermes Gateway 在终端执行以下命令启动Gateway服务： hermes gateway 启动成功后，终端会显示类似下面的信息： [API Server] API server listening on http://127.0.0.1:8642 这表示API Server已经在8642端口运行。保持这个终端窗口开启，不要关闭。 第三步：Docker部署Open WebUI 在另一个终端窗口执行以下Docker命令，拉取并启动Open WebUI： docker run -d -p 3000:8080 \ -e OPENAI_API_BASE_URL=http://host.docker.internal:8642/v1 \ -e OPENAI_API_KEY=your-secret-key \ --add-host=host.docker.internal:host-gateway \ -v open-webui:/app/backend/data \ --name open-webui \ --restart always \ ghcr.io/open-webui/open-webui:main 命令解释： -p 3000:8080：将容器8080端口映射到本机3000端口。OPENAI_API_BASE_URL：指向Hermes的API地址，末尾必须带/v1。OPENAI_API_KEY：必须与你在Hermes中设置的API_SERVER_KEY完全一致。-v open-webui:/app/backend/data：数据持久化，避免重启后配置丢失。 第四步：访问Web界面 打开浏览器，访问http://localhost:3000。首次访问需要注册一个管理员账号，注册完成后即可开始使用。 在聊天界面的模型下拉框中，你会看到你的Hermes Agent以默认名称hermes-agent出现。选择它，发送一条消息测试。 验证成功标准 发送"Hello"后，如果收到Agent的回复，并且终端窗口中显示了工具调用日志（如搜索、文件操作等），说明WebUI已正确连接。 方案二：Docker Compose持久化部署 如果你希望部署更稳定、可长期运行，推荐使用Docker Compose方式。 创建docker-compose.yml 在项目目录下创建docker-compose.yml文件，内容如下： services: open-webui: image: ghcr.io/open-webui/open-webui:main ports: - "3000:8080" volumes: - open-webui:/app/backend/data environment: - OPENAI_API_BASE_URL=http://host.docker.internal:8642/v1 - OPENAI_API_KEY=your-secret-key extra_hosts: - "host.docker.internal:host-gateway" restart: always volumes: open-webui: 然后执行启动命令： docker compose up -d -d参数表示后台运行。服务会自动在开机时启动，数据保存在Docker volume中。 配置AI模型连接 WebUI搭建完成后，还需要确保Hermes Agent能正确调用LLM。运行以下命令配置模型： hermes model 按照交互提示依次选择： Provider：选择你的API提供商（如OpenRouter、Anthropic、阿里云等）。API Key：粘贴从对应平台获取的密钥。Model：选择具体的模型名称（如gpt-4o、claude-sonnet-4等）。 关键提醒 配置完成后必须重启Hermes Gateway才能生效。按Ctrl+C停止当前gateway进程，然后重新执行hermes gateway启动。 两种方案对比 维度 方案一：docker run 方案二：docker compose 部署速度 一条命令，即刻启动 需先写YAML文件 持久化 有volume，但管理较松散 结构清晰，易于维护 重启策略 需手动设置--restart 内置restart: always 适用场景 快速体验、本地测试 长期运行、生产部署 常见问题排查 问题一：Open WebUI提示连接失败 检查清单： Hermes Gateway是否已启动？终端应显示API Server监听在8642端口。OPENAI_API_KEY是否与API_SERVER_KEY完全一致？包括大小写。如果是Linux系统，尝试将host.docker.internal替换为宿主机的实际IP地址。 问题二：WebUI能打开但发送消息无响应 这通常是模型配置问题。在终端执行： hermes chat -q "Hello" 如果CLI也无法回复，说明模型Key或Provider配置有误，先修复CLI端的问题。 问题三：需要局域网或公网访问 默认配置仅允许本机访问。如需局域网访问： 修改Hermes配置：API_SERVER_HOST=0.0.0.0修改Docker端口映射：-p 0.0.0.0:3000:8080确保防火墙放行3000和8642端口。 总结 给Hermes Agent安装Web界面，核心思路是启动它的API Server，再用Open WebUI作为前端连接。整个过程可以归纳为三步： 启API：在~/.hermes/.env中打开API_SERVER_ENABLED。跑服务：执行hermes gateway启动后端。装界面：Docker启动Open WebUI并指向Hermes的API地址。 配置完成后，你就能在浏览器里享受完整的聊天体验，包括对话历史管理、多用户支持、文件上传等高级功能，同时底层依然调用Hermes Agent强大的工具链。 下一步 你可以为团队配置多用户访问，或者将Open WebUI部署到云服务器实现远程访问。Hermes Agent的Gateway还支持连接Telegram、Discord、Slack等平台，实现真正的全渠道AI助手。 作者：老金｜专注企业AI架构，帮你省钱避坑