# 2026-10-28: Context managers and validation tests

Status: validation-testing exercise complete.

## Statements and expressions

A statement is an instruction Python executes, such as assignment, import,
return, or an if statement. An expression evaluates to a value, such as
`transaction.category == category`, which evaluates to a boolean. The colon
belongs to the surrounding if statement, not the comparison expression.

## Context managers and with

`with` is a statement that uses an object's context-manager protocol to manage
entry into and exit from a block. The context manager defines that behavior;
`with` itself does not mean file handling or expected-error checking.

After successful entry (`__enter__`), Python calls `__exit__` when the block ends,
including if its code raises an exception. The exit method receives exception
information and can suppress an exception or allow it to propagate.

Examples: files close on exit, locks release, and database transaction managers
may commit or roll back. `pytest.raises` checks an expected exception. Handling
an exception never resumes the interrupted block: remaining statements inside
it are skipped, and execution continues after the block if the error is handled.

A managed context is not a new variable scope. Scope describes where a name
can be accessed. Functions create local scopes; if, for, and with blocks do not
create separate variable scopes. Names assigned inside a with block can remain
accessible afterward, although a managed resource may already be closed.

## Why pytest.raises instead of just try/except?

For invalid input, ValueError is the expected correct behavior. A test that calls
`pytest.fail` upon catching that exception reverses the intended expectation.
A try/except that merely catches it also fails to detect the absence of an error.
An equivalent manual check needs an else branch to fail if no error is raised.

```python
with pytest.raises(ValueError):
    Transaction("", Decimal("20.50"), "Food")
```

This context manager passes the check when ValueError (or a subclass) occurs,
fails when no exception occurs, and lets unexpected exception types fail the test.
The learner needed several comparisons with try/except, then correctly restated
the distinction between the with statement and its context-manager object.

## Import lesson reinforced

Object construction runs initialization even without print statements. The
blank-merchant demonstration had to move under the main guard so importing the
validated class does not raise before pytest runs the test. The expected invalid
construction belongs inside the pytest.raises block in the test instead.

## Implemented and verified

Source: [test_transaction_validation.py](../exercises/test_transaction_validation.py).

- Empty merchant raises ValueError.
- Whitespace-only merchant raises ValueError.
- Valid merchant is accepted and retained as an attribute; no raises context is
  needed because an unexpected exception automatically fails that test.

Learner shared passing output for each. Mentor inspected the saved tests and ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **7 passed in 0.01s**, exit 0. This includes the four earlier tests and
three merchant-validation tests, not complete application coverage.

## Next task

Introduce pytest parametrization to express the empty and whitespace merchant
cases as one test with multiple inputs. Explain the decorator before use;
general decorator mechanics and building decorators remain future lessons.
Keep the valid-input test separate. Shared transaction models and recording
development dependencies remain future project cleanup.
