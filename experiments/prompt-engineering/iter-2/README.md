# 迭代 2

先来设计一个结构化的流程。

Building blocks：

> "4 weapons" in the prompting arsenal:
>
> Summarizing (e.g., summarizing user reviews for brevity)
>
> Inferring (e.g., sentiment classification, topic extraction)
>
> Transforming text (e.g., translation, spelling & grammar correction)
>
> Expanding (e.g., automatically writing emails)

回顾一下迭代 1，我手动做的事情，可以归结为这些 blocks：

1. 设定扩充，故事续写——Expanding
2. 描写——transforming，给例子让它模仿。
3. 角色动力学——summarizing 动机，inferring 行为。
4. 不对称，伏笔：Inferring
5. 创造 AI 可以利用的材料——剧情梗概，角色梗概，这些都是 summarizing

3 和 4 做得不好，注意到它们都是有高度逻辑性的强推理任务。尝试用 GPT4 来做原型。

## task 1: 模仿描写

- Principle 1: Write clear and specific instructions
- Principle 2: Give the model time to “think”

## task 2: 故事的动力学

task 1 的文笔已经达到基准，但是仍然空洞乏味，因为缺乏内容。没有人物故事，没有伏笔，没有暗示。

或者说，它缺乏一个贯穿情节的脊椎。

- “观众不仅聪明，而且比大多数电影更聪明。”
- 如果一段描写背后没有其意图，如果散乱的意图没有串成一线，观众将会轻而易举地识破。
- 作家所能做的一切就是，尽其所能，以求超越聚精会神的观众所表现出的敏锐的集体感知力。

回顾一下罗伯特·麦基的《故事》。

笔记在 [./story-dynamics.md](./story-dynamics.md)

## 已有的实践参考

https://www.allabtai.com/how-to-write-a-great-story-with-gpt-4/

我的这个流程，独创的价值有两点：

1. 重点放在 review and edit，给细化、修改的流程提供好用的工具。
2. 根据戏剧理论来规范框架，制造 prompt。

可以参考的东西，the rating prompt：https://www.allabtai.com/gpt-4-prompt-engineering-the-rate-this-prompt/

How to Master Reverse Prompt Engineering with ChatGPT：https://www.allabtai.com/how-to-master-reverse-prompt-engineering-with-chatgpt/

这也是一个纯工程的状态：https://www.youtube.com/watch?v=UUHQfl5t9eI

- summarize by 2 steps to get some details
- 只在意长度。这根本不算是一本书

## task 3

task 2 很失败。主要是很难让它像我想象的那样工作。

我需要在技术上做一些改进，同时扔掉一些对它处理复杂信息能力的期望。

这是真的写出全长作品的人：[Generating a full-length work of fiction with GPT-4](https://medium.com/@chiaracoetzee/generating-a-full-length-work-of-fiction-with-gpt-4-4052cfeddef3)

- 他是通过编辑大纲的方式来做到的。
- 我可以先生成一个，“含有故事动力学的大纲”。
- 然后再对大纲做操作，可能的操作有：
  - 人类介入来调整
  - 提取出人物弧光，人物真相的揭露等，summarize。
  - 各场景的价值转变，各幕更大的价值，不可逆转的变化。

或许我只应该给出最小的人物，因为情节就是人物，人物就是情节。

他技巧上可以参考的有：

1. Iterative refinement: Start with a high level outline. Make a detailed chapter outline. Then write a draft version of the full chapter (this will be much shorter than desired). Then expand each scene into a longer, more detailed scene.
2. Bounding(outside in): have it first write the first parts, then the last parts, then fill in the middle parts.
3. Continuity notes: 我用自己的形式。

他也整理了一些不足之处：

1. 后向引用：

Reference without introduction: Occasionally, the AI will reference things that have not really been introduced/explained yet, like Langdon knowing about Lord Malakhar in Chapter 4, or Aria having a physical pendant after her dream of Queen Neria. It feels like you must have missed something.

通过一个记忆机制来试着解决这个问题。

2. 开头、结尾段，和章节之间不连续。

我也发现了这个问题。

3. 细节脱漏。伏笔掉了。

我的意见是，我们只能选择哪一部分不掉，不可能所有的都不掉。

然后就是尽量让每一个细节都有意义。少就是多。LLM 倾向于无意义的堆积。

4. 重复累赘。

5. 结构太过常规了。

Almost invariably the AI chose to write 6–8 scenes per chapter, and about 1–2 pages per scene. This feels less organic than a lot of human-written works where some scenes/chapters are short and others are longer.

“动态展开的 prompt”这个建议很有趣，不过先等我做出一个效果不错的静态模式再说。

It might have been better to develop a dynamic expansion structure where it continues to expand until it is somehow satisfied that it has achieved the desired level of detail.

## Prompt Engineering Guide

“The description is intended for furniture retailers“

The description is intended for 这个方法很有趣。描述期望的读者。

“提取信息”这种说法比“总结”效果更好。存疑，我试试。

## 5 使用 API

API 非常慢。

## 6 纯粹开戏剧性

我发现 4 5 的大纲已经非常好了。6 这样全无背景的，只会写出寡淡无味的麦片粥。

作者对于世界的信息量达到临界点，好东西才会产生。

那么我需要做的就是压缩长度，增加一个 ctx 内部的信息。

我一开始没有压缩我自己的描写，因为想要保留一些我自己的 tone，我认为有价值。

但是这实际上是把不同抽象层次的问题放在同一层解决，解决不了。大纲层次不需要文笔。

## 7 故事的种子

“有两个概念支撑着整个创作过程：一是前提，即激发作家创作欲望的想法;二是主控思想，即通过最后--幕高潮中的动作和审美情感所表达的故事的終极意思。不过，前提却不像主控思想，它很少是一种闭合式的陈述。更可能的情况是，它尾一个开放式结尾的问题：如果 ⋯…将会发生什么？如果一条鲨鱼游进度假的海滩吞食了一个游客，將会发生什么？《大白鲨》。”

从前提开始，生成一个故事。

对白是追求欲望的人物之间，自然而然的交谈，不是作者宣讲其观念的讲坛。