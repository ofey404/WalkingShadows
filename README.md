# Walking Shadows

This repository reproduces Stanford's article:
[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)

> Life's but a walking shadow; a poor player,
> that struts and frets his hour upon the stage,
> and then is heard no more:
> it is a tale told by an idiot, full of sound and fury,
> signifying nothing.

## Goal & Roadmap

Goal:

1. Reproduce the article.
2. Write it in business quality, battle-tested python.

Roadmap:

- [ ] Create a style guide, based on langchain package.
- [ ] Implement a baby level memory stream.

## Takeaways of my reading materials

Those markdown files are written under [Markmap | Visualize your markdown in VSCode](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode).

- [./article_takeaway.md](./article_takeaway.md)
- [./prompt_engineering_takeaway.md](./prompt_engineering_takeaway.md)

## Build System

This project uses [Bazel](https://bazel.build/) as its build system.
I'd like to try out its test caching feature for python.

Commands:

```bash
 bazel run //src:src_bin

./scripts/update_bazel_build.sh

./scripts/build_image.sh
```
