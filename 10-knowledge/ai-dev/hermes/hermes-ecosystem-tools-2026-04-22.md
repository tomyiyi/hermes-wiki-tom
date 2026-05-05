---
title: Hermes Ecosystem Tools — 生态工具全景
created: 2026-04-22
tags: [hermes-agent, ecosystem, monitoring, dashboard, wiki]
related: hermes-agent-core-concepts, hermes-ecosystem-2026-04-21
---

# Hermes 生态工具全景 (2026-04-22)

> 来源：微信公众号文章 + 5个项目 GitHub 深度阅读 + Hermes Agent 源码验证
> 验证状态：源码核实 ✅

---

## 0x00 生态结构总览

Hermes 生态已经形成清晰的层次：

| 层次 | 项目 | 解决的问题 |
|------|------|-----------|
| **地图** | Hermes Atlas | 信息散落 → 能导航 |
| **文档** | Hermes-Wiki | 内部复杂 → 能理解 |
| **观测** | hermes-hud | 状态黑盒 → 能看见 |
| **管理** | hermes-control-interface | 能跑难管 → 能控制 |
| **入口** | hermes-web-ui | 技术门槛 → 能上手 |

---

## 0x01 Hermes Atlas

**仓库：** ksimback/hermes-ecosystem  
**站点：** hermesatlas.com  
**Stars：** (增长中)

### 核心价值
把 80+ 散落的 Hermes 相关项目做成分类索引 + 可搜索的地图。

### 技术架构
```
Vercel 静态部署
├── index.html         # 单页地图应用
├── api/stars.js       # GitHub GraphQL API 实时拉星 + Redis 缓存
├── api/chat.js        # RAG pipeline (Gemma 4) 做生态问答
├── data/repos.json    # 84 个过滤后项目（单一数据源）
└── data/chunks.json   # 预计算嵌入 (7MB, 283 chunks)
```

### 对日常使用的价值
- 发现还没用但值得装的项目
- 生态全景一目了然
- 收藏：https://hermesatlas.com

---

## 0x02 Hermes-Wiki

**仓库：** cclank/Hermes-Wiki  
**Stars：** 201

### 核心价值
36 个概念页面，全部**逐行对照源码验证**，覆盖 Hermes 内部所有关键模块。

### 页面分类

**Agent 核心**
- `agent-loop-and-prompt-assembly` — Agent 循环 / 系统提示构建 / 执行指导
- `tool-registry-architecture` — 中央工具注册系统
- `model-tools-dispatch` — 工具编排与动态 schema 调整
- `toolsets-system` — 14+ 平台工具集
- `prompt-builder-architecture` — 模块化系统提示组装
- `auxiliary-client-architecture` — 辅助 LLM 客户端路由 + 自动降级

**记忆与会话**
- `memory-system-architecture` — 三层架构（MemoryStore/MemoryManager/MemoryProvider）
- `session-search-and-sessiondb` — FTS5 搜索 + LLM 摘要
- `context-compressor-architecture` — 自动上下文压缩 v3
- `skills-and-memory-interaction` — Skills 与 Memory 的决策树

**性能优化**
- `parallel-tool-execution` — 智能并发安全检测
- `prompt-caching-optimization` — 冻结快照，75% 成本节省

**安全**
- `security-defense-system` — 多层防御 + 危险命令审批（manual/smart/off）
- `interrupt-and-fault-tolerance` — 结构化错误分类 + Fallback 模型链

**平台**
- `messaging-gateway-architecture` — 16+ 平台统一网关
- `terminal-backends` — 6 种终端后端
- `mcp-and-plugins` — MCP 集成 + 插件钩子系统

### 对日常使用的价值
想深入理解 Hermes 内部机制的唯一可靠来源。和官方文档互补——Wiki 讲为什么和怎么运作，官方文档讲怎么用。

---

## 0x03 hermes-hud

**仓库：** joeynyc/hermes-hud  
**Stars：** ~615  
**语言：** Python 3.11+ / TUI

### 核心价值
读取 `~/.hermes/` 数据，实时监控 Agent 状态。长期跑 Hermes 必备。

