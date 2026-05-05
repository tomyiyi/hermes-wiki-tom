---
title: batch7_lark_cli_absorption
tags:
  - Trae_Solo
  - Architecture
  - NewAge_Origin
  - Feishu
  - Agent
date: 2026-04-14
source: Trae_Solo_Mind_Sync
---

# Batch 7: The Feishu/Lark Control Upgrade (lark-cli)

## Reconnaissance
- **Target**: `yjwong/lark-cli` (A token-efficient CLI for Lark/Feishu APIs, designed for AI assistants like Claude Code).
- **Core Problem Solved**: The official Feishu MCP servers or raw API calls return massive, deeply nested JSON trees (e.g., Document Blocks). This causes context window explosion and massive token costs for LLMs.

## Abstract & Pattern Recognition
- **Markdown Conversion**: Instead of raw blocks, it requests `content_type=markdown` from Feishu, flattening documents into plain text. This is 2-3x more token-efficient.
- **Compact JSON**: It strips HTTP traces and returns high-signal, flat JSON like `{"success": true, "message_id": "om_xxx"}`.
- **CLI as the Physical Executor**: It handles Auth, OAuth flows, and Token refreshing in a compiled Go binary. The Agent doesn't need to write Python `requests` code; it just executes shell commands.
- **Declarative Skills**: It ships with `skills/SKILL.md` files (YAML Frontmatter + SOP Prompts), proving that our `skill_parser.py` architecture in NewAge is the industry standard.

## NewAge Integration (10-Dimensional Scorecard Guidance)
To integrate `lark-cli` into NewAge, we must evaluate it against our 10D framework:

1. **Efficiency (Token Saving)**: 
   - *Action*: NewAge will use `lark-cli` to read/write Feishu Docs instead of raw APIs.
   - *Scorecard Check*: Does the context size drop significantly when reading a large PRD document? (Yes, due to Markdown conversion).
2. **Security & Recoverability**:
   - *Action*: The `lark-cli` binary execution must be routed through NewAge's `PreToolUse` hook.
   - *Scorecard Check*: If the LLM tries to execute `lark msg send --to @all "System deleting..."`, the hook must intercept and block it.
3. **Robustness (Auto-Healing)**:
   - *Action*: If `lark-cli` returns `{"error": "invalid_scope"}`, NewAge's fluid orchestrator must catch this JSON and automatically execute `lark auth login --add-scope` without human intervention.
4. **Autonomy (Swarm Integration)**:
   - *Action*: NewAge can spawn a background Daemon (Subagent) that uses `lark mail search` or `lark cal freebusy` to automatically organize the user's schedule, pushing the summary back via our `GatewayStreamConsumer`.

## Next Steps for NewAge
1. **Physical Installation**: Install the Go binary `lark` into NewAge's environment path.
2. **Skill Registration**: Copy `lark-cli`'s `SKILL.md` files into NewAge's `skills/` directory and parse them using `skill_parser.py`.
3. **E2E Testing**: Create a scorecard test where NewAge uses `lark-cli` to read a document, summarize it, and send a rich card back to the user.
