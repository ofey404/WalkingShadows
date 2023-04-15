# Roadmap

This file collects phase goals of this project.

It begins with a checklist, then detailed records
in reverse chronological order.

- [x] Project structure and build system.
- [x] Grab what we want from Phaser game engine.
- [ ] Implement 0.1 version: a philosopher in the cave
  - [x] Connect frontend and backend
  - [ ] Create a CI
  - [ ] Connect OpenAI, take langchain into project
  - [ ] Build feature
- [ ] Create a style guide, based on langchain package.
- [ ] Use bazel/gazelle for js.
- [ ] Implement a baby level memory stream.

## 0.1 Philosopher in the cave

This is the first version of the simulation.

- Goal: Implement the full pipeline of minimum viable product.
- Non feature goal: Get myself familiar with Phaser game engine.

Content:

- Only 1 agent: A philosopher.
- Environment: A cave with nothing but a pile of campfire.
- Activity: As the flame flickered, the philosopher contemplates, start a thought.
- Interaction: The player can pass a small note to him.

## Phaser game engine

- Github: <https://github.com/photonstorm/phaser>
- Bazel for nodejs: <https://github.com/benchsci/rules_nodejs_gazelle>
- Grab what we want from: <http://labs.phaser.io/>

## Flask

- A good tutorial from Real Python: [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 1](https://realpython.com/flask-connexion-rest-api/)
