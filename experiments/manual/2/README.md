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

# task 1: 模仿描写

- Principle 1: Write clear and specific instructions
- Principle 2: Give the model time to “think”
