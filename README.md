# Walking Shadows

In this repo, I'm building a web tool for quickly building story prototypes with LLM.

Based on:

1. ML Storytelling researches
2. Stanford's article:
   [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)

For the name, see:

> Life's but a walking shadow; a poor player,
> that struts and frets his hour upon the stage,
> and then is heard no more:
> it is a tale told by an idiot, full of sound and fury,
> signifying nothing.

## Roadmap

Goal:

1. Build a writing-aid tool with verified technologies,
   like stanford's generative agents, and other ML story telling papers.
2. Write it in business quality, battle-tested python.

For roadmap, see [./docs/roadmap.md](./docs/roadmap.md).

For current development status, see [this repo's issue board](https://github.com/ofey404/WalkingShadows/issues).

This is the latest snapshot:

![latest](https://user-images.githubusercontent.com/35857538/232515871-47538f30-d68a-4d9c-8e41-cc25a40b745a.png)

![latest](https://user-images.githubusercontent.com/35857538/232516190-e8ba0777-6d4a-4d6d-bcb8-0eebbecdc81f.png)

## Takeaways of my reading materials

Those markdown files are written under [Markmap | Visualize your markdown in VSCode](https://marketplace.visualstudio.com/items?itemName=gera2ld.markmap-vscode).

- [./docs/article_takeaway.md](./docs/article_takeaway.md)
- [./docs/prompt_engineering_takeaway.md](./docs/prompt_engineering_takeaway.md)

## Build System

This project uses [Bazel](https://bazel.build/) as its build system.
I'd like to try out its test caching feature for python.

Commands:

```bash
./scripts/update_bazel_build.sh
./scripts/build_image.sh
./scripts/launch.sh
./scripts/start_frontend.sh
./scripts/start_backend.sh
./scripts/test.sh
```
