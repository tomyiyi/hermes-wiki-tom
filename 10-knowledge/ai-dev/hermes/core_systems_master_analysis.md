---
title: core_systems_master_analysis
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
  - Agent
  - Memory
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# Master Architectural Analysis: The 5 Core Systems

Based on a deep physical codebase analysis of OpenClaw, Deer-Flow, MemPalace, Hermes-Agent, and Claude-Code, we have extracted the ultimate blueprints for NewAge's evolution.

## 1. OpenClaw: The Execution Plane
- **Agent Control Plane (ACP)**: Replaces synchronous execution with an event-driven lifecycle stream (`lifecycle_start`, `text_delta`, `tool_call`, `error`).
- **Live Model Switch**: Business-level fallback. If an agent loops or fails reasoning, catch `LiveSessionModelSwitchError` and dynamically upgrade the model mid-session.
- **Docker Sandbox Snapshotting**: Generate a "Skill Snapshot" for the specific workspace to prevent tool/context pollution across sub-agents.

## 2. Deer-Flow: Dynamic Orchestration & Auto-Healing
- **Middleware Chain Pattern**: Replaces hardcoded [[LangGraph]] nodes. Tools and LLM calls are intercepted by middlewares (e.g., `ToolErrorHandlingMiddleware`, `SandboxMiddleware`).
- **Circuit Breaker**: Implements exponential backoff for LLM API calls. Classifies errors (quota, auth, transient) and opens the circuit after max retries to prevent death loops.
- **Implicit Sandbox Healing**: Instead of asking the LLM to fix `ModuleNotFoundError`, the sandbox middleware intercepts the error, runs `pip install` silently, and resumes execution.

## 3. MemPalace: Memory Compression & Topology
- **AAAK Lossy Compression**: Compresses raw text into dense, LLM-readable dialects (Entities, Topics, Key Quote, Emotions, Flags) before vectorizing, saving massive context tokens.
- **Wing-Room-Drawer Topology**: Moves away from flat vector tables. Introduces `wing` (domain/project) and `room` (topic) metadata. Enables cross-domain "Tunnels".
- **Progressive Loading Stack (L0-L3)**: Instead of sniffing top-K for everything, use L0 (Identity) fixed in system prompt, L1 (Core events summary), L2 (On-demand room loading), L3 (Deep semantic search).
- **CRITICAL FIX**: Never write `[0.0]*1536` dummy vectors on embedding failure. It collapses the cosine distance space.

## 4. Hermes-Agent: Gateway & Skill Control
- **Adaptive Backoff Streaming**: For IMs (like Lark/Telegram) that rate-limit edits, use a queue-based consumer. If HTTP 429 hits, dynamically increase edit intervals (e.g., 1.5s -> 3s -> 6s) and fallback to "send-once-at-end".
- **Smart Model Routing**: Sniff intents before routing. Simple/chat queries go to a fast, cheap model; code/tool queries go to the primary physical-access model.
- **Declarative Skills**: Move away from Python class inheritance for skills. Use `SKILL.md` with YAML frontmatter to define prompt, triggers, and rules.

## 5. Claude-Code: Prompt Engineering & MCP
- **Frontmatter-Driven Prompts**: System prompts must be `.md` files with strict structures: Role, Process, Quality Standards, Edge Cases.
- **Model Context Protocol (MCP)**: Decouple tools. Build them as standard MCP servers.
- **Allowed-Tools Whitelisting**: Dynamically inject `allowed-tools` per task. Do not expose all tools globally.
- **Lifecycle Hooks**: Implement `PreToolUse` hooks with a RuleEngine to intercept and reject dangerous bash commands (`rm -rf`) before they execute, feeding the error back to the LLM for self-correction.

## Immediate Action Items for NewAge
1. Fix LanceDB dummy vector corruption bug and upgrade schema (`wing`, `room`).
2. Implement Circuit Breaker in LLM router.
3. Implement Adaptive Backoff in Lark Gateway.
4. Refactor skills to use `SKILL.md` declarative format.
