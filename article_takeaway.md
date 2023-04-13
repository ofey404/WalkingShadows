# Agent Architecture

## Memory and Retrieval

- memory stream
- retrival function
  - recency
  - importance
  - relevance
  - normalize to [0, 1], then combine them

## Reflection

- another type of memory
  - given recent experience, what question can ask?
- when importance score exceeds threshold
- reflection on reflections

## Plannning and reacting

- also store in memory stream
- Planning:
  - top down recursive generation
  - agent summary + previous day
- Update the plan
- Dialogue
  - retrieve and summarize related memory


