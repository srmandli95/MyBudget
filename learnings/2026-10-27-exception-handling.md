# 2026-10-27: Handling validation exceptions

Status: lesson complete based on learner-reported success; current saved script
independently run for its valid-input path.

## Concepts covered

- `raise ValueError(...)` signals unacceptable input and interrupts the current operation.
- `try` executes code that may fail. A matching `except ValueError as error`
  handles that exception and binds the exception object to `error`.
- After a handled error, execution continues after the handler. An unhandled
  error propagates and can stop the script.
- A failed construction does not assign a newly initialized transaction to the
  target name. Print a successfully constructed object inside the `try` block.
- Catch the expected exception type. `except ValueError` does not catch AttributeError.
- Keep domain validation in the class; the caller decides how to respond to failure.

## Bug investigated

The learner added `.strip()` checks to merchant, amount, and category. Merchant
and category are strings, but amount is a Decimal, which has no `.strip()` method.
A blank merchant raised ValueError first and hid that later bug. A valid merchant
would reach the amount check and raise AttributeError instead.

The learner removed the amount check. Blank-string validation remains for merchant
and category. Appropriate monetary validation needs separate rules; negative
amounts may represent refunds.

## Code and verification

Source: [transaction_exception_handling.py](../exercises/transaction_exception_handling.py).

- Learner initially shared output demonstrating a handled blank-merchant error
  followed by `Continues`.
- Learner subsequently reported the exercise works after removing the amount check.
- Current saved file contains one valid Costco transaction inside `try`, a
  ValueError handler, and a final print. It does not preserve all three attempts
  or print the successfully created transaction.
- Mentor ran that current file successfully; output was `Continues` and exit
  status was 0. This verifies the current valid-input path, not all three cases.
- No automated tests were added or executed.

## Next task

Use a list and a loop to process multiple fictional transaction inputs, handle
individual validation failures, and calculate spending across valid transactions.
Preserve valid, empty, and whitespace-only merchant cases in that exercise so
their behavior is repeatable rather than requiring manual file edits.
