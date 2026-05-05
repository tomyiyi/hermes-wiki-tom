---
title: gstack 迁移记录
created: 2026-05-04
updated: 2026-05-04
layer: action
type: summary
tags: [AI-Agent, gstack]
solves_what:
  - "解决：如何将 gstack 集成到 Hermes"
  - "用户：用户对 YC 方法论和自动化软件工程有兴趣"
  - "失效：gstack 依赖 Claude Code CLI，用户选择不安装"
---

# gstack 迁移记录（2026-05-04）

## 核心发现
- Hermes 已原生集成 gstack skills（完整43个，49个文件）
- 迁移版本：~/Desktop/hermes-experiments/gstack-migration/hermes-skills-final/
- gstack 的 browser(browse) → Hermes CDP 替代已完成
- 核心价值：YC Office Hours、Plan CEO Review、Review、Investigate、CSo 等工作流方法论已注册为 Hermes skills

## 结论
- 用户偏好：不安装 Claude Code，优先 Hermes 内部能力
- gstack 依赖 Claude Code CLI，用户明确拒绝不启动不集成
- skills 文档已清理出处标注
