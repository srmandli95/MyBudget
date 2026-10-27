# 2026-10-26: Decimal, functions, and type hints

Status: complete, as requested by the learner.

## Concepts covered

- `decimal` is a standard-library module; `Decimal` is a class provided by it.
- `from decimal import Decimal` makes the class name available directly.
  Alternatively, `import decimal` allows `decimal.Decimal("500.00")`.
- Calling `Decimal("500.00")` creates a Decimal object. Importing or annotating
  with the class does not create an amount.
- Construct amounts from strings to avoid importing float approximation into them.
- Type hints describe expected inputs and outputs. Ordinary Python execution
  does not automatically enforce them or convert arguments.
- Names and function parameters refer to objects. Operators act on the objects'
  values through behavior supplied by their types, not on reference addresses.
- Decimal supports subtraction through its special-method machinery (`__sub__`).
  Subtraction returns a new Decimal object; the original immutable amounts remain unchanged.
- A function returns a result for other code to use. Printing that result is a
  separate responsibility.

## Implemented exercise

Source: [decimal_budget.py](../exercises/decimal_budget.py).

```python
from decimal import Decimal


def calculate_remaining(budget: Decimal, spent: Decimal) -> Decimal:
    return budget - spent


print(calculate_remaining(Decimal("500.00"), Decimal("75.25")))
```

## Misunderstanding corrected

The original call used `500.00` and `75.25`, which are floats. Decimal annotations
did not convert them. The learner changed the call to construct Decimal objects
from strings. The learner also removed unnecessary parentheses around the return
expression.

## Verified results

The mentor ran the updated exercise successfully and observed `424.75`.
This verifies the sample calculation; it is not an automated test suite.
Equal-budget and over-budget cases were suggested but their execution has not
been demonstrated. Lesson completion does not imply those checks were run.

## Next step

Introduce classes, constructors, attributes, and instances by modeling one
fictional transaction. Continue quickly through familiar concepts and pause for
implementation at unfamiliar ones, per the learner's preference.
