---
title: MiniMax React Browser Agent
created: 2026-04-27
updated: 2026-04-27
layer: action
type: entity
tags: [AI-Agent, AI-Agent]
---

# MiniMax React Browser Agent

## What
MiniMax (M2.7) + Playwright + LangGraph ReAct Agent，实现浏览器自动化。

## Why
browser-use 等框架对 LLM output format 有硬性要求，MiniMax 不兼容。自建方案绕开框架限制，MiniMax 通过 function calling 控制浏览器。

## Stack
- **LLM**: MiniMax-M2.7（OpenAI-compatible endpoint，`api.minimaxi.com/v1`）
- **Browser**: Playwright (chromium, headless)
- **Agent**: LangGraph ReAct 循环（bind_tools → tool call → 状态更新）

## Key Discovery
- Base URL 是 `api.minimaxi.com` 不是 `api.minimax.io`
- API Key 和 Hermes 用的 token plan 是同一个
- MiniMax 返回的 tool call 用 `args` 不是标准 OpenAI 的 `arguments`
  - 这导致初始实现 KeyError，直到打印 response 发现差异
- browser-use 不兼容 MiniMax 的根本原因：browser-use 期望 LLM 返回自定义 JSON schema（`AgentOutput`），MiniMax 虽支持 function calling 但该特定输出格式无法满足

## Trial & Error Timeline
1. 先试 browser-use → API Key 在 OpenAI endpoint 报 401（base URL 错误）
2. 换 `api.minimax.io` → 认证通，但 tool call 失败（"Result failed items"）
3. 发现 mmx CLI 存的是 `api.minimaxi.com` → 认证通过
4. 测 MiniMax function calling → 确认支持，但 key 是 `args` 不是 `arguments`
5. 自建 LangGraph ReAct Agent → 一次跑通

## Available Tools
| Tool | Description |
|------|-------------|
| `navigate(url)` | 打开 URL |
| `click(selector)` | 点击 CSS 元素 |
| `fill_input(selector, text)` | 填写输入框 |
| `press_key(key)` | 按键盘键 |
| `get_page_info()` | 获取页面标题+内容 |
| `take_screenshot()` | 截图保存到 /tmp/browser_screenshot.png |

## Install
```bash
# Python 3.11+
/opt/homebrew/bin/python3.11 -m pip install playwright langchain-openai langgraph
playwright install chromium
```

## Run
```bash
/opt/homebrew/bin/python3.11 ~/Desktop/hermes-wiki/30-ops/skills/minimax-react-browser-agent/agent.py \
  "Go to https://example.com and tell me the page title"
```

## Test Cases
| Task | Steps | Result |
|------|-------|--------|
| example.com 读取标题 | 2步（导航+获取信息） | ✅ |
| httpbin.org 表单提交 | 3步（填写+提交+读取结果） | ✅ |
| httpbin.org/html 读作者 | 2步 | ✅ |
| 截图 | 2步 | ✅ |

## Limitations
- 小红书等强反爬平台会拦截（需要登录墙/验证码）
- 复杂 JS 网站可能有延迟，需要加 asyncio.sleep
- 无代理池，多IP需求场景不适用

## File
- `agent.py` — 完整 Agent 实现（152行）
