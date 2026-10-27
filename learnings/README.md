# Daily learning journal

Notes and small experiments from building MyBudget.

Keep one Markdown file per day, named `YYYY-MM-DD-topic.md`. Record what you
understand, examples, experiments actually run, and questions to revisit.
Use fictional financial data in examples.

## Entries

- [2026-10-27: Automated checks with assert — complete](2026-10-27-assertions.md)
- [2026-10-27: Configurable monthly budgets — complete](2026-10-27-configurable-budgets.md)
- [2026-10-27: Lists, loops, and category totals — complete](2026-10-27-loops-and-category-totals.md)
- [2026-10-27: Exception handling — complete](2026-10-27-exception-handling.md)
- [2026-10-27: Dataclasses, identity, and validation](2026-10-27-dataclasses-and-validation.md)
- [2026-10-26: Transaction classes and instances — complete](2026-10-26-transaction-class.md)

- [2026-10-26: How Python executes a program](2026-10-26-python-execution.md)
- [2026-10-26: Decimal, functions, and type hints — complete](2026-10-26-decimal-and-type-hints.md)

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

This folder is tracked with the Mybudget project. Git is initialized and the
GitHub remote `origin` is configured.

After writing or reviewing a daily entry, inspect and commit the journal changes:

```sh
git status
git add learnings/
git diff --cached
git commit -m "Document Python execution fundamentals"
```

Staging selects changes for a commit. A commit saves a local snapshot; it does
not upload anything to GitHub. Use `git push` after committing when ready to
upload. The commands above are the workflow for future daily entries; check
`git status` before staging. Stage exercise code separately when it belongs in
the same commit.
