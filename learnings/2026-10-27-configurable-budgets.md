# 2026-10-27: Configurable monthly budgets

Status: lesson complete.

## Concepts learned

- Dictionaries map category names to Decimal monthly limits, keeping configuration
  separate from calculation logic.
- `.items()` supplies key-value pairs; `.values()` supplies the amounts.
- `sum(budgets.values(), Decimal("0.00"))` totals the configured limits.
- `category in budgets` checks dictionary keys. `category in transaction.category`
  checks a substring; use `==` for exact category matching.
- Looping over budgets includes categories with no purchases.
- Category spending accumulates all matching amounts. Start at Decimal zero
  before the loop and return the total after the loop.
- With no matches, the function returns Decimal zero, so the caller needs no
  fallback from None. Remaining budget is limit minus spending.

## Debugging lessons

- A fallback `else` incorrectly charged miscellaneous for the gas transaction.
  Replacing transaction-specific branches with aggregation fixed that design.
- An unconditional assignment overwrote computed remaining values. Indentation
  controls which statements execute conditionally.
- Returning inside the loop ended the function on its first iteration. Returning
  after the loop permits multiple matching purchases and a consistent zero result.
- Corrected `Trasnaction` to `Transaction` and used `list[Transaction]` consistently.

The learner became confused by the combined task. Breaking it into one function
fix and one scenario at a time helped; continue this approach when needed.

## Implementation and results

Source: [monthly_budgets.py](../exercises/monthly_budgets.py).

Learner reported grocery remaining amounts of `100.00` for spending `400.00`,
`75.00` after another `25.00` purchase, and `-25.00` when that purchase became
`125.00`. Miscellaneous retained its full `150.00` with no purchases.

Mentor inspected and ran the final saved script successfully, exit 0:

```text
Total budget: 1100.00
category: Groceries, limit: 500.00, remaining: -25.00
category: Restaurants, limit: 200.00, remaining: 100.00
category: Gas, limit: 250.00, remaining: 50.00
category: miscellaneous, limit: 150.00, remaining: 150.00
```

Earlier intermediate scenarios are learner-reported, not separate mentor reruns.
No saved automated test suite yet. The simple category/amount dataclass does not
include earlier validation hooks. Category keys are case sensitive; subscriptions
remain separate. Data is fictional and held in memory.

## Next task

Automated tests: begin with assertions, then introduce pytest and its setup.
Cover multiple matches, no matches, empty input, and overspending. Explain imports
before expecting the learner to use them. Milestone 1 remains in progress.
