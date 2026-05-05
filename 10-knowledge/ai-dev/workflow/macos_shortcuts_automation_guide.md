---
title: macos_shortcuts_automation_guide
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
  - Agent
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# macOS Shortcuts CLI 自动化与 AI Agent 集成全指南

macOS 提供了原生的 `shortcuts` 命令行工具，允许开发者通过终端调用“快捷指令”应用中的脚本。结合 Python 或 AI Agent，可以实现对 macOS 系统级功能（如发短信、控制智能家居、处理文件、获取系统状态等）的深度且极其稳定的控制。

## 1. 为什么选择 Shortcuts CLI 而不是 JXA / AppleScript？
* **极度稳定**：苹果官方原生支持，不会因为 macOS 升级导致底层 API 变更而跑不通。
* **安全沙盒**：AI Agent 无法自己瞎写危险的底层脚本，它只能调用人类（主理人）预先在图形界面捏好的安全工作流。
* **所见即所得**：主理人可以在 Mac 上用拖拽的方式快速创建复杂的自动化逻辑，Agent 只需要负责触发和传参。

## 2. CLI 基础操作

* **列出所有快捷指令**：`shortcuts list`
* **无输入运行**：`shortcuts run "快捷指令名称"`
* **通过标准输入（stdin）传参**：`echo "测试文本" | shortcuts run "朗读文本"`
* **传递结构化数据（JSON 传多参数）**：这是与代码集成的核心技巧。通过 `echo '{"name":"Alice","action":"test"}' | shortcuts run "ProcessData"`，并在快捷指令内部使用“从输入中获取字典”操作来解析变量。
* **保存输出文件**：`shortcuts run "生成报告" -o /path/to/output.pdf`

## 3. Python 自动化集成示例

```python
import subprocess
import json

def run_macos_shortcut(shortcut_name: str, input_data: dict = None) -> str:
    """运行 macOS 快捷指令并返回结果"""
    cmd = ["shortcuts", "run", shortcut_name]
    
    try:
        if input_data:
            # 将字典转换为 JSON 字符串并通过 stdin 传入
            json_str = json.dumps(input_data)
            result = subprocess.run(
                cmd, 
                input=json_str.encode('utf-8'),
                capture_output=True, 
                check=True
            )
        else:
            result = subprocess.run(cmd, capture_output=True, check=True)
            
        return result.stdout.decode('utf-8').strip()
        
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr.decode('utf-8')}"
```

## 4. AI Agent 集成方案 (NewAge 架构建议)

在 NewAge 中，我们可以开发一个 `mac_shortcuts_controller.py` 技能：
1. **能力发现**：技能初始化时，自动执行 `shortcuts list`，将 Mac 上所有的快捷指令名称注册到 Agent 的内存中。
2. **动态传参**：大模型根据用户的自然语言（如：“把这份早报发给老板”），自动构造 JSON 参数 `{"target": "老板", "content": "早报内容..."}`。
3. **安全触发**：底层 Python 脚本通过 `subprocess` 调用该快捷指令，并将 JSON 喂给它。

**快捷指令端的配合（主理人需要做的）**：
1. 在快捷指令 App 中新建一个指令。
2. 第一步添加：**接收输入**。
3. 第二步添加：**从输入中获取字典**。
4. 第三步添加：**获取字典值**（比如获取键 `content`）。
5. 往下走正常的业务逻辑（比如发送 iMessage、存入备忘录等）。

## 5. 避坑指南与局限性 (Critical)

1. **绝对禁止 UI 弹窗**：在给 Agent 用的快捷指令里，**必须关闭“运行时显示”**，且绝对不能有“要求输入”、“从菜单中选取”等操作。否则会导致终端 CLI 进程永久挂死 (Hang)。
2. **首次权限弹窗**：如果快捷指令涉及到隐私（如发短信、读相册），第一次通过 CLI 运行会弹权限框，必须由人类手动点一次允许，之后 Agent 才能无人值守运行。
3. **锁屏失效**：大部分涉及到 GUI 或隐私数据的快捷指令，在 Mac 锁屏或睡眠状态下会执行失败。
4. **返回值类型**：CLI 只能接收纯文本标准输出。如果快捷指令返回的是图片或复杂对象，必须在指令内部转成 Base64 文本，或者直接让指令把文件保存到硬盘特定目录，Agent 再去读取。