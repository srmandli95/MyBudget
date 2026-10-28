# 2026-10-28: Pytest parametrization

Status: complete.

## Concept and implementation

Parametrization runs the same test logic with several inputs. The learner
replaced two repeated invalid-merchant tests with:

```python
@pytest.mark.parametrize("merchant", ["", " ", "   ", "\t"])
def test_rejects_blank_merchant(merchant):
    with pytest.raises(ValueError):
        Transaction(merchant, Decimal("59.99"), "Gas")
```

The decorator attaches parameter information to the test function. Pytest
collects one test case for each supplied value, calls the test with that value,
and reports each case separately. The parameter name in the function must match
the name specified in the decorator. A tab (`\t`) is whitespace removed by strip.
The valid-merchant test remains separate because it expects successful construction.

## Debugging

Initially the function had no merchant parameter despite the decorator naming
one. Pytest reported an error during collection, before executing the tests.
Adding `merchant` to the function signature fixed the mismatch. The learner then
added the three-space input to complete all four planned invalid cases.

Reinforced context-manager understanding before this exercise: with uses an
object's entry and exit behavior; pytest.raises fails if no expected error occurs.
General decorator internals are still a later lesson, not considered mastered
solely from using this pytest decorator.

## Verification

Source: [test_transaction_validation.py](../exercises/test_transaction_validation.py).

The learner reported all four invalid cases passing. Mentor inspected the saved
file and independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **9 passed in 0.01s**, exit 0. These are one setup subtraction test,
three category-total tests, one valid-merchant test, and four invalid-merchant
cases. The validation file alone now contains five runnable test cases, despite
having only two test functions.

## Next topic

Pytest fixtures: reuse sample-transaction setup across tests without repeating
construction code. Explain how requesting a fixture by name works and begin with
the default function scope so mutable test data is fresh for each test.
