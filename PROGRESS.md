# Progress

Last updated: 2026-10-29.

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; monthly-filtering tests in progress.
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
- calculate_remaining implemented; under-, at-, and over-limit tests verified.
- Tested remaining-budget function integrated into the demonstration.
- Date objects, month/year comparisons, and required transaction_date field introduced.
- Fixed the demonstration's missing date import and restored the no-match test.
- Monthly category filtering with mixed-date/category fixture and Decimal accumulator.
- Empty-input monthly test checks both zero value and Decimal result type.

## Latest verification

Mentor ran `uv run --locked python -m pytest exercises -v`: **15 passed in 0.01s**,
exit 0, Python 3.14.6 and pytest 9.2.0. pyproject.toml and uv.lock record the
project and dependencies; .venv remains ignored. Use Python's module invocation
from the project root to make exercises imports work.

Category budget example: limits total 1100.00; groceries remaining -25.00,
restaurants 100.00, gas 50.00, miscellaneous 150.00. Data is fictional.
Mentor reran the module demonstration after the date-field changes; same results, exit 0.

## Next recommended task

calculate_monthly_category_total is implemented with category/year/month matching
and a Decimal accumulator. Learner's expanded fixture includes other-month,
other-category, and other-year purchases; target October groceries remain 70.00.
Empty-list test now checks zero value and Decimal type. Mentor inspected it and
ran the full suite after fixture expansion: 15 passed, exit 0.
Next: nonempty-input test with no monthly/category matches, expecting Decimal
zero. Monthly report integration remains pending. Let the learner implement.

Current model requires transaction_date; fixtures and demonstration supply dates.
sample_no_groceries preserves the no-category-match scenario. Latest verification
includes all date-field fixes and new monthly tests: 15 tests pass. The demonstration
last exited 0 after the date fixes; it still uses all-dates category totals.
Decimal return annotation on calculate_remaining remains optional cleanup pending.
Initial failing test-first run was suggested but not observed; do not claim it ran.
calculate_category_total now lives in mybudget/calculations.py; demonstration
and category tests import it there.
The budget Transaction now lives in mybudget/models.py; conftest imports it there.
The earlier validated Transaction still has merchant and remains separate. Do not
swap models without a deliberate field/validation change and caller/test updates.
Broader financial rules, integration, and milestone completion checks remain.

## Learning-record convention

User requests **one revision file, appended after each lesson**: LEARNING_NOTES.md.
It now contains 23 lessons in learning order, including empty-input result-type checks.
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
