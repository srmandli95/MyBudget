# 2026-10-27: Dataclasses, identity, and validation

## Dataclasses and representation

`@dataclass` examines declared fields and generates methods such as `__init__`,
`__repr__`, and `__eq__`. Importing `dataclass` alone does not apply it.
Conceptually, the decorator applies `Transaction = dataclass(Transaction)` after
the class definition. The generated initializer assigns fields; annotations do
not automatically convert inputs or enforce their types.

`__repr__` produces a developer-facing text representation of an object.
`repr(transaction)` explicitly requests it. `print(transaction)` uses string
conversion, which falls back to the representation when there is no custom
`__str__` implementation.

## Equality, identity, and references

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

## Modules and imports

`dataclasses`, `decimal`, and `copy` are standard-library modules. They provide
the `dataclass` function, `Decimal` class, and `copy` function respectively.
A module is an importable unit of code; a package organizes modules; library is
a broader term for reusable code. Own modules and dependency management come later.

## Validation with __post_init__

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

## Debugging and current verification

Source: [transaction_dataclass_postinit.py](../exercises/transaction_dataclass_postinit.py).

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

## Next practice

Run merchant cases `"Costco"`, `""`, and `"   "` separately and review the output.
Then learn how to handle expected exceptions with `try` and `except`.
