# Learning notes

## First session: running source code

Introduced for practice, not yet demonstrated by the learner:
- Source code is text containing instructions in a programming language.
- A shell interprets terminal commands and locates executables using PATH.
- Running `python3 hello_budget.py` starts Python as a process managed by the OS.
- In CPython, source is compiled into bytecode, then executed by the interpreter.
- A program file persists on disk; its running process uses memory and CPU time.

Exercise pending: create a script that prints the project name and one fictional expense.
Next: names, values, and functions, followed by Decimal currency arithmetic and transaction modeling.

## Python execution discussion

Daily notes: [How Python executes a program](learnings/2026-10-26-python-execution.md).

Learner correctly identified the interpreter executable and predicted that a
syntax error prevents top-level execution. Clarified that CPython compiles source
into bytecode, then executes bytecode instructions rather than source lines.
Both stages happen through one `python3 filename.py` command.

Learner ran both error experiments and shared output. Mentor reproduced both:
syntax error prevents the first print; undefined-name execution error occurs
after the first print. Both exit with status 1 as intended. No application tests yet.
