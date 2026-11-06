# MyBudget: concepts for revision

A study guide to the concepts we have covered, grouped by topic. Read in order
for a refresher or use the contents to jump to a concept. Examples explain ideas;
they are not a log of daily activities or individual test results.

Keep extending the relevant sections as we learn. Current work and verification
belong in [PROGRESS.md](PROGRESS.md). The original chronological journal is
preserved in the [session history archive](learnings/SESSION_HISTORY.md).

## Contents

1. [Python and execution](#python-and-execution)
2. [Statements, expressions, and scope](#statements-expressions-and-scope)
3. [Functions and type hints](#functions-and-type-hints)
4. [Objects, references, and copying](#objects-references-and-copying)
5. [Classes, instances, and methods](#classes-instances-and-methods)
6. [Dataclasses and special methods](#dataclasses-and-special-methods)
7. [Decimal and money](#decimal-and-money)
8. [Collections and loops](#collections-and-loops)
9. [Iterables and iterators](#iterables-and-iterators)
10. [Dates and monthly reporting](#dates-and-monthly-reporting)
11. [Modules, packages, and imports](#modules-packages-and-imports)
12. [Exceptions and validation](#exceptions-and-validation)
13. [Context managers and with](#context-managers-and-with)
14. [Testing and pytest](#testing-and-pytest)
15. [Fixtures and parametrization](#fixtures-and-parametrization)
16. [Code organization and refactoring](#code-organization-and-refactoring)
17. [Environments, dependencies, and uv](#environments-dependencies-and-uv)
18. [Git and GitHub](#git-and-github)
19. [Quick revision questions](#quick-revision-questions)

## Python and execution

**Python is a language; CPython is software implementing that language.** CPython
is the interpreter we use, written primarily in C. `python3` launches the installed
interpreter; a `.py` file supplies source code for it to process.

```sh
python3 budget.py
```

Here, `python3` names an executable and `budget.py` is an argument. The shell
searches PATH to find the executable. A relative source path is resolved from
the current working directory.

An **executable** is a launchable program file on disk. A **process** is a running
instance, with memory and CPU time managed by the operating system. One application
can run several processes. Closing an application does not delete its executable.

For an ordinary CPython script:

```text
Shell finds Python → OS starts process → Python reads source
    → tokenization and parsing → compilation to bytecode → execution
```

Bytecode is an intermediate instruction format for Python's interpreter, not
native CPU machine code. CPython's evaluation machinery carries out its operations;
the CPU executes the interpreter's machine instructions underneath. One source
line can produce several bytecode instructions.

Syntax checking happens during source processing/compilation. The script must
compile before its top-level code runs, so a syntax error at the end can prevent
an earlier print from executing. A runtime error occurs when an executed operation
fails after compilation. Python is called interpreted, but CPython still compiles
to bytecode. **One command performs both stages.**

`python3` without a filename normally opens an interactive session in a terminal.
`python3 missing.py` instead reports that the requested file cannot be opened.

## Statements, expressions, and scope

An **expression evaluates to a value**. A **statement performs an instruction**
and may contain expressions.

```python
remaining = budget - spent
```

`budget - spent` is an expression; the whole assignment is a statement. Python
evaluates the right side and binds the left-hand name to the result. `=` assigns;
`==` compares.

```python
if transaction.category == category:
    total += transaction.amount
```

The comparison produces True or False. The `if`, colon, and body form a compound
statement. Indentation defines the body. `and` requires both conditions; `or`
requires at least one. Parentheses clarify the intended grouping:

```python
not (1 <= month <= 12)    # Negates the whole valid range.
month < 1 or month > 12   # Expresses the invalid cases directly.
```

**Scope is where a name can be accessed directly.** Parameters and assignments
inside a function are normally local to that call. Functions can read module-level
names. A function's local name is not directly accessible outside it.

```python
def calculate():
    total = 100
    return total

answer = calculate()
# answer is accessible here; calculate's local name total is not.
```

`if`, `for`, and `with` blocks do not introduce separate variable scopes. A name
assigned there can remain accessible afterward if assignment occurred. Scope is
not object lifetime: another reference can keep an object reachable after one
local name disappears.

## Functions and type hints

**A function names an operation and provides a reusable interface.** Parameters
are names in the definition; arguments are supplied by the caller.

```python
from decimal import Decimal


def calculate_remaining(budget: Decimal, spent: Decimal) -> Decimal:
    return budget - spent


remaining = calculate_remaining(Decimal("500.00"), Decimal("75.00"))
```

`def` creates a function. The body runs on a call. `return` ends that call
immediately and sends a value back. Reaching the end without returning produces
None. `-> None` describes no useful return value, such as a validation function.

**Return data from calculations; print where results are displayed.** Printing
shows text but does not return that text as the calculation result.

| Annotation | Intended value |
| --- | --- |
| `Decimal` | A Decimal instance |
| `list[Transaction]` | A list of Transaction instances |
| `dict[str, Decimal]` | A dictionary mapping strings to Decimal values |

Hints document contracts for people, editors, and static checkers. **Ordinary
Python execution does not enforce them or convert inputs automatically.**

```python
amount: Decimal = "hello"  # A hint does not turn this string into money.
amount = Decimal("49.99")  # A constructor call creates a Decimal object.
```

Function composition combines operations by calling existing functions. Our
monthly summary uses category spending and remaining-budget functions instead
of copying their rules.

### Functions as objects

Defining a function creates a function object and binds its name. Referring to
the name retrieves the object; parentheses call it:

```python
operation = calculate_remaining  # Existing function; no calculation yet.
result = operation(Decimal("500.00"), Decimal("75.00"))
```

operation and calculate_remaining refer to the same object. Assignment does not
itself mean object creation: the right-hand expression might create an instance,
retrieve an existing object, or call a function and produce its returned value.
Calling a class normally constructs an instance; calling a function executes its
body. Both use parentheses, but the callable determines what happens.

A function can receive another function as an argument:

```python
def run_calculation(operation, budget, spent):
    return operation(budget, spent)

result = run_calculation(calculate_remaining, Decimal("500.00"), Decimal("75.00"))
```

Pass the function without parentheses to let the receiver call it. Passing
calculate_remaining(...) instead evaluates that call first and passes its result,
which is a Decimal rather than the intended operation. Receiving a function lets
an operation's behavior be supplied by its caller. Returning functions and closures
will build on this to explain decorators.

### Nested functions and closures

A function can define and return another function. A **closure** lets the inner
function retain access to an enclosing function's local bindings, even after
the outer call finishes:

```python
def make_category_checker(category):
    def checker(transaction):
        return transaction.category == category
    return checker

is_grocery = make_category_checker("Groceries")
```

Calling make_category_checker creates and returns a checker function. Calling
is_grocery(transaction) later runs that inner function with its retained category.
Return checker without parentheses to return behavior for later execution;
return checker(...) would execute it immediately and return its result instead.

The captured name belongs to the **outer** function, not the inner function's
own local scope. Python retains bindings through closure cells; the returned
function keeps those cells reachable. It does not keep the entire outer call
running or manually copy every local variable. A closure retains access to a
binding, not necessarily a frozen snapshot of a value.

Separate calls can create independently configured functions, such as a grocery
checker and a gas checker. This is useful for callbacks and for decorators that
retain the function they wrap. In contrast, using only an inner function's own
parameters/locals does not require capturing an enclosing variable.

Optional inspection: function.__code__.co_freevars names captured variables;
function.__closure__ holds their cells, whose cell_contents exposes the binding.
Recognition matters more than memorizing inspection attributes: look for an
inner function using an enclosing function's local name.

### Function decorators: wrapping behavior

A decorator receives a function and returns a function to use in its place.
Our first example adds messages around an existing calculation:

```python
def announce(operation):
    def wrapper(budget, spent):
        print("Starting calculation")
        result = operation(budget, spent)
        print("Calculation finished")
        return result
    return wrapper

calculate = announce(calculate_remaining)
result = calculate(Decimal("500.00"), Decimal("75.00"))
```

Applying announce creates the wrapper without running the calculation. Calling
the returned wrapper later runs before/after behavior and the original operation.
The wrapper retains operation through a closure. The original function object
still exists; the wrapper delegates to it rather than modifying its body.

Return the original result so callers receive the same useful value. To perform
work afterward, store the value before returning; return operation(...) would
exit immediately. In this basic example, if operation raises, the after message
is skipped; guaranteed cleanup/timing would require a deliberate try/finally.

This first wrapper accepts only budget/spent. General argument forwarding,
metadata preservation, timing, and @ syntax are upcoming extensions, not implied
by completing this example.

## Objects, references, and copying

An **object** has a type, identity, and associated value/state. A **reference**
lets Python reach it. Names refer to objects; the name is not the object itself.

```python
other = purchase
```

No copy occurs. Both names refer to the same instance: **aliasing**. Changing
that instance's attribute through one name is visible through the other.

```text
purchase ──┐
           ├──→ one Transaction instance
other ─────┘
```

Assignment binds a name to the right-hand expression's result. That expression
might supply an existing object or create a new one. Function parameters refer
to supplied objects too; passing arguments does not automatically copy them.

| Operation | Meaning |
| --- | --- |
| `a is b` | Both references identify the same object |
| `a == b` | Equality under the type's rules |
| `id(a)` | Identity of the object while it exists |

Dataclasses normally compare field values for the same class. Separate instances
can be equal while `is` is false. In CPython, id is the memory address; other
implementations need not use addresses. IDs can differ between runs and be reused
after objects are destroyed.

```python
from copy import copy

another = copy(purchase)
```

For our Transaction this creates a separate instance, but it is a **shallow copy**:
attribute references are copied, not recursively duplicated objects. Independent
outer objects do not guarantee independent nested mutable data.

Lists and default dataclass instances are mutable. Decimal is immutable: arithmetic
produces a result object rather than changing the operand. Python follows references
to operate on values; **it does not subtract reference addresses** when evaluating
`budget - spent`.

## Classes, instances, and methods

**A class keeps related data and operations on that data together.** An instance
is one object of that class. Attributes hold data; methods express behavior.

```python
class Transaction:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount
```

Calling the class creates an instance and calls its initializer. `self` is that
instance and is supplied automatically in this call pattern. `amount` is a local
parameter; `self.amount` is an attribute that remains on the instance afterward.

```python
purchase = Transaction("Groceries", Decimal("40.00"))
print(purchase.amount)
```

Each instance has its own instance attributes. Behavior can mean validating data,
changing a category, or calculating with attributes. Validation is one kind of
behavior, not its entire meaning.

### When to choose a class or function

- Use a class to represent related information and responsibilities: a transaction
  or budget.
- Use a standalone function for an operation on supplied inputs: calculating totals
  across transactions.
- A method is a function associated with a class. Business logic can live in either
  place; choose where the responsibility fits.
- Dictionaries can group data too. A class provides a specific type and a place
  for its construction rules. A class can also primarily hold data.
- Do not create an otherwise meaningless calculator instance just to house a
  straightforward function.

An object is not automatically a database record or HTTP request. Later, code
will validate request data, construct objects, and persist records. Classes alone
do not provide user isolation or authorization.

## Dataclasses and special methods

A dataclass is an ordinary class with methods generated from declared fields.

```python
from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Budget:
    category: str
    limit: Decimal

    def __post_init__(self):
        if not self.category.strip():
            raise ValueError("Category must not be blank")
```

`@dataclass` is a class decorator: conceptually Python applies
`Budget = dataclass(Budget)` after the definition. It generates initialization,
representation, and equality behavior. General decorator implementation is a
future lesson; using the syntax is not mastery of all decorator mechanics.

| Method | Purpose |
| --- | --- |
| `__init__` | Initializes an instance |
| `__post_init__` | Hook called by the dataclass-generated initializer |
| `__repr__` | Developer-facing text representation |
| `__eq__` | Equality behavior for `==` |
| `__sub__` | Part of subtraction behavior for `-` |

Names must match exactly: `__postinit__` is not the recognized hook. Generated
assignment does not validate or convert fields automatically. Default dataclass
instances are mutable unless configured otherwise.

`repr(budget)` gives a representation such as
`Budget(category='Groceries', limit=Decimal('500.00'))`. `print(budget)` uses string
conversion; without a custom `__str__`, it falls back to the representation.
This describes the object without changing it.

## Decimal and money

Binary floats approximate many decimal fractions:

```python
0.1 + 0.2  # 0.30000000000000004
```

Construct Decimal from decimal strings for our monetary calculations:

```python
Decimal("0.1") + Decimal("0.2")  # Decimal('0.3')
```

`Decimal(0.1)` receives an already-approximated float. Integer minor units, such
as cents, are another valid representation with different trade-offs. Decimal
still has precision/rounding rules; it is not unlimited exact arithmetic for
every operation. A currency precision/rounding policy is future work.

### Valid type versus valid value

```python
if not isinstance(amount, Decimal):
    raise TypeError("Amount must be a Decimal")
if not amount.is_finite():
    raise ValueError("Amount must be finite")
```

Check type before calling a Decimal method. Decimal supports NaN and positive/
negative infinity: valid Decimal objects but invalid monetary values for us.
Finite zero and negative values pass is_finite().

Our domain conventions:

- Positive transaction amounts mean spending; negative ones mean refunds.
- Budget limits allow zero and reject negative values.
- Each transaction affects its own dated month. A later refund does not rewrite
  the original purchase month. A refund-only month can have remaining funds above
  the configured budget limit.

These rules differ by entity. Do not reject refunds because budget limits must
be nonnegative. Future bank providers may use different signs and need translation.

## Collections and loops

| Collection | Role | MyBudget example |
| --- | --- | --- |
| List | Ordered items; duplicates allowed | Transactions or Budget objects |
| Dictionary | Unique keys mapped to values | Category → remaining amount |
| Set | Unique values and membership checks | Previously seen category names |

Containers hold references to objects. A loop binds its variable to each object,
not a copy. This accumulator pattern belongs inside a calculation function:

```python
total = Decimal("0.00")
for transaction in transactions:
    if transaction.category == category:
        total += transaction.amount
return total
```

Initialize before the loop; add inside; return afterward. Initializing inside
loses previous results; returning inside stops early. Empty input leaves Decimal
zero unchanged. `range(9, 11)` yields the numbers 9 and 10: its stop is excluded.
See the next section for how iterators supply loop values.

### List comprehensions

A list comprehension builds a new list from an iterable, optionally filtering
items or transforming each value. It is useful for simple operations that read
more clearly than separate initialization, loop, and append statements.

```python
grocery_amounts = [
    transaction.amount
    for transaction in transactions
    if transaction.category == "Groceries"
]
```

The expression comes first; for describes traversal; the trailing if decides
which items to include. Nonmatching items contribute no entry.

To choose between two values rather than skip an item, put the conditional
expression before for:

```python
amounts_or_zero = [
    transaction.amount if transaction.category == "Groceries" else Decimal("0.00")
    for transaction in transactions
]
```

This includes one entry per input, replacing nonmatching amounts with zero.
A comprehension creates the full result list immediately. It consumes a generator
source if given one; it is not lazy merely because its source is a generator.
Use ordinary loops for multi-step logic, side effects, or complex error handling.
The main benefit is clarity for simple transformations, not making everything one line.

### Dictionary comprehensions and generated pairs

```python
limits = {budget.category: budget.limit for budget in budgets}
pairs = ((budget.category, budget.limit) for budget in budgets)
```

The dictionary comprehension eagerly builds a mapping. The generator expression
produces two-element tuples (key, value) on demand. dict(pairs) consumes those
pairs and builds the mapping in memory. There is no separate lazy dictionary
comprehension form. Repeated keys overwrite earlier values; validation is needed
when duplicates should be rejected rather than replaced.

### Dictionary lookup and assignment

```python
remaining[category] = amount   # Create or replace a value.
remaining[category] += amount  # Read existing value, add, then store.
category in remaining         # Check keys.
```

Reading an absent ordinary-dictionary key raises KeyError. defaultdict can supply
a default, but isn't necessary when assigning a complete result once. items()
provides key/value pairs; values() provides values. Lists have neither method.

When both operands are strings, `category in transaction.category` checks a
substring. Use `==` for our exact category matching, which is case sensitive.

### Duplicate detection with a set

```python
seen = set()
for budget in budgets:
    if budget.category in seen:
        raise ValueError("Duplicate budget category")
    seen.add(budget.category)
```

Check before adding. The first occurrence is accepted; the second is rejected.
This avoids silent dictionary overwrites. Duplicate budget categories and duplicate
bank transactions are different problems.

One scan of n transactions takes O(n) time. Dictionary/set membership is average
O(1) for suitable keys, not a worst-case guarantee. Our summary scans transactions
for each budget: roughly O(b × n). Deeper complexity/algorithm study remains ahead;
optimization should address measured needs.

## Iterables and iterators

An **iterable** can provide an iterator through `iter(...)`. An **iterator**
maintains progress and supplies its next item through `next(...)`.
A list stores items; its iterator tracks a traversal through those items.

```python
amounts = [Decimal("40.00"), Decimal("20.00"), Decimal("10.00")]
cursor = iter(amounts)
print(next(cursor))  # 40.00

for amount in cursor:
    print(amount)   # 20.00, then 10.00

for amount in cursor:
    print(amount)   # Nothing: this iterator is exhausted.

for amount in amounts:
    print(amount)   # 40.00, 20.00, 10.00: a fresh list iterator.
```

A for loop obtains an iterator once, repeatedly asks for its next item, and
stops on StopIteration. A manual next call on an exhausted iterator raises that
exception instead of quietly printing nothing.

An iterator is itself iterable: `iter(cursor)` returns that same cursor, not a
reset copy. Consequently a new for loop over an exhausted iterator does not
restart it. A list can supply a fresh independent iterator on each traversal.
Do not assume every iterable can be restarted: iterators are iterables too.

The loop always asks through iter(...); it does not need a separate type check.
An object's __iter__ defines what iterator it supplies. Lists supply fresh list
iterators; an iterator's __iter__ returns itself. The iterator's __next__ supplies
the next item. A list is iterable but not itself an iterator, so next(a_list)
raises TypeError; next(iter(a_list)) is valid.

Consuming a list iterator does not remove items from its source list. Exhaustion
belongs to that iterator's progress, not the list's contents. Creating another
iterator with `iter(amounts)` starts a new traversal.

This matters for MyBudget: a reusable list of transactions and a one-pass stream
cannot always be processed with the same repeated-loop assumptions. Generators
produce such streams on demand.

### Generators and yield

A function containing yield is a **generator function**. Calling it creates a
**generator object**, which is an iterator. Its body starts when a consumer asks
for the next value, not when that object is created.

```python
def sample_amounts():
    print("Preparing first amount")
    yield Decimal("20.00")
    print("Preparing second amount")
    yield Decimal("50.00")

cursor = sample_amounts()  # No preparation messages yet.
first = next(cursor)      # Runs to first yield, returns 20.00, and pauses.
for amount in cursor:    # Resumes and consumes the remaining value.
    print(amount)
```

yield is a keyword, not an iterator itself. It supplies a value and suspends
execution, preserving position and local state. return ends the generator;
reaching the end also exhausts it. Further next calls raise StopIteration, which
a for loop handles automatically. Create a new generator for a new traversal.

The consumer drives execution through next or a loop. Generators do not produce
continuously in the background and are not inherently async or parallel.
This is lazy, incremental production: a file reader can parse a record, yield
an amount, and resume when another is requested. A running total avoids storing
every amount. Using list(...) to collect all results retains them in memory again.

### Generator expressions

A generator expression is a compact way to produce values lazily:

```python
grocery_amounts = (
    transaction.amount
    for transaction in transactions
    if transaction.category == "Groceries"
)
total = sum(grocery_amounts, Decimal("0.00"))
```

The same comprehension with square brackets builds a list eagerly. Parentheses
around an expression containing for create a generator expression; parentheses
around an ordinary calculation do not. A generator expression is already an
iterator and has the same one-pass consumption behavior as a generator function.

sum consumes the matching amounts incrementally without creating an intermediate
amount list. Summing the same exhausted generator again returns the supplied
starting value. A source list still occupies memory; avoiding one intermediate
list does not make the entire program a stream. Printing a generator displays
its representation, not all its values.

Use a generator expression for a simple transformation consumed once. Use a list
comprehension when the result needs repeated traversal, indexing, or storage.

### Producing objects incrementally

Yielding from a prebuilt list is different from producing objects incrementally:

```python
def generate_transactions(count):
    for _ in range(count):
        yield Transaction("Groceries", Decimal("10.00"), date(2026, 10, 5))
```

Each request resumes the loop, constructs one Transaction, and yields it. In
contrast, building a list of transactions inside the generator creates every
listed object when that list-building statement is first executed. Lazy start
alone does not guarantee incremental production or low memory use.

The consumer can print each object and add its amount to a Decimal total without
retaining all previously yielded transactions. Producing more items than a fixed
prebuilt list contains would also fail if using indexed access; direct generation
avoids that unnecessary limit. `_` conventionally names a value not used by the body.

One-pass streams need care: a calculation that loops through its transaction
input repeatedly for different budgets may exhaust a generator on its first pass.
Review consumption patterns before replacing reusable lists with generators.

### Consumers and materializing a stream

list(source) is also a consumer of the iteration protocol. Conceptually, it gets
iter(source), repeatedly requests items, and stores references to each yielded
object until exhaustion:

```python
transactions = list(generate_transactions(3))
```

The generator function is called once to create a generator object. Item requests
resume that object; they do not call the generator function again. An internal
producer loop preserves its position across yields while an external consumer
loop requests values. Yield one Transaction per request, not a list containing
transactions, when the receiving calculation expects individual transactions.

After materialization the generator is exhausted, but the list can supply fresh
iterators for repeated traversals. This retains all objects and gives up the
incremental-memory advantage. list(an_exhausted_generator) is empty. Storing
references in the list does not itself copy the yielded objects.

In our per-budget calculation, the first category scan consumes every transaction,
including nonmatching ones. A second scan of the same generator has nothing left.
Materializing a fresh generator into a list restores correct repeated traversal.
An alternative is redesigning the calculation to accumulate category totals in
one pass, retaining only those totals.

### One-pass aggregation and Iterable inputs

Iterable[Transaction] describes an input that can supply transactions to a loop.
It accepts reusable collections such as lists and one-pass sources such as
generators. It does not promise indexing, length, or a fresh traversal. Iterator
is the narrower concept: an object with next-item behavior. A generator is both.

To total a stream by category, loop over transactions once and update a dictionary:

```python
totals = {}
for transaction in transactions:
    if transaction.category not in totals:
        totals[transaction.category] = transaction.amount
    else:
        totals[transaction.category] += transaction.amount
```

Alternatively, get(key, default) supplies a starting value without inserting it:

```python
totals[transaction.category] = (
    totals.get(transaction.category, Decimal("0.00")) + transaction.amount
)
```

Both forms preserve the same accumulation rule. This visits n transactions once
and retains k category totals: average O(n) time for dictionary operations and
O(k) additional storage, rather than retaining all n transaction references.
Each category's total can later be combined with its budget without rereading
the exhausted stream. This example totals across all dates; monthly filtering
must be included explicitly when applying it to a monthly report.

## Dates and monthly reporting

```python
from datetime import date

purchased_on = date(2026, 10, 5)
in_selected_period = purchased_on.year == 2026 and purchased_on.month == 10
```

The constructor takes year/month/day and rejects impossible calendar dates.
The instance's year, month, and day are integer attributes, not conversion
functions such as `date.day("10")`. Match both year and month so October in
another year is excluded.

Period validation must happen before processing data, even with no budgets or
transactions. A helper inside an empty loop never runs. Date-only values have no
time-of-day or timezone; converting provider timestamps to a reporting date is
a separate future decision.

## Modules, packages, and imports

| Term | Meaning |
| --- | --- |
| Module | Importable unit of code, often a .py file |
| Package | Organizes modules/subpackages; our regular package has __init__.py |
| Library | General term for reusable code |
| Standard library | Code supplied with Python |

```python
from decimal import Decimal  # Module → class
from copy import copy        # Module → function
import decimal              # Use decimal.Decimal(...)
```

Importing makes names available; calling a class creates an object. Each module
has its own namespace: importing Transaction doesn't also import the date name
from its defining file into the caller.

### Import-time execution and the main guard

A first normal import initializes the module by executing its top-level code,
even when requesting only one function. Assignments and calls run. def creates
a function without executing its body. Class bodies execute to build classes.
Imported modules are normally cached afterward.

```python
def calculate():
    return 42

if __name__ == "__main__":
    print(calculate())
```

Direct execution sets __name__ to __main__, so the demonstration runs. Importing
uses the module name and skips that guarded block. This prevents sample creation,
printing, and intentionally invalid construction during test imports.

### Finding modules

`from mybudget.models import Transaction` names models inside mybudget. Python
uses its module search path, not merely adjacent files. For our layout, run from
the project root:

```sh
uv run python -m exercises.monthly_budgets
uv run python -m pytest tests -v
```

`python -m` includes the current directory in the module search path for this
workflow. Launching an installed command directly may set the path differently.

## Exceptions and validation

An exception signals that an operation cannot complete normally. It interrupts
the current path and searches for a handler. If it escapes initialization, the
constructor does not return a successfully initialized instance.

```python
try:
    purchase = Transaction(category, amount, transaction_date)
except ValueError as error:
    print("Invalid transaction:", error)
```

Later lines inside try are skipped on failure. After handling, execution continues
after the handler; it never resumes the interrupted block. `as error` names the
exception object. Catch the expected type rather than hiding all programming bugs.

| Exception | Typical meaning |
| --- | --- |
| SyntaxError | Invalid source structure |
| NameError | Name isn't defined |
| AttributeError | Object lacks the requested attribute |
| TypeError | Wrong kind of input or unsupported operation |
| ValueError | Allowed type, unacceptable value |
| KeyError | Dictionary key doesn't exist |
| AssertionError | Asserted expectation is false |

`.strip()` returns text without surrounding whitespace; it doesn't modify the
stored string. Empty text is false, so `if not category.strip():` rejects empty
and whitespace-only categories. It assumes the input is a string; a broader input
policy is separate work.

Put rules where their inputs/state belong. Budget's initializer knows its category
and limit, not a separately supplied reporting month. A shared validate_month
function suits the current calculation entry points. A ReportPeriod class is a
possible future design, not necessary just to obtain a post-init hook.

## Context managers and with

**with is a statement. A context manager is the object supplying entry and exit
behavior around its block.**

```python
with open("notes.txt", "w") as file:
    file.write("Learning Python")
# File is closed when control leaves the block.
```

After successful entry, exit behavior runs when leaving the block, including
when it raises. File closing is reliable even when writing fails. Other managers
release locks, manage database transactions, or check expected test exceptions.

Python uses __enter__ and __exit__. `as file` binds the result of entry, which
need not always be the manager itself. Exit receives exception information, or
None values if no exception occurred. Returning a truthy value can suppress an
exception; otherwise it can propagate.

```python
with pytest.raises(ValueError):
    operation_expected_to_fail()
```

Here pytest supplies the manager. It verifies the expected exception occurred.
No exception means failure; an unexpected error also fails the test. Suppressing
an expected exception does not execute skipped lines inside the block.

**Managed context is not variable scope.** Names assigned inside with can remain
accessible afterward, although the resource may be closed. Ordinary arithmetic
doesn't need a with block.

## Testing and pytest

A test states expected behavior and compares the actual result. Good inputs
should distinguish correct behavior from a plausible incorrect implementation.

```python
def test_remaining_budget_when_over_limit():
    actual = calculate_remaining(Decimal("500.00"), Decimal("525.00"))
    assert actual == Decimal("-25.00")
```

Arrange–Act–Assert means prepare inputs, call the operation, check the result.
Pytest discovers test_*.py files and test_* functions. Names should describe
expected behavior; negative cases don't need a special naming convention.

`assert` raises AssertionError for a false condition. Python optimization can
disable assertions, so they are development checks rather than input validation.
Integer zero equals Decimal zero; use isinstance when result type matters too.

### Expected exceptions

```python
with pytest.raises(ValueError):
    Budget("Groceries", Decimal("-1.00"))
```

Here the exception means validation succeeded. A bare try/except that catches
it would not detect the absence of an error. Keep setup outside the block and
only the intended failing operation inside it.

### Test-first work and testing judgment

Write an expectation, observe a failure for the expected reason, implement the
behavior, then refactor while tests pass. Collection errors and assertion failures
occur at different stages. Tests can also document existing intended behavior.

Remember:

- Empty input differs from nonempty input with no matches.
- Test allowed boundaries as well as values just outside them.
- Filtering tests need excluded items, not only matches.
- Non-finite-value tests need Decimal objects, not strings rejected by a type check.
- A failing test may contain an incorrect input or expectation itself.
- Passing calculation tests don't establish correct demonstration output/imports.
- Move on once a concept is understood; repeat tests when a new idea or meaningful
  behavior/risk warrants them, not merely to repeat a familiar pattern.

```sh
uv run --locked python -m pytest tests exercises -v
uv run --locked python -m pytest tests -v
uv run --locked python -m pytest tests/test_refunds.py -v
uv run --locked python -m pytest tests/test_refunds.py::test_refund_reduces_monthly_spending -v
```

`-v` means verbose output, not different selection. Collection prepares test
cases; fixture setup happens before the test body; assertions run during the test.

## Fixtures and parametrization

**Fixtures: one setup definition → reused by many tests.**

```python
@pytest.fixture
def sample_amount():
    return Decimal("40.00")

def test_amount_is_positive(sample_amount):
    assert sample_amount > 0
```

Pytest finds the fixture by parameter name, calls it, and passes the returned
value into the test. The parameter receives data, not the fixture function.
By default it is function-scoped. A fixture constructing fresh objects each time
provides fresh data per requesting test. Reusing setup need not share an instance.

**Parametrization: one test definition → run with many input values.**

```python
@pytest.mark.parametrize("month", [0, 13])
def test_invalid_month(month):
    with pytest.raises(ValueError):
        validate_month(month)
```

The decorator names the parameter and supplies cases. The function must accept
that named parameter or collection fails. A list returned by a fixture doesn't
automatically create a separate test run for every item. These mechanisms can
be used together; parametrized fixtures and broader scopes remain future study.

### Location and setup errors

- Use a local fixture when only one test module needs it.
- tests/conftest.py supplies fixtures to tests there and below without explicit
  conftest imports; a sibling directory does not automatically see them.
- Redefining a fixture function name in one module replaces the earlier definition.
  Separate modules can have same-name local fixtures.
- Constructing an invalid object inside a fixture fails during setup, before the
  test's pytest.raises runs. Supply raw inputs or construct inside the checker.
- Merely defining an unused fixture does not run its body.

## Code organization and refactoring

```text
mybudget/   → application models and calculations
tests/      → application behavior tests and their fixtures
exercises/  → learning experiments and demonstrations
```

A **refactor** changes organization while preserving behavior. Move reusable
code to its application home rather than maintaining independent copies.

Calculate the full summary once, then present its entries:

```python
remaining = calculate_monthly_remaining(budgets, transactions, year, month)
for budget in budgets:
    print(budget.category, remaining[budget.category])
```

Calling the whole-summary calculation inside the printing loop recalculates every
category repeatedly. Correct output can still do unnecessary work.

Keep configuration separate from calculation rules. Prefer focused module names
such as models or calculations; introduce validation.py when it becomes a useful
boundary. Avoid a generic helpers.py collecting unrelated responsibilities.
Separate modules do not imply separate processes or services.

## Environments, dependencies, and uv

A virtual environment isolates a project's installed Python packages. A package
manager installs/resolves packages. uv manages both; the environment is still needed.

| Artifact | Purpose | Commit? |
| --- | --- | --- |
| pyproject.toml | Metadata, supported Python, declared dependencies | Yes |
| uv.lock | Resolved versions/artifacts, including transitive dependencies | Yes |
| .venv/ | Installed local environment | No |

A direct dependency is requested by our project. A transitive dependency is
needed by a dependency. Runtime dependencies support running the app; development
dependencies support development/testing. Pinning pytest alone doesn't pin all
supporting packages. Lockfiles record resolution, not the entire OS environment.

```sh
uv init --bare --name mybudget --python 3.14  # One-time setup, already done
uv add --dev "pytest==9.2.0"                  # Record a dev dependency
uv sync --locked                            # Synchronize from existing lock
uv run --locked python -m pytest tests -v    # Run in project environment
```

The project Python requirement describes supported versions, not the app's own
version. --locked requires an up-to-date lockfile rather than updating it implicitly.

Activation is optional with uv run:

```sh
source .venv/bin/activate
python -m pytest tests -v
deactivate
```

Activation changes the current shell's PATH. Deactivation doesn't delete .venv.
`python -m pip` selects pip through that interpreter. `sys.executable` helps verify
the selected interpreter. A virtual environment is not a complete virtual machine.

## Git and GitHub

Git stores local version history; GitHub hosts a remote copy. Saving, staging,
committing, and pushing are distinct operations.

```text
Edit/save → git add → staged changes → git commit → local history → git push → remote
```

| Command | Purpose |
| --- | --- |
| `git init -b main` | Initialize local history |
| `git status` | Inspect pending changes |
| `git add <paths>` | Select changes for a snapshot |
| `git diff --cached` | Review staged changes |
| `git commit -m "message"` | Save staged snapshot locally |
| `git log --oneline` | Inspect history |
| `git remote add origin <url>` | Save another repository's address |
| `git push -u origin main` | Upload and configure upstream tracking |

You can add origin after git init, before staging/committing. It doesn't upload.
HEAD identifies the current checkout; a branch name points to a commit. A clean
working tree doesn't itself establish that the remote has the latest commit.

.gitignore excludes matching untracked files from normal staging; it doesn't
remove secrets already committed. Keep .venv, local secrets, and real financial
records out of this repository, regardless of visibility.

## Quick revision questions

Try answering without looking above:

1. What happens between entering python3 budget.py and seeing output?
2. How do source code, executable, process, bytecode, and object differ?
3. Why does assignment alias rather than necessarily copy an object?
4. When is a class useful instead of a function? What does self refer to?
5. What does dataclass generate, and what do type hints not enforce?
6. Why construct Decimal from strings? Why can a Decimal still be invalid money?
7. How do return and print differ? Where should a loop's accumulator and return go?
8. Why can += on a missing dictionary key fail while = succeeds?
9. What executes when importing one function? Why use the main guard?
10. How do TypeError, ValueError, and fixture setup errors differ?
11. Who defines the behavior of with? Does it create a variable scope?
12. Why does pytest.raises fail when no exception occurs?
13. How do fixtures and parametrization differ? When does fixture code execute?
14. Could an incorrect filter pass a test containing only matching items?
15. Why validate a report month even with no configured budgets?
16. Why can a refund-only month have remaining funds above its budget?
17. What belongs in pyproject.toml, uv.lock, and .venv? Which go to Git?
18. Why does looping over an exhausted iterator print nothing, while a list can be traversed again?

### Coming next, not yet covered in depth

Iterator and generator basics are covered above. General decorator implementation,
advanced OOP/composition/protocols, deeper algorithms, databases, HTTP, frontend,
processes/threads/async, the GIL, distributed systems, security, and operations
remain on the roadmap. Mentioning a subject doesn't mean it has been mastered.
