# MyBudget

A personal finance application built through an incremental engineering apprenticeship.

Current goal: a Python expense engine using fictional transactions held in memory.
The learner writes the core implementation; mentoring, review, and testing accompany each small step.

## Environment

Verified on macOS: Python 3.14.6 and Git 2.55.0; VS Code command available.
The current implementation is a set of standalone learning exercises in
`exercises/`, using only Python's standard library. They cover Decimal calculations,
transaction classes, dataclasses, validation, exceptions, and category totals.
Some scripts intentionally raise errors; see the exercise README.
Daily learning notes are in `learnings/`. The next task is configurable budgets
using dictionaries; there is no web application or database yet.

Run the latest category-total exercise from the project directory:

```sh
python3 exercises/transaction_totals.py
```

It currently prints `0.00` twice for an unmatched category and an empty list.

See LEARNING_MASTER_PROMPT.md for the learning agreement, ROADMAP.md for milestones,
and PROGRESS.md for the next task.
