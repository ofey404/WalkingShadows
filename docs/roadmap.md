# Roadmap

This file collects phase goals of this project.

It begins with a checklist, then detailed records
in reverse chronological order.

- [x] Project structure and build system.
- [x] Grab what we want from Phaser game engine.
- [ ] 0.1 version: A philosopher in a cave
  - [x] Connect frontend and backend
  - [x] Create a CI
  - [x] Create a style guide, based on langchain package. (pydantic)
  - [x] Connect OpenAI, take langchain into project
  - [ ] Implement a baby level memory stream.
    - [ ] Feature: Memory retrival
  - [ ] Fix frontend display
  - [ ] Agent + Environment (the campfire flickered)
    - [ ] Feature: Interaction with environment.
    - [ ] Feature: Reflection
- [ ] 0.2 version: Philosopher and a friend.
  - [ ] Multiple agents. Rather than single.
    - [ ] Feature: Interaction.
  - [ ] Friend bring food to the philosopher.
    - [ ] Feature: Planning.

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

- A good tutorial from Real Python:
  [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 1](https://realpython.com/flask-connexion-rest-api/)
- Which logger to use in a Python Flask app with Connexion:
  <https://stackoverflow.com/questions/59732627/which-logger-to-use-in-a-python-flask-app-with-connexion>

## Python project layout

- Python Application Layouts: A Reference:
  <https://realpython.com/python-application-layouts/>
