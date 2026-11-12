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
    - [Object lifetime, weak references, and cyclic collection](#object-lifetime-weak-references-and-cyclic-collection)
5. [Classes, instances, and methods](#classes-instances-and-methods)
    - [Composition, instance methods, and default factories](#composition-instance-methods-and-default-factories)
    - [Properties versus instance methods](#properties-versus-instance-methods)
    - [Polymorphism, duck typing, and classes without instance data](#polymorphism-duck-typing-and-classes-without-instance-data)
    - [Inheritance, overriding, and super](#inheritance-overriding-and-super)
    - [Abstract base classes and required methods](#abstract-base-classes-and-required-methods)
    - [Class methods and alternative constructors](#class-methods-and-alternative-constructors)
    - [Static methods versus module functions](#static-methods-versus-module-functions)
    - [Encapsulation and public, internal, and private naming](#encapsulation-and-public-internal-and-private-naming)
6. [Dataclasses and special methods](#dataclasses-and-special-methods)
7. [Decimal and money](#decimal-and-money)
8. [Collections and loops](#collections-and-loops)
9. [Iterables and iterators](#iterables-and-iterators)
10. [Dates and monthly reporting](#dates-and-monthly-reporting)
11. [Modules, packages, and imports](#modules-packages-and-imports)
12. [Exceptions and validation](#exceptions-and-validation)
13. [Context managers and with](#context-managers-and-with)
    - [Text files and persistence](#text-files-and-persistence)
    - [JSON serialization and text encoding](#json-serialization-and-text-encoding)
    - [Converting domain objects to JSON data and back](#converting-domain-objects-to-json-data-and-back)
14. [Testing and pytest](#testing-and-pytest)
15. [Fixtures and parametrization](#fixtures-and-parametrization)
16. [Code organization and refactoring](#code-organization-and-refactoring)
17. [Environments, dependencies, and uv](#environments-dependencies-and-uv)
18. [Command-line interfaces and argparse](#command-line-interfaces-and-argparse)
    - [Subcommands and subparsers](#subcommands-and-subparsers)
19. [Git and GitHub](#git-and-github)
20. [Quick revision questions](#quick-revision-questions)

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

### Variable positional arguments: *args

An asterisk on a function parameter collects positional arguments into a tuple:

```python
def total_expenses(*amounts):
    return sum(amounts, Decimal("0.00"))

total_expenses(Decimal("10.00"), Decimal("20.00"))
total_expenses()  # amounts is an empty tuple; result is Decimal zero.
```

args is a conventional name, not a keyword: *amounts provides the same collection
behavior. A tuple is an ordered collection whose elements cannot be replaced,
added, or removed. It can still refer to mutable objects; immutability of the
container does not recursively make its contents immutable.

sum defaults to integer zero if no starting value is supplied. Giving Decimal
zero preserves the intended result type for empty inputs.

### Argument collection versus unpacking

The position of * or ** determines its role:

| Syntax | In a function definition | In a function call |
| --- | --- | --- |
| `*args` | Collect extra positional arguments into a tuple | Unpack iterable items into positional arguments |
| `**kwargs` | Collect extra keyword arguments into a dictionary | Unpack mapping entries into keyword arguments |

args and kwargs are conventional names, not special keywords. *amounts and
**details work the same way.

```python
def show(*args):
    print(args)

values = [10, 20, 30]
show(*values)  # Equivalent to show(10, 20, 30); prints (10, 20, 30).
```

This makes one call with three arguments, not three calls. The body prints the
tuple once; use a loop inside the function to print each value separately.
Without the star, show(values) receives one argument: the list itself.

```python
def show_budget(**details):
    print(details)

settings = {"category": "Groceries", "limit": 500}
show_budget(**settings)  # Equivalent to category="Groceries", limit=500.
```

At the call, the dictionary supplies named arguments. At the definition, those
arguments are collected into details. With explicit named parameters as well,
only the extra keyword arguments are collected by **kwargs.

** is not an exception-handling safety net. The mapping's keyword keys must be
strings, and the receiving signature must accept the resulting arguments.
Unexpected names without **kwargs, missing required arguments, or duplicate
values for a parameter can still raise TypeError.

These two directions let a generic decorator collect its caller's arguments and
then unpack them when forwarding to the original function, without knowing its
specific parameter names in advance.

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

### Decorator application with @

```python
@announce
def calculate(budget, spent):
    return calculate_remaining(budget, spent)
```

This means: define calculate, then rebind it with calculate = announce(calculate).
The decorator receives the newly defined calculate function, not the separate
calculate_remaining function it calls. announce returns wrapper; calculate then
refers to that wrapper. A later calculate(...) call invokes wrapper, which calls
the original calculate through its retained operation reference. That original
body delegates to calculate_remaining. Decoration and calculation happen at
different times: applying the decorator does not execute the calculation.

Decorators are useful for reusable surrounding behavior such as timing, logging,
caching, or retries. They add indirection, so prefer a plain call when wrapping
does not provide useful reuse or consistency. The first wrapper accepts only
budget/spent; use argument collection/unpacking to generalize it.

### Generic argument forwarding in decorators

```python
def announce(operation):
    def wrapper(*args, **kwargs):
        print("Starting operation")
        result = operation(*args, **kwargs)
        print("Finished operation")
        return result
    return wrapper
```

The wrapper definition collects positional arguments into args and keyword
arguments into kwargs. The operation call unpacks them, preserving how the
caller supplied inputs. The wrapper need not name budget/spent/category itself.

For calculate(Decimal("500.00"), spent=Decimal("75.00")), args contains one
Decimal and kwargs maps spent to the other. The same wrapper also accepts a
category-only function. It forwards arguments; it does not make invalid arguments
valid or silence errors raised by the original function.

Returning result preserves the original function's output. Metadata preservation
requires another step; flexible forwarding alone does not supply it.

### Function metadata and functools.wraps

Functions expose descriptive attributes such as __name__ and __doc__. A docstring
is a string placed first in the function body. Rebinding a decorated function's
name to a wrapper normally exposes the wrapper's name/documentation instead.

```python
from functools import wraps

def announce(operation):
    @wraps(operation)
    def wrapper(*args, **kwargs):
        return operation(*args, **kwargs)
    return wrapper
```

wraps copies useful original metadata onto the wrapper, including name and
docstring, and supplies __wrapped__ pointing to the original callable. The
wrapper still executes and remains a different object; its body is not replaced.

After decorating calculate, calculate.__name__ describes the original function;
calculate.__code__.co_name still identifies the wrapper's compiled code name.
calculate.__wrapped__ accesses the original function. The wrapper's previous
metadata is not separately saved automatically; inspect or save it before copying
if needed. A missing original docstring produces None, which is expected.

Metadata helps inspection, documentation, and tooling represent a decorated
function meaningfully. It does not enforce types, validate arguments, or preserve
business behavior automatically; the wrapper must still forward and return correctly.

### Measuring elapsed time with a decorator

time.perf_counter() supplies a high-resolution elapsed-time reading in seconds.
Its absolute value is not a calendar timestamp; subtract two readings to obtain
a duration. The elapsed interval includes waiting as well as execution.

```python
start = perf_counter()
result = operation(*args, **kwargs)
elapsed = perf_counter() - start
print(f"{operation.__name__} took {elapsed:.6f} seconds")
return result
```

Place this inside a generic wrapper with wraps(operation) to retain descriptive
metadata. :.6f controls displayed decimal places, not measurement accuracy.
The decorator adds its own overhead. Tiny operations and single samples cannot
establish a reliable benchmark or an application's capacity.

This simple form reports time only when the operation returns normally. If it
raises, subsequent timing/printing is skipped. Use try/finally to report on exit:

```python
start = perf_counter()
try:
    result = operation(*args, **kwargs)
finally:
    elapsed = perf_counter() - start
    print(f"{operation.__name__} took {elapsed:.6f} seconds")
return result
```

On success, finally reports time and the function returns result. On failure,
finally still reports time and the original exception continues outward; the
return after the block is not reached. The wrapper preserves failure semantics
instead of turning errors into normal-looking results.

### Preserving the wrapped function's result

A decorator can inspect a calculation's result and report status without
replacing its return value:

```python
def report_status(operation):
    def wrapper(budget, spent):
        balance = operation(budget, spent)
        print("Within budget" if balance >= 0 else "Over budget")
        return balance
    return wrapper
```

Returning a status string instead would change the calculation's interface: a
caller expecting Decimal could no longer use its result in arithmetic. Printing
the status and returning balance are separate responsibilities. Zero means
exactly at the limit and belongs with the within-budget case.

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

### Object lifetime, weak references, and cyclic collection

del removes a name binding (or a specified container entry/attribute); it does
not directly command destruction of the referenced object. Other references may
keep the object alive. In CPython, reference counting normally reclaims an object
when its reference count reaches zero. Exact reclamation timing is not a portable
promise across Python implementations.

```python
first = Note("Learning memory management")
second = first
observer = weakref.ref(first)

del first
print(observer() is not None)  # True: second still keeps it alive
del second
print(observer() is None)      # True in our CPython experiment
```

A weak reference observes an object without keeping it alive. Calling it returns
the object if it exists, otherwise None. Our ordinary dataclass Note supports
weak references; not every Python object supports them. Holding the object
returned by the observer in another variable would itself keep it alive.

Reference counting alone cannot reclaim every unreachable object. In a cycle,
objects may reference each other after all outside strong references disappear:

```text
Rest of program: no strong path to either object
       A → B → A
```

The internal references are real, but the group is unreachable from the rest
of the running program. CPython's cyclic collector detects unreachable cycles
among tracked objects and can reclaim them despite their nonzero counts.
Deleting the names did not already delete the objects; it removed the program's
access paths. Internal references do not make an isolated group reachable.

```python
import gc
import weakref

class Node:
    pass

was_enabled = gc.isenabled()
gc.disable()
try:
    first = Node()
    second = Node()
    first.other = second
    second.other = first
    observer = weakref.ref(first)
    del first
    del second
    print(observer() is not None)  # True before cyclic collection
    gc.collect()
    print(observer() is None)      # True after explicit collection
finally:
    if was_enabled:
        gc.enable()
```

gc.disable disables automatic cyclic collection, not reference counting.
gc.collect explicitly requests collection even while automatic collection is
disabled. Restoring the prior setting makes the experiment self-contained;
normally leave automatic collection enabled. This cycle example illustrates
the mechanism; its execution status is tracked in PROGRESS.md.

Reclaimed object memory need not immediately reduce the process's operating-system
memory footprint, since Python's allocators may retain memory for reuse. Do not
depend on garbage collection for timely resource cleanup: with remains the right
tool for files and other resources with defined exit behavior.

Revision checks: What does del remove? Why does a second reference keep an object
alive? Why does a weak reference not do so? Why can reference counts stay nonzero
for unreachable objects? What does gc.disable leave enabled?

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

### Composition, instance methods, and default factories

Composition builds an object using other objects: a BudgetTracker **has
transactions**. The tracker keeps a list of references to Transaction instances;
adding a transaction does not copy it. One class can create many independent
tracker instances; separate class definitions are unnecessary.

```python
from dataclasses import dataclass, field

@dataclass
class BudgetTracker:
    transactions: list[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)
```

add_transaction is an instance method. In first.add_transaction(transaction),
self refers to first. The method changes that instance's list; -> None indicates
it returns no result. A dataclass still supports methods you define: generated
initialization and custom operations work together.

default_factory=list tells the generated initializer to call list() when no
transactions argument is supplied. The default is a fresh empty list [], not
the integer 0. Each such instance receives a different list:

```python
first = BudgetTracker()
second = BudgetTracker()
first.add_transaction(transaction)

print(first.transactions is second.transactions)  # False
print(first.transactions[0] is transaction)        # True
```

Passing an explicit list bypasses the factory for that field. BudgetTracker(items)
stores that list reference; it does not copy items. Passing the same list to two
trackers makes them share it, so additions through either tracker are visible
through both. The factory does not guarantee independence for supplied lists.

Use field(default_factory=list), passing the callable list rather than calling
list() there. The callable creates each default when an instance needs it.
Dataclasses reject a direct list default such as transactions = [] for this field.

Revision checks: What does self refer to during a method call? What is composed
inside a tracker? When does the factory run? Why can lists be distinct while a
contained transaction is the same object?

### Properties versus instance methods

A property provides attribute-style access backed by code. @property decorates
a getter method; reading the attribute invokes that getter without parentheses:

```python
# Inside BudgetTracker:
@property
def total_spent(self) -> Decimal:
    return sum(
        (transaction.amount for transaction in self.transactions),
        Decimal("0.00"),
    )

# Caller:
print(tracker.total_spent)
```

tracker.transactions reads a stored list attribute; tracker.total_spent executes
the getter to compute a value. This getter sums the current list on each access.
property does not cache the result or store a separate running total. Appending
another transaction changes the result of the next access.

An ordinary instance method calculate_total() can use exactly the same code.
There is no calculation or performance advantage inherent in choosing property.
For our tracker either interface is reasonable; property is optional.

| Interface | What it presents to callers |
| --- | --- |
| tracker.calculate_total() | An operation to perform |
| tracker.total_spent | A value associated with the object |

A property is useful when you want attribute access while calculating or
controlling the value. It can also preserve an existing attribute-style interface
if implementation changes from stored data to a calculation. Prefer ordinary
methods for actions, work requiring caller-supplied arguments, or surprising or
expensive operations such as network requests. A total over a very large list
may also warrant a method or a different implementation to make its cost clear.

A getter-only property rejects normal assignment such as
tracker.total_spent = Decimal("0.00") with AttributeError. This does not freeze
the tracker or its transactions: changing the source list still affects the
computed total. Setter/deleter behavior is a separate topic, not yet practiced.

Common mistakes: assuming a property is required whenever a method returns
data, assuming it caches its value, calling this Decimal-valued property with
parentheses, or treating a getter-only property as full object immutability.

Revision checks: Can a method compute the same total? What executes on each
property read? Why might attribute-style access be useful? What remains mutable
when a computed property has no setter?

### Polymorphism, duck typing, and classes without instance data

Polymorphism lets different objects respond to a shared operation with their
own behavior. In our example, objects of different classes are interchangeable
at the call site because each supports write(report):

```python
class ConsoleDestination:
    def write(self, report: str) -> None:
        print(report)

class FileDestination:
    def write(self, report: str) -> None:
        with open("polymorphism_report.txt", "w", encoding="utf-8") as file:
            file.write(report)

def deliver_report(destination, report: str) -> None:
    destination.write(report)

deliver_report(ConsoleDestination(), "Remaining budget: 424.75")
deliver_report(FileDestination(), "Remaining budget: 424.75")
```

deliver_report stays the same; the receiving object's method supplies the
behavior. Merely giving unrelated methods the same name is not the full idea:
the caller must be able to use them through a compatible operation. Here both
accept a report string. Python does not require a common parent class for this
example. Duck typing means using an object according to the operations it
supports rather than checking its exact class first.

This helps callers work with interchangeable implementations without adding
branches for each destination type. A new destination supporting write(report)
could be supplied without editing deliver_report. For tiny tasks a conditional
or a standalone function can also be reasonable; these classes demonstrate
the mechanism rather than being required just to print or save text.

Instance attributes are optional. ConsoleDestination provides behavior without
storing data on self; report is a method parameter, and self still refers to
the instance. A class can provide data, behavior, or both. If each file destination
needed a configurable filename, an initializer could store self.filename so
different instances remember different paths. A dataclass is not required when
there are no data fields to initialize here.

Common mistakes: assuming all classes require instance attributes, thinking
polymorphism requires inheritance, or assuming matching names alone guarantee
compatible parameters and behavior.

Revision checks: Which object selects the write implementation? What does
deliver_report need to know about its destination? Why is report not an instance
attribute? When might a file destination need instance state?

### Inheritance, overriding, and super

Inheritance defines a class as a specialized kind of another class. Composition
expresses a has-a relationship (a tracker has transactions); inheritance expresses
an is-a relationship (a labeled console destination is a console destination).
Use inheritance when that substitutability fits, not merely to avoid a few lines.

```python
class LabeledConsoleDestination(ConsoleDestination):
    def write(self, report: str) -> None:
        super().write(f"MyBudget: {report}")
```

ConsoleDestination is the base class; LabeledConsoleDestination is the subclass.
The class declaration establishes inheritance. The subclass can use inherited
methods, override them, or add new methods. Overriding means defining a method
with the same name to customize behavior. It can do work before and after a
super call or replace the behavior entirely.

super() does not establish inheritance or create a parent instance. It provides
access to the next implementation in the method resolution order. In this
single-inheritance example, super().write invokes ConsoleDestination.write with
the same subclass instance as self. Multiple inheritance and its lookup order
have not yet been practiced.

Instance data belongs to that one instance. Methods are normally stored on the
classes and found through attribute lookup, not copied into every instance.
Calling an inherited method does not switch to another object's data.

```python
class FileDestination:
    def __init__(self, filename):
        self.filename = filename

class LabeledFileDestination(FileDestination):
    def __init__(self, filename, label):
        super().__init__(filename)
        self.label = label
```

The base initializer assigns filename on the same instance on which the subclass
initializer assigns label. If a subclass defines no initializer, it inherits the
base initializer. When it defines its own initializer, the base initializer is
not automatically called; super().__init__(...) explicitly delegates that work.
This initializer example was explained, not exercised in the destination script.

Common mistakes: calling super a mechanism that creates inheritance, imagining
a separate parent instance, assuming methods are copied into each instance, or
forgetting required base initialization when overriding __init__.

Revision checks: Which line establishes inheritance? Can a subclass inherit a
method without super? What instance receives a super call? Where are methods
normally stored? How does initialization create inherited instance data?

### Abstract base classes and required methods

An abstract base class can declare operations that concrete subclasses must
provide before their instances can be created. It represents a general concept
such as a report destination without choosing where the report is written.

```python
from abc import ABC, abstractmethod

class ReportDestination(ABC):
    @abstractmethod
    def write(self, report: str) -> None:
        pass

class ConsoleDestination(ReportDestination):
    def write(self, report: str) -> None:
        print(report)

destination = ConsoleDestination()
destination.write("MyBudget report")
```

ABC supplies the abstract-class machinery; @abstractmethod marks write as a
requirement. pass is just an empty body and does not enforce anything itself.
ReportDestination cannot be instantiated while it has an abstract method.
A subclass containing only pass inherits the unimplemented abstract requirement
and also cannot be instantiated: creating it raises TypeError.

The concrete ConsoleDestination overrides write with a non-abstract method,
so object creation is allowed. No super call is required to fulfill this
requirement. If a subclass inherits a concrete implementation, it need not
override that method again merely to be instantiable. Inheriting ABC alone,
without any remaining abstract methods, does not prohibit instantiation.

This check ensures that an abstract requirement has a non-abstract implementation,
not that the implementation behaves correctly. An ordinary override whose body
is only pass satisfies this mechanism but does nothing. Parameter types and
compatible signatures are not automatically enforced by ABC either.

| Approach | Failure point for a missing implementation |
| --- | --- |
| Duck typing | Calling an unsupported operation fails at runtime |
| Abstract base class | Instantiating a subclass with remaining abstract methods raises TypeError |

An ABC is an optional explicit contract within an inheritance hierarchy; duck
typing remains valid without that hierarchy.

**Overriding versus overloading:** our exercise is overriding. A subclass defines
its own version of the inherited write method, making an abstract requirement
concrete. Overloading usually refers to multiple versions selected by parameter
signature. Repeating def write in one Python class does not create that dispatch;
the later definition replaces the earlier binding. Advanced alternatives have
not been practiced, so keep this lesson focused on overriding.

Revision checks: What marks write abstract? Why does an empty subclass fail at
construction? Why is the concrete implementation overriding? Does ABC verify
that the method prints anything or that its type hints are obeyed?

### Class methods and alternative constructors

@classmethod makes Python supply the class as the first argument, conventionally
named cls. An instance method receives an instance as self instead. A common use
is a named alternative creation method that prepares inputs, calls the normal
constructor, and returns the resulting instance:

```python
from dataclasses import dataclass
from decimal import Decimal

@dataclass
class BudgetConfig:
    category: str
    limit: Decimal

    @classmethod
    def from_dict(cls, data):
        return cls(
            category=data["category"],
            limit=Decimal(data["limit"]),
        )

budget = BudgetConfig.from_dict({"category": "Groceries", "limit": "500.00"})
```

Python passes BudgetConfig as cls. The method reads dictionary values, converts
the amount string to Decimal, calls cls(...), and returns a BudgetConfig object.
No existing instance is required. The normal constructor still works:
BudgetConfig("Groceries", Decimal("500.00")). The class method uses that
construction path rather than replacing it or bypassing initialization.

Why use it? It gives the class a discoverable, named creation recipe, similar
to date.fromisoformat(text). Repeated callers can use BudgetConfig.from_dict(data)
without repeating conversion details. A standalone function is equally valid;
class methods are optional organization, not a requirement for conversion.

Using cls rather than hardcoding BudgetConfig also lets an inherited factory
construct the subclass used for the call, provided its constructor accepts the
supplied arguments. That subclass example was discussed, not exercised.

The factory depends on a working constructor. @dataclass generates __init__ from
declared fields; removing category and limit means the generated initializer
does not accept them. Removing @dataclass without writing an appropriate
initializer also removes that generated behavior. from_dict does not create
constructor parameters or field definitions automatically.

Distinguish type(budget), the object's class, from type(budget.limit), its field's
type. Both creation routes can produce equal dataclass values with Decimal limits.
@classmethod is unrelated to @abstractmethod: one controls class binding; the
other marks an abstract requirement. They are not alternative forms of each other.

Revision checks: What is cls? Why is no instance needed to call from_dict?
Does from_dict replace __init__? Could a standalone function do this conversion?
What happens if the dataclass fields or generated initializer are removed?

### Static methods versus module functions

@staticmethod places a function on a class without supplying an automatic first
argument. It receives neither self nor cls and uses only the explicit arguments:

```python
class BudgetMath:
    @staticmethod
    def is_over_budget(budget: Decimal, spent: Decimal) -> bool:
        return spent > budget

BudgetMath.is_over_budget(Decimal("500.00"), Decimal("550.00"))  # True
```

| Method kind | Automatic first argument | Typical reason |
| --- | --- | --- |
| Instance method | self, the instance | Work with instance state |
| Class method | cls, the class | Work with the class, often through an alternative constructor |
| Static method | None | Group a closely related function under a class without using instance/class state |

A static method adds no calculation capability. A module-level function can do
the same work. Prefer a static method when the function belongs closely to an
existing class and that location makes it easier to find and understand. General
helpers can remain module functions, such as mybudget.calculations functions.
Do not create utility classes merely because helpers need a place to live:
modules already group related functions in Python. Our BudgetMath class is an
exercise in the mechanism, not a recommendation to move all calculations there.

Compared with the traditional Java utility-class pattern, a common Python
equivalent is a module of functions. That organizational difference does not
mean every helper needs a static method in Python.

Returning a comparison directly is sufficient for a boolean result. Over budget
means spent > budget; equality is exactly at the limit, not over it. A condition
budget - spent <= 0 incorrectly includes equality; use spent > budget or a
strictly negative remaining balance.

Revision checks: What does Python automatically pass to a static method? Could
the same helper be a module function? Why might it belong on an existing class?
How do you distinguish spending at the limit from spending over it?

### Encapsulation and public, internal, and private naming

Encapsulation provides a clear public interface while keeping implementation
details internal. For a tracker, add_transaction can be a public operation and
_transactions its internal storage. Naming communicates intended use; it is
not a security boundary.

| Name | Common shorthand | Actual Python behavior |
| --- | --- | --- |
| label | Public | Intended for external use |
| _label | Protected/internal | Convention only; directly accessible |
| __label | Private | Name mangling; accessible through its mangled name |

Python does not enforce Java-style protected/private attribute access. A caller
can access tracker._transactions, but should normally depend on the public
interface instead. Internal implementation may change without preserving those
details for callers. These conventions also apply to method names.

An attribute __label defined within BudgetTracker is mangled to
_BudgetTracker__label. tracker.__label normally raises AttributeError, while
tracker._BudgetTracker__label can access the attribute. Mangling helps prevent
accidental subclass name collisions, not intentional external access.

```python
class ReportDestination:
    def __init__(self):
        self.__label = "MyBudget"

    def show_label(self):
        print(self.__label)

class EmailDestination(ReportDestination):
    def __init__(self):
        super().__init__()
        self.__label = "Monthly email"
```

There is one EmailDestination instance with two differently named attributes:
_ReportDestination__label and _EmailDestination__label. The base method uses
the former. Developers can independently choose the same internal name without
accidentally overwriting each other's state. With a single shared _label name,
the subclass assignment would overwrite the base assignment on that instance.
When sharing/customizing the value is intentional, _label is often clearer;
double underscores are not needed for every internal attribute.

Names such as __init__, with double underscores at both ends, are special
protocol names, not this private-name convention. Name mangling applies to
double-leading names without the double-trailing form.

Properties are separate from access naming. @property can expose a computed
transaction_count through tracker.transaction_count instead of a method call,
but it does not hide the backing list or make it immutable. A normal method
could provide the count too.

Common mistakes: treating underscores as enforced permissions, calling mangled
data inaccessible, assuming inheritance requires reusing all internal names,
or equating a getter-only property with complete protection of its source data.

Revision checks: Which access rules are conventions? Why can a mangled name
still be accessed? Why might a base class and subclass independently need the
same internal name? How do __label and __init__ differ?

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

### try/finally and exit work

except handles a matching exception. finally performs exit work whenever control
leaves the try block, whether normally, through return, or through an exception.
It does not by itself catch the exception. Keep returns out of finally when they
would replace an earlier result or suppress an error. If finally itself raises,
it can also replace the outward failure; keep cleanup/reporting deliberate.

For `print(calculate(...))`, arguments are evaluated before print is called. If
calculate raises, its own finally can run, but the outer print never receives a
value and is not called. These are two separate output locations.

### Standard output, standard error, and buffering

print normally writes to stdout; an unhandled-exception traceback is written to
stderr. Buffering and how streams are merged can make a traceback appear before
an earlier print. Display order across these streams does not necessarily reflect
the order the Python statements executed.

For a terminal experiment, `uv run python -u -m exercises.timing_decorator` uses
unbuffered Python stdout/stderr. `print(..., flush=True)` can explicitly flush a
particular stdout message. This affects output delivery, not try/finally semantics.

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

### Building a context manager with a class

```python
from time import perf_counter

class Timer:
    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.6f} seconds")
        return False
```

For `with Timer() as timer:`, Timer() first creates the instance, then Python
calls its entry method. The value returned by __enter__ is bound to timer.
Returning self supplies the same instance, not a copy. It is optional: another
return value would be bound instead, and no return would provide None.

The keyword implements the context-manager protocol; a variable named timer is
not itself special. Normal start/stop methods would require explicit calls, but
the recognized dunder methods let with coordinate entry and exit. Special methods
can be called directly, but prefer the associated language operation for normal use.

On exit, Python supplies the exception class, exception instance, and traceback
object, or three None values for normal completion. Returning False lets any
exception propagate; it does not mean cleanup failed. Returning True suppresses
the exception, without resuming interrupted statements inside the block.

State shared between methods belongs on the instance: self.start is created in
entry and read in exit. Plain start would be local to __enter__; exit cannot
access it by that name. Reading self.start without first assigning it raises
AttributeError. Each Timer instance has its own attributes. Returning self alone
does not copy local variables into the instance.

The method names use double underscores, often pronounced dunder: dunder enter,
dunder exit. Python invokes these specific protocol hooks, not arbitrary method
names. The same principle connects iter/next and arithmetic to their special methods.

### How with, context managers, and decorators relate

These names describe different parts of one entry → work → exit pattern:

| Term | Role |
| --- | --- |
| Context manager | Object that defines entry and exit behavior around a block |
| `with` | Statement that uses that object and coordinates entry, body, and exit |
| `__enter__` / `__exit__` | Methods for implementing that behavior in a class |
| `@contextmanager` | Standard-library decorator that adapts a generator function into a factory for context managers |
| A function decorator such as `@timed` | Wraps a function call; useful when the entire call should receive the extra behavior |

Choose either the class implementation or the generator implementation; they
provide the same protocol to `with`. You do not need to implement both for one
timer. Use a class when explicit instance state or additional methods help. A
generator-based manager is convenient for a short setup/cleanup sequence.

`with` can surround several statements chosen by the caller. A timing decorator
surrounds calls to the decorated function. Direct start/stop method calls are
also possible, but the caller must arrange reliable cleanup with `try/finally`.
`with` packages that responsibility for reuse. Exit is arranged after successful
entry, including when the body raises; if entry itself fails, its exit method
is not automatically called.

### Building a context manager with a generator

```python
from contextlib import contextmanager
from time import perf_counter

@contextmanager
def timer():
    start = perf_counter()
    try:
        yield
    finally:
        elapsed = perf_counter() - start
        print(elapsed)

with timer():
    print("Doing budget calculations")
```

The sequence is:

1. `timer()` creates a context manager through the decorator.
2. On entry, the manager advances the generator: record start, then pause at yield.
3. Python runs the indented **with body** while the generator is suspended.
4. On exit, the manager resumes the generator. Its finally block reports elapsed
   time; an exception from the body is delivered back at the yield point, so
   finally also runs on that path.

`yield` does not call timer or execute the with body itself. It provides a pause
point; the context manager handles advancing and resuming the generator. This
generator must yield exactly once. Bare yield supplies None; yielding a value
would make that value available through `with timer() as value`.

The generator retains its local start across suspension. In the class version,
separate methods shared self.start instead. The try/finally structure ensures
cleanup; yield alone does not guarantee it. With no exception handler suppressing
the body's error, that error propagates after cleanup.

Revision checks: Who calls timer? Who advances its generator? What runs while
the generator is paused? Why is yield inside try? When would a function decorator
be more convenient than a with block?

### Text files and persistence

Objects in memory ordinarily disappear when the process ends. A file stores
information on disk for later runs. Text is encoded as bytes; encoding="utf-8"
explicitly selects that representation. Saving display text does not preserve
the Python object's type or automatically reconstruct it when read.

```python
remaining = calculate_remaining(Decimal("500.00"), Decimal("75.25"))

with open("budget_note.txt", "w", encoding="utf-8") as file:
    file.write(f"Remaining budget: {remaining}\n")

with open("budget_note.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)
```

open returns a file object. Its context-manager entry supplies the object bound
to file; exit closes it, including when the body raises. This behavior is built
in; no custom context manager is needed.

- "w" creates a file if needed, or truncates an existing file when opened.
- "r" opens an existing file for reading; a missing file raises FileNotFoundError.
- write(text) writes a string; the f-string converts our Decimal into display text.
- read() without a size reads the remaining contents into a string in memory.
- `\n` is a newline. print adds another newline by default, so printing content
  that already ends in one can display an extra blank line.

A relative path such as budget_note.txt is resolved against the process's
current working directory, not automatically the script's directory. Running
our module from the MyBudget root creates the file there.

Closing the file does not delete its saved contents or the content string in
memory. The with block introduces no variable scope: content remains accessible
afterward, while further reads through the closed file object fail.

Common mistakes: accidentally overwriting existing contents with "w", expecting
read to return a Decimal, or assuming paths follow the source file's location.

Revision checks: Why use with for files? When does "w" erase previous contents?
What remains after closing the file? Where are relative paths resolved?

### JSON serialization and text encoding

Serialization converts data into a representation that can be stored or sent.
Deserialization reads that representation back into usable data. JSON is a text
format for structured values such as objects, arrays, strings, numbers, booleans,
and null. Python's json module maps dictionaries to JSON objects and lists to
arrays; loading reconstructs corresponding Python values, not arbitrary classes.

```python
import json
from decimal import Decimal

remaining = Decimal("424.75")
data = {"category": "Groceries", "remaining": str(remaining)}

with open("budget.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

with open("budget.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

amount = Decimal(loaded["remaining"])
```

| Function | Input/output |
| --- | --- |
| json.dump(data, file) | Writes JSON text to a file object |
| json.dumps(data) | Returns JSON text as a Python string |
| json.load(file) | Reads JSON from a file object and returns Python data |
| json.loads(text) | Parses JSON text from a string and returns Python data |

Remember the s as "string." Passing a file as a second positional argument to
dumps raises TypeError; use dump for the file operation.

The default JSON encoder does not support Decimal: attempting to serialize one
raises TypeError. We explicitly store its decimal string to preserve the value
without converting through a binary float. On loading, it remains a string
until our code calls Decimal. JSON does not know that the remaining field means
money or that its string should become a Decimal.

Serialization and character encoding perform different conversions:

```text
Python dictionary → JSON text → UTF-8 bytes on disk
                  serialize     encode

Bytes on disk → JSON text → Python dictionary
               decode      deserialize
```

json.dump supplies JSON text; the file object opened with encoding="utf-8"
encodes that text into bytes. Reading reverses those steps. UTF-8 describes how
characters are represented as bytes, not how dictionaries are structured; it
also applies to ordinary text files. JSON may escape characters in its textual
representation; those escapes are separate from the file's character encoding.

Common mistakes: confusing dump with dumps, expecting Decimal to serialize
automatically, assuming loaded strings regain their original Python types, or
treating serialization and encoding as the same operation.

Revision checks: What does load return for our saved dictionary? Why explicitly
convert the amount twice? How does JSON serialization differ from UTF-8 encoding?
Which function would produce JSON text without opening a file?

### Converting domain objects to JSON data and back

A domain object such as Transaction groups application data and rules. The
default JSON encoder cannot directly serialize that custom object, Decimal, or
date. Explicitly convert its attributes into supported values:

```python
transaction_dict = {
    "category": transaction.category,
    "amount": str(transaction.amount),
    "transaction_date": transaction.transaction_date.isoformat(),
}
```

date.isoformat() produces text such as "2026-10-05". After dumping this dictionary
and loading it, reconstruct the domain object explicitly:

```python
restored = Transaction(
    category=loaded["category"],
    amount=Decimal(loaded["amount"]),
    transaction_date=date.fromisoformat(loaded["transaction_date"]),
)
```

The round trip is Transaction → dictionary with strings → JSON text → loaded
dictionary → new Transaction. json.load does not call Transaction or restore
Python-specific types. The constructor restores the object and runs its existing
__post_init__ validation; the explicit conversions can also raise errors first.

For this dataclass, restored == transaction compares field values and is True
when the round trip preserves them. They are distinct instances; equality does
not mean that loading recovered the same in-memory object.

Common mistakes:

- dictionary[category] looks up the variable category; dictionary["category"]
  uses a literal string key. An undefined unquoted name raises NameError.
- Convert transaction.amount, not transaction.category, for the amount field.
  Decimal("Groceries") raises decimal.InvalidOperation because it is not numeric.
- Access the date through transaction.transaction_date before calling isoformat.
- Constructor keyword names must match exactly: transaction_date and
  transation_date are different names; the latter raises TypeError here.
- After correcting conversion code, rerun the writing step so the saved file
  contains the corrected data.

Revision checks: What type does json.load return here? Which step reconstructs
the date? When does model validation run? Why can == be True for separate objects?

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

## Command-line interfaces and argparse

A command-line interface (CLI) accepts inputs when a program is launched and
displays results in the terminal. Python's standard-library argparse module
parses command-line text into named values and supplies usage/help output.

```python
import argparse
from decimal import Decimal
from mybudget.calculations import calculate_remaining

def main():
    parser = argparse.ArgumentParser(description="MyBudget calculations")
    parser.add_argument("--budget", required=True)
    parser.add_argument("--spent", required=True)
    args = parser.parse_args()
    return calculate_remaining(Decimal(args.budget), Decimal(args.spent))

if __name__ == "__main__":
    print(main())
```

From the project root:

```sh
uv run python -m mybudget.cli --budget 500.00 --spent 75.25
uv run python -m mybudget.cli --help
```

ArgumentParser configures the interface. add_argument declares each named option;
required=True means it must be provided. parse_args normally reads the process's
command-line arguments and returns a Namespace, accessed here as args.budget and
args.spent. Without an explicit type conversion, these values are strings.
Decimal converts them for the existing arithmetic function. --help displays
generated help and exits without performing the calculation.

The CLI handles input/output; calculations.py retains the arithmetic. A main
function provides a callable entry point, and the main guard runs it only when
the module is executed as the program rather than normally imported.

return passes a value to the caller; it does not display that value. main()
alone discards this returned Decimal when run as a module. print(main()) both
calls main and displays its result. An interactive Python prompt may display
expression results automatically; ordinary module execution does not.

The module name mybudget.cli maps to mybudget/cli.py in this project. Create and
save that file before running it; running from the right directory cannot make
a missing module exist. Commands and file paths are separate: the root is
Mybudget, while the package directory inside it is mybudget.

### Custom argument conversion and readable errors

argparse accepts a conversion callback through type=. Pass the function object
without parentheses; argparse calls it with argument text and stores its return
value in the parsed Namespace:

```python
from decimal import Decimal, InvalidOperation

def parse_amount(text: str) -> Decimal:
    try:
        return Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(
            "Enter a numeric amount, for example 500.00"
        )

parser.add_argument("--budget", required=True, type=parse_amount)
parser.add_argument("--spent", required=True, type=parse_amount)
```

args.budget and args.spent are now Decimal values; main need not convert them
again. This connects function objects to library callbacks: the library controls
when the supplied function is called.

Catch InvalidOperation specifically rather than using bare except, which also
catches unrelated failures and interruption exceptions. Translate the conversion
failure to ArgumentTypeError to expose a useful input message at the CLI boundary.
argparse also catches TypeError and ValueError from a converter, but normally
supplies its own generic invalid-value message for those. ArgumentTypeError lets
our message appear with the offending argument's name.

For invalid text, argparse prints usage and its error message to standard error
and exits with status 2 instead of showing a traceback. Normal calculation exits
with status 0. The reusable calculation function remains independent of CLI
error presentation.

This converter checks parseability, not the complete policy for money:
Decimal("NaN") and Decimal("Infinity") parse successfully. Finite-value checks
and budget/spending sign policy remain deferred, not implemented by this handler.
CLI-specific automated tests are also not yet added.

Revision checks: What type is args.budget without a converter? What does argparse
provide for --help? Why separate main from the guard? Why is return alone silent
in a module? Which directory should contain cli.py? Why pass type=parse_amount
instead of calling it? How does ArgumentTypeError affect error presentation?

### Subcommands and subparsers

A subcommand selects an operation within one command-line program. Git's status,
commit, and push and uv's run, add, and sync illustrate this command pattern;
these examples do not imply those tools use Python's argparse internally.

A subparser defines a subcommand and the arguments belonging to it. It does not
automatically call an application function with a matching name.

```python
parser = argparse.ArgumentParser(description="MyBudget")
commands = parser.add_subparsers(dest="command", required=True)
calculate_parser = commands.add_parser(
    "calculate", help="Calculate the remaining budget"
)
calculate_parser.add_argument("--budget", required=True, type=parse_amount)
calculate_parser.add_argument("--spent", required=True, type=parse_amount)

args = parser.parse_args()
```

- add_subparsers creates the object used to register commands.
- dest="command" stores the selected name in args.command.
- required=True requires a command to be selected.
- add_parser("calculate") registers the command and returns its argument parser.
- Arguments added to calculate_parser belong to that command.
- The main parser's parse_args() reads input and uses the selected subparser.

For `python -m mybudget.cli calculate --budget 500.00 --spent 75.25`,
args.command is "calculate" and the amount fields are Decimals through our
converter. The program still explicitly calls calculate_remaining afterward.
With multiple operations it will need dispatch logic; registering a command alone
does not implement its behavior.

Each future subcommand can have different inputs: calculate uses budget/spent,
add could use category/amount/date, and report could use year/month. Only
calculate is currently implemented. Top-level --help describes commands;
calculate --help describes that command's inputs.

Common mistake: parser.calculate_parser() is not the parsing call. The name
calculate_parser is a local variable containing an object, not an attribute or
method automatically created on the main parser. Use parser.parse_args().
Parser configuration describes allowed input; parse_args actually reads it.

Revision checks: What is the difference between a command and its subparser?
Where does the selected name appear? Why call parse_args on the main parser?
Does naming a command calculate connect it to calculate_remaining automatically?

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
