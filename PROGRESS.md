# Progress

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; remaining-budget tests in progress.
The project consists of working standalone exercises, not yet an integrated engine.

## Completed learning

- Python execution, syntax versus runtime errors, references, and assignment.
- Decimal arithmetic, functions, type hints, classes, dataclasses, and validation.
- Equality, identity, aliasing, context managers, and exception handling.
- Lists, loops, category totals, dictionaries, and configurable monthly budgets.
- Assertions, pytest, import behavior, the main guard, parametrization, and fixtures.
- Shared fixture in exercises/conftest.py, discovered without explicit imports.
- uv project setup, development dependencies, lockfiles, and optional activation.
- Models, regular packages, and a behavior-preserving refactor into mybudget/models.py.
- Category calculation moved into mybudget/calculations.py; demo and tests import it there.
- calculate_remaining implemented; under-limit test verified. Test-first workflow introduced.

## Latest verification

Mentor ran `uv run --locked python -m pytest exercises -v`: **11 passed in 0.01s**,
exit 0, Python 3.14.6 and pytest 9.2.0. pyproject.toml and uv.lock record the
project and dependencies; .venv remains ignored. Use Python's module invocation
from the project root to make exercises imports work.

Category budget example: limits total 1100.00; groceries remaining -25.00,
restaurants 100.00, gas 50.00, miscellaneous 150.00. Data is fictional.
Mentor reran the module demonstration after calculation extraction; same results, exit 0.

## Next recommended task

calculate_remaining now returns budget minus spent; under-limit test passes.
Next: learner adds the missing Decimal return annotation, then separate tests
for spending exactly at the limit (zero) and above it (negative). After verification,
update the demonstration to call the function and confirm unchanged output.
Initial failing test-first run was suggested but not observed; do not claim it ran.
calculate_category_total now lives in mybudget/calculations.py; demonstration
and category tests import it there.
The budget Transaction now lives in mybudget/models.py; conftest imports it there.
The earlier validated Transaction still has merchant and remains separate. Do not
swap models without a deliberate field/validation change and caller/test updates.
Broader financial rules, integration, and milestone completion checks remain.

## Learning-record convention

User requests **one revision file, appended after each lesson**: LEARNING_NOTES.md.
It now contains 17 lessons in learning order, including the remaining-budget test checkpoint.
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
