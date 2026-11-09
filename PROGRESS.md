# Progress

Last updated: 2026-11-09.

## Current milestone

Milestone 1: Python budget calculation engine. Phase 1; generator-based timer,
text-file handling, and basic JSON serialization exercises complete.
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
- Iterable versus iterator, next(), exhaustion, and fresh traversal of a list.
- Generator functions/objects, yield suspension, and consumer-driven execution.
- Text-file reading/writing, UTF-8 encoding, and JSON serialization/deserialization.
- JSON file versus string APIs and explicit Decimal → string → Decimal conversion.

## Latest verification

Inspected exercises/json_basics.py and ran
.venv/bin/python -m exercises.json_basics: exit 0, printed Groceries, 424.75,
and <class 'decimal.Decimal'>. Earlier run also verified budget.json stored
{"category": "Groceries", "remaining": "424.75"}. Final code reconstructs the
Decimal after loading. Explained dump/dumps and load/loads, unsupported Decimal
serialization, and JSON text versus UTF-8 bytes. Concept guide updated by topic.
No application tests run for this standalone exercise.
Next proposed lesson: serialize a Transaction with Decimal and date fields,
then reconstruct it, introducing explicit object-to-data conversion.

Inspected exercises/file_basics.py and executed
.venv/bin/python -m exercises.file_basics: exit 0. Printed and independently read
budget_note.txt containing "Remaining budget: 424.75". Both write/read operations
use with and UTF-8; content is printed after the read block. No application tests
run for this standalone exercise. Concept guide now covers text persistence,
file modes, automatic closing, paths, and retained in-memory text.
JSON serialization subsequently completed; see latest checkpoint above.

Mentor inspected exercises/timer_context.py and ran it with the project
interpreter: exit 0, elapsed time: 0.000009. __enter__ stores self.start and returns
self; __exit__ stores/prints self.elapsed and returns False. Current script does
not print its remaining-budget value; only timing was observed. No app tests run.

Mentor inspected timing_decorator.py using try/finally and ran the user's uv
module command: expected exit 1 from Decimal-minus-string TypeError; timing line
still printed. Explained stdout versus stderr buffering and outer print argument
evaluation. Learner confirmed seeing the timing line. This is an intentional
failure experiment, not an application regression. No application tests run.

Mentor inspected exercises/timing_decorator.py and ran it with the project
interpreter: exit 0, calculate took 0.000002 seconds, then 425.00. It uses wraps,
generic forwarding, perf_counter subtraction, and preserves the Decimal result.
Timing varies; this single trivial call is not a performance benchmark. No app tests.

Mentor inspected exercises/generic_decorator.py with @wraps(operation) and ran
it using the project interpreter: exit 0. calculate reports its preserved name
and docstring; describe_category has its preserved name and None docstring because
none is defined. Return values and before/after behavior remain correct.

Mentor inspected exercises/generic_decorator.py and ran the user-requested
`uv run python -m exercises.generic_decorator`: exit 0. Both functions print
Starting operation/Finished operation; returned results are 425.00 and
Calculate: Groceries. Generic wrapper correctly forwards mixed positional and
keyword arguments. No app code changes or app tests for this learning exercise.

Mentor inspected exercises/variable_arguments.py and ran it with the project
interpreter: exit 0. *amounts receives tuples for two, three, and zero inputs;
totals 30.00, 35.00, 0.00. Learner corrected sum's default integer start to explicit
Decimal zero. No app changes or app tests for the learning exercise.

Mentor inspected exercises/decorator_status.py and executed its calls plus an
exactly-at-limit call: within budget/425.00, over budget/-25.00, within budget/0.00.
Asserted zero result remains Decimal. Learner fixed string return to printing
status plus returning balance, then corrected >= 0 boundary. No application tests.

Mentor inspected the saved @announce version of exercises/decorators.py and ran
it with the project interpreter: exit 0, Starting calculation, Calculation
finished, 425.00. The decorated local calculate delegates to imported
calculate_remaining. User requests another exercise for confidence.

Mentor inspected exercises/decorators.py and ran it with the project interpreter:
exit 0; Starting calculation, Calculation finished, then 425.00. Wrapper retains
the original function and returns its result. No app code changes or app tests.

Mentor inspected exercises/closures.py and ran `.venv/bin/python -m exercises.closures`:
exit 0, True then False. Learner returns an inner checker retaining Groceries and
uses it on grocery and gas transactions. This is a valid variation on the suggested
two-checker/one-transaction exercise. No application code changes or tests in review.

Mentor inspected exercises/function_objects.py and ran it with the project
interpreter: exit 0, True followed by 425.00 twice. The learner aliases an existing
function, calls the alias, and passes the function to another function. No app
code changes or application tests for this standalone learning exercise.

