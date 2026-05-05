---
title: "[conversations] conversations 沉淀时自动判断确定性标签"
created: 2026-04-11
updated: 2026-04-11
layer: backlog
type: action
status: completed
priority: high
owner: hermes
execution_target: "2026-04-12"
tags: [backlog, conversations, certainty, automation]
sources: [conversations/conversations-archive.md]
---

# [Backlog] conversations 确定性自动判断

## 做什么
在 `save_conversation.py` 执行时，自动根据对话内容判断 certainty 标签（confirmed / inferred / speculative），写入 frontmatter 不需要人工标注。

## 什么时候做
2026-04-12（与 ingest AI 推荐同天）

## 怎么做
在 `save_conversation.py` 里加一个简单 heuristic：

```python
def auto_certainty(topic: str, insights: list[str]) -> str:
    # confirmed: 有明确事实/数字/代码/配置
    confirmed_signals = ['=', ':', '//', 'ip:', 'url:', 'http', 'def ', 'import ']
    # speculative: 有'可能'/'也许'/'如果'/'假设'
    speculative_signals = ['可能', '也许', '如果', '假设', '大概', '推测']

    has_confirmed = any(s in ' '.join(insights) for s in confirmed_signals)
    has_speculative = any(s in ' '.join(insights) for s in speculative_signals)

    if has_confirmed and not has_speculative:
        return 'confirmed'
    elif has_speculative:
        return 'speculative'
    return 'inferred'
```

## 反馈要求
完成后在当前文件记录：
- 前 5 次自动判断是否准确（需要你反馈）
- 是否需要加新的信号词
- 是否有误判案例

## 备注
确定性标签是为了后续查 wiki 时，知道哪些结论可以直接用、哪些要再验证。
