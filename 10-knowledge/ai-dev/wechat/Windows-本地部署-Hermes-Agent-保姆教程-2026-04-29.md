---
title: wechat Windows 本地部署 Hermes Agent 保姆教程 2026 04 29
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: query
tags: [AI-Agent]
---

﻿---
title: Windows 本地部署 Hermes Agent 保姆教程（小白避坑版）
created: 2026-04-29
updated: 2026-04-29
layer: processed
type: summary
tags: [wechat, hermes, Ubuntu, Linux, Telegram, Windows]
source: https://mp.weixin.qq.com/s?src=11&timestamp=1777424653&ver=6689&signature=AXtwgXQIcd8tcLKHbCxhp3L0ZYnJ2nPVMlrl6hYsU7sz3ooUwt62l1WrXi-YpwxIWEydt-WchtpcXCGETu1bhbvozIG4*Q1xhi43sDiaoxq9oeHIdR914hMpzm9*VmnM&new=1
account: 胡说黑科技
pubTime: 2026年4月29日 06:01
---

## 摘要

前言最近看到不少博主分享 Hermes Agent 的安装教程，但大多数都是针对 Linux 和 macOS 系统，专门讲 Windows 的教程少之又少，于是我自己动手，在 Windows 上成功安装并运行了 Hermes Agent，体验下来效果相当不错过程中也踩了一些坑，摸索出了对应的解决方法，小白一看就会，在这里一并分享出来，希望对同样使用 Windows 的朋友有所帮助废话不多说，直接上教程！ 胡说黑科技交流群一、在 Windows 上安装并配置 WSL21.安装 WSL以 管理员身份 打开 PowerShell，并执行以下命令：shellwsl --install执行完毕后，重启你...

---

## 核心要点

（待整理）

---

## 原文（来源：胡说黑科技）