Mentor inspected the saved generator expression in transaction_comprehensions.py
and ran `.venv/bin/python -m exercises.transaction_comprehensions`: exit 0,
120.00 on the first sum and 0.00 on the second. It uses parentheses and consumes
the same generator twice. No application changes or application tests in this review.

Mentor inspected exercises/transaction_comprehensions.py and ran it through uv:
exit 0, list of grocery Decimal amounts 40.00, 20.00, 10.00, 40.00, 10.00.
The filter excludes Gas/Vacation and includes groceries across all dates.
No application code/test changes or app-suite run for this quick concept exercise.

Mentor inspected exercises/stream_category_totals.py and ran it through uv:
exit 0, Groceries 15.00 and Gas 20.00. It accepts Iterable[Transaction], consumes
the generator once, and accumulates using dictionary membership plus assignment.
No application code changes or application tests for this standalone exercise.

Mentor inspected exercises/generator_reuse.py and ran it through uv: exit 0,
Groceries 90.00, Gas 80.00 after list(fresh_generator) materialization. This is a
standalone experiment; no application implementation or tests changed in review.

Mentor inspected exercises/transaction_stream.py and ran it through uv: exit 0,
three Transaction representations and total 30.00. Function now constructs and
yields one transaction inside range(count), rather than building a fixed list.
No application tests run for this standalone learning exercise.

Mentor inspected the updated exercises/transaction_generator.py and ran it through
uv: exit 0. The external Generator created message appears first; two next calls
then print preparation messages and values 20.00 and 50.00. Third amount remains
unrequested. No application tests run for this standalone learning exercise.

Mentor inspected and ran `uv run --locked python -m exercises.transaction_iteration`:
exit 0. next(cursor) prints 40.00; first cursor loop prints 20.00 and 10.00;
second cursor loop prints no items; looping over amounts prints all three again.
No application tests rerun for this standalone learning exercise.

Latest focused run: Transaction model tests, 9 passed, exit 0. Full application
suite was last run before the latest non-finite-test corrections (38 passed then).
No application tests were rerun for the concept-note reorganization, which changes
documentation only. Python 3.14.6, pytest 9.2.0; dependencies recorded through uv.

Category budget example: limits total 1100.00; groceries remaining -25.00,
restaurants 100.00, gas 50.00, miscellaneous 150.00. Data is fictional.
Mentor reran the module demonstration after the date-field changes; same results, exit 0.

## Learning priority and next task

User explicitly prioritizes learning new concepts over tightening every edge case.
They are comfortable with unit tests, pytest fixtures, parametrization, and the
current validation patterns. Advance when understanding is demonstrated; use
focused verification rather than more repetitions of the same test pattern.
Do not silently drop deferred correctness work or call the application complete.

