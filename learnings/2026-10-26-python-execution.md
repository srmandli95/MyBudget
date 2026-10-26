# 2026-10-26: How Python executes a program

## Language, interpreter, and executable

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

## What the command means

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

## The execution pipeline

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

## Names and objects

```python
merchant = "Sample Grocery"
print(merchant)
```

`merchant` is a name bound to a string object. `print` receives that object and
writes its text representation to standard output, normally shown in the terminal.
The source file persists on disk after execution; this process's in-memory
bindings do not persist into the next run.

## Syntax errors versus execution errors

### Syntax error

```python
print("Starting MyBudget")
remaining =
```

The assignment is incomplete. Compilation fails, so the first line does not execute.

### Runtime exception

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

## Understanding demonstrated

- Correctly identified `python3` as the interpreter executable in the command.
- Correctly predicted that a syntax error at the end of the same script prevents
  a print at the beginning from executing.
- Explained the compilation and execution sequence, then refined the distinction
  between source lines and bytecode instructions.
- Confirmed that one command performs both compilation and execution.

## Experiments and results

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

## Next practice

Create a small MyBudget script with fictional expense data. Practice defining
a name before using it, and distinguish a string literal from a name lookup.
