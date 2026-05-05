---
title: "Boundary Definition: A Prompt Framework to Find Your Most Niche Needs"
source: "https://mmguo.dev/writings/boundary-method/?lang=en"
author:
  - "[[mm guo]]"
published: 2026-03-22
created: 2026-04-30
description: "边界定义法：一个场景-张力-输出的提示词框架，帮你用AI精准找到最小众、最刁钻的个性化需求。"
tags:
  - "clippings"
---
Have you ever wanted AI to help you, but couldn't even articulate what you needed?

I'm sharing a method called Boundary Definition along with 6 prompts — a framework you can use every time you write a prompt.

Start by looking at this prompt:

prompt

Find an insider consensus currently forming in Silicon Valley's AI circles. This viewpoint typically surfaces only in expert closed-door discussions, technical retrospectives, or internal practice. Most people have never heard of it, yet it offers profound cognitive insight even to non-specialists. Write 3 tweets of 120 words each from the first-person perspective of a startup founder, an investor, and a tech journalist. Each should be uniquely insightful, with credible narrative voice and personal style.

This prompt follows a structure: "Scene – Tension – Output"

- Scene Viewpoints circulating in Silicon Valley's AI circles
- Tension Experts agree, the public doesn't know, yet it's illuminating
- Output Mimic insiders publishing firsthand information

Once you separate these three parts clearly, the remix possibilities are endless. As long as your prompt is precise, the LLM can leverage its synthesis abilities to deliver any form of response. The method can be understood through this diagram:

![Boundary Definition framework diagram](https://mmguo.dev/writings/boundary-method/boundary-framework.png)

Imagine you're learning a new field or trying to get AI to write something for you. With this framework, you can guide AI to explore a range of possible answers rather than relying on a single fixed prompt.

Every time you write a prompt, imagine drawing three circles

- Circle one: Scene — the more focused, the better; this is AI's "search space"
- Circle two: Tension — requires distilling and observing needs; this is AI's "dream catcher"
- Circle three: Output — defines how AI helps you; this is AI's "output format"

Let me use a travel prompt as an example to see how the three circles work

prompt

Find a foreign travel destination that someone who regularly watches Lonely Planet and travel documentaries would bookmark. It should be relatively easy to reach from Beijing, offer a unique experience, not be an Instagram-checkpoint kind of place, yet still attract a fair number of visitors — a niche choice. Once found, write a concise 500-word Xiaohongshu-style review explaining why you recommend it as the best National Day trip destination, including a brief overview of transportation, costs, and suggested itinerary.

This was a real need of mine. AI recommended Dubrovnik, Georgia, and Iceland. Interestingly, I had actually bookmarked all of them. Sometimes AI seems to know me better than I know myself. Try these prompts — they're magical.

We all have moments of wanting "some travel suggestions," but our actual needs are usually quite particular. Wanting fewer crowds yet convenience, a premium experience without spending too much — these conflicting desires constantly show up in our decisions. AI excels at synthesizing information. As long as you define the boundary, even if you don't know what lies at the intersection, it can find it for you. And within any decision branch, you can keep nesting — choosing itineraries, selecting hotels.

Although the title says this helps you find niche needs, having "picky needs" is actually universal. Everyone is different; nearly every need can be highly customized. I believe AI's ability to identify vague and subtle needs is actually underestimated. Using AI to transform people's fuzzy intuitions into something visible holds infinite value.

How to create value space

Describing the scene and output is relatively easy, but defining the tension often requires observation of reality. Here are a few prompts that only define "tension" — notice how each one points to a highly valuable "answer space":

Motivation recognition

prompt

Find a subtle motivation for paying for virtual products — one that people rarely discuss or admit to online, that usually goes unnoticed, but under specific circumstances becomes unusually strong.

Useful for product positioning and marketing copy — finding the key leverage point for conversion.

Startup opportunity

prompt

Identify a startup opportunity for an AI product. It should not be a universally applicable, already widespread AI office automation scenario, but should involve outsourcing at least some key steps in a professional judgment process — not purely information processing or tool-type usage.

This can help you open up thinking within a specific framework and see if there's a viable idea in your own domain.

Intimate relationships

prompt

Describe a common but rarely publicly discussed interaction pattern in intimate relationships. It should be something most long-term couples have experienced, but would almost never notice during the early stages of dating.

This can help identify unspoken difficulties during emotional bottlenecks, and can serve as a content engine for relationship bloggers.

These are just broad examples — your own needs are the real treasure. Using this method regularly with AI can enhance the quality of answers across every stage of exploration, learning, and execution. Over time, the compound returns on your cognition will be significant.

Of course, not all complex boundaries have a real intersection. For instance, "plan a career path that satisfies my boss, earns colleagues' approval, and doesn't exhaust me" — AI will likely only produce platitudes. The core of the Boundary Definition method: what you circle must be a space that genuinely exists, not a wish list at war with itself.

Amanda Askell's prompt

Every prompt in this article is a remix of [a prompt Amanda Askell shared in March](https://x.com/AmandaAskell/status/1898862562764300514) this year.

![Amanda Askell Prompt Tweet](https://mmguo.dev/writings/boundary-method/amanda-tweet.png)

prompt

Try to identify a relatively obscure principle or idea within the field of xx (discipline name). This principle should be something an early undergraduate has never heard of but a late-stage graduate student would know. It should be relatively niche, yet still interesting and useful. Once you've identified such a principle, devise a story that can illustrate it. The story should have three paragraphs and fully explain the principle you chose, without naming it directly in the story. You may name the principle in the final paragraph, followed by a separate paragraph explaining it and how the story illustrates it.

This prompt is far more sophisticated than what I've discussed today — it points toward recursive thinking and meta-prompting systems. I've built tens of thousands of words of documentation and dozens of prompts of varying complexity around it. I'll gradually share more in the future.

As I wrote this article, a thought struck me — AI loves saying "not x, but y." Is this sentence pattern its own way of creating constraint spaces? Does constraint breed creativity? It seems counterintuitive, but think of poetry — it's precisely the limitations of meter that create beauty.