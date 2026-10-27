# Progress

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; exception-handling lesson complete.

## Verified

- Project directory was empty.
- Python 3.14.6 and Git 2.55.0 execute successfully.
- VS Code command is available at /opt/homebrew/bin/code.
- Git is initialized on `main` with commit `bd04556`. GitHub remote `origin`
  is configured, and local tracking information shows `main` at `origin/main`.

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
