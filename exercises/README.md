# Python fundamentals exercises

These scripts demonstrate different execution stages and financial calculations.

## Latest exercise

```sh
python3 exercises/transaction_totals.py
```

`calculate_category_total` sums Decimal amounts for the requested category.
The saved script prints `0.00` for Subscriptions and an empty list. Direct checks
also verified Food `118.98` and Gas `59.49`. No saved automated test suite yet.

Other exercises cover Decimal functions, transaction classes, dataclasses, and
validation with exception handling. Some intentionally raise validation errors.

## Intentional execution errors

From the Mybudget directory:

```sh
python3 exercises/syntax_error_demo.py
python3 exercises/runtime_error_demo.py
```

- `syntax_error_demo.py`: expect SyntaxError and no printed greeting.
- `runtime_error_demo.py`: expect the greeting followed by NameError.

Both error demos exit with status 1 by design. They are learning examples, not application tests.
