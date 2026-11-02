# Progress

Last updated: 2026-11-02.

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; same-month refund behavior verified.
The project consists of working standalone exercises, not yet an integrated engine.

## Completed learning

- Python execution, syntax versus runtime errors, references, and assignment.
- Decimal arithmetic, functions, type hints, classes, dataclasses, and validation.
- Equality, identity, aliasing, context managers, and exception handling.
- Lists, loops, category totals, dictionaries, and configurable monthly budgets.
- Assertions, pytest, import behavior, the main guard, parametrization, and fixtures.
- Shared fixture in exercises/conftest.py, discovered without explicit imports.
- uv project setup, development dependencies, lockfiles, and optional activation.
- Models, regular packages, and a behavior-preserving refactor into mybudget/models.py.
- Category calculation moved into mybudget/calculations.py; demo and tests import it there.
- calculate_remaining implemented; under-, at-, and over-limit tests verified.
- Tested remaining-budget function integrated into the demonstration.
- Date objects, month/year comparisons, and required transaction_date field introduced.
- Fixed the demonstration's missing date import and restored the no-match test.
- Monthly category filtering with mixed-date/category fixture and Decimal accumulator.
- Empty-input monthly test checks both zero value and Decimal result type.
- Budget dataclass with category/limit fields; valid construction and negative-limit rejection tested.
- Fixture setup errors versus expected exceptions inside a test clarified by experiment.

## Latest verification

Mentor ran `uv run --locked python -m pytest tests exercises -v`: **32 passed in 0.03s**,
exit 0, Python 3.14.6 and pytest 9.2.0. pyproject.toml and uv.lock record the
project and dependencies; .venv remains ignored. Use Python's module invocation
from the project root to make exercises imports work.

Category budget example: limits total 1100.00; groceries remaining -25.00,
restaurants 100.00, gas 50.00, miscellaneous 150.00. Data is fictional.
Mentor reran the module demonstration after the date-field changes; same results, exit 0.

## Next recommended task

Latest checkpoint (2026-11-02): signed amount rule introduced: expenses positive,
refunds negative. Learner's new refund test verifies 100.00 purchase plus -25.00
refund leaves 425.00 of a 500.00 grocery budget. Mentor inspected fixture/test and
ran refund file: 1 passed, exit 0. Full suite not rerun since this new test.
Fix refund fixture annotation from list(Transaction) to list[Transaction].
Next: a refund in the following month, using transaction-date attribution policy.
Let the learner write the tests; existing calculation may already satisfy them.

## Previous test-directory checkpoint

Latest checkpoint (2026-11-02): application tests and conftest.py moved into tests/;
two learning test files remain in exercises/. Mentor checked layout/imports and
ran both groups: **32 passed**, exit 0 (26 app cases, 6 learning cases).
Use `uv run --locked python -m pytest tests exercises -v` for all tests, or tests
alone for application cases. AGENTS.md updated; old exercises-only commands omit
the application suite now. Journal lesson 38 records the refactor.

Next: define signed expense/refund behavior and write a focused test before
changing financial logic. The shared Transaction still lacks the validation of
the earlier exercise model. Confirm milestone 1's remaining criteria before SQLite.

## Previous duplicate-category checkpoint

Latest checkpoint (2026-11-02): summary rejects duplicate category names using
seen_categories set; matching is exact/case sensitive. Mentor inspected and ran
summary file: 6 passed, exit 0. Full suite last verified 31 cases before this added
test; not rerun in this focused check. Duplicate test still creates its inputs
inside pytest.raises; recommend moving setup outside to isolate the summary call.
Optional error-message improvement: identify the duplicate category.

Next: small test-scope cleanup, then organize application tests separately from
learning experiments. Explain moves and fixture visibility before implementation.
Duplicate transaction detection, numeric/type policy, year validation, and shared
transaction validation remain future work; milestone 1 is not declared complete.

## Previous shared-validation checkpoint

