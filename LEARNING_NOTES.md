# Learning notes

## Pytest and imports: complete

Learner set up `.venv` and pytest and wrote four passing tests: setup subtraction,
matching-category sum, empty input, and nonmatching input. Mentor independently
ran the two test files through `.venv/bin/python`: 4 passed, exit 0.

Clarified virtual environments versus pip, interpreter selection, test discovery,
and Arrange–Act–Assert. Spent additional time on module initialization: importing
even one name executes the module's top-level code, while function bodies wait
for calls. Learner moved demo code under the `__main__` guard and understood its
purpose. Explained the dotted import path from the project root.

See [pytest and import notes](learnings/2026-10-28-pytest-and-imports.md).
Next: `pytest.raises` for validation, inspecting which Transaction model is used
and guarding demonstration code before import. Do not conflate the simple budget
model with the earlier merchant-validating model.

## Assertions: complete

Learner saved checks for grocery spending `525.00` and Decimal zero for empty
input. Intentionally expecting `524.00` raised AssertionError (learner output).
Restored checks ran successfully for learner and mentor: `Both checks passed`.
Assertions can be disabled by optimization, so they do not replace input validation.
See [assertion notes](learnings/2026-10-27-assertions.md).

Next: virtual-environment setup, then pytest. Learner knows virtual environments
but agrees to walk through setup. No separate pytest suite introduced yet.

## Configurable budgets: complete

Learner implemented dictionary-based Decimal limits, `.items()` iteration, and
category spending aggregation to calculate remaining budgets. Covered dictionary
membership, exact string matching, `.values()`, and `sum`. Debugged incorrect
fallbacks, overwritten results, and early returns. Reduced the task to one change
and one check at a time when the learner became confused.

Mentor ran the final script successfully: total limits `1100.00`; remaining
Groceries `-25.00`, Restaurants `100.00`, Gas `50.00`, miscellaneous `150.00`.
Learner also reported `75.00` grocery remaining with the smaller extra purchase.
See [lesson notes](learnings/2026-10-27-configurable-budgets.md).
Next: automated tests; no saved test suite yet.

## Category totals: complete

Learner extended the totals loop with `if trans.category == category`, and renamed
it `calculate_category_total`. Verified Food `118.98`, Gas `59.49`, unmatched
Subscriptions `0.00`, and empty-list `0.00`, all Decimal results. Mentor ran the
saved file and four direct assertion checks successfully. No saved test suite yet.
The category function replaces the earlier overall-total function in the file.
Details: [loops and category totals](learnings/2026-10-27-loops-and-category-totals.md).
Next: dictionaries for configurable budgets and remaining category amounts.

## Lists and loops: transaction totals exercise complete

Learner implemented `calculate_total` in `exercises/transaction_totals.py`.
The accumulator starts at Decimal zero before the loop, adds each transaction's
amount, and returns after iteration. Corrected adding an entire Transaction
object to a Decimal by accessing `trans.amount`.

Mentor ran the saved script: three amounts of `59.49` total `178.47`.
Separately verified an empty list returns a Decimal equal to `0.00`.
The empty-list check is not yet saved in the learner's exercise file.
Optional cleanup: use consistent plural `transactions` naming instead of
`transaction` and the misspelled `trancsaction`.

## When to use classes and functions

Learner's definition: **A class keeps related data and operations on that data together.**

- Data is held in instance attributes, such as a transaction's merchant, amount,
  and category.
- Behavior means operations expressed through methods, such as validating the
  merchant or changing the category. Validation is one kind of behavior.
- A standalone function is often enough for an operation on supplied inputs,
  such as `calculate_remaining(budget, spent)` or `calculate_total(transactions)`.
- Business logic can live in functions or methods; choose where the responsibility
  fits. Classes are not required for all code and may also simply model data.
- A dictionary can group values too. A Transaction class gives that information
  a specific type and a place for its construction rules. Those rules require
  explicit validation; annotations alone do not enforce them.

Learner confirmed understanding after comparing a transaction instance with a
standalone remaining-budget calculation. Next planned implementation: lists and
loops for transaction totals.

