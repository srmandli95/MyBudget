# MyBudget learning journal

The single revision file for this apprenticeship. Lessons are in learning order;
append new completed lessons at the end and update this contents list.

Current checkpoint: shared budget model extracted; 10 tests pass. See [PROGRESS.md](PROGRESS.md)
for the current task and [ROADMAP.md](ROADMAP.md) for the curriculum.

Earlier entries preserve what was known and verified at that lesson. Historical
pending tasks and test counts describe that point in time; later entries record
subsequent completion. The dated files in learnings/ remain as an archive.

## Contents

- [Lesson 01: 2026-10-26: How Python executes a program](#lesson-01)
- [Lesson 02: 2026-10-26: Decimal, functions, and type hints](#lesson-02)
- [Lesson 03: 2026-10-26: Transaction classes and instances](#lesson-03)
- [Lesson 04: 2026-10-27: Dataclasses, identity, and validation](#lesson-04)
- [Lesson 05: 2026-10-27: Handling validation exceptions](#lesson-05)
- [Lesson 06: 2026-10-27: When to use classes and functions](#lesson-06)
- [Lesson 07: 2026-10-27: Lists, loops, and category totals](#lesson-07)
- [Lesson 08: 2026-10-27: Configurable monthly budgets](#lesson-08)
- [Lesson 09: 2026-10-27: Automated checks with assert](#lesson-09)
- [Lesson 10: 2026-10-28: First pytest tests and import behavior](#lesson-10)
- [Lesson 11: 2026-10-28: Context managers and validation tests](#lesson-11)
- [Lesson 12: 2026-10-28: Pytest parametrization](#lesson-12)
- [Lesson 13: 2026-10-28: Pytest fixtures and sharing setup](#lesson-13)
- [Lesson 14: 2026-10-28: uv, dependency resolution, and lockfiles](#lesson-14)
- [Lesson 15: 2026-10-28: Models, packages, and a small refactor](#lesson-15)

<a id="lesson-01"></a>

## Lesson 01: 2026-10-26: How Python executes a program

### Language, interpreter, and executable

- **Python** is a programming language with syntax and behavior rules.
- **CPython** is the usual implementation of Python, written primarily in C.
  It provides the interpreter we are discussing.
- **`python3`** is the command that launches the installed Python 3 interpreter.
- **Source code** is the text we write in a file such as `budget.py`.
- An **executable** is a program file the operating system can launch.
- A **process** is a running instance of a program, with memory and CPU time
  managed by the operating system.

An application such as Chrome includes executables and supporting resources.
On macOS, an `.app` is an application bundle containing these files.
One application can use multiple processes. Closing it stops its running
processes; its installed files remain on disk.

### What the command means

```sh
python3 budget.py
```

`python3` names the executable to start. `budget.py` is an argument telling
Python which source file to execute.

The shell searches the directories in **PATH** to find `python3`. The operating
system starts the interpreter process, which receives the filename argument.
A relative filename is resolved from the current working directory.

- `python3` with no filename normally starts an interactive session in a terminal.
- `python3 missing.py` starts Python, but it reports an error and exits if it
  cannot open the requested file.

### The execution pipeline

```text
Shell finds python3
    ↓
Operating system starts the interpreter process
    ↓
CPython reads the source file
    ↓
Tokenize and parse the source into a syntax tree
    ↓
Compile into a code object containing bytecode
    ↓
Execute the bytecode instructions
    ↓
Program finishes, or an unhandled exception stops execution
```

Syntax checking happens while processing and compiling the source. For an
ordinary script, its compilation must succeed before its top-level code executes.

**Bytecode** is an intermediate instruction format for Python's interpreter;
it is not the CPU's machine code. CPython's evaluation loop executes the
bytecode operations. Underneath, the CPU executes the interpreter's machine
instructions, which carry out those operations.

Conceptually, the evaluation loop repeatedly gets an instruction, determines
the requested operation, and performs it. It executes bytecode instructions,
not one source line at a time: one Python line can produce several instructions.

```python
remaining = budget - expense
```

Conceptually: look up `budget`, look up `expense`, subtract their values, and
bind `remaining` to the result.

**Compilation and execution require only one command:** `python3 budget.py`.
CPython manages both stages automatically. Python is commonly called interpreted,
but that does not mean CPython skips compilation into bytecode.

### Names and objects

```python
merchant = "Sample Grocery"
print(merchant)
```

`merchant` is a name bound to a string object. `print` receives that object and
writes its text representation to standard output, normally shown in the terminal.
The source file persists on disk after execution; this process's in-memory
bindings do not persist into the next run.

### Syntax errors versus execution errors

#### Syntax error

```python
print("Starting MyBudget")
remaining =
```

The assignment is incomplete. Compilation fails, so the first line does not execute.

#### Runtime exception

```python
print("Starting MyBudget")
remaining = unknown_budget
print("Finished")
```

This has valid syntax. Assuming `unknown_budget` has not been defined, execution
prints the first message, then raises `NameError`. The final line does not execute
because this program does not handle the exception.

An exception can be handled by application code; it does not always terminate
the whole program. Exception handling is a later lesson.

### Understanding demonstrated

- Correctly identified `python3` as the interpreter executable in the command.
- Correctly predicted that a syntax error at the end of the same script prevents
  a print at the beginning from executing.
- Explained the compilation and execution sequence, then refined the distinction
  between source lines and bytecode instructions.
- Confirmed that one command performs both compilation and execution.

### Experiments and results

Completed two intentional failure experiments. The learner shared terminal output,
and the mentor independently ran both files and reproduced the results:

- `python3 exercises/syntax_error_demo.py`: `my_name =` on line 3 raises
  `SyntaxError: invalid syntax`. The earlier `print("hello world")` does not execute.
- `python3 exercises/runtime_error_demo.py`: prints
  `Hello world this would cause runtime error`, then line 3, `myname= inputname`,
  raises `NameError: name 'inputname' is not defined`.

Both processes exit with status 1, as expected for these unhandled errors.
These are intentionally failing learning examples, not application failures.

A traceback identifies the file, line, and execution context of a runtime failure.
`<module>` means code executing at the top level of the file. For assignment,
Python evaluates the right-hand expression before binding the left-hand name;
looking up the undefined `inputname` fails before `myname` can be assigned.

Previously verified environment: macOS, Python 3.14.6, Git 2.55.0, and a VS Code
command available on PATH.

### Next practice

Create a small MyBudget script with fictional expense data. Practice defining
a name before using it, and distinguish a string literal from a name lookup.

<a id="lesson-02"></a>

## Lesson 02: 2026-10-26: Decimal, functions, and type hints

Status: complete, as requested by the learner.

### Concepts covered

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

### Implemented exercise

Source: [decimal_budget.py](exercises/decimal_budget.py).

```python
from decimal import Decimal


def calculate_remaining(budget: Decimal, spent: Decimal) -> Decimal:
    return budget - spent


print(calculate_remaining(Decimal("500.00"), Decimal("75.25")))
```

### Misunderstanding corrected

The original call used `500.00` and `75.25`, which are floats. Decimal annotations
did not convert them. The learner changed the call to construct Decimal objects
from strings. The learner also removed unnecessary parentheses around the return
expression.

### Verified results

The mentor ran the updated exercise successfully and observed `424.75`.
This verifies the sample calculation; it is not an automated test suite.
Equal-budget and over-budget cases were suggested but their execution has not
been demonstrated. Lesson completion does not imply those checks were run.

### Next step

Introduce classes, constructors, attributes, and instances by modeling one
fictional transaction. Continue quickly through familiar concepts and pause for
implementation at unfamiliar ones, per the learner's preference.

<a id="lesson-03"></a>

## Lesson 03: 2026-10-26: Transaction classes and instances

Status: exercise complete and reviewed.

### Concepts learned

- A class defines a type; calling it creates an instance.
- `__init__` initializes that instance. `self` refers to the instance being initialized.
- Parameters such as `amount` are local to the method call; `self.amount` stores
  a reference as an instance attribute that remains accessible afterward.
- Each transaction has its own merchant, amount, and category attributes.
- Adding the two Decimal amount attributes produces a new Decimal result.
- An f-string embeds expressions in braces into text, such as
  `f"Total spending: {t1.amount + t2.amount}"`.

### Code reviewed and executed

Source: [transaction_model.py](exercises/transaction_model.py).

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

### Limits and next step

This verifies the sample execution, not automated tests or input validation.
Next: compare this explicit class with a dataclass before adding validation.

<a id="lesson-04"></a>

## Lesson 04: 2026-10-27: Dataclasses, identity, and validation

### Dataclasses and representation

`@dataclass` examines declared fields and generates methods such as `__init__`,
`__repr__`, and `__eq__`. Importing `dataclass` alone does not apply it.
Conceptually, the decorator applies `Transaction = dataclass(Transaction)` after
the class definition. The generated initializer assigns fields; annotations do
not automatically convert inputs or enforce their types.

`__repr__` produces a developer-facing text representation of an object.
`repr(transaction)` explicitly requests it. `print(transaction)` uses string
conversion, which falls back to the representation when there is no custom
`__str__` implementation.

### Equality, identity, and references

- `==` uses a type's equality behavior. By default, dataclass equality compares
  field values for instances of the same class.
- `is` checks whether two references refer to the same object.
- `other = transaction` binds another name to the existing instance; it does not copy it.
- Changing an attribute through either name changes that shared instance. This
  sharing of one object through multiple names is called aliasing.
- Assignment binds a name to the result of the right-hand expression. That
  expression might supply an existing object or create a new one.
- For this transaction class, `copy(transaction)` creates a distinct instance.
  It is a shallow copy: referenced attribute objects are shared rather than
  recursively copied. It is not a general guarantee of independent nested data.
- `id(object)` reports its identity. CPython uses its memory address; other
  implementations need not. IDs can be reused after an object is destroyed.

Matching fields alone do not prove duplicate bank transactions: separate genuine
purchases may share merchant, amount, and category.

### Modules and imports

`dataclasses`, `decimal`, and `copy` are standard-library modules. They provide
the `dataclass` function, `Decimal` class, and `copy` function respectively.
A module is an importable unit of code; a package organizes modules; library is
a broader term for reusable code. Own modules and dependency management come later.

### Validation with __post_init__

A merchant must contain at least one non-whitespace character. Correct types
alone do not guarantee valid business data.

The dataclass-generated initializer assigns the fields, then calls the defined
`__post_init__` hook. The learner implemented:

```python
def __post_init__(self) -> None:
    if not self.merchant.strip():
        raise ValueError("marchant should not be blank")
```

`.strip()` returns a string with surrounding whitespace removed; it does not
change the original attribute. An empty string is false in a condition. Both
`""` and `"   "` therefore trigger this check. Checking only `merchant == ""`
would miss strings containing spaces. This assumes merchant is already a string.

`raise ValueError(...)` rejects an unacceptable value. If the exception escapes
initialization, the constructor call fails instead of returning an initialized
instance to the caller. Negative amounts are not rejected by this rule; a refund
policy requires a separate decision.

### Debugging and current verification

Source: [transaction_dataclass_postinit.py](exercises/transaction_dataclass_postinit.py).

The learner shared a run raising `TypeError: Transaction() takes no arguments`.
Inspection found the class lacked `@dataclass`, so no field initializer was
generated. There was also a `self.merchannt` typo that would cause AttributeError
after fixing the decorator.

Latest source inspection confirms both fixes: the decorator is present and the
check uses `self.merchant`. The file currently attempts construction with `" "`
as merchant. The error-message typo `marchant` is cosmetic and remains unchanged.

The mentor has not executed this revised validation script. Valid, empty, and
whitespace-only cases remain to be verified. Equality and identity were discussed
and understood conceptually; no execution results for those experiments were recorded.

### Next practice

Run merchant cases `"Costco"`, `""`, and `"   "` separately and review the output.
Then learn how to handle expected exceptions with `try` and `except`.

<a id="lesson-05"></a>

## Lesson 05: 2026-10-27: Handling validation exceptions

Status: lesson complete based on learner-reported success; current saved script
independently run for its valid-input path.

### Concepts covered

- `raise ValueError(...)` signals unacceptable input and interrupts the current operation.
- `try` executes code that may fail. A matching `except ValueError as error`
  handles that exception and binds the exception object to `error`.
- After a handled error, execution continues after the handler. An unhandled
  error propagates and can stop the script.
- A failed construction does not assign a newly initialized transaction to the
  target name. Print a successfully constructed object inside the `try` block.
- Catch the expected exception type. `except ValueError` does not catch AttributeError.
- Keep domain validation in the class; the caller decides how to respond to failure.

### Bug investigated

The learner added `.strip()` checks to merchant, amount, and category. Merchant
and category are strings, but amount is a Decimal, which has no `.strip()` method.
A blank merchant raised ValueError first and hid that later bug. A valid merchant
would reach the amount check and raise AttributeError instead.

The learner removed the amount check. Blank-string validation remains for merchant
and category. Appropriate monetary validation needs separate rules; negative
amounts may represent refunds.

### Code and verification

Source: [transaction_exception_handling.py](exercises/transaction_exception_handling.py).

- Learner initially shared output demonstrating a handled blank-merchant error
  followed by `Continues`.
- Learner subsequently reported the exercise works after removing the amount check.
- Current saved file contains one valid Costco transaction inside `try`, a
  ValueError handler, and a final print. It does not preserve all three attempts
  or print the successfully created transaction.
- Mentor ran that current file successfully; output was `Continues` and exit
  status was 0. This verifies the current valid-input path, not all three cases.
- No automated tests were added or executed.

### Next task

Use a list and a loop to process multiple fictional transaction inputs, handle
individual validation failures, and calculate spending across valid transactions.
Preserve valid, empty, and whitespace-only merchant cases in that exercise so
their behavior is repeatable rather than requiring manual file edits.

<a id="lesson-06"></a>

## Lesson 06: 2026-10-27: When to use classes and functions

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

<a id="lesson-07"></a>

## Lesson 07: 2026-10-27: Lists, loops, and category totals

Status: exercise complete.

### Concepts covered

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

### Debugging and implementation

Initially, adding a Transaction instance directly to a Decimal raised TypeError.
The fix was accessing its Decimal attribute with `trans.amount`.

The learner then adapted the overall-total function into
`calculate_category_total(transaction, category)`. Source:
[transaction_totals.py](exercises/transaction_totals.py).
It uses a Decimal zero, a loop, a matching-category condition, and a return after
the loop. The list variable spelling was corrected to `transactions`.

### Verification

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

### Limitations and next step

The category parameter name is clear, but the list parameter is still singular
`transaction`; optional cleanup is plural `transactions`.
The separate overall-total function can be restored later if needed.
This exercise's dataclass has no validation hook; validation remains in the
earlier exercises. No bank data or services are involved.

Next: use a dictionary to map categories to configurable Decimal monthly limits,
then combine those limits with category spending to calculate remaining budgets.

<a id="lesson-08"></a>

## Lesson 08: 2026-10-27: Configurable monthly budgets

Status: lesson complete.

### Concepts learned

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

### Debugging lessons

- A fallback `else` incorrectly charged miscellaneous for the gas transaction.
  Replacing transaction-specific branches with aggregation fixed that design.
- An unconditional assignment overwrote computed remaining values. Indentation
  controls which statements execute conditionally.
- Returning inside the loop ended the function on its first iteration. Returning
  after the loop permits multiple matching purchases and a consistent zero result.
- Corrected `Trasnaction` to `Transaction` and used `list[Transaction]` consistently.

The learner became confused by the combined task. Breaking it into one function
fix and one scenario at a time helped; continue this approach when needed.

### Implementation and results

Source: [monthly_budgets.py](exercises/monthly_budgets.py).

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

### Next task

Automated tests: begin with assertions, then introduce pytest and its setup.
Cover multiple matches, no matches, empty input, and overspending. Explain imports
before expecting the learner to use them. Milestone 1 remains in progress.

<a id="lesson-09"></a>

## Lesson 09: 2026-10-27: Automated checks with assert

Status: complete.

### Concepts learned

`assert condition` checks an expectation. A true condition allows execution to
continue; a false condition raises AssertionError. An unhandled failure stops
the script, so a success message must appear after every check it describes.

Assertions automate comparisons previously made by reading terminal output.
They are development checks, not input validation: Python can omit them with
optimization enabled. Continue using explicit validation and exceptions for
invalid user data.

### Exercise and results

Source: [monthly_budgets.py](exercises/monthly_budgets.py).

```python
assert calculate_category_total(transactions, "Groceries") == Decimal("525.00")
assert calculate_category_total([], "Groceries") == Decimal("0.00")
print("Both checks passed")
```

Learner intentionally changed the first expectation to `524.00` and shared the
resulting AssertionError, confirming that a mismatch is detected. The expectation
was restored to `525.00`, and the learner shared the passing output.

Mentor inspected and ran the current saved script successfully (exit 0), observing
`Both checks passed`. Both the multiple-purchase and empty-input checks are now
saved in the script. This is not yet a separate pytest test suite.

### Next task

Set up a project virtual environment, then introduce pytest, separate test
functions, discovery, and failure reports. Learner reports familiarity with
virtual environments but is happy to walk through the setup. Let the learner
run the setup commands; explain their purpose and verify the selected interpreter.

<a id="lesson-10"></a>

## Lesson 10: 2026-10-28: First pytest tests and import behavior

Status: first pytest lesson complete; recorded at this session checkpoint.

### Environment and commands

- A virtual environment provides a project-specific Python/package environment.
- pip installs packages; it is distinct from the environment itself.
- `python3 -m venv .venv` creates the environment.
- `source .venv/bin/activate` adjusts the current shell's PATH.
- `python -m pip install pytest` installs through the selected interpreter.
- `.venv/bin/python` explicitly selects the environment without activation.
- `.venv/` is ignored by Git; dependency recording remains a future setup task.

### Tests

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

### Imports and the main guard

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

### Verification

Learner reported all four tests passing. Mentor inspected the files and independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py -v
```

Observed Python 3.14.6, pytest 9.2.0, exit 0, and **4 passed in 0.01s**.
This verifies these tests; it is not a claim of complete application coverage.

### Next task

Teach `pytest.raises` to check expected validation exceptions. Before importing
the validation exercise, inspect its top-level demonstration and guard it as
needed. The Transaction in monthly_budgets.py currently has only category and
amount and no merchant validation; distinguish it from the earlier validated
model rather than assuming they are interchangeable. Keep the next exercise small.

<a id="lesson-11"></a>

## Lesson 11: 2026-10-28: Context managers and validation tests

Status: validation-testing exercise complete.

### Statements and expressions

A statement is an instruction Python executes, such as assignment, import,
return, or an if statement. An expression evaluates to a value, such as
`transaction.category == category`, which evaluates to a boolean. The colon
belongs to the surrounding if statement, not the comparison expression.

### Context managers and with

`with` is a statement that uses an object's context-manager protocol to manage
entry into and exit from a block. The context manager defines that behavior;
`with` itself does not mean file handling or expected-error checking.

After successful entry (`__enter__`), Python calls `__exit__` when the block ends,
including if its code raises an exception. The exit method receives exception
information and can suppress an exception or allow it to propagate.

Examples: files close on exit, locks release, and database transaction managers
may commit or roll back. `pytest.raises` checks an expected exception. Handling
an exception never resumes the interrupted block: remaining statements inside
it are skipped, and execution continues after the block if the error is handled.

A managed context is not a new variable scope. Scope describes where a name
can be accessed. Functions create local scopes; if, for, and with blocks do not
create separate variable scopes. Names assigned inside a with block can remain
accessible afterward, although a managed resource may already be closed.

### Why pytest.raises instead of just try/except?

For invalid input, ValueError is the expected correct behavior. A test that calls
`pytest.fail` upon catching that exception reverses the intended expectation.
A try/except that merely catches it also fails to detect the absence of an error.
An equivalent manual check needs an else branch to fail if no error is raised.

```python
with pytest.raises(ValueError):
    Transaction("", Decimal("20.50"), "Food")
```

This context manager passes the check when ValueError (or a subclass) occurs,
fails when no exception occurs, and lets unexpected exception types fail the test.
The learner needed several comparisons with try/except, then correctly restated
the distinction between the with statement and its context-manager object.

### Import lesson reinforced

Object construction runs initialization even without print statements. The
blank-merchant demonstration had to move under the main guard so importing the
validated class does not raise before pytest runs the test. The expected invalid
construction belongs inside the pytest.raises block in the test instead.

### Implemented and verified

Source: [test_transaction_validation.py](exercises/test_transaction_validation.py).

- Empty merchant raises ValueError.
- Whitespace-only merchant raises ValueError.
- Valid merchant is accepted and retained as an attribute; no raises context is
  needed because an unexpected exception automatically fails that test.

Learner shared passing output for each. Mentor inspected the saved tests and ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **7 passed in 0.01s**, exit 0. This includes the four earlier tests and
three merchant-validation tests, not complete application coverage.

### Next task

Introduce pytest parametrization to express the empty and whitespace merchant
cases as one test with multiple inputs. Explain the decorator before use;
general decorator mechanics and building decorators remain future lessons.
Keep the valid-input test separate. Shared transaction models and recording
development dependencies remain future project cleanup.

<a id="lesson-12"></a>

## Lesson 12: 2026-10-28: Pytest parametrization

Status: complete.

### Concept and implementation

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

### Debugging

Initially the function had no merchant parameter despite the decorator naming
one. Pytest reported an error during collection, before executing the tests.
Adding `merchant` to the function signature fixed the mismatch. The learner then
added the three-space input to complete all four planned invalid cases.

Reinforced context-manager understanding before this exercise: with uses an
object's entry and exit behavior; pytest.raises fails if no expected error occurs.
General decorator internals are still a later lesson, not considered mastered
solely from using this pytest decorator.

### Verification

Source: [test_transaction_validation.py](exercises/test_transaction_validation.py).

The learner reported all four invalid cases passing. Mentor inspected the saved
file and independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **9 passed in 0.01s**, exit 0. These are one setup subtraction test,
three category-total tests, one valid-merchant test, and four invalid-merchant
cases. The validation file alone now contains five runnable test cases, despite
having only two test functions.

### Next topic

Pytest fixtures: reuse sample-transaction setup across tests without repeating
construction code. Explain how requesting a fixture by name works and begin with
the default function scope so mutable test data is fresh for each test.

<a id="lesson-13"></a>

## Lesson 13: 2026-10-28: Pytest fixtures and sharing setup

Status: local fixture and conftest.py sharing exercises complete.

### Learner's distinction: fixtures versus parametrization

- **Fixtures: one setup definition → reused by many tests.**
- **Parametrization: one test definition → run with many input values.**

Reusing setup does not necessarily share one object: this default function-scoped
fixture constructs fresh sample objects for each requesting test. Providing a
list through a fixture does not automatically run a separate test for each item.
Both mechanisms can be used together. Parametrized fixtures remain a later topic.

### Latest verification: shared fixture

Learner moved sample_transaction into exercises/conftest.py, preserving its name
and three transactions. Mentor inspected both files: the local definition was
removed and tests request the fixture without importing it. Ran
`.venv/bin/python -m pytest exercises -v`: **10 passed in 0.01s**, exit 0.
Optional cleanup: remove the unused pytest import from test_monthly_budgets.py.
The earlier sections below describe the local-fixture stage before this move.

### Fixtures

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

### Names and sharing

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

### Implementation and verification

Source: [test_monthly_budgets.py](exercises/test_monthly_budgets.py).

The learner reused the local fixture in tests for Groceries 50.00 and Gas 20.00.
Empty-input and nonmatching-category tests remain independent of the fixture.
The learner reported four category tests passing.

Mentor independently ran:

```sh
.venv/bin/python -m pytest exercises/test_budget_basics.py exercises/test_monthly_budgets.py exercises/test_transaction_validation.py -v
```

Result: **10 passed in 0.01s**, exit 0: four category tests, five validation
cases, and one setup subtraction test. No test code was changed during recording.

### Next task

Optional small exercise: move the existing fixture into exercises/conftest.py,
remove its old definition, preserve its name and data, and rerun the tests.
Explain that shared setup is useful when multiple modules actually need it;
the current fixture is used only in one module, so moving it is a learning
exercise rather than a requirement for correctness.

<a id="lesson-14"></a>

## Lesson 14: 2026-10-28: uv, dependency resolution, and lockfiles

Status: setup complete and verified.

### What the tools do

- A virtual environment isolates a project's installed Python packages.
- A package manager installs packages and resolves dependencies. uv manages both
  project dependencies and the environment; it does not eliminate the environment.
- A direct dependency is one we request, such as pytest. Transitive dependencies
  are packages needed by those dependencies, such as pluggy.
- Pinning pytest alone in a requirements file would not pin every supporting
  package. A lockfile records resolved direct and transitive dependency versions.

### Project files

| File or directory | Purpose | Commit to Git? |
| --- | --- | --- |
| `pyproject.toml` | Metadata, supported Python version, and declared dependencies | Yes |
| `uv.lock` | Resolved dependency versions and package artifact information | Yes |
| `.venv/` | Local interpreter environment and installed packages | No |

The project requires Python `>=3.14`, has no declared runtime dependencies, and
records `pytest==9.2.0` in the dev dependency group. Version `0.1.0` describes
MyBudget, not Python or pytest. The lockfile is generated by uv; do not maintain
it manually. A lockfile does not freeze the OS or every aspect of the machine.

### Commands used and their purpose

```sh
uv init --bare --name mybudget --python 3.14
uv add --dev "pytest==9.2.0"
uv run python -m pytest exercises -v
```

- `init --bare` created only pyproject.toml for the existing project.
- `add --dev` recorded pytest, resolved its dependencies, generated uv.lock,
  and synchronized the environment.
- `run` selects and synchronizes the project environment before running a command.
- `uv run --locked ...` requires the existing lockfile to remain up to date
  rather than allowing an implicit lockfile update.

For someone cloning this repository with uv and a suitable Python available:

```sh
uv sync --locked
uv run --locked python -m pytest exercises -v
```

`uv sync --locked` recreates/synchronizes the environment using the recorded
resolution. It can download missing packages; the environment itself is not
copied through Git.

### Import-path error and correction

The learner initially ran `uv run pytest exercises -v`. Loading conftest.py
failed with `ModuleNotFoundError: No module named 'exercises'`.

Our imports start at the project root. Running `uv run python -m pytest ...`
from Mybudget ensures the current directory is on Python's module search path.
Launching the installed pytest command can set up that path differently.
This project uses the module invocation consistently; the fix required no test
logic changes.

### Activation is optional

```sh
source .venv/bin/activate
python -m pytest exercises -v
deactivate
```

Activation adjusts the current shell's PATH. Deactivation reverses that shell
setup without deleting the environment. `uv run` selects the project environment
without needing manual activation. Keep .venv ignored by Git.

### Verified result

Mentor inspected pyproject.toml and uv.lock and ran:

```sh
uv run --locked python -m pytest exercises -v
```

Observed Python 3.14.6, pytest 9.2.0, **10 passed in 0.02s**, exit 0.
The sandbox initially blocked uv's external cache; verification succeeded after
permission was granted. No application or test implementation was changed.

### Learning-record preference

Append each future completed lesson to this file, in learning order. Include
an explanation, focused examples, mistakes corrected, actual verification, and
next steps. Update the contents list and PROGRESS.md. Keep old lessons for
revision rather than prepending repeated session checkpoints. The dated files
in learnings/ are a historical archive; this is the primary revision document.

### Next recommended lesson

Introduce a shared application module and consolidate the repeated Transaction
models progressively. Explain responsibilities and agree on the small model
change before editing; do not generate the solution for the learner.

<a id="lesson-15"></a>

## Lesson 15: 2026-10-28: Models, packages, and a small refactor

Status: model-extraction exercise complete.

### What a model means

A model represents something the application works with. Transaction represents
the information about a purchase needed by the current calculation. Model is a
description of its role, not a Python keyword. models.py is an ordinary module.
Database and API models will later represent data for their specific purposes.

### Why move the class?

Reusable application code should have a home outside demonstration scripts.
A refactor changes organization while preserving behavior. Moving rather than
copying the class gives active callers one definition to maintain.

The learner created:

```text
mybudget/
├── __init__.py
└── models.py
```

An empty __init__.py makes this a regular Python package. models.py contains the
existing two-field dataclass:

```python
@dataclass
class Transaction:
    category: str
    amount: Decimal
```

It imports Decimal and dataclass itself. monthly_budgets.py and conftest.py now use:

```python
from mybudget.models import Transaction
```

The original budget-model definition and its dataclass import were removed from
monthly_budgets.py. Its calculation function and guarded demonstration remain.
This change relocates the model; it does not add validation or alter its fields.

### One change at a time

The earlier validation exercise has a different Transaction with merchant,
amount, category, and a merchant check. It remains separate. Consolidating that
model would require a deliberate field/validation change and caller/test updates.
Passing these tests does not mean the two models have already been unified.

### Verification

The learner reported passing tests and unchanged demonstration output. Mentor
inspected the saved model and imports and independently ran both commands:

```sh
uv run --locked python -m pytest exercises -v
uv run --locked python -m exercises.monthly_budgets
```

Both exited 0. Tests: **10 passed in 0.01s**. Demonstration: total limits 1100.00;
remaining Groceries -25.00, Restaurants 100.00, Gas 50.00, miscellaneous 150.00;
final output `Both checks passed`.

Run modules from the project root with -m so imports can find the sibling
mybudget package. The earlier test imports through exercises.monthly_budgets
still work because that module imports Transaction; updating them to its direct
application home can be part of the next small refactor.

### Next task

Move calculate_category_total into mybudget/calculations.py. Update the
demonstration and tests to import reusable code from its application home,
preserve behavior, and rerun the same checks. Let the learner make the move.