Latest checkpoint (2026-11-02): validate_month defined in calculations.py and
called by both monthly functions before iteration. Invalid 0/13 rejected even
with no budgets/transactions; valid empty-budget result remains {}. Mentor
inspected implementation and ran full suite: **31 passed**, exit 0.
Discussed why Budget.__post_init__ does not own the separately supplied report
month, possible future ReportPeriod model, and focused module placement.

Next: agree on duplicate budget-category policy, write a test demonstrating
current dictionary overwrite behavior, then implement the chosen rule. Let the
learner code it. Organizing app tests separately from exercises remains pending.

## Previous empty-budget checkpoint

Latest checkpoint (2026-11-02): empty-budget rule tested: valid period plus no
budgets returns {}, even with transactions. Mentor ran summary test file:
3 passed, exit 0. Full suite not rerun during this check.
Next: test invalid month rejection for calculate_monthly_remaining with no budgets;
current per-category validation is skipped when its budget loop is empty.
Let the learner first observe the failure, then fix validation placement.
Duplicate-category policy and test-directory organizing remain pending.

## Previous report-integration checkpoint

Latest checkpoint (2026-10-31): report now calls calculate_monthly_remaining once
outside the printing loop. Learner resolved repeated calculation and restored
per-category printing. Mentor inspected final saved source and ran the report:
correct December 2026 output, exit 0. Full suite previously passed 28 cases during
integration review; not rerun for the final demonstration-only indentation edit.

Next: define/test empty-budget and duplicate-category contracts for the summary
function in small learner exercises. Organizing application tests into tests/
separately from historical exercises remains pending. Do not generate solutions
or treat the financial engine as production-complete.

## Previous summary-function checkpoint

Latest checkpoint (2026-10-30): calculate_monthly_remaining now composes monthly
category spending and remaining calculations and returns a plain dictionary.
Budget import, fixture annotation, = versus +=, printing removal, and helper
reuse verified in saved files. October 2026 and 2027 tests cover all three sample
budgets, including Vacation. Mentor ran full suite: **28 passed**, exit 0.

Next: use this function in exercises/monthly_budgets.py instead of the per-budget
calculation loop; preserve printing and period configuration. Let the learner
implement and verify unchanged output. Empty budgets and duplicate categories
remain unspecified/test gaps; avoid treating the engine as complete yet.

## Previous report checkpoint

Latest checkpoint (2026-10-30): Budget objects integrated into the report. List
iteration uses category/limit attributes; Decimal accumulator totals limits.
Mentor ran full suite (26 passed) and December report (1100.00 total, all full
limits remaining), both exit 0. Report period is displayed.

Next: extract report calculation into a reusable function returning a summary,
keeping printing in the demonstration. Explain the return structure and give a
small test-first exercise. Do not generate the implementation for the learner.
Duplicate budget-category policy, broader numeric validation, shared transaction
validation, unused fixture cleanup, and test-directory organization remain pending.

## Previous zero-limit checkpoint

Latest checkpoint (2026-10-30): zero-limit test passes; valid Budget test now
asserts limit 50.00; blank-category naming typo fixed. Mentor ran Budget test file:
6 passed, exit 0. Full suite not rerun since these focused model checks.
Next: integrate Budget objects into the monthly report, preserving configuration
values and output. Explain list-of-objects iteration versus dictionary.items()
before changes. Let the learner implement in small steps. Broader numeric/type
validation, unused fixture cleanup, and test-directory organization remain pending.

## Previous blank-category checkpoint

Latest checkpoint (2026-10-30): learner completed blank-category parametrization
for empty text, a space, and a tab, using a valid positive limit. Negative-limit
test renamed correctly. Mentor ran the Budget test file: 5 passed, exit 0; no full
suite rerun in this focused check. Minor typo: black_category should be blank_category.
Next: zero-limit acceptance test and valid fixture limit assertion (50.00).
Then integrate Budget in the report as a separate step. Unused invalid fixture
cleanup and moving app tests to tests/ remain pending.

## Previous Budget-model checkpoint

