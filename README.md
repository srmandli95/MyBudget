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
For revision, read the [single learning journal](LEARNING_NOTES.md). New lessons
are appended there in learning order. The dated files in `learnings/` are an archive.
Configurable budgets and uv setup are complete; there is no web application or
database yet. See PROGRESS.md for the next small task.

## Setup and tests

With uv installed and Python 3.14 or newer available, run from the project root:

```sh
uv sync --locked
uv run --locked python -m pytest exercises -v
```

The current suite has 10 passing cases. uv manages `.venv`; manual activation is
optional. Commit `pyproject.toml` and `uv.lock`, not `.venv/`.
Use `python -m pytest` through uv so project-root imports resolve correctly.

Run the latest category-total exercise from the project directory:

```sh
python3 exercises/transaction_totals.py
```

It currently prints `0.00` twice for an unmatched category and an empty list.

See LEARNING_MASTER_PROMPT.md for the learning agreement, ROADMAP.md for milestones,
and PROGRESS.md for the next task.
