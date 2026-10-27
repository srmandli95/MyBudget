# Learning notes

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
