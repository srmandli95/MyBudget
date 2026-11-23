# MyBudget: interview and revision notes

Direct answers to concepts covered so far. Read the first sentence for quick revision; use the example or distinction when you need more depth. These notes describe concepts, not which features or tests are complete. Current status belongs in [PROGRESS.md](PROGRESS.md).

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
14. [Text files and JSON](#text-files-and-json)
15. [Testing and pytest](#testing-and-pytest)
16. [Fixtures and parametrization](#fixtures-and-parametrization)
17. [Code organization and dependency injection](#code-organization-and-dependency-injection)
18. [Environments, dependencies, and uv](#environments-dependencies-and-uv)
19. [Command-line interfaces and argparse](#command-line-interfaces-and-argparse)
20. [SQLite and relational databases](#sqlite-and-relational-databases)
21. [HTTP and client-server communication](#http-and-client-server-communication)
22. [Git and GitHub](#git-and-github)

## Python and execution

### What is Python, and what is CPython?

**Python is a programming language; CPython is its most widely used implementation, written mainly in C.** The `python3` executable launches the installed interpreter. A `.py` file contains source code for it to process.

### What happens when you run `python3 app.py`?

**The shell finds the executable, the OS starts a process, and CPython compiles the source to bytecode and executes it.** Both compilation and execution happen through this one command. Bytecode is interpreter instructions, not native CPU machine code; the CPU runs the interpreter underneath.

### Is Python interpreted or compiled?

**In ordinary CPython execution, it is both: source is compiled to bytecode, then that bytecode is interpreted.** Execution is not simply reading and executing each source line independently. One source line can produce multiple bytecode instructions.

### How do syntax errors differ from runtime errors?

**Syntax errors prevent compilation; runtime errors occur when an executed operation fails.** A syntax error near the end of a script can prevent an earlier `print` from running. A `NameError` may occur after earlier valid operations have executed.

### What is an executable versus a process?

**An executable is a launchable program file; a process is a running instance with its own runtime state.** Python and Chrome have executables. Closing a process does not delete its executable. The shell normally locates commands through `PATH`.

## Statements, expressions, and scope

### What is an expression versus a statement?

**An expression evaluates to a value; a statement performs an instruction and can contain expressions.** In `remaining = budget - spent`, subtraction is an expression and the whole assignment is a statement. `transaction.category == category` is a boolean expression.

### What is scope?

**Scope determines where a name can be accessed directly.** For ordinary function name lookup, remember LEGB: Local, Enclosing function, Global module, Built-ins. Function parameters and assignments are normally local; `if`, `for`, and `with` do not create separate variable scopes.

### How do scope and object lifetime differ?

**Scope concerns access to a name; lifetime concerns how long an object exists.** A function's local name disappears after the call, but a returned object can remain alive through another reference.

### How should you express an invalid range?

**Reject values outside the full valid interval.** For months, use `not (1 <= month <= 12)` or `month < 1 or month > 12`. Negating only part of a compound condition changes its meaning.

## Functions and type hints

### What is a function?

**A function is a reusable callable that accepts arguments and performs an operation, optionally returning a result.** Parameters are names in its definition; arguments are values supplied by a caller. `def` creates the function; a call executes its body.

### How do `return` and `print` differ?

**`return` sends a value to the caller and ends the call; `print` displays text.** A function with no explicit return returns `None`. Ordinary scripts do not automatically display returned values; `print(main())` displays the result of `main()`.

### Are Python type hints enforced?

**Ordinary Python execution does not enforce type hints or convert values from them.** `amount: Decimal = "hello"` still binds a string. Hints support documentation, editors, and static checkers; validation and conversion need executable code.

| Hint | Intended value |
| --- | --- |
| `Decimal` | A Decimal instance |
| `list[Transaction]` | A list of Transaction objects |
| `dict[str, Decimal]` | String keys mapped to Decimal values |
| `-> None` | No useful returned result |

### What do `*args` and `**kwargs` do?

**In a definition they collect arguments; in a call they unpack values into arguments.** The names `args` and `kwargs` are conventions.

| Syntax | Definition | Call |
| --- | --- | --- |
| `*args` | Extra positional arguments → tuple | Iterable items → positional arguments |
| `**kwargs` | Extra keyword arguments → dict | String-keyed mapping → keyword arguments |

```python
values = [10, 20, 30]
show(*values)          # One call: show(10, 20, 30)
show_budget(**data)   # Mapping entries become named arguments
```

Unpacking does not make multiple calls. Unexpected, missing, or duplicate arguments can still raise `TypeError`.

### What does it mean that functions are objects?

**Functions can be assigned, passed as arguments, and returned like other objects.** `operation = calculate_remaining` passes the function; `operation = calculate_remaining(...)` calls it and assigns its result. This enables callbacks, closures, and decorators.

### What is a closure?

**A closure is a function that retains access to bindings from an enclosing function after that outer call has returned.** It captures bindings, not necessarily frozen copies of values.

```python
def make_checker(limit):
    def checker(amount):
        return amount <= limit
    return checker

within_budget = make_checker(500)
within_budget(400)  # Inner function still accesses limit
```

### What is a decorator?

**A decorator takes a function or class and returns the object that will be bound in its place, often adding behavior.** For a function, `@announce` above its definition is equivalent to `calculate = announce(calculate)`. The replacement is commonly a wrapper that calls the original.

```python
from functools import wraps

def announce(operation):
    @wraps(operation)
    def wrapper(*args, **kwargs):
        print("Starting")
        result = operation(*args, **kwargs)
        print("Finished")
        return result
    return wrapper
```

Use `try/finally` when after-work must run even on failure. Preserve the original result unless intentionally changing the interface.

### Why use `functools.wraps`?

**`wraps` preserves descriptive metadata such as the original name and docstring on a wrapper and adds `__wrapped__`.** It does not turn the wrapper into the original function. Copied `__name__` can differ from the wrapper's underlying `__code__.co_name`.

### How do you time an operation?

**Subtract two `time.perf_counter()` readings to measure elapsed duration.** Place the end reading in `finally` to measure failed calls too. Elapsed time includes waiting; `:.6f` changes display precision, not measurement accuracy. A tiny single call is not a reliable benchmark.

## Objects, references, and copying

### What is an object, and what does assignment do?

**An object has identity, type, and state/value; assignment binds a name to an object.** `second = first` does not copy the object. Both names refer to it. `=` does not mean every assignment creates a new object or a new memory location.

### What is `is` versus `==`?

**`is` compares identity; `==` invokes value-equality behavior defined by the type.** Two separately created dataclass instances can be equal without being the same object. `id(obj)` identifies an object during its lifetime; CPython uses its memory address, but that is not a portable Python guarantee.

### What is mutable versus immutable?

**A mutable object can change in place; an immutable object's value cannot.** Lists and dictionaries are mutable; strings, integers, and Decimal values are immutable. A tuple is immutable but can contain references to mutable objects.

### What is a shallow copy?

**A shallow copy creates a new outer object while retaining references to its nested objects.** Changing a shared nested list can affect both copies. Independent outer identity does not imply independent contents.

### How can Decimal objects be subtracted if variables contain references?

**Python follows the references and invokes the objects' subtraction behavior.** It subtracts their numeric values, not memory addresses, and produces a result object.

### What does `del` do?

**`del name` removes a name binding, not necessarily the object.** Other references can keep the object alive. Removing an attribute or container item similarly removes that particular reference.

### How does CPython reclaim objects?

**CPython primarily uses reference counting, supplemented by cyclic garbage collection.** Objects are normally reclaimed when their reference count reaches zero. The cyclic collector can reclaim unreachable groups that still reference each other. Internal references within an isolated cycle do not make it reachable from the rest of the program.

### What is a weak reference?

**A weak reference observes an object without keeping it alive.** Calling `weakref.ref(obj)` returns an observer; calling that observer returns the object if it remains alive, otherwise `None`. Not every type supports weak references.

### What do `gc.disable()` and `gc.collect()` do?

**`gc.disable()` disables automatic cycle collection, not reference counting; `gc.collect()` explicitly requests collection.** Exact collection timing is implementation-dependent. Reclaimed memory may stay in Python's allocator for reuse rather than immediately return to the OS. Use `with` for timely resource cleanup.

## Classes, instances, and methods

### When should you use a class instead of a function?

**Use a class when related state and operations benefit from a meaningful type and interface; use a function for an operation that does not need an instance.** A dictionary can also group data. Classes can provide data, behavior, or both; instance attributes are not mandatory.

### What are `self` and instance attributes?

**`self` refers to the instance receiving a method call; `self.amount` is an attribute on that instance.** A plain `amount` parameter is local to the call. Methods normally live on classes and are found through lookup; they are not copied into each instance.

### What is composition?

**Composition builds an object using other objects: a “has-a” relationship.** A BudgetTracker has Transaction objects. Appending a transaction to its list stores a reference, not a copy. Multiple independent trackers do not require multiple class definitions.

### Why use `field(default_factory=list)`?

**It creates a fresh empty list for each dataclass instance when no value is supplied for that field.** The default is `[]`, not `0`. Explicitly passing the same list to two instances still makes them share it; the factory does not copy supplied arguments.

### What is a property, and why use it instead of a method?

**A property provides attribute-style access backed by code.** A computed `tracker.total_spent` runs a getter; `tracker.calculate_total()` can compute the same result. The choice is an interface decision, not a calculation advantage. A property can preserve attribute syntax while controlling or computing the value.

A getter-only property rejects normal assignment but does not freeze the object. Properties do not automatically cache values; avoid hiding surprising or expensive work behind them.

### What is polymorphism?

**Polymorphism lets different objects be used through the same operation while each supplies its own behavior.** `destination.write(report)` can print through ConsoleDestination or save through FileDestination. Matching method names alone are insufficient if their interfaces or meaning are incompatible.

### What is duck typing?

**Duck typing uses an object according to the operations it supports rather than requiring a particular class.** `deliver_report` needs a suitable `write(report)`, not a specific destination type. A shared parent class is optional; unsupported operations fail when used.

### What is inheritance?

**Inheritance defines a class using another class's behavior: an “is-a” relationship.** A labeled console destination is a kind of console destination; a tracker has transactions through composition. Inheritance should fit substitutability, not merely save lines.

### What is method overriding?

**Overriding means a subclass defines its own version of an inherited method.** It can replace behavior, extend it, or delegate unchanged behavior. Even a body containing only `pass` counts as an override. The base class itself remains unchanged.

### Is `super()` required for overriding?

**No. Defining the subclass method creates the override; `super()` optionally delegates to the next implementation in the method resolution order.** In our single-inheritance examples that is the base method, running on the same instance—not a separate parent object.

```python
class LabeledConsoleDestination(ConsoleDestination):
    def write(self, report):
        super().write(f"MyBudget: {report}")
```

A subclass inherits an initializer when it does not define one. If it defines its own, base initialization is not automatic; call `super().__init__(...)` when required.

### How does overriding differ from overloading?

**Overriding customizes inherited behavior; overloading usually selects among same-named operations by signature.** Repeating a method definition in one Python class does not create Java-style overload dispatch—the later definition replaces the earlier binding. Advanced dispatch alternatives have not been covered.

### What is an abstract base class?

**An abstract base class declares requirements that must have concrete implementations before instances can be created.** Use `ABC` and `@abstractmethod`. A subclass that still has abstract methods cannot be instantiated and raises `TypeError`.

A non-abstract override containing `pass` satisfies this mechanism but does nothing. ABC does not verify useful behavior, matching type hints, or compatible signatures. Inheriting `ABC` alone without remaining abstract methods does not prevent instantiation.

### How do instance, class, and static methods differ?

| Method | Automatic argument | Purpose |
| --- | --- | --- |
| Instance method | `self`: receiving instance | Work with instance state/behavior |
| `@classmethod` | `cls`: receiving class | Class-related behavior, often alternative construction |
| `@staticmethod` | None | Related function grouped on a class |

### Why use a class method?

**A class method can provide a named creation recipe before any instance exists.** `BudgetConfig.from_dict(data)` converts input, calls `cls(...)`, and returns a new instance; it uses the normal constructor rather than replacing it. An inherited factory can create the receiving subclass if its constructor is compatible. A standalone factory function is also valid.

### When should a helper be a static method?

**Use a static method when association with an existing class makes a function easier to find and understand, but it needs neither `self` nor `cls`.** General helpers can remain module functions. Python does not require Java-style utility classes to contain functions.

### What is encapsulation in Python?

**Encapsulation exposes a clear public interface while treating implementation details as internal.** Python mostly uses conventions and name mangling rather than Java-style enforced access modifiers.

| Name | Common label | Actual behavior |
| --- | --- | --- |
| `label` | Public | Intended for callers |
| `_label` | Protected/internal | Convention; still directly accessible |
| `__label` | Private | Name-mangled; accessible through the mangled name |

### Why does Python mangle double-leading-underscore names?

**Name mangling reduces accidental collisions between base-class and subclass internals; it is not security.** `Base.__label` and `Child.__label` become `_Base__label` and `_Child__label` on the same instance. Intentional shared/customizable state often uses a single underscore instead. `__init__` has double underscores at both ends and is a special protocol name, not this private-name convention.

## Dataclasses and special methods

### What does `@dataclass` generate?

**It generates methods such as `__init__`, `__repr__`, and `__eq__` from declared fields on an ordinary class.** Custom instance methods still work. It does not enforce type hints or validate values automatically.

```python
@dataclass
class Budget:
    category: str
    limit: Decimal
```

Removing these field declarations means the generated initializer no longer accepts them. A factory method does not recreate missing constructor parameters.

### What is `__post_init__`?

**It is a hook called after field assignment by a dataclass-generated initializer.** Use it for additional initialization or validation. Its name must be exact; `__postinit__` is not the same hook.

### What are dunder methods?

**Dunder methods are specially named hooks that integrate classes with Python operations.** `__repr__` supplies a developer-facing representation, `__eq__` supports equality, `__sub__` supports subtraction, and `__enter__`/`__exit__` support `with`. They can be called directly, but ordinary code usually uses the corresponding operation.

## Decimal and money

### Why use Decimal instead of float for our money calculations?

**Decimal represents decimal inputs directly and supports explicit decimal precision/rounding rules; binary floats approximate many decimal fractions.** Construct from strings: `Decimal("0.1")`, not `Decimal(0.1)`, which receives an already-approximated float. Decimal arithmetic is still subject to context precision and rounding.

### Is every Decimal a valid money amount?

**No. Decimal supports NaN and infinity, and currency values also need scale and range policies.** `isinstance` checks type; `amount.is_finite()` checks finiteness. Call the method—`amount.is_finite` without parentheses is just a method reference.

### What are our spending and refund conventions?

**Positive transactions are spending; negative transactions are refunds.** Each affects its own dated month. A later refund does not rewrite the purchase month, so a refund-only month can have remaining funds above the budget limit. Budget limits follow a separate nonnegative-value rule.

### How do integer cents represent money?

**For a two-decimal currency, store the amount in integer minor units: 15.25 dollars becomes 1525 cents.** SQL can sum integers, then Python converts using `Decimal(total_cents) / 100`. This avoids floating-point summation within the integer range; currency scale, Decimal context, overflow, and rounding still need explicit policies.

### Why not blindly use `int(amount * 100)`?

**`int` truncates fractional results, so it can silently discard fractions of a cent.** Choose rejection or rounding first. Extra trailing zeroes such as `15.250` do not introduce fractional cents. `:.2f` controls display; it is not a storage-validation policy. Existing decimal-text data needs deliberate migration before changing representation.

## Collections and loops

### How do lists, tuples, dictionaries, and sets differ?

| Type | Main use | Key distinction |
| --- | --- | --- |
| List | Ordered sequence | Mutable; duplicates allowed |
| Tuple | Fixed sequence | Immutable container; contents may reference mutable objects |
| Dict | Key → value mapping | Keys are unique; retains insertion order |
| Set | Unique values/membership | No positional indexing or guaranteed iteration order |

### How do you accumulate a filtered total correctly?

**Initialize before the loop, add each matching item's amount, and return after the loop.** Returning inside the loop stops at the first item. Starting with `Decimal("0.00")` preserves a Decimal zero for empty input. Add `transaction.amount`, not the entire Transaction object.

### How do comprehension forms differ?

```python
[x.amount for x in transactions if x.category == "Gas"]  # Eager list + filter
["over" if x < 0 else "within" for x in balances]          # Choose a value
{k: v for k, v in pairs}                                 # Eager dict
(x.amount for x in transactions)                         # Lazy generator
```

**A trailing `if` filters items; an `if/else` before `for` chooses the output value.** Parentheses alone do not create a generator—the generator-expression syntax does.

### Why does `mapping[key] += value` sometimes raise KeyError?

**`+=` first reads the existing value, so the key must already exist.** Plain assignment creates/replaces an entry. For accumulation, initialize first or use `mapping[key] = mapping.get(key, zero) + value`. `get` supplies a fallback without inserting it.

### How do you detect duplicates using a set?

**Track seen values; reject a value already present, then add new ones.** A set provides convenient membership checks. Category-name comparison is case-sensitive unless an explicit normalization policy changes it.

## Iterables and iterators

### What is an iterable versus an iterator?

**An iterable can supply an iterator through `iter()`; an iterator tracks progress and supplies items through `next()`.** A list is iterable but is not itself an iterator. `iter(list)` normally creates a fresh list iterator; `iter(iterator)` returns that iterator itself.

### How does a for loop work?

**It calls `iter(source)`, repeatedly requests `next(iterator)`, and stops at `StopIteration`.** It does not need to guess whether the source is a list or generator. Repeating a loop over a list starts a fresh traversal; repeating it over an exhausted iterator yields nothing.

### What is a generator?

**A generator is an iterator produced by a function containing `yield` or by a generator expression.** Calling a generator function creates the generator object; its body starts when advanced. `yield` produces a value and suspends execution while preserving state. The consumer resumes it; repeated `next` calls do not call the function again.

### Why is a generator both iterable and iterator?

**It supplies items with `next` and returns itself from `iter`.** These are two protocol roles on one object, not an extra iterator wrapped around another. Its progress is shared across consumers of that same generator.

### Why use generators?

**They can produce items on demand without retaining every produced object.** They are usually single-pass and do not automatically reset. Constructing a whole list inside a generator before yielding still allocates that list. Generators control suspension, not automatic background or asynchronous execution.

### What happens with `list(generator)`?

**The list constructor consumes the generator and stores references to every yielded item.** The generator becomes exhausted; the resulting list can be traversed repeatedly. This gives up streaming memory benefits. In `calculate(list(generator))`, list construction finishes before `calculate` is called because arguments are evaluated first.

### Why can repeated category scans break a generator-based calculation?

**The first scan consumes every item, including nonmatches, leaving no items for later categories.** Materialize once if repeated traversal is required, or redesign as one-pass aggregation. Category totals can be accumulated in average O(n) time and O(k) extra storage for n transactions and k categories. `Iterable[Transaction]` does not promise indexing or restartability.

## Dates and monthly reporting

### How do you construct and serialize dates?

**`date(year, month, day)` takes integers; `date.fromisoformat(text)` parses an ISO string.** `date.isoformat()` produces text such as `"2026-11-14"`. Date attributes `.year`, `.month`, and `.day` are integer values, not conversion functions.

### What makes a monthly filter correct?

**Match both year and month and validate the period before iteration.** Month-only filtering mixes years. Validation hidden inside an empty loop never runs. Date-only objects have no time-of-day or timezone; timestamp-to-reporting-date policy is separate.

## Modules, packages, and imports

### What is a module, package, or library?

**A module is an importable unit, often a `.py` file; a package organizes modules; library is a general term for reusable code.** Our regular `mybudget` package contains `__init__.py`. In `from decimal import Decimal`, `decimal` is the module and `Decimal` is the class.

### How do built-ins and library categories differ?

| Category | Meaning | Example |
| --- | --- | --- |
| Built-in | Available without import | `print`, `len`, `list` |
| Standard library | Distributed with Python; usually imported | `decimal`, `json`, `sqlite3` |
| Third-party | Distributed separately and installed | pytest, FastAPI |
| Project/internal | Code we or our organization maintain | `mybudget.models`, a private company package |

**JFrog Artifactory is a repository hosting packages, not a distinct kind of library.** An internal package stays internal; mirroring externally authored code does not change its origin. `sqlite3` needs no extra install in our environment; `sqllite3` is a misspelling.

### Does importing one function execute the whole module?

**The first normal import executes the module's top-level code, then retrieves the requested name.** Definitions create objects; unguarded calls, sample data, and prints also execute. Modules are normally cached after import. Function bodies run when called, not merely when defined.

### Why use the main guard?

**`if __name__ == "__main__":` runs demonstration/entry-point code only when the module is executed as the program.** Normal imports use the module name and skip that block, preventing unwanted output, exceptions, or sample execution.

### Why can an imported module not use the caller's imports?

**Each module has its own namespace.** Importing Decimal in a demo does not define Decimal inside storage.py. Python 3.14 defers annotation evaluation, so unresolved hint names may fail when inspected even if a demo initially runs.

### Why run `python -m mybudget.cli` from the project root?

**`-m` locates and executes a module through Python's import system; this invocation includes the current directory in the module search path.** Running a nested file directly can produce a different search path. Correct working directory does not fix a missing or unsaved module.

## Exceptions and validation

### What is raising versus handling an exception?

**Raising signals failure and interrupts normal execution; handling catches a matching failure with `except`.** Execution does not resume at the failed statement. Model validation may raise an error; a CLI or caller decides how to report it.

| Exception | Typical meaning |
| --- | --- |
| `NameError` | Undefined name |
| `AttributeError` | Unsupported/missing attribute |
| `TypeError` | Wrong type, signature, or unsupported operation |
| `ValueError` | Suitable type but unacceptable value |
| `KeyError` | Missing dictionary key |
| `AssertionError` | Failed assertion |

### Why catch specific exceptions?

**Specific catches handle expected failures without hiding unrelated bugs.** Bare `except:` also catches interruption exceptions. `except ValueError as error` binds the exception instance; `except ValueError():` incorrectly uses an instance as the catch target.

### When do constructor argument errors occur?

**Argument expressions are evaluated before the constructor is called.** A failing `date.fromisoformat(...)` prevents Transaction construction and its `__post_init__` validation. Keyword names must match exactly; type hints do not fix misspelled names.

### What is finally for?

**`finally` runs on exit from its associated try, including normal completion, return, and exceptions.** Use it for cleanup. It does not itself catch or suppress a failure. A new error in finally can obscure the original failure and skip later cleanup statements.

### Why can output appear after a traceback?

**Normal prints use stdout, while tracebacks use stderr; buffering can make their displayed order surprising.** `python -u` disables standard-stream buffering for debugging. An outer `print(f())` is never called if evaluating `f()` raises.

## Context managers and with

### What is a context manager?

**A context manager defines entry and exit behavior around a block; `with` is the statement that uses it.** It helps reliably release resources or perform exit checks when a block finishes or raises. A file object and `pytest.raises` provide different examples of that protocol.

### How do `__enter__` and `__exit__` work?

**After evaluating the manager, `with` calls entry, runs the body, and calls exit after successful entry.** `as value` receives the result of `__enter__`, which can be `self` or another value. If entry itself raises, its exit is not automatically called.

`__exit__(self, exc_type, exc_value, traceback)` receives exception details, or three None values on normal exit. A truthy return suppresses the exception; false/None allows propagation. Suppression does not resume interrupted statements inside the body.

### Why use `self.start` in a class-based timer?

**Separate methods need shared instance state.** A plain `start` local in `__enter__` is not accessible in `__exit__`. Returning self does not copy method locals into attributes.

### What does `@contextmanager` do?

**It adapts a generator function into a factory for context manager objects.** On entry the manager advances to the single `yield`; the generator pauses while the with body runs; on exit the manager resumes it or delivers the body's exception at the yield point.

```python
@contextmanager
def timer():
    start = perf_counter()
    try:
        yield
    finally:
        print(perf_counter() - start)
```

The generator retains local `start` across suspension. `yield` does not call the function again or run the with body itself; the manager coordinates execution. The generator must yield exactly once.

### How do these mechanisms relate?

| Mechanism | Role |
| --- | --- |
| `with` | Uses a context manager around a chosen block |
| `__enter__` / `__exit__` | Class-based implementation of the protocol |
| `@contextmanager` | Alternative generator-based implementation |
| A regular function decorator | Commonly wraps a whole function call |
| `try/finally` | Explicit exit/cleanup logic without a reusable manager |

**Choose a class or generator implementation; both are not required for one manager.** `with` creates a managed lifetime, not a new variable scope. Values read inside may remain usable after the resource closes.

## Text files and JSON

### How do you read and write text files?

**Use `open` to obtain a file object and `with` to close it reliably.** `"w"` creates/truncates, `"r"` reads an existing file, `write` accepts text, and `read()` returns remaining text. Relative paths use the working directory, not automatically the script's directory.

```python
with open("budget_note.txt", "w", encoding="utf-8") as file:
    file.write("Remaining: 424.75\n")
```

Closing does not delete the file or text already read into memory. `print` adds a newline by default, so printing text already ending in one can add a blank line.

### What is serialization versus encoding?

**Serialization represents structured data as a storable/transmittable format; encoding represents text characters as bytes.** Our write path is dictionary → JSON text → UTF-8 bytes. Reading reverses it: bytes → decoded text → Python data. UTF-8 knows characters, not dictionary structure.

### What do JSON's dump/load functions do?

| Function | Purpose |
| --- | --- |
| `json.dump(data, file)` | Write JSON text to a file object |
| `json.dumps(data)` | Return JSON text as a string |
| `json.load(file)` | Read JSON and return Python data |
| `json.loads(text)` | Parse JSON from a string |

**Remember the `s` as string.** JSON objects become dictionaries and arrays become lists; loading does not reconstruct arbitrary Python classes.

### How do you save Decimal, date, and custom objects as JSON?

**Explicitly convert unsupported values into supported data, then reconstruct their types after loading.** Store Decimal as a decimal string and date as ISO text. Convert loaded fields through `Decimal`, `date.fromisoformat`, and the model constructor; model validation then runs. A reconstructed dataclass can compare equal without being the same object.

## Testing and pytest

### What does a useful unit test check?

**It checks externally meaningful behavior against an expected result, using inputs that distinguish correct from plausible incorrect implementations.** Arrange inputs, Act by calling the operation, Assert the result. Use focused tests instead of duplicating implementation details or repeating familiar patterns indefinitely.

### What does assert do?

**A false assertion raises AssertionError.** Assertions support development checks, not production input validation, because Python optimization can disable them. Equality alone may not prove the returned type: integer zero can equal Decimal zero.

### How does `pytest.raises` work?

**It passes when the expected exception occurs inside the with body and fails if none occurs or an unexpected exception escapes.** Put the operation expected to fail inside the block; an exception during fixture setup occurs before that block can catch it.

```python
with pytest.raises(ValueError):
    Transaction("", Decimal("10.00"), date(2026, 1, 1))
```

### What is TDD?

**Test-driven development follows a failing behavioral test, a minimal implementation that passes, then refactoring.** Import/collection errors differ from a failed behavior assertion; interpret the reason before treating a failure as the intended test signal.

### How do you run tests or one selected test?

```sh
uv run --locked python -m pytest tests exercises -v
uv run --locked python -m pytest tests/test_monthly_budgets.py::test_remaining_budget_when_under_limit -v
```

**`-v` means verbose output.** Application tests live in tests/; historical learning tests remain in exercises/. Test names should describe behavior; negative tests do not need a special naming prefix.

## Fixtures and parametrization

### What is a pytest fixture?

**A fixture supplies reusable test setup/data through a test function's named parameter.** Default scope is per test function; returning a freshly built list gives each test independent data. Pytest resolves the fixture rather than requiring the test to call it manually.

### What is parametrization?

**Parametrization runs the same test definition with multiple input values.** The parameter named by `@pytest.mark.parametrize` must be accepted by the test. Fixtures reuse setup across tests; parametrization varies cases for a test. Both can be combined.

### Where should fixtures live?

**Keep local fixtures in their test module; place shared fixtures in `conftest.py` for automatic discovery in that directory and below.** Do not import conftest manually. Same names in separate modules are possible; redefining a function in the same namespace replaces the earlier binding. A fixture that raises during setup produces a setup error, not a caught test-body exception.

## Code organization and dependency injection

### What is separation of concerns?

**Give each component a clear responsibility so changes do not spread unnecessarily.** Models represent data/rules, calculations perform arithmetic, storage executes SQL/conversion, and CLI/API adapters handle input/output. Folder count and service classes are not standards by themselves; introduce layers when responsibilities justify them.

### What is a refactor?

**A refactor changes internal structure while preserving behavior.** Moving shared calculations into a module is a refactor. General helpers can live in focused modules rather than an unrelated catch-all helpers class/module. Modules are not automatically separate processes or services.

### What is dependency injection?

**Dependency injection supplies a dependency from outside rather than creating it inside the code that uses it.** Passing `sqlite3.Connection` into save/load functions is DI without a framework. Callers can supply a file-backed or in-memory connection.

### Who should own commits and connection cleanup?

**The caller that owns the connection/workflow controls its lifetime and transaction boundary.** Storage functions execute operations without silently committing each one, allowing several saves to succeed or roll back together. This is our chosen boundary, not a universal requirement for every design.

### Will FastAPI replace the CLI's business logic?

**No. CLI and API are separate input/output adapters that can reuse the same application logic.** FastAPI endpoints will receive HTTP input rather than run CLI commands. The CLI can remain optional for development or administrative workflows.

## Environments, dependencies, and uv

### What is a virtual environment versus a package manager?

**A virtual environment isolates installed packages; a package manager installs/resolves them.** uv can manage both, but using uv does not eliminate the environment. A virtual environment is not a full virtual machine.

| Artifact | Purpose | Track in Git? |
| --- | --- | --- |
| `pyproject.toml` | Project metadata, supported Python, dependencies | Yes |
| `uv.lock` | Resolved dependency versions/artifacts | Yes |
| `.venv/` | Local installed environment | No |

### What are direct, transitive, runtime, and development dependencies?

**Direct dependencies are requested by the project; transitive ones are required by those dependencies.** Runtime dependencies support running the app; development dependencies support tasks such as testing. A lockfile records a resolution, not an entire OS environment.

### What does uv run do, and is activation required?

**`uv run` executes in the project's environment, so manual activation is optional.** `--locked` requires an up-to-date lockfile instead of silently updating it. Activation changes the shell's PATH; deactivation does not delete the environment.

```sh
uv sync --locked
uv run --locked python -m mybudget.cli --help
source .venv/bin/activate
deactivate
```

`python -m pip` chooses pip through that interpreter; `sys.executable` identifies the running Python.

## Command-line interfaces and argparse

### What does argparse provide?

**argparse turns command-line text into named values and provides usage/help/error handling.** Define options with add_argument, then call the main parser's parse_args. Values default to strings unless a converter is supplied.

### How does a custom argument converter work?

**Pass a function object as `type=parse_amount`; argparse calls it with text and stores its returned value.** Raise ArgumentTypeError for a readable input message. Catch the specific conversion error rather than bare except. Invalid CLI input normally exits with status 2; successful calculation exits with 0.

```python
parser.add_argument("--budget", required=True, type=parse_amount)
```

### What is a subparser?

**A subparser defines a subcommand and that command's own arguments.** Examples: calculate has budget/spent, report has year/month. Registration does not automatically connect a name to an application function; the program must dispatch the selected operation.

```python
commands = parser.add_subparsers(dest="command", required=True)
report_parser = commands.add_parser("report")
report_parser.add_argument("--year", type=int, required=True)
args = parser.parse_args()  # args.command contains the selected name
```

`report_parser` is a local variable, not a method automatically added to parser. Keep parsing inside main and use the main guard for entry-point execution.

## SQLite and relational databases

### What is SQLite, and where does its data live?

**SQLite is an embedded relational database engine, accessed through Python's standard-library sqlite3 module without a separate server.** A file-backed database persists on disk; reopening the same path accesses its committed data. Each ordinary `":memory:"` connection creates its own temporary database.

### What are tables, rows, columns, and a schema?

**A table groups records, a row is one record, a column is a field, and the schema defines their structure and rules.** SQL defines structures and reads/changes records. A table lives inside the database, not as a separate file.

### What do connection, cursor, execute, and fetch do?

**A connection manages access and transaction state; a cursor executes statements and exposes results.** Connection.execute returns a cursor. fetchone returns one row or None; fetchall returns the remaining rows, normally as a list of tuples. `fetchone()[0]` extracts the first column of one result row. A cursor is also iterable.

### What are the basic SQL operations?

| SQL | Purpose |
| --- | --- |
| `CREATE TABLE` | Define structure |
| `INSERT` | Create records |
| `SELECT` | Read records |
| `UPDATE ... SET ...` | Change records |
| `DELETE` | Remove records |
| `WHERE` | Filter matching records |
| `ORDER BY` | Request explicit result order |

**CRUD means Create, Read, Update, Delete of records.** Without WHERE, UPDATE/DELETE targets every row. No match in SELECT is an empty result, not an exception. Use separate execute calls for separate statements; a comma does not combine CREATE TABLE and INSERT.

### Why use parameterized queries?

**Parameters bind values as data rather than SQL code, handling quotes and helping prevent injection.** Use placeholders rather than f-string interpolation. Values follow placeholder order; table names and SQL keywords cannot be supplied as value parameters.

```python
connection.execute(
    "UPDATE transactions SET merchant = ? WHERE id = ?",
    ("Costco", 1),
)
```

A one-item parameter tuple needs a comma: `(1,)`, not `(1)`.

### What do database constraints enforce?

| Constraint | Rule |
| --- | --- |
| `PRIMARY KEY` | Row identity |
| `NOT NULL` | No SQL NULL in the field |
| `UNIQUE` | No duplicate non-NULL key values under the comparison rules |
| `CHECK` | Reject a false condition; in SQLite NULL does not itself fail it |
| `FOREIGN KEY` | References must resolve according to the relationship rule |

**Database constraints protect writes that bypass Python model construction.** Model validation protects its construction path; neither automatically supplies every business rule. Constraint violations typically raise sqlite3.IntegrityError; malformed SQL can raise OperationalError.

### Why is NOT NULL insufficient for a category name?

**It rejects NULL but allows empty and space-only strings.** `CHECK(length(trim(category)) > 0)` rejects empty/ordinary-space-only values. SQLite's default trim and Python's strip do not remove exactly the same whitespace. Keep NOT NULL because CHECK alone can accept a NULL condition result.

### How do UNIQUE and generated IDs differ?

**A primary key identifies each row; another UNIQUE key expresses business uniqueness, such as a category name.** Different IDs do not permit duplicate names when names are unique. Default text comparison distinguishes Groceries, Grocery, and groceries. Repeated expenses can be legitimate and should not be rejected just because their values coincide.

### How does SQLite generate an omitted integer primary key?

**In our ordinary tables, INTEGER PRIMARY KEY aliases rowid and SQLite assigns an omitted value, normally one above the largest existing ID.** AUTOINCREMENT is unnecessary for that basic behavior. Deleted IDs can sometimes be reused; IDs are not gap-free counts. The exact INTEGER spelling matters; ordinary non-STRICT SQLite type declarations are otherwise permissive.

### What is a foreign key and a one-to-many relationship?

**A foreign key references another row's key; one-to-many means many child rows can reference one parent.** Multiple transactions can reference one unique category. Enable SQLite enforcement on each connection with `PRAGMA foreign_keys = ON` before starting a transaction; changing that setting inside an active transaction does not enable it there.

### What is normalization, and why use it?

**Normalization organizes facts according to their keys to reduce unnecessary duplication and data anomalies.** Repeating category_name in every transaction makes renaming inconsistent (update anomaly), representing a category without a purchase awkward (insertion anomaly), and deleting its last purchase lose category information (deletion anomaly). Store category details once and reference them; repeating the category ID is an appropriate relationship, not duplication to eliminate.

### What are 1NF, 2NF, and 3NF?

**They are progressively stronger dependency rules; each requires the preceding normal forms.** These are practical explanations of common cases:

| Form | Rule | Example correction |
| --- | --- | --- |
| 1NF | No repeating groups; one value per field for the chosen model | Receipt 101 with items "Milk, Bread" → separate receipt-item rows |
| 2NF | Non-key attributes depend on the whole candidate key, not a proper subset | Budget keyed by category_id + month: move category_name, which depends only on category_id |
| 3NF | Remove inappropriate transitive dependencies of non-key attributes on keys | transaction_id → category_id → category_name: keep the name in categories |

The normalized budget example has categories(category_id, category_name) and monthly_budgets(category_id, month, budget_limit). The category/month combination identifies the limit; a join retrieves category details when needed. More tables are not a goal by themselves.

### Does depending on one key column mean an attribute must move?

**No: depending on the entire single-column key is fine; depending on only part of a composite key is the 2NF issue.** A composite key is one key made of multiple columns, not several independent keys.

| Whole key | Attribute dependency | 2NF assessment |
| --- | --- | --- |
| category_id | category_id → category_name | Fine: the whole key |
| category_id + month | category_id → category_name | Partial dependency: move name to categories |
| category_id + month | category_id + month → budget_limit | Fine: the whole key |

This checks 2NF only; satisfying it does not automatically prove 3NF or every other design rule.

### How does a join differ from a foreign key?

**A foreign key enforces a relationship; a join retrieves combined data using a matching condition.** A join does not change stored rows and does not require a declared foreign key. Table aliases such as t/c are query-local names, not new tables.

```sql
SELECT t.id, c.name, t.amount
FROM transactions AS t
INNER JOIN categories AS c ON t.category_id = c.id
ORDER BY t.id;
```

### What is INNER JOIN versus LEFT JOIN?

**INNER JOIN returns matching combinations; LEFT JOIN also preserves unmatched left rows with NULL right-side values.** Python receives those NULLs as None. Put categories on the left to include unused categories. A category with three matches produces three rows; one without matches produces one NULL-extended row. The join does not insert missing transactions.

### What does GROUP BY do?

**GROUP BY forms groups so aggregate functions can produce a summary for each group.** One unique category can have many transactions, summarized as one category count or total.

```sql
SELECT c.name, COUNT(t.id) AS transaction_count
FROM categories AS c
LEFT JOIN transactions AS t ON t.category_id = c.id
GROUP BY c.id, c.name
ORDER BY c.id;
```

### What is COUNT(*) versus COUNT(column)?

**COUNT(*) counts rows; COUNT(column) counts non-NULL values in that column.** An unmatched category still has one LEFT JOIN result row, so COUNT(*) gives 1 while COUNT(t.id) correctly reports 0 transactions.

### What does SUM return on an empty set, and why use COALESCE?

**SUM returns NULL when there are no non-NULL inputs; COALESCE supplies the first non-NULL alternative.** `COALESCE(SUM(amount_cents), 0)` produces zero spending for an empty set. It does not replace a real zero or modify stored data. Integer SUM remains bounded by SQLite's integer range.

### What is sqlite3.Row?

**It is a row representation supporting column-name access as well as positional access.** Set `connection.row_factory = sqlite3.Row` before creating query cursors. It changes Python result access, not stored values. Decimal/date fields still need explicit conversion before constructing a Transaction.

### What is a database transaction?

**A transaction groups changes that can be committed or rolled back together.** commit accepts pending changes; rollback undoes pending changes, not earlier commits. In our default sqlite3 exercises, the first write starts the write transaction; connection modes can change transaction behavior.

### Does one failed insert undo every earlier insert automatically?

**Not in our constraint-failure experiment: the handler explicitly rolls back the transaction.** A valid first insert followed by a rejected second insert demonstrates atomicity only when the first was still pending. Committing between them makes the first survive the later rollback. Closing is not a substitute for committing pending writes.

### What does ACID mean?

| Property | Direct answer |
| --- | --- |
| Atomicity | Grouped changes take effect together or are undone together |
| Consistency | Transactions preserve the database's declared rules |
| Isolation | Concurrent transactions have controlled visibility and interaction |
| Durability | Committed changes persist beyond the transaction/process |

**Consistency does not mean the database knows undeclared business rules.** Durability depends on database configuration and storage; surviving a normal restart does not prove every crash scenario.

### What did the two-connection isolation experiment show?

**A separate connection could not see an uncommitted update; its fresh read after commit saw the new value.** With a committed 100, first updated to 300; second read 100 before commit and 300 afterward. This assumes ordinary separate connections and no explicit long-running read transaction on second. It does not establish all snapshot, locking, or journal-mode behavior.

### When does SQLite acquire a write lock?

**In our default connection setup, executing an UPDATE starts a write transaction and acquires its write lock automatically.** SQLite allows one active writer per database, even for different rows. The lock remains until the transaction ends; commit or rollback releases it. Merely opening a connection does not lock the database for writing.

### Can another connection read or write while that transaction is open?

**In our experiment, another connection could read previously committed data but could not become a second writer.** `timeout=0` makes the second writer fail immediately with a busy/locked error instead of waiting for access. Read availability depends on journal mode and transaction phase; it is not guaranteed in every situation. Ending the first write transaction allows a later write attempt to proceed.

### What is rollback journaling versus WAL?

**Rollback journaling preserves original pages before modifying the main database; WAL appends changes to a separate write-ahead log.** A checkpoint later transfers committed WAL changes into the main database file. WAL supports overlapping readers and a writer more effectively, but still permits only one active writer. Readers can obtain visible data from both the database and log; the log is not merely uncommitted scratch space. [SQLite WAL guide](https://www.sqlite.org/wal.html).

### What is a read snapshot in WAL mode?

**A read transaction keeps a consistent view established by its first read, even if another connection commits newer data.** In our experiment the reader saw 100, still saw 100 after a writer committed 300, then saw 300 after ending its read transaction and reading again. A commit makes data available to new reads; it does not replace an existing transaction's snapshot. [SQLite isolation guide](https://www.sqlite.org/isolation.html).

### What does BEGIN do in the reader experiment?

**BEGIN explicitly starts a transaction; the first SELECT establishes its read snapshot.** Subsequent SELECTs remain in that transaction until commit or rollback. Without explicit BEGIN in our default setup, completed reads did not remain in one long-running transaction, so the next read saw newly committed data. BEGIN alone does not read or copy the entire database.

### What is an index, and what is its cost?

**An index is an extra search structure that can locate matching records without a full table scan.** It consumes storage and adds maintenance to inserts, deletes, and updates of indexed values. SQLite maintains it automatically. Index useful query patterns rather than every column; not every query benefits.

### What does EXPLAIN QUERY PLAN tell you?

**It describes SQLite's chosen access strategy, not measured execution time or returned data.** SCAN indicates scanning; SEARCH describes a subset lookup. A covering index contains everything needed for the query, avoiding a separate table lookup. An index can also be scanned, so SCAN alone does not mean no index exists.

Raw fields are node ID, parent ID, internal auxiliary value, and description. Current implementation uses an encoded estimated loop cost in that third field for these scans. Values such as 216 and 56 are not milliseconds, actual rows, or a measured speedup; this debug format can change. [SQLite plan guide](https://www.sqlite.org/eqp.html), [plan implementation](https://github.com/sqlite/sqlite/blob/master/src/wherecode.c), [cost definition](https://github.com/sqlite/sqlite/blob/master/src/whereInt.h).

### Why does column order matter in a composite index?

**A composite index is ordered by its first column, then subsequent columns within equal preceding values.** `(category, transaction_date)` can seek to a category/date range without scanning every category. It generally supports category alone and category-plus-date; date alone lacks the leading filter and may need a different strategy. Optimizer exceptions exist; inspect the plan. Index order is not guaranteed result order without ORDER BY.

### What is a schema migration?

**A migration explicitly evolves an existing schema while preserving or transforming data.** `ALTER TABLE transactions ADD COLUMN merchant TEXT` adds a nullable column and keeps existing rows, initially with NULL merchants. UPDATE afterward changes data. Editing CREATE TABLE IF NOT EXISTS does not update a table already present.

### How do you track applied migrations?

**Store a schema version and apply only the ordered changes still needed.** SQLite's `PRAGMA user_version` is a persisted application-controlled integer starting at 0. It does not infer or perform migrations; code defines version meaning and updates it.

Group the schema change and version-marker update in one explicit transaction so they succeed together. A later run skips completed changes. Larger runners must handle ordered steps and unsupported versions; a marker alone does not verify the actual schema. Schema version and application release version are separate.

## HTTP and client-server communication

### What is HTTP?

**HTTP (Hypertext Transfer Protocol) defines how clients request resources and how servers respond.** It is an application-layer protocol: it defines message semantics, while lower networking layers carry the data. Browsers, mobile apps, command-line tools, and other servers can all be HTTP clients.

### What are the parts of an HTTP request and response?

**A request identifies an operation and target; a response reports the outcome and may return data.** Headers carry metadata, and a body carries optional content such as JSON. The client initiates the exchange; the server responds.

| Message | Main parts | Example |
| --- | --- | --- |
| Request | Method, target, headers, optional body | GET /transactions asks for transaction data |
| Response | Status code, headers, optional body | 200 OK with a JSON list |

### What is HTTPS?

**HTTPS is HTTP protected by TLS, providing encryption, integrity protection, and server authentication through certificate validation.** HTTP defines what the messages mean; TLS protects their transport. HTTPS does not replace application authentication or authorization.

### How does an HTTP request travel from client to server?

**The client sends HTTP data through networking layers to a listening server, which processes it and sends a response back.** For a new TCP-based HTTPS connection, the simplified flow is DNS lookup → TCP connection → TLS handshake → HTTP exchange. DNS results and connections may be reused, so not every request repeats setup.

| Component | Role |
| --- | --- |
| DNS | Resolve a domain name to a destination address |
| IP address | Identify the network destination |
| Port | Help direct traffic to the appropriate service; HTTPS normally uses 443 |
| TCP | Provide reliable, ordered byte delivery for HTTP/1.1 and HTTP/2 |
| TLS | Protect the connection |
| OS/network infrastructure | Carry data in packets through network interfaces and routers |

This is a TCP-based example, not a claim that every HTTP version uses TCP. Your application function does not manually send individual network packets.

### How do the HTTP server and FastAPI fit together?

**Server software such as Uvicorn receives HTTP traffic and passes requests to the FastAPI application, which routes them to handlers.** Application code performs the requested operation, and the server sends the resulting HTTP response. Calculation and storage functions can remain independent of HTTP.

Sources: [MDN HTTP overview](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview), [MDN Internet overview](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work).

## Git and GitHub

### How do saving, staging, committing, and pushing differ?

**Saving changes files; staging selects the next snapshot; committing records local history; pushing uploads commits to a remote.** Git is the version-control system; GitHub hosts remote repositories. A clean working tree does not prove the remote is current.

```text
Edit/save → git add → git commit → git push
```

### What are origin, HEAD, and a branch?

**origin is a conventional remote name; HEAD identifies the current checkout; a branch name points to a commit.** Adding a remote does not upload anything and can happen before the first commit.

### Does .gitignore stop tracking an existing file?

**No. It excludes matching untracked files from normal staging.** `git rm --cached path` stops tracking while preserving the local file; it does not erase previous history. Keep local databases, journals, environments, and secrets out of ordinary commits while tracking source, schema/migration code, pyproject.toml, and uv.lock.
