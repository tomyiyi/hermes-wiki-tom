---
title: "让AI像人一样浏览网页！web-access Skills彻底解决数据抓取难题"
created: 2026-04-27
updated: 2026-04-27
layer: processed
type: summary
tags: [AI-Agent, web-access, CDP, 浏览器自动化, 反爬虫]
source: https://mp.weixin.qq.com/s/RTir4iDyiIRvdyIMwbxgZQ
author: Muru AI / 木汝科技
---

## 核心要点

web-access 是一个让 AI 能像真人一样操作浏览器的技能。通过 CDP（Chrome DevTools Protocol）直连用户 Chrome，绕过反爬机制，携带登录态操作需要认证的页面。

**安装：** `clawhub install web-access`

---

## 功能一览

| 功能 | 说明 |
|------|------|
| 🔍 搜索 | web_search 搜关键词、摘要 |
| 📄 抓取 | web_fetch 定向提取页面内容 |
| 🌐 浏览器CDP | 直接控制Chrome，绕过反爬机制 |
| 🔑 登录态 | 复用用户Chrome的登录状态 |

---

## 核心能力

### 1. 绕过反爬
传统抓取方案遇到反爬就歇菜。web-access 通过 CDP 直连浏览器，模拟真实用户操作，网站很难判断这是AI还是真人在看页面。

### 2. 登录态复用
Chrome 里已经登录的网站，AI 可以直接用。不需要单独配置账号密码，也不需要维护 cookie。CDP 启动的瞬间登录状态就被继承了。

### 3. 像人一样操作
点击、滚动、填表、截图——都支持。不是构造冷冰冰的 API 请求，而是模拟真实用户在页面上的行为。

---

## 和 agent-browser 的区别

| 对比 | web-access | agent-browser |
|------|------------|---------------|
| 登录态 | 复用用户Chrome | 需要单独登录 |
| 反爬 | 有绕过机制 | 无 |
| 适用场景 | 复杂网站、反爬站点 | 简单自动化 |

简单说：**web-access 能干的，agent-browser 干不了。**

---

## 适用场景

1. **公众号草稿箱文章** — CDP 直接连 Chrome，登录状态在线，进去 → 找到文章 → 复制出来
2. **小红书数据** — 小红书反爬极严，CDP 模拟浏览器访问，滚动加载、点击展开
3. **电商价格监控** — 并行 CDP，一次打开10个页面，一次性拿到所有价格数据
4. **批量填表** — CDP 自动填表 → 自动点提交 → 下一个

---

## 前置条件

- Node.js 22+
- Chrome 远程调试（`chrome://inspect` → 勾 Allow remote debugging）

---

## 设计理念

- 先了解页面结构，再决定下一步怎么搞
- 不盲目重试，一条路走不通就换条路
- 遇到弹窗登录墙——先判断是不是真挡住我了

---

## 总结

web-access 解决的核心问题：**让 AI 能像人一样上网。**

当需要 AI 处理网页相关任务时，它能：
- 绕过反爬机制
- 携带登录态操作需要认证的页面
- 模拟真实用户的交互行为
