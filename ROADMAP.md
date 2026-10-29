# Roadmap

Every milestone requires working code, relevant tests, and an explanation by the learner.
Introduce fundamentals progressively; pause after exercises for review.

Current checkpoint: milestone 1 in progress. Decimal arithmetic, transaction
models, validation, exception handling, lists, loops, and category filtering have
been covered. Category totals were verified for matching, unmatched, and empty
inputs. Dictionary-based budgets and remaining amounts are now implemented and
the final script verified. Next: automated tests. Milestone 1 is not complete;
an integrated engine and saved tests still remain.

Testing checkpoint: ten pytest cases now pass (setup subtraction, four
category-total behaviors, and five merchant-validation cases). Covered expected
exceptions, context managers, parametrization, and local fixtures. Sharing through
conftest.py is discussed; an optional move exercise is next.

Latest checkpoint: shared conftest.py fixture and uv dependency setup are complete;
the locked uv test run passes all 10 cases. Next: progressively consolidate shared
models and calculations. LEARNING_NOTES.md is the single appended revision journal.

Model extraction checkpoint: budget Transaction moved into mybudget/models.py;
10 tests and the demonstration still pass. Next: extract the category calculation.

Calculation extraction checkpoint: category calculation now lives in
mybudget/calculations.py; tests and demonstration pass unchanged. Next: extract
and test remaining-budget behavior below, at, and above the configured limit.

Latest date/testing checkpoint: shared Transaction has transaction_date;
remaining-budget boundary tests and report integration are complete. Monthly
filtering has mixed-input and empty-list tests; 15 total tests pass. Next: a
nonempty no-match monthly test, then monthly report integration. Milestone 1
remains in progress.
An integrated engine and broader tests remain before milestone 1 is complete.

| Milestone | Completion criterion |
| --- | --- |
| 1. Python engine | In-memory fictional transactions, configurable budgets, tested category totals and remaining amounts |
| 2. SQLite | Persist records and verify monthly reports and constraints |
| 3. FastAPI | Validated transaction and budget endpoints with API tests |
| 4. React | Dashboard and forms connected to the API, including error states |
| 5. Categorization and CSV | Deterministic rules and validated, repeatable imports |
| 6. Simulated synchronization | Compare sequential, threaded, and async fetching with measurements |
| 7. Background processing | Test retries, duplicate events, and recovery |
| 8. Bank integration | Evaluate current providers; obtain explicit approval before real connections |
| 9. Hardening and deployment | Verify isolation, security, observability, and recovery; approval before public or paid deployment |
| 10. Scaling experiments | Measure bottlenecks and justify architectural changes |
| 11. AI | Evaluate optional assistance against deterministic baselines; approval before sharing real financial data |

Detailed curriculum, including algorithms, security, testing, and operating systems:
LEARNING_MASTER_PROMPT.md.
