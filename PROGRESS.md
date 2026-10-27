# Progress

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; first saved assertion checks complete.

## Verified

- Project directory was empty.
- Python 3.14.6 and Git 2.55.0 execute successfully.
- VS Code command is available at /opt/homebrew/bin/code.
- Git is initialized on `main`; GitHub remote `origin` points to
  https://github.com/srmandli95/MyBudget.git.

## Completed

- Saved learning agreement and initial project documentation.
- Added `learnings/` with a daily journal format and Python execution fundamentals.
- Discussed CPython, executables, processes, bytecode, and syntax versus runtime errors.
- First calculation exercise implemented; no automated application tests yet.
- Learner wrote both error demos in `exercises/` and ran them. Mentor reproduced
  the expected SyntaxError and NameError; both exit with status 1.
- Prepared `.gitignore` and exercise documentation for the first commit.
- Variables exercise skipped at learner's request due to familiarity.
- Completed Decimal, functions, type hints, module/class imports, and object
  reference lesson. Learner's calculation ran successfully with output `424.75`.

## Next task

Latest checkpoint: two assertions are saved in `exercises/monthly_budgets.py`:
grocery spending `525.00` and empty-input total `0.00`. Learner demonstrated an
intentional failure with expected `524.00`, then restored passing checks. Mentor
ran the current script successfully and observed `Both checks passed`, exit 0.

Next: walk through a project virtual environment, then pytest setup and separate
test functions. Learner knows virtual environments but wants to proceed with the
setup. Let the learner execute commands and review results. No pytest suite yet.

## Previous configurable-budget checkpoint

Latest checkpoint: configurable budgets complete. Mentor ran
`exercises/monthly_budgets.py`: total limits `1100.00`; remaining Groceries
`-25.00`, Restaurants `100.00`, Gas `50.00`, miscellaneous `150.00`.
Learner checked multiple purchases, no purchases, and overspending incrementally.
See learnings/2026-10-27-configurable-budgets.md.

Next: automated tests, starting with assertions before pytest setup as needed.
No saved test suite yet. Keep tasks small; use one change and one check at a time
when the learner is confused. Milestone 1 is still in progress, not complete.

## Previous category-totals checkpoint

Latest checkpoint (2026-10-27): category filtering with a condition inside a loop
is complete. Mentor verified four Decimal results: Food `118.98`, Gas `59.49`,
unmatched Subscriptions `0.00`, and an empty list `0.00`.
The learner renamed the function `calculate_category_total` and fixed the list
variable spelling. It replaced the original overall-total function; both are not
currently present. No saved automated test suite yet.

Next: dictionaries for configurable monthly budgets, followed by combining budget
limits with category spending to calculate remaining amounts. Teach before asking
the learner to implement. Do not generate the solution in advance.
See learnings/2026-10-27-loops-and-category-totals.md for verification and limits.

## Prior checkpoint

Current stopping point (2026-10-27): learner reports success handling validation
errors with `try`/`except`. Covered dataclass representation, equality, identity,
aliasing, copying, `id()`, imports, and validation with `__post_init__`.

Mentor ran the saved exception-handling script with valid input: output
`Continues`, exit 0. Learner shared an earlier handled blank-merchant error.
The saved script contains only one valid attempt, not the full three-case exercise.
No automated tests yet. Details are in learnings/2026-10-27-exception-handling.md.

Next: lists and loops to process multiple fictional inputs, handle individual
validation failures, and total spending. Preserve valid, empty, and whitespace-only
merchant cases in the next exercise. Let the learner write the implementation.

## Session recovery

Read LEARNING_MASTER_PROMPT.md for the learning agreement, ROADMAP.md for the
milestones, this file for the current checkpoint, and LEARNING_NOTES.md plus
learnings/ for concepts and misunderstandings. Inspect actual exercise files
before assuming they match earlier notes. Mentor first: let the learner implement;
skip familiar material on request and pause at unfamiliar concepts.

## Open questions

- Which editor does the learner prefer?
- Equal-budget and over-budget calculation checks have not been demonstrated;
  the learner requested marking the current lesson complete.
