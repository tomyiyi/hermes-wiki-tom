---
title: "Graph of Skills (GoS)"
created: 2026-04-20
updated: 2026-04-20
layer: raw
type: summary
tags: [knowledge-base, skills, graph, retrieval, mcp, karpathy]
source_url: https://github.com/davidliuk/graph-of-skills
source_domain: github.com
source_author: David Liu et al.
archived: false
---

# Graph of Skills (GoS) — Raw Source

## Basic Info

- **Full name:** Graph of Skills (GoS)
- **Repo:** github.com/davidliuk/graph-of-skills
- **Paper:** arXiv:2604.05333
- **Data:** HuggingFace datasets (DLPenn/graph-of-skills-data)
- **License:** MIT
- **Python:** 3.10–3.12

## Core Description

Graph of Skills builds a **skill graph** offline from a library of `SKILL.md` documents, then retrieves a small, ranked set of relevant skills at task time. Instead of flooding the agent context with an entire skill library, GoS surfaces only the skills most likely to help — along with their prerequisites and related capabilities.

## Architecture

### Retrieval Pipeline

1. **Seed** — retrieve semantic candidates (embedding similarity) + lexical candidates (exact-match tokens)
2. **Merge** — combine both candidate pools
3. **Rerank** — rerank using the skill-graph structure (dependencies, co-occurrence, PPR)
4. **Return** — emit a capped, agent-readable skill bundle

### Benchmark Results

On **SkillsBench** (87 dockerized coding tasks) and **ALFWorld** (134 household games):

| Model | Method | SB R↑ | SB T↓ | SB S↓ | AW R↑ | AW T↓ | AW S↓ |
|-------|--------|------:|------:|------:|------:|------:|------:|
| Claude Sonnet 4.5 | Vanilla Skills | 25.0 | 967,791 | 465.8 | 89.3 | 1,524,401 | 53.2 |
| | Vector Skills | 19.3 | 894,640 | 357.3 | 93.6 | 28,407 | 37.8 |
| | **+ GoS** | **31.0** | **860,315** | 364.9 | **97.9** | **27,215** | 49.2 |
| MiniMax M2.7 | Vanilla Skills | 17.2 | 942,113 | 580.7 | 47.1 | 2,184,823 | 88.6 |
| | Vector Skills | 10.4 | 852,881 | 552.9 | 50.7 | 66,109 | 73.4 |
| | **+ GoS** | **18.7** | 867,452 | 502.5 | **54.3** | **65,227** | 68.8 |
| GPT-5.2 Codex | Vanilla Skills | 27.4 | 3,187,749 | 686.8 | 89.3 | 1,435,614 | 83.3 |
| | Vector Skills | 21.5 | 1,243,648 | 773.0 | 92.9 | 34,436 | 57.0 |
| | **+ GoS** | **34.4** | 1,379,773 | 715.6 | **93.6** | 46,462 | 64.7 |

**Key finding:** Token reduction up to **56×** (ALFWorld, Claude Sonnet 4.5) vs. Vanilla Skills.

## MCP Server Integration

GoS ships with a built-in MCP server (`gos-claude`) for Claude Code. Key tools:
- `search_skills` — quick ranked summary
- `retrieve_skill_bundle` — full SKILL.md content with scripts
- `get_skill_neighbors` — dependency/relationship graph
- `index_skills` — build graph from SKILL.md directory

## Key Technical Points

- Prebuilt workspaces: skills_200, skills_500, skills_1000, skills_2000
- Embedding model must match at index time and retrieval time
- Dependency-aware retrieval using Personalized PageRank (PPR)
- Agentskills.io compatible SKILL.md format
- uv-based installation

## Observations

- Built on `fast-graphrag` library
- MCP server exports for Claude Code integration
- Prebuilt workspaces downloadable via script
- No pip-installable package (install from source via `uv sync`)
