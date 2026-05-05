---
title: "Ilya Sutskever list"
source: "https://mmguo.dev/writings/ilya/?lang=zh"
author:
  - "[[mm guo]]"
published: 2026-04-02
created: 2026-04-30
description: "Ilya Sutskever 8个深度访谈合集与 30u30 阅读清单。一位僧侣式AI科学家对大语言模型最本真的思考。"
tags:
  - "clippings"
---
**真正的突破** 在于认识到一些早已存在的事物所具有的未被发现的理想属性。Transformer之所以被认为是突破，是因为它对大多数人来说并非显而易见。

要真正出色地 **预测下一个token** ，模型必须理解产生这些token的潜在现实 (underlying reality)。这不是简单的统计规律匹配，而是要理解"世界是如何创造这套统计数据的"。模型需要推断出人类行为背后的思想、情感、观念和行事方式。

**深入理解现有事物** ，这是前提。你需要对已有的工具、算法、理论有非常扎实的理解。不只是知道它们是什么，而是知道它们为什么这样工作，它们的优点、缺点，以及它们在不同条件下的行为。

**预测下一个token** ，意味着理解了导致这个token被创造出来的潜在现实。

— Ilya Sutskever

过去三年，我一遍一遍回看Ilya的采访，他是我心中僧侣式的AI科学家与工程师，他说的每一句话都打中我对LLM最本真的好奇。我在这里整理了Ilya 在近十年内参加的 8 次深度播客/公开访谈和Ilya 30u30，后续会更新一些关于Ilya以及论文相关的笔记，希望对你也有帮助。

① Talking Machines — 机器学习与魔法思维