### 读取的数据
```
~/.hermes/
├── sessions/           # 会话历史
├── memories/           # 记忆文件 (MEMORY.md, USER.md)
├── memory/
│   ├── memory.json     # MemoryStore 状态
│   ├── agent.json      # Agent 记忆
│   └── user.json       # 用户画像
├── skills/             # 已装技能
├── cron/
│   └── jobs.json       # 定时任务
├── .env                # API Key 存在性检查
├── config.yaml         # 容量阈值
└── state.db            # SQLite (FTS5 搜索数据)
```

### 9 个 Tab 功能
| Tab | 内容 |
|-----|------|
| 1-8 | 健康监控 / 记忆容量 / Sessions / Cron 等 |
| **9 — Patterns** | Prompt 模式分析：任务聚类 / 重复请求 / 高峰时段 / 常用工具链 |

### Patterns Tab 亮点
```python
# 任务聚类（关键词分类）
'git ops', 'debugging', 'code gen', 'refactor', 'research', 'config/ops', 'docs'

# 重复请求检测（3+ 次标记 ⚡）
Normalized first-message grouping

# 24 小时使用分布
sparkline 可视化

# 3 步工具链组合
Top sequences across all sessions
```

### 安装
```bash
pip install hermes-hud
hermes-hud
```

### 键盘快捷键
| 键 | 动作 |
|----|------|
| `1`-`9` | 切换 Tab |
| `j`/`k` | 上/下滚动 |
| `g`/`G` | 跳到顶/底 |
| `r` | 刷新数据 |
| `ctrl+p` | 命令面板（主题选择）|
| `q` | 退出 |

---

## 0x04 hermes-control-interface

**仓库：** xaspx/hermes-control-interface  
**Stars：** (增长中)  
**语言：** Vanilla JS + Vite · Node.js · Express · WebSocket · xterm.js

### 核心价值
自托管 Web 控制台，偏**运维管理**。密码门禁 behind a single password gate。

### 功能页面
**Home / Agents / Usage / Skills / Chat / Logs / Maintenance / Files**

### 与 hermes-web-ui 的区别
- hermes-web-ui：**通用入口**，解决"怎么顺手开始用"
- hermes-control-interface：**运维控制台**，解决"怎么长期把它管住"

### 亮点功能
1. **Multi-Agent Gateway** — 同时管理多个 Hermes profile，Systemd 服务管理
2. **RBAC v2** — 28 权限，12 分组，Admin/Viewer/Custom roles
3. **Token Analytics** — 按 model/platform/time range 拆解用量
4. **Web Terminal** — 浏览器里直接跑命令（xterm.js）
5. **文件浏览器** — 分屏编辑，root 限制 `~/.hermes` + 自定义路径

### 安装
```bash
npm install
npm run build
npm start
# 访问 http://localhost:10272
```

### 环境变量
```bash
HERMES_CONTROL_PASSWORD=xxx    # 必填
HERMES_CONTROL_SECRET=xxx      # 必填
PORT=10272
HERMES_CONTROL_HOME=~/.hermes
HERMES_CONTROL_ROOTS=["~/.hermes", "~/projects"]
```

---

## 0x05 hermes-web-ui

**仓库：** EKKOLearnAI/hermes-web-ui  
**Stars：** ~947（最热）  
**版本：** v0.3.5 (2026-04-18)  
**语言：** Vue 3 + TypeScript + Vite + Naive UI

### 核心价值
通用 Web 入口，让普通用户也能轻松使用 Hermes。

### 架构
```
Browser → BFF Server (Koa :8648) → Hermes Gateway (:8642)
              ↓
         Hermes CLI (sessions, logs, version)
              ↓
         ~/.hermes/config.yaml + auth.json
```

### 8 大功能

**AI Chat**
- SSE 实时流，支持 async run
- 多会话管理，按来源分组（Telegram/Discord/Slack 等）
- Markdown + 语法高亮 + 代码复制
- Tool call 卡片展开
- 文件上传
- 全局模型选择器（从 `auth.json` 发现）
- Per-session token 使用量显示

**Platform Channels（8 平台）**
| 平台 | 关键配置 |
|------|---------|
| Telegram | Bot token, mention control, reactions |
| Discord | Bot token, auto-thread, channel lists |
| Slack | Bot token, mention control |
| WhatsApp | Enable/disable, mention patterns |
| Matrix | Access token, homeserver, auto-thread |
| Feishu/Lark | App ID/Secret |
| WeChat | QR 码登录（浏览器）|
| WeCom | Bot ID/Secret |

