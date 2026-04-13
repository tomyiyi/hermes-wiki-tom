---
layer: raw
title: a7996cc07296_Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要
layer: raw
url: 
layer: raw
type: article
layer: raw
created: 2026-04-13
---

---
layer: raw
title: Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要
layer: raw
author: 零一
layer: raw
                    零一
layer: raw
date: 2026年4月12日
layer: raw
cover: /assets/img/news/Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要-0.png
layer: raw
head:
layer: raw
  - - meta
layer: raw
    - name: 新闻
---
      
Hermes Agent今天刚更新了v0.8.0，我觉得这次不一样。

不是功能堆砌的那种更新，是有一个东西让我觉得这件事开始认真了。

他们管这次更新叫"Intelligence Release"——智能发布。

* * *

## 先说背景，这个项目为什么值得关注

Hermes Agent是Nous Research做的开源AI Agent，核心卖点是"越用越懂你"——它会记住你的习惯，自动提炼你做过的任务变成可复用的技能，跨平台接入Telegram、Discord、Slack等等。

上个月v0.7.0 发布的时候已经有32k Stars，这个月涨到了60k+。

社区里有一批人在从Claude Code迁移过来。

![](/assets/img/news/Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要-0.png)

  

* * *

## v0.8.0更新了什么，有四个地方值得说

这次v0.8.0加了什么？

有四个更新我觉得值得说。

第一，Agent开始自己诊断自己的问题了。

这个比较有意思。

以前你用Hermes Agent调用工具出错了，它会告诉你出错了，但解决方式还是靠你。

v0.8.0加了一个自动化行为基准测试——Agent会自己跑测试，发现某个模型在调用特定工具时有问题，然后自动修复这个调用逻辑。

不是你在维护它，是它在维护自己。

第二，支持Gemini了。

Google AI Studio原生集成进来了。

现在 Hermes Agent 可以接入的模型变成了：OpenRouter 200+ 模型、OpenAI、Anthropic、Nous Portal、Kimi、MiniMax，加上这次新增的Gemini。

一个进程，接所有大模型，随时用/model命令切换，不用改代码不用重启。

第三，后台任务会主动推送通知了。

以前你让Agent跑一个长任务——比如部署一个服务、跑一段数据处理——你得自己去盯着看完成没有。

现在加了notify\_on\_complete，任务跑完了它会主动发消息通知你，推到Telegram或Discord都行。

你可以让它干活，然后去做别的事，干完了它来找你。

第四，还有一个免费的模型。

Nous自己的MiMo v2 Pro现在通过Nous Portal免费提供，专门为Agent场景优化，做工具调用和多步推理。

这对不想一直掏模型费用的人来说是个实在的东西。

* * *

## 那个比Gemini更重要的细节，在这里

我为什么觉得这次更新不一样？

因为"Agent自己诊断自己"这件事，是一个方向的转变。

之前大多数 AI工具的逻辑是：你发现问题，你去修。AI只是执行器。

Hermes Agent做的事情是：AI发现自己的问题，AI去修。你只需要设定目标。

这不是功能更新，是架构理念的移动——从"工具"到"自主体"。

当然现在还是早期，能修的问题很有限，但方向对了。

![](/assets/img/news/Hermes Agent今天更新了，有一个细节我觉得比Gemini支持更重要-1.png)

  

* * *

## 做出海工具站的人，这两个点实际有用

对做出海工具站的人，这次更新有没有实际价值？

我觉得有两个点：

一是Gemini支持。Gemini的长上下文做得很好，如果你有需要处理大量文档的场景（比如分析用户反馈、整理产品文档），可以直接切Gemini用，成本比Claude低。

二是后台推送通知。你可以让Agent每天定时跑一次数据汇总，跑完直接推Telegram，你不用开电脑也能看到结果。对副业时间有限的人来说，这个比较省心。

* * *

60k Stars，四个月从0涨到这里，开发节奏也快。

我不知道它最终会不会成为AI Agent的主流框架，但它在解决一件真实的事：让AI不只是听话，而是真的在学习和成长。

这件事如果做成了，很值得。

GitHub搜NousResearch/hermes-agent，有兴趣的可以看看。