#!/usr/bin/env python3
"""
MiniMax + Playwright + LangGraph ReAct Agent
Uses MiniMax M2.7 via OpenAI-compatible API (api.minimaxi.com/v1)
"""
import os
import asyncio
from typing import Literal
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from playwright.async_api import async_playwright

BASE_URL = "https://api.minimaxi.com/v1"
API_KEY = os.environ.get(
    "MINIMAX_API_KEY",
    "sk-cp-sYqPlblJmnjUAHmHTlYeAQ9NogdfW7dwxuirElv8jB4lNUKpsHrT5_k6s5L3r8-jxhsE1qbPT2ZeItFiDyWQCDmukE_DkrrN3SvG1UwMl0fxxNmIMNbAEoA"
)

llm = ChatOpenAI(
    model="MiniMax-M2.7",
    base_url=BASE_URL,
    api_key=API_KEY,
    temperature=0,
)

TOOL_DEFINITIONS = [
    {"type": "function", "function": {
        "name": "navigate",
        "description": "Navigate to a URL",
        "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}
    }},
    {"type": "function", "function": {
        "name": "click",
        "description": "Click an element by CSS selector",
        "parameters": {"type": "object", "properties": {"selector": {"type": "string"}}, "required": ["selector"]}
    }},
    {"type": "function", "function": {
        "name": "fill_input",
        "description": "Fill a text input",
        "parameters": {"type": "object", "properties": {"selector": {"type": "string"}, "text": {"type": "string"}}, "required": ["selector", "text"]}
    }},
    {"type": "function", "function": {
        "name": "press_key",
        "description": "Press keyboard key (e.g. 'Enter', 'Escape', 'ArrowDown')",
        "parameters": {"type": "object", "properties": {"key": {"type": "string"}}, "required": ["key"]}
    }},
    {"type": "function", "function": {
        "name": "get_page_info",
        "description": "Get page title and main text content",
        "parameters": {"type": "object", "properties": {}}
    }},
    {"type": "function", "function": {
        "name": "take_screenshot",
        "description": "Take a screenshot and save to /tmp/browser_screenshot.png",
        "parameters": {"type": "object", "properties": {}}
    }},
]

SYSTEM = """You are a browser automation agent. You control a headless Chromium browser via tools.
Available tools:
- navigate(url): Go to a URL
- click(selector): Click an element by CSS selector
- fill_input(selector, text): Fill a text input field
- press_key(key): Press a keyboard key
- get_page_info(): Get page title and visible text content
- take_screenshot(): Take a screenshot

Be efficient. Minimize steps. State your answer clearly when done."""

class State(dict):
    messages: list

# ─── Shared browser (single page per session) ───
_browser = None
_page = None
_pw_ctx = None

async def get_page():
    global _browser, _page, _pw_ctx
    if _browser is None:
        _pw_ctx = async_playwright()
        pw = await _pw_ctx.__aenter__()
        _browser = await pw.chromium.launch(headless=True)
        _page = await _browser.new_page()
    return _page

async def close_browser():
    global _browser, _page, _pw_ctx
    if _page:
        await _page.close()
        _page = None
    if _browser:
        await _browser.close()
        _browser = None
    if _pw_ctx:
        await _pw_ctx.__aexit__(None, None, None)
        _pw_ctx = None

async def run_tool(name: str, args: dict) -> str:
    page = await get_page()
    try:
        if name == "navigate":
            await page.goto(args["url"], wait_until="domcontentloaded", timeout=15000)
            await asyncio.sleep(1)
            return f"✅ Navigated to {args['url']}"

        elif name == "click":
            await page.click(args["selector"], timeout=5000)
            await asyncio.sleep(1)
            return f"✅ Clicked {args['selector']}"

        elif name == "fill_input":
            await page.fill(args["selector"], args["text"])
            await asyncio.sleep(0.5)
            return f"✅ Filled '{args['text']}' into {args['selector']}"

        elif name == "press_key":
            await page.keyboard.press(args["key"])
            await asyncio.sleep(0.3)
            return f"✅ Pressed key: {args['key']}"

        elif name == "get_page_info":
            title = await page.title()
            content = await page.evaluate(
                "() => document.body ? document.body.innerText.slice(0, 1200) : ''"
            )
            return f"Title: {title}\n\nContent:\n{content[:800]}"

        elif name == "take_screenshot":
            await page.screenshot(path="/tmp/browser_screenshot.png")
            return "📸 Screenshot saved to /tmp/browser_screenshot.png"

        return f"Unknown tool: {name}"
    except Exception as e:
        return f"❌ Error: {e}"

# ─── LangGraph ReAct ───
async def agent_node(state: State) -> State:
    messages = state["messages"]
    ai_msg = llm.bind_tools(TOOL_DEFINITIONS).invoke(messages)
    messages = messages + [ai_msg]

    if not ai_msg.tool_calls:
        return {"messages": messages}

    for tc in ai_msg.tool_calls:
        result = await run_tool(tc["name"], tc["args"])
        messages.append(ToolMessage(content=result, tool_call_id=tc["id"]))

    return {"messages": messages}

def should_continue(state: State) -> Literal["agent", "__end__"]:
    last = state["messages"][-1]
    if isinstance(last, AIMessage) and not last.tool_calls:
        return "__end__"
    return "agent"

# ─── Run ───
async def run(task: str, max_steps: int = 20):
    graph = StateGraph(State)
    graph.add_node("agent", agent_node)
    graph.set_entry_point("agent")
    graph.add_conditional_edges("agent", should_continue, {"agent": "agent", "__end__": END})
    compiled = graph.compile()

    print(f"\n🎯 Task: {task}\n")
    print("=" * 60)

    result = await compiled.ainvoke(
        {"messages": [SystemMessage(content=SYSTEM), HumanMessage(content=task)]},
        {"recursion_limit": max_steps}
    )

    print("=" * 60)
    print("\n📋 Response:\n")
    final = result["messages"][-1]
    if isinstance(final, AIMessage):
        print(final.content)

    await close_browser()
    return result

if __name__ == "__main__":
    import sys
    task = sys.argv[1] if len(sys.argv) > 1 else "Go to https://example.com and tell me the page title."
    asyncio.run(run(task))