- 时间 2015 年 1 月
- 节目 Talking Machines
- 主持人 Katherine Gorman & Ryan Adams
- 链接 [Robohub 页面](https://robohub.org/talking-machines-machine-learning-and-magical-thinking-with-ilya-sutskever/) · [Spotify](https://open.spotify.com/episode/1piGXNxoS4A6NKdWV7Dqfm)

Ilya 讲述了自己从数学转向机器学习的心路历程。他发现"学习"从严格数学角度看几乎不可能——归纳推理无法被严格证明，但人类确实在做。深度神经网络的优化同样没有理论保证，但经验表明它确实有效。他还谈到了权重初始化的尺度问题如何在多年间阻碍了深度网络的训练。

> 做好机器学习研究需要一种 "magical thinking"——如果你习惯了严格证明结果，那么归纳推理看起来几乎就像魔法。我对学习特别着迷，正是因为我知道人类能做到，但从朴素的数学观点看，学习似乎是不可能的。

② Lex Fridman Podcast #94 — 深度学习

- 时间 2020 年 5 月
- 节目 Lex Fridman Podcast #94
- 主持人 Lex Fridman (MIT)
- 链接 [官方页面](https://lexfridman.com/ilya-sutskever/) · [Spotify](https://open.spotify.com/episode/1u3n11xrcap61wuuvK8RGn) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/94-ilya-sutskever-deep-learning/id1434243584?i=1000474021606)

深度学习的演变史；2010-2011 年的顿悟时刻（将大规模数据与端到端训练联系起来）；AlexNet 的诞生；神经网络与人脑的异同；AGI 与人类价值观对齐；AI 模型分阶段发布的伦理考量（以 GPT-2 为例）；自我博弈（self-play）的潜力；AGI 治理中"AI 为 CEO、人类为董事会"的民主模型。

> 当你什么都不知道时，你只会注意到非常粗糙的表面模式——字符之间有空格，有时逗号后面跟大写字母。然后你可能注意到某些词经常出现，注意到拼写的规律，注意到语法。而当你在所有这些方面都变得非常好之后，你就开始注意到语义，开始注意到事实。但要做到这一点，语言模型需要更大。

> 神经网络有推理的能力，但如果你在一个不需要推理的任务上训练它，它就不会推理。神经网络会以最简单的方式解决你摆在它面前的问题。

③ Clearer Thinking Podcast — AI 究竟"理解"了什么？

- 时间 2022 年 10 月
- 节目 Clearer Thinking with Spencer Greenberg
- 主持人 Spencer Greenberg
- 链接 [官方页面（含完整文字稿）](https://podcast.clearerthinking.org/episode/128/chatgpt-co-creator-ilya-sutskever-what-if-anything-do-ais-understand/) · [Spotify](https://open.spotify.com/episode/1IwbWg1SzwYrps250192fW) · [Apple Podcasts](https://podcasts.apple.com/us/podcast/what-if-anything-do-ais-understand-with-chatgpt-co/id1535406429?i=1000584036468)

机器是否真正具有智能？GPT-3 只训练了"预测下一个词"这一个任务，为什么却似乎理解了那么多东西？预测与理解之间的本质联系是什么？近年来使 GPT-3 成为可能的关键突破有哪些？学术界能否继续站在 AI 研究前沿？AI 如何同时"记忆"训练数据又具备泛化能力？无限扩大数据和算力是否存在概念性的天花板？AI 带来的危险的主要类别。

> 神经网络本质上是一种可以自我编程的并行计算机。

> 假设你读完了一本推理小说，翻到最后一页——如果一个系统能真正预测这一页的下一个词，它就必须具备真正的理解能力。

> 我们对智能的直觉并不完美。很多任务比人们想象的要"窄"得多——计算机做到了不意味着它能做一切。

④ Eye on A.I. — GPT-4 背后的大脑

- 时间 2023 年 3 月
- 节目 Eye on A.I.
- 主持人 Craig S. Smith（前纽约时报记者）
- 链接 [Apple Podcasts](https://podcasts.apple.com/us/podcast/ilya-sutskever-the-mastermind-behind-gpt-4-and/id1438378439?i=1000604382855) · [Player FM](https://player.fm/series/eye-on-ai/ilya-sutskever) · [HackerNoon 文字版](https://hackernoon.com/an-interview-with-ilya-sutskever-co-founder-of-openai)

GPT-4 发布前夕，Ilya 系统阐述了他对大语言模型本质的理解。他认为"预测下一个词"不是肤浅的统计游戏，而是通往深层世界理解的路径；预训练模型学到的是现实世界过程的压缩表示；RLHF 不是在教知识，而是在教行为；多模态有用但非必需，纯文本也能学到颜色关系。他还回溯了自己投身 AI 的原点——对意识的哲学困惑，以及17岁时与 Hinton 合作的核心直觉：人脑也只是一个神经元速度较慢的神经网络。

> 学习统计规律远比表面看起来重要得多。要做好预测，你必须理解产生数据的底层过程。

> 大型生成模型从数据中学到的，是产生这些数据的现实世界过程的压缩表示。

> 我们的预训练模型已经知道了关于底层现实的一切必要知识。——这意味着 RLHF 不是在教知识，而是在教行为：模型已经"懂了"，只是还不会"做人"。

> 意识让我深感不安。——他投身 AI 的最初驱动力不是商业也不是工程，而是对意识之谜的哲学困惑。

⑤ NVIDIA GTC 炉边对话 — 与黄仁勋谈 AI 的今天与未来

- 时间 2023 年 3 月（GPT-4 发布次日录制）
- 场合 NVIDIA GTC Spring 2023
- 对话者 Jensen Huang（黄仁勋，NVIDIA 创始人兼 CEO）
- 链接 [NVIDIA 官方页面](https://www.nvidia.com/en-us/on-demand/session/gtcspring23-s52092/) · [NVIDIA 博客报道](https://blogs.nvidia.com/blog/sutskever-openai-gtc/)

在 GPT-4 发布的第二天，黄仁勋与 Ilya 进行了约一小时的深度对话。回顾了从 AlexNet 到 GPT-4 的十年历程；讨论了 ImageNet 竞赛的"不连续性突破"；GPU 与神经网络的天然契合；ChatGPT 与 GPT-4 的本质区别（GPT-4 能更好地预测下一个词）；多模态（文本、图像、视频）对 AI 理解世界的重要性；以及 AI 推理能力的边界。

> 当我们训练一个大型神经网络去准确预测互联网上各种文本的下一个词时，我们所做的其实是在学习一个世界模型。表面上看，我们只是在学习文本中的统计相关性。但事实证明，要真正"学好"这些统计相关性、真正把它们压缩好，神经网络学到的是产生这些文本的过程的某种表征。

> （无监督学习的解决方案）直觉上你可以看出为什么它应该有效。如果你把数据压缩得足够好，你就必然能提取出其中隐藏的所有秘密。因此，这就是关键。

⑥ Dwarkesh Podcast（第一次）— 构建 AGI

- 时间 2023 年 3 月
- 节目 Dwarkesh Podcast (The Lunar Society)
- 主持人 Dwarkesh Patel
- 链接 [官方页面（含完整文字稿）](https://www.dwarkesh.com/p/ilya-sutskever) · [Spotify](https://open.spotify.com/episode/5p5oJYgVN8vMvEW2nngBN7)

AGI 时间线；泄密与间谍问题；生成式模型之后是什么；后 AGI 未来的经济形态；与微软合作及与 Google 竞争（TPU vs GPU）；超人类 AI 对齐的困难；技术进步的必然性；"新想法是否被高估了"。

> 数据的出现源于计算机变得更好更便宜……每个人有了个人电脑，就想连网，于是有了互联网。有了互联网，海量数据就突然出现了。——整个 AI 革命背后是一条深层的技术必然性链条。

> 我就是不想跟深度学习对赌。我要下最大的赌注。我不知道具体怎么走，但它会自己找到出路。

⑦ NeurIPS 2024 大会演讲

- 时间 2024 年 12 月
- 场合 NeurIPS 2024（温哥华）
- 形式 大会特邀演讲
- 链接 [YouTube 视频](https://www.youtube.com/results?search_query=ilya+sutskever+neurips+2024) · [Substack 文字整理](https://substack.com/home/post/p-153753146)

这是 Ilya 离开 OpenAI 后的首次重大公开露面。他回顾了十年深度学习历程；重申连接主义（connectionism）是经受住时间考验的核心思想；讨论了生物学启发与 AI 的关系；提出"Peak Data"（数据即将耗尽）问题；探讨了模型自我纠错推理错误的可能性；以及 AI 伦理与权利问题。

> 我们所知的预训练将毫无疑问地终结。

> 数据是 AI 的化石燃料——它以某种方式被创造出来，现在我们在消耗它。我们只有一个互联网。

> AI 越是推理，就越不可预测。

> 我们的自我是我们自身世界模型的一部分。

⑧ Dwarkesh Podcast（第二次）— 从规模化时代到研究时代

- 时间 2025 年 11 月
- 节目 Dwarkesh Podcast
- 主持人 Dwarkesh Patel
- 链接 [官方页面（含完整文字稿）](https://www.dwarkesh.com/p/ilya-sutskever-2)

SSI（Safe Superintelligence）公司战略；预训练的局限与数据耗尽；从"规模化时代"到"研究时代"的范式转移；AI 模型在基准测试上表现优异但实际经济影响滞后的困惑；泛化能力不足的根源；价值函数与情感的类比；持续学习（continual learning）；超级智能 5-20 年时间线；AI 对齐难题的坦诚。

> 在个人层面上，指引我的是一种关于"AI应该是什么样"的美学——通过思考人是怎样的来思考AI应该怎样。

> 没有丑陋存在的空间。只有美、简洁、优雅，以及来自大脑的正确启发。

> 这些东西越多地存在，你就越能对一种自上而下的信念充满信心。自上而下的信念，就是当实验结果与你矛盾时，支撑你继续走下去的东西。

> 因为如果你总是只信任数据，有时候你可能做的是正确的事，但代码有bug。你怎么知道应该继续debug，还是该得出结论说方向错了？

> 你必须说"事情一定是这样的，所以我们必须继续走下去。"这就是自上而下的信念，它建立在这种多维度的美和来自大脑的启发之上。

Ilya Sutskever 的深度学习清单

（网传）Ilya 建议的系统学习深度学习的 30 篇关键工作，我读了其中我能看懂的部分，个人觉得这份清单非常可信。

完整清单： [Ilya 30u30 阅读列表](https://arc.net/folder/D0472A20-9C20-4D3F-B145-D2865C0A9FEE)