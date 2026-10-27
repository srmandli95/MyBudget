# 2026-10-27: Lists, loops, and category totals

Status: exercise complete.

## Concepts covered

- A list is an ordered collection of references to objects.
- A `for` loop visits items through an iterator; its loop variable refers to
  the current object rather than copying it.
- Initialize an accumulator before iteration so each pass builds on the prior result.
- Return after the loop to include all matching items.
- `total += transaction.amount` adds a Decimal amount and rebinds the total.
  It does not change the transaction's amount.
- An `if` condition selects transactions whose category matches the requested one.
  String equality is case sensitive: `Food` and `food` differ.
- One pass over n transactions takes O(n) time and constant extra accumulator storage.

## Debugging and implementation

Initially, adding a Transaction instance directly to a Decimal raised TypeError.
The fix was accessing its Decimal attribute with `trans.amount`.

The learner then adapted the overall-total function into
`calculate_category_total(transaction, category)`. Source:
[transaction_totals.py](../exercises/transaction_totals.py).
It uses a Decimal zero, a loop, a matching-category condition, and a return after
the loop. The list variable spelling was corrected to `transactions`.

## Verification

Earlier overall-total implementation: mentor verified `178.47` for three `59.49`
amounts and Decimal zero for an empty list. That implementation was subsequently
replaced by category filtering; it is not a separate function in the current file.

The learner reported `118.98` for Food, then `0.00` for an unmatched category and
an empty list. Mentor independently executed the current file and checked the
function with assertions, including that every result is a Decimal:

| Input | Category | Expected and observed |
| --- | --- | --- |
| Current three transactions | Food | 118.98 |
| Current three transactions | Gas | 59.49 |
| Current three transactions | Subscriptions | 0.00 |
| Empty list | Food | 0.00 |

All four checks passed. These were direct verification checks, not a saved
automated test suite. The saved script prints only the two zero-result cases.

## Limitations and next step

The category parameter name is clear, but the list parameter is still singular
`transaction`; optional cleanup is plural `transactions`.
The separate overall-total function can be restored later if needed.
This exercise's dataclass has no validation hook; validation remains in the
earlier exercises. No bank data or services are involved.

Next: use a dictionary to map categories to configurable Decimal monthly limits,
then combine those limits with category spending to calculate remaining budgets.