**Usage Analytics**
- Token 拆解（input/output）
- Cache hit rate
- Model 使用分布
- 30 天日趋势图

**Scheduled Jobs**
- Cron 表达式预设
- 立即触发

**Web Terminal**
- node-pty + @xterm/xterm
- WebSocket 流式
- 窗口自适应

### 安装（npm）
```bash
npm install -g hermes-web-ui
hermes-web-ui start
# 打开 http://localhost:8648
```

### 安装（Docker）
```bash
docker compose up -d --build hermes-agent hermes-webui
# 访问 http://localhost:6060
```

### CLI 命令
```bash
hermes-web-ui start              # 守护进程模式
hermes-web-ui start --port 9000  # 自定义端口
hermes-web-ui stop               # 停止
hermes-web-ui restart            # 重启
hermes-web-ui status             # 状态
hermes-web-ui update             # 更新
```

---

## 0x06 源码验证 — Hermes Agent 数据结构

通过源码（`hermes_state.py`）验证了 Hermes 实际数据布局：

### `~/.hermes/` 结构
```
├── state.db              # SQLite (10.7MB) — WAL 模式，核心数据
│   ├── sessions 表        # 元数据：model/source/_tokens/cost/started_at
│   ├── messages 表       # 完整消息历史
│   └── messages_fts FTS5 # 全文搜索
├── sessions/             # 115 个会话文件（JSON/JSONL）
├── memories/             # MEMORY.md + USER.md（冻结快照）
├── memory/
│   ├── memory.json       # MemoryStore 状态
│   ├── agent.json        # Agent 记忆
│   └── user.json         # 用户画像
├── skills/               # 27 个技能
├── cron/
│   └── jobs.json         # 定时任务
├── logs/                 # gateway.log / agent.log / errors.log
├── cache/                # screenshots / images / documents
├── plugins/              # 插件目录
├── config.yaml           # 主配置
├── .env                  # API Keys
└── auth.json             # Provider 凭证
```

### SessionDB Schema（state.db）
```sql
sessions (
    id, source, user_id, model, model_config,
    system_prompt, parent_session_id,
    started_at, ended_at, end_reason,
    message_count, tool_call_count,
    input_tokens, output_tokens,
    cache_read_tokens, cache_write_tokens,  -- 75%成本节省的关键
    reasoning_tokens,
    billing_provider, billing_base_url, billing_mode,
    estimated_cost_usd, actual_cost_usd, cost_status, cost_source,
    pricing_version, title
)

messages (
    id, session_id, role, content,
    tool_call_id, tool_calls, tool_name,
    timestamp, token_count, finish_reason,
    reasoning, reasoning_details, codex_reasoning_items
)

messages_fts -- FTS5 虚拟表，自动触发器同步
```

### Hermes Agent Insights Engine
内置 `agent/insights.py`，直接查询 `state.db` 生成用量报告：
- Token 消耗 / 成本估算 / 工具使用模式 / 活动时间趋势
- 支持 `hermes insights` 命令

---

## 0x07 实用建议

### 日常监控 → hermes-hud
```bash
pip install hermes-hud && hermes-hud
```
- 长期跑 Hermes 必备
- Tab 9 的 Patterns 功能最有价值——发现重复任务链和常见工具组合

### 快速查 Hermes 状态 → 官方 dashboard
```bash
hermes dashboard
# http://127.0.0.1:9119
```
- 你已经在用 ✅

### 想给非技术用户 → hermes-web-ui
```bash
npm install -g hermes-web-ui && hermes-web-ui start
# http://localhost:8648
```
- Web UI 更友好，支持多平台 channel 配置

### 深度理解 Hermes → Hermes-Wiki
- https://github.com/cclank/Hermes-Wiki
- 36 个模块全覆盖，源码级准确

### 生态全景 → Hermes Atlas
- https://hermesatlas.com
- 80+ 项目分类索引，发现新工具

### 多 Agent 运维管理 → hermes-control-interface
```bash
npm install && npm run build && npm start
# http://localhost:10272
```
- 需要密码，有权限控制，适合团队或正式环境
