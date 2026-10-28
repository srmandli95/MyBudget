# 2026-10-28: First pytest tests and import behavior

Status: first pytest lesson complete; recorded at this session checkpoint.

## Environment and commands

- A virtual environment provides a project-specific Python/package environment.
- pip installs packages; it is distinct from the environment itself.
- `python3 -m venv .venv` creates the environment.
- `source .venv/bin/activate` adjusts the current shell's PATH.
- `python -m pip install pytest` installs through the selected interpreter.
- `.venv/bin/python` explicitly selects the environment without activation.
- `.venv/` is ignored by Git; dependency recording remains a future setup task.

## Tests

Pytest discovers `test_*.py` files and `test_*` functions. Assertions check
expectations; pytest reports results independently for each test. `-v` displays
individual test names. Arrange–Act–Assert means prepare inputs, call the operation,
and check the result.

The learner wrote:

- A Decimal subtraction test to verify the test setup.
- A category-total test adding two grocery purchases while excluding Gas.
- An empty-list test expecting Decimal zero.
- A nonempty, no-matching-category test expecting Decimal zero.

Empty input and no matching category exercise different paths: in the latter,
the loop runs but its condition never matches.

## Imports and the main guard

The first import of a module in a process executes its top-level statements to
initialize its names. This includes assignments, calls, and class/function
definitions. A function definition creates the function; its body runs only when
called. Modules are normally cached, so repeated imports do not rerun initialization.

Even `from exercises.monthly_budgets import calculate_category_total` initializes
the module, not just the requested definition. The dotted path identifies the
module inside exercises; importing is governed by Python's module search path,
not simply by files being adjacent.

The learner moved sample data, reports, and demonstration assertions under:

```python
if __name__ == "__main__":
    # Demonstration code
```

Direct execution sets `__name__` to `__main__`, so that block runs. Importing uses
the module name, so it skips the demonstration. Imports, Transaction, and the
category-total function remain at top level and available to tests.

## Verification

Learner reported all four tests passing. Mentor inspected the files and independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py -v
```

Observed Python 3.14.6, pytest 9.2.0, exit 0, and **4 passed in 0.01s**.
This verifies these tests; it is not a claim of complete application coverage.

## Next task

Teach `pytest.raises` to check expected validation exceptions. Before importing
the validation exercise, inspect its top-level demonstration and guard it as
needed. The Transaction in monthly_budgets.py currently has only category and
amount and no merchant validation; distinguish it from the earlier validated
model rather than assuming they are interchangeable. Keep the next exercise small.