Session stopping point (2026-10-29): learner requested recording and continuation
later. Budget now has category and limit (not monthly_limit), with blank-category
and negative-limit validation. Two saved tests pass, but coverage is incomplete.

Resume with small exercises: rename test_invalid_category to reflect its actual
negative-limit check; assert the valid fixture's limit is 50.00; test blank and
whitespace categories and zero-limit acceptance. The unused invalid-construction
fixture remains in conftest.py; it can be removed. It no longer raises because no
test requests it. Budget has not been integrated into the dictionary report yet.
Mentor verified full suite: 22 passed. See journal lesson 29 for the fixture error
and the learner's correct prediction. No application/test code changed during recording.

## Previous monthly-boundary checkpoint

Latest checkpoint: month validation boundary exercise complete. Learner tests
invalid 0/13 with empty input and valid 1/12 returning zero. Mentor inspected the
saved tests and ran the full suite: **20 passed**, exit 0. The new valid-boundary
test checks equality only; Decimal type is verified by the earlier empty-input test.

Next: introduce a Budget dataclass and explicit monthly-limit validation. Agree
on rules and explain responsibilities before the learner implements. Keep existing
dictionary configuration initially; don't rewrite the report and model together.

## Monthly-filtering checkpoint history

calculate_monthly_category_total is implemented with category/year/month matching
and a Decimal accumulator. Learner's expanded fixture includes other-month,
other-category, and other-year purchases; target October groceries remain 70.00.
Empty-list test now checks zero value and Decimal type. Mentor inspected it and
ran the full suite after fixture expansion: 15 passed, exit 0.
Monthly filtering is now integrated in the demonstration with year 2026/month 10.
Mentor inspected and ran the report: expected October results, exit 0. Full suite
rerun after integration: 16 passed. Empty and nonempty no-month-match tests pass.
Learner reported full remaining limits for November. Added month-range validation
before iteration; corrected boolean grouping and a test accidentally passing 12
instead of invalid 13. Mentor reproduced the failure, then verified the corrected
test and full suite: 17 passed at that checkpoint. Invalid months 0/13 are now
parametrized with empty input; mentor ran the monthly file: 5 passed, exit 0.
Full suite not rerun since parametrization. Next: valid boundary months 1/12
with empty input, asserting Decimal zero and successful completion.

Current model requires transaction_date; fixtures and demonstration supply dates.
sample_no_groceries preserves the no-category-match scenario. Latest verification
includes all date-field fixes and monthly tests: 16 tests pass. The demonstration
now uses monthly category totals and exits 0 for October 2026.
Decimal return annotation on calculate_remaining remains optional cleanup pending.
Initial failing test-first run was suggested but not observed; do not claim it ran.
calculate_category_total now lives in mybudget/calculations.py; demonstration
and category tests import it there.
The budget Transaction now lives in mybudget/models.py; conftest imports it there.
The earlier validated Transaction still has merchant and remains separate. Do not
swap models without a deliberate field/validation change and caller/test updates.
Broader financial rules, integration, and milestone completion checks remain.

## Learning-record convention

User requests **one revision file, appended after each lesson**: LEARNING_NOTES.md.
It now contains 39 lessons in learning order, including signed expense/refund amounts.
Append future lessons at the bottom, update contents, and refresh this checkpoint.
The dated learnings/ files are retained as a historical archive, not the primary
place for new entries. Do not keep prepending duplicate checkpoints to the journal.

## Session recovery and teaching preferences

Read LEARNING_MASTER_PROMPT.md, LEARNING_NOTES.md, ROADMAP.md, and this checkpoint.
Inspect actual files before assuming prior changes exist. Mentor first: let the
learner implement core code. Skip familiar material on request; pause at unfamiliar
concepts. When confused, use one change and one check at a time. General decorator
internals, generators, concurrency, GIL, databases, and web development remain
future lessons; mentioning them does not mean they were mastered.

## Repository

Branch main; origin: https://github.com/srmandli95/MyBudget.git.
Commit or push only as authorized. Saving learning notes does not itself mean
that they have been committed or uploaded.
