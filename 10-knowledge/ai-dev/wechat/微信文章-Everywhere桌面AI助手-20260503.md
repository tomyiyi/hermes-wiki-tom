---
title: "Everywhere：一个真正"懂你屏幕"的桌面 AI 神器"
created: 2026-05-03
updated: 2026-05-03
layer: processed
type: summary
tags: [wechat, AI工具, 桌面助手, 开源]
sources: ["https://mp.weixin.qq.com/s/ghIslC3c-lx7BEZ7Od9eEA"]
derived_from: []
solves_what:
  - 解决"AI使用时的窗口切换成本"问题——按快捷键直接在当前窗口旁唤出AI，已读取屏幕内容
  - 目标用户：程序员（命令行操作）、产品经理（阅读长文）、看盘用户（行情查询）
  - 核心价值：无需手动搬运上下文，AI直接感知当前屏幕
---

## 核心要点

Everywhere 是一款桌面 AI 助手，核心能力：**按快捷键唤出，AI 直接读懂你当前屏幕的内容**。无需切换窗口、无需手动粘贴上下文。

底层技术：
- 多模态（屏幕截图输入模型）
- **无障碍 API + UI 自动化**（从 OS UI 层提取结构化数据，知道你在哪个应用、哪个界面元素）
- 基于 .NET + Avalonia 跨平台框架开发

支持的模型：OpenAI、Claude、Gemini、DeepSeek、Kimi、MiniMax、SiliconCloud、Ollama 本地部署、MCP

已支持能力：网页浏览、子代理派发、本地文件系统、终端脚本执行、MCP 工具协议

## 真实使用场景

| 场景 | 说明 |
|------|------|
| 拔除报错 | 运行出错，直接在错误旁唤出问"这个错什么意思" |
| 阅读长文 | 问"给我总结一下"，生成当前页面内容的摘要 |
| 外语翻译 | 选中生词，直接在屏幕旁出翻译结果 |
| 命令行操作 | 自然语言执行 Shell 命令（如"清理8080端口进程"） |
| 查看行情 | 不离开图表，直接查询财报和资讯 |

## 技术架构

- 开发框架：.NET + Avalonia（跨平台 UI）
- 开发者：国内独立开发者 DearVa，GitHub 项目
- 公司：Sylinko Inc.
- 支持平台：Windows（exe 安装向导 / zip 便携包）、macOS（Apple Silicon / Intel 两种包）、Linux 开发中
- 官网下载：https://everywhere.sylinko.com/download

## 评价

**优点**：专注解决切换成本问题、不锁死模型、可本地部署、有 MCP 支持

**不足**：项目早期，记忆系统/语音交互未上线，部分软件无障碍 API 支持不完善

> GitHub：https://github.com/DearVa/Everywhere
