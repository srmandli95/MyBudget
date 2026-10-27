# 2026-10-26: Transaction classes and instances

Status: exercise complete and reviewed.

## Concepts learned

- A class defines a type; calling it creates an instance.
- `__init__` initializes that instance. `self` refers to the instance being initialized.
- Parameters such as `amount` are local to the method call; `self.amount` stores
  a reference as an instance attribute that remains accessible afterward.
- Each transaction has its own merchant, amount, and category attributes.
- Adding the two Decimal amount attributes produces a new Decimal result.
- An f-string embeds expressions in braces into text, such as
  `f"Total spending: {t1.amount + t2.amount}"`.

## Code reviewed and executed

Source: [transaction_model.py](../exercises/transaction_model.py).

The learner implemented the constructor and created two transactions with
Decimal amounts `59.89` and `10.99`. The mentor ran the script successfully:

```text
merchant: Costco , amount: 59.89
merchant: AMB , amount: 10.99
Total sum of tranction 70.88
```

All exercise requirements were met. Small optional cleanup: use clearer names
than `t1` and `t2`, simplify printed formatting, and correct the output typo.
No changes to the learner's implementation were made during review.

## Limits and next step

This verifies the sample execution, not automated tests or input validation.
Next: compare this explicit class with a dataclass before adding validation.
