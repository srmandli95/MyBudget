# Python fundamentals exercises

These two scripts intentionally fail to demonstrate different execution stages.

From the Mybudget directory:

```sh
python3 exercises/syntax_error_demo.py
python3 exercises/runtime_error_demo.py
```

- `syntax_error_demo.py`: expect SyntaxError and no printed greeting.
- `runtime_error_demo.py`: expect the greeting followed by NameError.

Both exit with status 1 by design. They are learning examples, not application tests.
