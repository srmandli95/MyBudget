# Daily learning journal

Notes and small experiments from building MyBudget.

Keep one Markdown file per day, named `YYYY-MM-DD-topic.md`. Record what you
understand, examples, experiments actually run, and questions to revisit.
Use fictional financial data in examples.

## Entries

- [2026-10-26: How Python executes a program](2026-10-26-python-execution.md)

## Suggested daily entry

```markdown
# YYYY-MM-DD: Topic

## What I learned

Explain the concept in my own words.

## Example

Add a small example and explain it.

## Experiments and results

Record commands actually run and their observed output.

## Questions and next steps

Record anything still unclear.
```

## Git workflow

This folder lives inside Mybudget and can be tracked with the project.
This folder is intended to be tracked together with the project. The project is
not yet a Git repository, and no GitHub remote is configured. Initialize once
from the Mybudget directory before using the daily workflow:

```sh
git init -b main
```

After writing or reviewing a daily entry, inspect and commit the journal changes:

```sh
git status
git add learnings/
git diff --cached
git commit -m "Document Python execution fundamentals"
```

Staging selects changes for a commit. A commit saves a local snapshot; it does
not upload anything to GitHub. Pushing requires a GitHub repository and a remote,
which we will configure separately. The commands above are the workflow for future
daily entries; check `git status` before staging.