## First session: running source code

Introduced for practice, not yet demonstrated by the learner:
- Source code is text containing instructions in a programming language.
- A shell interprets terminal commands and locates executables using PATH.
- Running `python3 hello_budget.py` starts Python as a process managed by the OS.
- In CPython, source is compiled into bytecode, then executed by the interpreter.
- A program file persists on disk; its running process uses memory and CPU time.

The initial greeting exercise was superseded by the learner's error demos and
Decimal calculation exercise.

## Python execution discussion

Daily notes: [How Python executes a program](learnings/2026-10-26-python-execution.md).

Learner correctly identified the interpreter executable and predicted that a
syntax error prevents top-level execution. Clarified that CPython compiles source
into bytecode, then executes bytecode instructions rather than source lines.
Both stages happen through one `python3 filename.py` command.

Learner ran both error experiments and shared output. Mentor reproduced both:
syntax error prevents the first print; undefined-name execution error occurs
after the first print. Both exit with status 1 as intended. No application tests yet.

## Names, values, and assignment: familiar

Introducing: a name refers to an object; assignment evaluates the right-hand
expression and binds the left-hand name. A computed integer result does not
automatically update when an input name is reassigned.

Learner reported familiarity and requested skipping this exercise. It was not
implemented or tested. Move quickly through known concepts; stop at unfamiliar ones.

## Decimal, functions, and type hints: complete

See [lesson notes](learnings/2026-10-26-decimal-and-type-hints.md).
Learner implemented `calculate_remaining` with Decimal inputs and output hints,
corrected float arguments to Decimal constructors, and clarified module/class
imports, references, and operator behavior. Mentor verified output `424.75`.
Additional edge-case runs have not been demonstrated.

## Transaction class: complete

Learner implemented merchant, Decimal amount, and category instance attributes,
created two transactions, and printed their amounts and total. Mentor ran the
exercise successfully: `59.89 + 10.99 = 70.88`.
Learner distinguished instance attributes from local parameters.
See [review notes](learnings/2026-10-26-transaction-class.md).

Next: compare explicit initialization with a dataclass, then introduce validation.

## Dataclass checkpoint: 2026-10-27

Learner understands that `@dataclass` generates `__init__` assignments from
declared fields. Clarified the decorator by comparing it to
`Transaction = dataclass(Transaction)`.

Learner initially passed a string amount despite its Decimal annotation, then
corrected it to `Decimal("59.99")`. Revisited that annotations do not convert values.

Explained `__repr__` as an inspectable text representation of an object and
`repr(t1)` as an explicit request for it. `print(t1)` uses string conversion,
which falls back to the representation when no custom `__str__` is supplied.
Learner restated the representation concept correctly.

Latest file includes `print(repr(t1))`; read but not yet run by the mentor.
Next lesson: equality versus identity, then validation.

## Identity and validation checkpoint: 2026-10-27

See [daily notes](learnings/2026-10-27-dataclasses-and-validation.md) for dataclass
methods, imports, equality versus identity, assignment, copying, and `id()`.
Learner correctly reasoned that aliased names observe changes to the same object.

Introduced validation through `__post_init__`, `ValueError`, and blank merchant
checks. Explained why whitespace-only text requires `.strip()` before testing
emptiness. Diagnosed a missing decorator and an attribute typo. Latest source
inspection confirms both are fixed; revised validation cases have not been run
by the mentor. Next: verify all three merchant cases, then exception handling.

## Exception handling checkpoint: 2026-10-27

Covered `try`, `except ValueError as error`, propagation, and continuation after
handled errors. Corrected `.strip()` on a Decimal amount; blank merchant validation
had raised first and hidden that AttributeError. Amount check removed.

Learner reported the exercise works. Current saved script contains one valid
transaction attempt; mentor ran it successfully, observing `Continues` and exit 0.
The learner previously shared a handled blank-merchant error. The three-case
experiment is not preserved in the file; no automated tests yet.
See [exception-handling notes](learnings/2026-10-27-exception-handling.md).

Next: lists and loops for processing several fictional transaction inputs,
preserving validation cases, and totaling valid spending.
