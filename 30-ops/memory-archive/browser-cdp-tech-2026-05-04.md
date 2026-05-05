---
title: 浏览器/CDP 自动化技术细节
created: 2026-05-04
updated: 2026-05-04
layer: processed
type: entity
tags: [automation, browser]
---

# 浏览器/CDP 自动化技术细节（2026-05-04）

## 验证有效的方案

### Playwright stealth
- 成功绕过 FT中文网 Cloudflare + 微信公众号反爬
- 关键参数：`--disable-blink-features=AutomationControlled`

### 本机 Chrome 调试实例（最稳）
- 启动参数：`--remote-debugging-port=9222`
- 连接方式：native-devtools MCP 连接 9222
- 成功抓取 FT 中文网

### CDP Bridge
- cdp-bridge.py → 端口 9225
- 真实 Chrome 实例 → 端口 9222

## 已知问题
- Chrome CDP：根命令不帶 sessionId，session 命令必須帶
- Runtime.evaluate 返回 `msg.result.result.value`
- sessionId: null 报错 -32600
- SSH garbage.vicp.net：端口22可达但IP白名單拦截，kex_exchange_identification 阶段断连
