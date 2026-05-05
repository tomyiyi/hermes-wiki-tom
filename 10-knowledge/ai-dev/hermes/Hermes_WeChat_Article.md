---
title: Hermes Agent 终于有入门指南了
tags:
  - Hermes
  - WeChat
---

# Hermes Agent 终于有入门指南了

Hermes（爱马仕） Agent，Nous Research 出的那个开源 Agent 框架，出圈了，它能从对话中自主创造技能、迭代优化并跨会话构建用户模型，做到真的可以自我进化。
43.7K GitHub 星，20+ LLM 提供商，14 个平台，6 个执行后端。技术层面没什么好挑的。但让开发者真正头疼的不是功能不够，是不知道怎么用。
官方文档？看过的人都懂。
有人注意到了这个 gap。4 月 8 号，Kevin Simback 甩出一张 Hermes 生态全景图——他把自己能找到的所有相关 GitHub 仓库扒了个遍，按类别整理，还用 Claude 逐个做了安全检查。最后搞出一个网站，80+ 项目，颗颗精选。
同一天，另一个老哥更直接——甩出一本《Hermes Agent: The Complete Guide》，江湖人称「橙宝书」。80+ 工具、Skill、MCP 插件，从安装配置到多 Agent 编排，手把手教你从零搭一个生产级 Agent 出来。
48 小时，568 星。
这个数字很说明问题。Sagar 在评论区留了一句：「技术从来不是瓶颈，文档才是。」确实如此。强大的开源框架一大堆，但「能用」和「能用起来」之间那条沟，跨过去的没几个。
橙宝书本质上是把 Hermes 团队内部那些散落在各处的工作流程、配置技巧、实战经验，拧巴到了一起。有个有趣的细节：Sharbel 建议可以直接把橙宝书发给 Hermes Agent，让它带着你读——这很 Hermes。
目前生态覆盖这些方向：
核心官方
：Hermes-Function-Calling、atropos、hermes-agent-self-evolution
工作空间与 GUI
：hermes-workspace、hermes-desktop
Skill 系统
：Anthropic-Cybersecurity-Skills、avoid-ai-writing、pydantic-ai-skills
多 Agent 编排
：mission-control、swarmclaw
部署与基础设施
：llm-agents.nix、hermes-agent-docker
当然，争议也有。有人质疑这不就是趁热度收割？官方文档写得挺全的，花时间读不就行了。
但说实话，官方文档「全」和「能用」是两码事。一个 43.7K 星的项目，文档写得跟技术备忘录似的，入门门槛摆在那里。橙宝书和生态地图的价值，不在于重复官方做了什么，而在于帮后来者省掉那些本不必踩的坑。
——
资源汇总
橙宝书 GitHub：https://github.com/alchaincyf/hermes-agent-orange-book
生态地图网站：https://hermes-ecosystem.vercel.app/
生态地图源码：https://github.com/ksimback/hermes-ecosystem
Hermes Agent 官方：https://github.com/NousResearch/hermes-agent
关注公众号回复“进群”入群讨论。