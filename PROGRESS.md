# Progress

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; uv setup complete.
The project consists of working standalone exercises, not yet an integrated engine.

## Completed learning

- Python execution, syntax versus runtime errors, references, and assignment.
- Decimal arithmetic, functions, type hints, classes, dataclasses, and validation.
- Equality, identity, aliasing, context managers, and exception handling.
- Lists, loops, category totals, dictionaries, and configurable monthly budgets.
- Assertions, pytest, import behavior, the main guard, parametrization, and fixtures.
- Shared fixture in exercises/conftest.py, discovered without explicit imports.
- uv project setup, development dependencies, lockfiles, and optional activation.

## Latest verification

Mentor ran `uv run --locked python -m pytest exercises -v`: **10 passed in 0.02s**,
exit 0, Python 3.14.6 and pytest 9.2.0. pyproject.toml and uv.lock record the
project and dependencies; .venv remains ignored. Use Python's module invocation
from the project root to make exercises imports work.

Category budget example: limits total 1100.00; groceries remaining -25.00,
restaurants 100.00, gas 50.00, miscellaneous 150.00. Data is fictional.

## Next recommended task

Introduce a shared application module to consolidate repeated Transaction models
and calculation logic progressively. Explain the model differences and the small
proposed change first, then let the learner implement. The budget exercise's
Transaction currently has category and amount; the validated earlier model also
has merchant. Do not assume they can be swapped without updating callers/tests.
Broader financial rules, integration, and milestone completion checks remain.

## Learning-record convention

User requests **one revision file, appended after each lesson**: LEARNING_NOTES.md.
It now contains 14 lessons in learning order with a contents list, including uv.
Append future lessons at the bottom, update contents, and refresh this checkpoint.
The dated learnings/ files are retained as a historical archive, not the primary
place for new entries. Do not keep prepending duplicate checkpoints to the journal.

## Session recovery and teaching preferences

Read LEARNING_MASTER_PROMPT.md, LEARNING_NOTES.md, ROADMAP.md, and this checkpoint.
Inspect actual files before assuming prior changes exist. Mentor first: let the
learner implement core code. Skip familiar material on request; pause at unfamiliar
concepts. When confused, use one change and one check at a time. General decorator
internals, generators, concurrency, GIL, databases, and web development remain
future lessons; mentioning them does not mean they were mastered.

## Repository

Branch main; origin: https://github.com/srmandli95/MyBudget.git.
Commit or push only as authorized. Saving learning notes does not itself mean
that they have been committed or uploaded.
