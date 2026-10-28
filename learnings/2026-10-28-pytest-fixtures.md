# 2026-10-28: Pytest fixtures and sharing setup

Status: local fixture exercise complete; conftest.py discussed, not implemented.

## Fixtures

A fixture prepares data or resources needed by a test. The learner decorated
`sample_transaction` with `@pytest.fixture` and returned three fictional
transactions: Groceries 40.00, Gas 20.00, and Groceries 10.00.

A test requests a fixture by naming it as a parameter. Pytest finds and calls
the fixture and passes its returned list into the test. The parameter receives
the list, not the fixture function; the test does not call the fixture directly.

The default fixture scope is function: for each requesting test, this fixture
runs again and constructs a fresh list and fresh transactions. That prevents
one test's changes to this data from leaking into another. Broader scopes and
cleanup fixtures are future topics.

Parametrization runs a test for several inputs; fixtures provide reusable setup.
They can be used together but serve different purposes.

## Names and sharing

- In one module, defining another function with the same fixture name replaces
  the earlier definition. Use distinct names for different local datasets.
- Different test modules can each define local fixtures with the same name.
- Keep a fixture local when only that module needs it.
- For sharing across test files, place it in `conftest.py`. Pytest discovers
  fixtures there for tests in that directory and its subdirectories; tests
  request them by name without importing conftest.py.
- More specific fixture definitions can override shared ones; detailed override
  rules remain a later topic. Ordinary fixture-module imports are possible,
  but conftest.py is the usual project-sharing mechanism.

Moving the fixture must preserve all three transactions so existing expectations
remain valid. No conftest.py exists in the inspected exercise files yet.

## Implementation and verification

Source: [test_monthly_budgets.py](../exercises/test_monthly_budgets.py).

The learner reused the local fixture in tests for Groceries 50.00 and Gas 20.00.
Empty-input and nonmatching-category tests remain independent of the fixture.
The learner reported four category tests passing.

Mentor independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **10 passed in 0.01s**, exit 0: four category tests, five validation
cases, and one setup subtraction test. No test code was changed during recording.

## Next task

Optional small exercise: move the existing fixture into exercises/conftest.py,
remove its old definition, preserve its name and data, and rerun the tests.
Explain that shared setup is useful when multiple modules actually need it;
the current fixture is used only in one module, so moving it is a learning
exercise rather than a requirement for correctness.