Iterator exercise complete. Learner initially predicted an iterator would restart
and the list would not; clarified and demonstrated the opposite. Consuming the
iterator does not remove items from its list. Concept guide updated by topic.
Generator exercise verified: learner wrote three yields and consumed with next.
Clarified yield is a keyword; the generator object is the iterator. Discussed
incremental CSV processing as a real-world connection; saved exercise yields
amounts, not file records. Concept guide updated under iterators.
Transaction-generator exercise complete: learner initially built a fixed list
inside the generator, then changed to constructing one transaction per yield.
Explained that first request executes list creation in full; lazy start does not
alone eliminate retained collections. Corrected direct-file invocation to module
execution so sibling package imports resolve. Concept guide updated by topic.
Generator-reuse experiment complete. Clarified generator function versus generator
object versus yielded item; internal producer loop and consumer next requests;
iter(source) behavior for lists versus iterators; list() as a consumer retaining
yielded references. Learner confirmed the materialized-list version works, and
mentor independently observed correct results. Source skipping still consumes items.
One-pass aggregation now implemented correctly in an exercise. Learner uses an
if/else for first/existing category; get is an alternative, not a required rewrite.
The sample includes dates from different periods; function intentionally totals
across all dates. Reviewed average O(n) traversal/O(k) aggregate storage. Existing
application monthly summary still uses list/repeated traversal; not migrated yet.
List-comprehension filter now implemented and verified. Explained trailing if
(filter) versus conditional expression before for (choose one of two values).
Learner requested quick concept practice; don't require additional drills or sum
checks before advancing. Concept guide updated under collections.
Generator expression now saved and verified: [] comprehension changed to (),
then two sums demonstrate exhaustion (120.00, 0.00). Explained parentheses alone
do not create a generator; the comprehension expression does. Guide updated.
Function-object exercise now verified. Clarified that = binds a name and does not
itself create an instance, and parentheses call a callable. A function name is an
object reference; passing a call would supply its result instead. Concept guide
updated by topic, including dictionary comprehensions discussed alongside iteration.
Closure exercise verified. Explained the inner function's use of an outer local
binding, retention after outer return, closure cells, and returning a function
instead of calling it. Concept guide updated under functions.
Manual decorator now verified with before/after messages. Learner initially
returned operation(...) directly; explained storing the result before after-work
and returning it. Concept guide updated under functions.
@announce now implemented and verified. Clarified the extra local calculate
function, what is passed implicitly, wrapper return/rebinding, and later call flow.
Explained practical reasons for decorators. Additional report_status exercise
now complete: captures operation, reports status, preserves Decimal result,
and includes zero in the within-budget case. Concept guide updated by topic.
*amounts collection now verified, including tuple inspection and empty tuple.
Clarified sum's default integer starting value versus Decimal start.
Learner correctly restated * collection/unpacking and ** keyword mapping behavior.
Clarified unpacking makes multiple arguments to one call, not multiple calls;
printing the collected tuple once displays values together. ** is not an error
handling safety net. Concept guide updated by topic. keyword_arguments.py exists
but was not reviewed or executed during this notes-only update.
Previous stopping-point task is complete: generic decorator saved and verified
on 2026-11-08. Both differing signatures work with wrapper(*args, **kwargs) and
operation(*args, **kwargs), preserving results. Category label says Calculate:
rather than Category:, a cosmetic variation. Concept guide updated by topic.
Metadata exercise complete: @wraps applied, names/docstrings inspected; explained
__wrapped__, wrapper code name versus copied metadata, and object identity.
Timing decorator with try/finally now verified for deliberate failure. Learner
understands finally reports elapsed time while the error propagates; it initially
looked absent because stdout's timing line appeared after stderr's traceback.
Updated concept guide with exit semantics, output streams, and python -u.
Class-based Timer now implemented and verified on normal completion. Discussed
dunder methods versus normal methods, protocol lookup by with, instance creation,
__enter__ return/as binding, exception parameters and False versus True on exit.
Learner fixed local start to self.start after NameError/AttributeError, clarifying
method-local scope versus per-instance attributes. Concept guide updated by topic.
Generator-based timer now implemented in exercises/generator_timer.py. Inspected
and executed with .venv/bin/python -m exercises.generator_timer: exit 0, printed
425.00 followed by elapsed time. No application tests run for this standalone
exercise. Explained the distinction between with, a context manager, class
entry/exit methods, @contextmanager, and function decorators. Recorded the
entry → yield/pause → with body → finally sequence in the concept guide.
Learner requested clarification of these relationships; revisit briefly before
advancing rather than assuming all generator-manager mechanics are mastered.
Monthly stream integration can follow later; don't repeat tests as a learning blocker.
General decorators,
OOP composition/protocols, algorithms,
databases, concurrency, GIL, and distributed systems remain future topics.

## Current code and verification checkpoint

Shared Transaction rejects blank category, non-Decimal amounts, and non-finite
Decimal values. Negative refunds are accepted. Budget validates blank category
and negative limit. Monthly calculations validate month and reject duplicate
budget categories. Summary calculation and report printing are separated.

Latest focused verification: Transaction model file, 9 passed, exit 0. Non-finite
checks now use actual Decimal values and expect ValueError. Earlier whole-app
run passed 38 cases before the corrected non-finite tests; do not treat it as a
full rerun of the latest files. Application tests live in tests/, historical
learning tests in exercises/, with shared fixtures in tests/conftest.py.

## Deferred hardening (not learning blockers)

- Restore None to non-Decimal inputs and clarify amount validation messages.
- Apply equivalent type/finite checks to Budget.limit before comparison.
- Explicit category/date/year/type policy and currency precision/rounding policy.
- Unify or archive earlier exercise-only models deliberately; remove unused fixtures.
- Reassess milestone 1 completion criteria and add meaningful missing financial
  behavior before declaring the engine complete or ready for real data.

## Learning-record convention

User requests **one concept-based revision guide**: LEARNING_NOTES.md. It is now
organized by concept with a contents list, explanations, focused examples,
common mistakes, and recall questions. Update relevant concept sections as we
learn; do not append a new entry per test/day. This supersedes the earlier
chronological-lesson convention. Session history is preserved in
learnings/SESSION_HISTORY.md; daily files are archives. Verification and next tasks
stay in this progress file. Iterator/generator basics and text-file handling have
been covered along with basic JSON; next proposed topic is object-to-data conversion.

## Session recovery and teaching preferences

Read LEARNING_MASTER_PROMPT.md, LEARNING_NOTES.md, ROADMAP.md, and this checkpoint.
Inspect actual files before assuming prior changes exist. Mentor first: let the
learner implement core code. Skip familiar material on request; pause at unfamiliar
concepts. When confused, use one change and one check at a time. Function decorators
and generator basics have been practiced; concurrency, GIL, databases, and web
development remain future lessons. Mentioning a topic does not mean it was mastered.

## Repository

Branch main; origin: https://github.com/srmandli95/MyBudget.git.
Commit or push only as authorized. Saving learning notes does not itself mean
that they have been committed or uploaded.
