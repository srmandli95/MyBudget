# 2026-10-27: Automated checks with assert

Status: complete.

## Concepts learned

`assert condition` checks an expectation. A true condition allows execution to
continue; a false condition raises AssertionError. An unhandled failure stops
the script, so a success message must appear after every check it describes.

Assertions automate comparisons previously made by reading terminal output.
They are development checks, not input validation: Python can omit them with
optimization enabled. Continue using explicit validation and exceptions for
invalid user data.

## Exercise and results

Source: [monthly_budgets.py](../exercises/monthly_budgets.py).

```python
assert calculate_category_total(transactions, "Groceries") == Decimal("525.00")
assert calculate_category_total([], "Groceries") == Decimal("0.00")
print("Both checks passed")
```

Learner intentionally changed the first expectation to `524.00` and shared the
resulting AssertionError, confirming that a mismatch is detected. The expectation
was restored to `525.00`, and the learner shared the passing output.

Mentor inspected and ran the current saved script successfully (exit 0), observing
`Both checks passed`. Both the multiple-purchase and empty-input checks are now
saved in the script. This is not yet a separate pytest test suite.

## Next task

Set up a project virtual environment, then introduce pytest, separate test
functions, discovery, and failure reports. Learner reports familiarity with
virtual environments but is happy to walk through the setup. Let the learner
run the setup commands; explain their purpose and verify the selected interpreter.