前言最近看到不少博主分享 Hermes Agent 的安装教程，但大多数都是针对 Linux 和 macOS 系统，专门讲 Windows 的教程少之又少，于是我自己动手，在 Windows 上成功安装并运行了 Hermes Agent，体验下来效果相当不错过程中也踩了一些坑，摸索出了对应的解决方法，小白一看就会，在这里一并分享出来，希望对同样使用 Windows 的朋友有所帮助废话不多说，直接上教程！ 胡说黑科技交流群一、在 Windows 上安装并配置 WSL21.安装 WSL以 管理员身份 打开 PowerShell，并执行以下命令：shellwsl --install执行完毕后，重启你的电脑2.设置 WSL2 为默认版本查看在线商店可下载的 Linux 发行版列表，再次进入 PowerShell ，并执行以下命令：shellwsl.exe --list --online效果如图：我选择的 Ubuntu-20.04，执行以下命令：shellwsl.exe --install Ubuntu-20.04它好像自动给我下了Ubuntu 22.04 LTS（最新 LTS 版本）安装完毕，可以查询当前Ubuntu的型号，查询代码和效果如下：shellwsl.exe --list --verbose我这里有两个，我需要切换一下 Ubuntu 22.04，命令如下：shellwsl --set-default Ubuntu-20.043.安装 Linux 发行版（推荐 Ubuntu）1打开 Microsoft Store (微软应用商店)2搜索 “Ubuntu”3选择 “Ubuntu 20.04 LTS” (或最新 LTS 版本)，点击 “获取” 进行安装4.初始化 Ubuntu1安装完成后，在开始菜单中启动 “Ubuntu”2首次启动会要求你创建一个 Linux 用户名和密码（这与你的 Windows 账户无关，请必须牢记）3初始化完成后，你就拥有了一个功能完备的 Linux 终端补充必看：安装完毕之后，会弹出一个适用于Linux的Windows子系统设置💡我们需要修改一下网络设置，默认为Nat模式，我们千万不要选那个模式，你选了那个模式之后，它的各种网络请求都不会跟你电脑配置相同，导致后续安装出问题，大家一定要选择Mirrored这个模式（非常重要，我没改之前卡了好久）💡注：选择Mirrored这个模式之后，它就会跟随你电脑的网络，比如说我电脑这里挂代理，因为我们下载一些从GitHub上拉项目，安装都需要网络代理支持的，如果说你选择NAT的话，就没办法下载成功💡关闭防火墙，启用localhost转发打开，自动代理开启，设置完重启电脑我们的操作环境切换到了 WSL2 的 Ubuntu 终端1.执行官方一键安装脚本在 Ubuntu 终端中粘贴并运行(Linux / macOS同理)：bashcurl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash这个脚本会自动完成以下工作：▸安装 uv (超快的 Python 包安装器和虚拟环境管理器)▸安装 Python 3.11+▸克隆 Hermes Agent 仓库▸创建并激活虚拟环境▸安装所有依赖▸将 hermes 命令添加到你的 PATH2.重载 Shell 并验证安装安装完成后，为了让 hermes 命令生效，需要重载你的 Shell 配置：bash# 对于 Bash 用户source ~/.bashrc# 对于 Zsh 用户（如果你已切换）source ~/.zshrc验证是否安装成功：bashhermes --version应该能看到类似 hermes x.x.x 的输出，如图：3.配置模型提供商运行设置向导，连接你的大模型 API，输入下面命令，启动配置向导：bashhermes setup来到这个页面，选择 Quick setup💡Quick setup（推荐）— 只配置核心的：AI provider、模型、和消息平台💡Full setup — 配置所有选项，更细致但步骤更多在交互式界面中：💡选择你的模型提供商（如 OpenAI, Anthropic, OpenRouter, 或国内便宜好用的大模型）💡输入对应的 API Key，有人会问老师我没有怎么办？下面我会讲💡选择一个默认模型（如 gpt-4o, claude-3-5） 我选择一个便宜的minimax-m2.5获取 API Key 的简单方法（以 OpenRouter 为例）：▸注册账号去▸充值一点钱（几美元就够用很久）▸在 dashboard 里复制你的 API Key（一串很长的字符）4.配置聊天软件（以 Telegram 为例）来到这个页面我们选择 Set up messaging now▸Set up messaging now（推荐）— 现在就绑定平台，装完即可使用▸Skip — 跳过，之后用 hermes setup gateway 命令再配置我们选择 Telegram，下面番外篇要连配置完成后，你可以通过 hermes 命令直接与 Agent 对话，测试其基本功能避坑提示：💡网络问题：如果 curl 命令卡住或失败，很可能是网络问题。请确保你的 WSL2 能正常访问 GitHub。必要时可配置 Git 代理💡权限问题：不要在 WSL2 中使用 sudo 来运行 hermes 命令，这可能导致权限混乱。始终以普通用户身份运行三、小白常见问题 & 建议1.安装是卡住了怎么办💡耐心等待，第一次会下载很多东西2.我没有API Key怎么办💡上面有获取 API Key 的简单方法3.我想24小时运行怎么办💡荐买个便宜 VPS（阿里云、腾讯云 5-10 美元/月），在 VPS 上安装，操作同理4.我想把我的OpenClaw 迁移过来怎么怎么办💡直接用 hermes claw migrate 命令即可常用命令（记住这几个行）▸hermes （进入交互式聊天）▸hermes setup （一站式配置向导）▸hermes model （切换模型）▸hermes tools （配置可用工具）▸hermes config set KEY 值 （设置单个配置）▸hermes claw migrate （如果你以前用 OpenClaw，可以一键迁移数据）四、番外篇连接聊天软件以 Telegram 为例（超级简单）：1打开 Telegram，搜索2发送 /newbot3给机器人起名字和用户名（比如 星辰机器人小助理）4BotFather 会给你一个 Bot Token（一长串英文数字），复制下来然后在终端输入：bashhermes gateway或者用配置命令设置 Telegram Token，我用的第二种自动帮我配置好了具体配置可以输入：bashhermes config set TELEGRAM_BOT_TOKEN 你的token在这里启动网关：bashhermes gateway telegram然后在 Telegram 里搜索你的机器人，可以开始聊天了如果你的电脑/VPS 一直开着，它会 24小时在线结语大家有什么问题可以评论区留言，教程编写不易，如果此教程对你有帮助麻烦给我一个小小的关注WSL子系统安装在C盘会很占内存，可以做迁移，可以看这位大佬的教程WSL 安装官方文档：https://learn.microsoft.com/zh-cn/windows/wsl/install官方 GitHub：https://github.com/NousResearch/hermes-agentHermes 学习官方文档：https://hermes-agent.nousresearch.com/