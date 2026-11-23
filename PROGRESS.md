# Progress

Last updated: 2026-11-23.

## Current milestone

Learning/build split confirmed (2026-11-21): cover backend concepts first, then
build the integrated backend. Use concise explanations and isolated experiments
for new mechanisms, with MyBudget examples for context. Do not resume routine
application integration simply because a concept chapter finishes. Current
conceptual track is HTTP → FastAPI/backend fundamentals → relevant concurrency,
background processing, security, and architecture, before frontend. Exact next
lessons can adapt to unfamiliar concepts. Application deliverables remain a
separate incomplete build track. AGENTS/master prompt/roadmap reflect this choice.

Latest direction (2026-11-21): learner wants new concepts now and application
development/integration later. Defer the remaining SQLite/report/budget wiring;
do not assign more integration tasks as prerequisites to HTTP/FastAPI learning.
Begin Milestone 3's conceptual material while keeping Milestone 2's application
deliverable explicitly incomplete. This does not change the agreed order of
concurrency before frontend. HTTP request/response and client-to-server flow
now discussed along with GET/POST/PUT/PATCH/DELETE and safe/idempotent semantics.
Status-code families and common responses now covered, including 401 versus 403.
Next lesson: request data locations (path/query parameters, headers, and body).
No feature wiring is required first.

Learning-order change (2026-11-19): after finishing SQLite (2) and FastAPI (3),
cover simulated synchronization/concurrency (6) before React (4). Full order:
1 → 2 → 3 → 6 → 4 → 5 → 7 → 8 → 9 → 10 → 11. Numbers remain stable IDs.
Use simulated providers through CLI/API experiments without a frontend or CSV
dependency. The active conceptual track is now HTTP/backend fundamentals, not
the later concurrency milestone. ROADMAP.md and the master prompt reflect the plan.

Latest teaching direction (2026-11-18): prioritize new concepts and fast forward
progress, with depth when unfamiliar. One focused example/exercise per new idea;
skip repeated validation/conversion drills and defer routine standards/hardening
to application work. Learner identified money conversion as familiar validation,
not a new topic. Index/query-plan lessons have since been covered.
Do not require bounds/rounding helpers or more money-validation drills first.
Index/query-plan, composite-index, and basic schema-migration lessons covered.
Migration-version tracking, ACID overview, and basic two-connection isolation
now covered along with basic write locking/contention and WAL read snapshots.
Normalization, anomalies, and practical 1NF/2NF/3NF examples now discussed.
Next: remaining Milestone 2 application integration. Avoid repeated CRUD or cleanup
drills as prerequisites to learning the mechanism.

Milestone 2: SQLite persistence, beginning. Milestone 1's functional criteria are
met: shared models, configurable in-memory budgets, tested calculations/refunds,
and CLI calculation/monthly-report integration using explicit fictional data.
The learner demonstrated concepts throughout the apprenticeship; the final
optional module-responsibility recap was offered but not answered. Do not treat
it as completed or block forward learning on another quiz. Remaining Python
topics and deferred hardening continue alongside the application.

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
- Explicit Transaction-to-dictionary conversion, ISO date strings, and reconstruction.
- Tracker composition, instance methods, per-instance list factories, and computed properties.
- Polymorphism through compatible write methods, duck typing, and optional instance data.
- Inheritance, overriding, super delegation, and one-instance data versus class methods.
- Abstract base classes, required abstract methods, and concrete subclass implementations.
- Class methods, cls binding, and alternative constructors that convert input data.
- Static methods, no implicit first argument, and choosing module functions versus class grouping.

## Latest verification

HTTP status lesson recorded: explained 1xx–5xx families and common 200/201/204,
400/401/403/404/409, and 500 responses. Learner correctly distinguished 4xx/5xx,
then asked about token errors; clarified missing/invalid/expired authentication
normally produces 401, while authenticated lack of permission is a typical 403.
Corrected ambiguous mnemonic: 401 does not mean authentication succeeded.
Also covered empty collection 200/[] versus missing item 404 and status versus
body. Concept guide updated with concise Q&A and HTTP-spec source. No API
implementation, experiment, or automated tests performed. Next: request inputs.

HTTP methods lesson recorded: covered method/path combinations, resource versus
database row, PUT replacement versus PATCH modifications, safety, idempotency,
and retry-after-timeout motivation. Learner questioned why an increment through
PUT would differ; clarified method contracts versus arbitrary backend behavior,
and that PATCH can be idempotent when setting a fixed value. Learner confirmed
understanding. Added concise Q&A/tables and RFC 9110/5789 sources to the guide.
Conceptual discussion only: no API implementation, HTTP experiment, or tests run.
Next topic is response status codes; keep backend-learning-first preference.

HTTP foundation lesson recorded on 2026-11-23. Covered HTTP/HTTPS, client request
and server response, method/target/headers/body/status, and new TCP-based HTTPS
flow through DNS, ports, TCP, TLS, packet transport, and server application routing.
Clarified HTTP message semantics versus underlying delivery and server software
versus business logic. Learner confirmed understanding; no network experiment,
FastAPI implementation, or automated test was performed. Added concise Q&A and
contents link to LEARNING_NOTES.md using previously consulted MDN sources.
Next: HTTP methods; retain concepts-first/development-later preference.

CLI add integration checkpoint before deferring development: reviewed main's
add branch, then tested the actual CLI in an isolated temporary working directory
using project imports. It saved a fictional Groceries/40.00/2026-11-21 transaction;
after the subprocess exited, a separate read-only connection retrieved that row.
Initial missing commit parentheses lost pending writes; learner corrected it.
Final inspection confirms finally only closes the connection, with diagnostic
query removed. Full suite not rerun for these changes. Working user database was
not modified by mentor's isolated checks. Report still uses demo data; persisted
budget configuration, storage/report workflow integration, and related checks
remain deferred. No new concept-note entry needed for this integration practice.

Normalization lesson discussed without another coding drill. Recorded update,
insertion, and deletion anomalies; practical 1NF repeating-group, 2NF partial-key,
and 3NF transitive-dependency examples. Learner initially inferred that dependence
on a single column requires extraction; clarified whole single-column key is
fine, while dependence on only a proper subset of a composite key is the 2NF
problem. Learner confirmed understanding. Added concise Q&A with a dependency
table to the guide. No new code executed or tests run for this discussion.
Next step is application integration rather than more normalization drills;
Milestone 2 persistence/reporting workflow is still incomplete.

Reviewed exercises/sqlite_wal.py and ran with the project interpreter: exit 0,
printed 100, 100, 300. Setup enables WAL on a dedicated database and resets the
counter. Reader BEGIN plus first SELECT establishes a snapshot; writer commits
300 while reader stays open; reader sees 100 until ending its transaction, then
fresh read sees 300. Initial 100/300/300 output lacked BEGIN; learner corrected
it. Final reviewed script lacks explicit reader/writer close; tracked as routine
cleanup, not a learning blocker. Added concise Q&A on WAL/checkpointing, snapshot,
and BEGIN. No app suite run or app journal mode changed. Next: normalization;
no extra snapshot drills are needed after demonstrated understanding.

Write-locking lesson: learner reported exercises/sqlite_locking works after
adding the counters table/starting row. Explained automatic lock acquisition on
UPDATE in our default transaction setup, one active writer, timeout=0, and release
when the transaction ends. Clarified that another connection can read the old
committed value in this experiment; read blocking depends on journal mode/phase.
Added two concise Q&A entries to the revision guide. Exercise file exists but
mentor has not inspected or executed it in this notes-only update; successful
outcome is learner-reported, not independently verified. No tests run or app code
changed. Next: WAL/journal modes and snapshots; avoid another write-lock drill.

Revision-guide rewrite requested on 2026-11-19. Reorganized LEARNING_NOTES.md
from 3,086 lines into concise question-and-answer entries grouped by concept.
Each answer begins directly, with limited examples/tables and essential caveats;
removed repeated quizzes, lesson walkthroughs, exercise-specific status, and stale
future-topic claims. Retained coverage of Python/OOP, testing/tools, SQL/storage,
indexes, migrations, and ACID/isolation. Updated AGENTS.md and the master prompt
to preserve this style in future sessions. This is a documentation change, not
a new learning milestone or implementation task. Active next topic remains
SQLite write locking/contention and journal-mode behavior. Validated all 21
contents links, syntax of 12 illustrative Python snippets, Markdown fence balance,
and whitespace checks. These checks do not execute the examples. No app code changed
and no application tests run for the notes rewrite; no commit/push performed.

Reviewed exercises/sqlite_isolation.py and ran it with the project interpreter:
exit 0, printed "before first commit", [(1, 100)], "after first commit",
[(1, 300)]. One dedicated file is reset to a committed 100; first connection
updates to 300, second reads before and after first.commit(), then both close.
Corrected initial commit-before-only-read arrangement through learner edits;
final sequence independently verifies hiding pending writes and fresh-read
visibility after commit. Concept guide updated with ACID and assumptions.
No app suite or crash/concurrency benchmark run. Long-running read transactions,
WAL/snapshots, and write contention have not yet been demonstrated. This is a
standalone lesson, not application storage integration or completed concurrency.

Migration-version lesson: inspected exercises/sqlite_migration_versions.py at
the troubleshooting stage; it had no version branch or printed messages and
attempted ALTER on every run. Explained reading PRAGMA user_version, conditional
migration, and explicit BEGIN grouping schema change with marker update. Learner
subsequently reported "Already at version 1" and correctly summarized schema
versions for alterations. Final edited script was not independently inspected
or run by the mentor; do not claim a verified two-run sequence. Concept guide
updated. No application suite run or actual app migration implementation done.
Next lesson introduced: ACID overview, without repetitive implementation drills;
isolation/concurrent-connection experiments remain pending.

Reviewed exercises/sqlite_migrations.py and ran it with the project interpreter:
exit 0, printed [(1, 'Groceries', 2000, None)] followed by
[(1, 'Groceries', 2000, 'Costco')]. ALTER TABLE adds a nullable merchant column
without losing the row; UPDATE backfills the merchant. Corrected extra string
quote, parameter ordering, and cursor versus fetched rows through learner edits.
Last reviewed script lacked explicit close; learner later said done, but that
cleanup was not reinspected. Record it as unverified, not a learning blocker.
Concept guide updated only for migration/schema-versus-data concepts. No app
suite run. Application database migrations remain unimplemented. Next: version
tracking to skip changes already applied to a persistent database.

Inspected exercises/sqlite_composite_indexes.py and ran it with the project
interpreter: exit 0, SEARCH transactions USING COVERING INDEX idx_category_date
(category=? AND transaction_date>?). Confirmed first query uses both columns.
Saved script at review time had only the category/date query, no date-only
comparison, and did not explicitly close the connection; suggested both changes,
but neither was independently rechecked. Learner understood category-first/date-
within-category ordering after clarifying direct seeking versus scanning every
category. Concept guide updated with column order and leading-column lookup.
No performance benchmark or application suite run; do not imply measured speedup.

Index lesson: learner supplied EXPLAIN QUERY PLAN output showing SCAN transactions
before indexing and SEARCH transactions USING COVERING INDEX
idx_transactions_category (category=?) afterward. exercises/sqlite_indexes.py
exists, but mentor did not inspect/run it during this notes-only update. This is
learner-provided output, not a measured performance benchmark. Consulted official
SQLite docs/source to explain node/parent IDs and implementation-specific third
cost field. Recorded index storage/write-maintenance trade-offs, covering index,
and plans versus actual timing. Learner correctly summarized retrieval benefits
and asked about write overhead; no repeated timing drill is required.
No application tests run or commit/push performed.

Reviewed updated exercises/sqlite_money.py and ran it with the project
interpreter: exit 0, printed 0.00 before inserts and 45.00 afterward. Empty-table
query uses COALESCE(SUM(amount_cents), 0). Populated-table query still uses plain
SUM; suggested using the same safe expression there, but that follow-up has not
been verified. Normal query work is now inside try and finally only closes,
resolving the earlier cleanup-structure issue. Concept guide updated with
NULL/None versus zero, first-non-NULL fallback, and aggregate behavior.
No application tests run. App storage still uses text amounts; precision policy
and deliberate migration remain pending before integer storage integration.

Inspected exercises/sqlite_money.py and ran it with the project interpreter:
exit 0, printed 45.00. In-memory table stores 2000 and 2500 cents, SQL SUM returns
4500, and Python converts through Decimal before division/display. Concept guide
updated with minor-unit representation, aggregate result extraction, truncation
policy, empty SUM, integer range, and application migration still pending.
Current saved script still performs normal query work inside finally; suggested
moving it into try so failures do not mask setup errors or skip close. That
organizational correction is not saved/verified and should not be called complete.
No application tests run; app storage schema remains text amounts. Next proposed
concept: explicit amount precision policy and empty-summary handling before
integrating integer amounts into application storage.

Reviewed grouped query in exercises/sqlite_relationships.py and ran it with the
project interpreter: exit 0, printed expected foreign-key error followed by
[('Groceries', 1), ('Gas', 0), ('Grocery', 0)]. This verifies LEFT JOIN includes
unused categories and COUNT(t.id)/GROUP BY produces correct counts. Learner
initially added Grocery as a category rather than another Groceries transaction;
explained distinct names under UNIQUE and multiple children referencing one
category ID. Learner then reported the revised multi-transaction version worked;
that final edit was not independently rerun by the mentor. Concept guide updated
with aggregation and COUNT(*) versus non-NULL-column counting. No application
suite run. Next proposed new concept: exact money storage as integer minor units
before SQL SUM/grouped monetary reports. Application schema migration is not yet
implemented and text amounts must not be silently reinterpreted as integers.

LEFT JOIN lesson discussed; learner correctly restated that all left rows are
preserved with matching right-side rows. Clarified SQL NULL maps to Python None
for unmatched columns, table order matters, and several matches produce several
result combinations. Learner reported completing the exercise, but mentor has
not inspected or executed the updated LEFT JOIN script. Record conceptual
understanding separately from unverified saved output. Concept guide updated;
no tests run during this notes-only update. Next: grouped aggregation, beginning
with transaction counts per category and COUNT behavior on unmatched rows.

Inspected updated exercises/sqlite_relationships.py and ran
.venv/bin/python -m exercises.sqlite_relationships: exit 0, printed
"FOREIGN KEY constraint failed" and [(1, 'Groceries', '20.00')]. This independently
verifies the corrected foreign-key experiment as well as the INNER JOIN using
aliases t/c and ON t.category_id = c.id. Learner corrected multiline SQL from
ordinary quotes to triple quotes after a Python SyntaxError. Concept guide now
covers joins, aliases, matched results, and retrieval versus enforcement.
No application suite run for this standalone lesson. Next proposed new concept:
LEFT JOIN, to include categories that have no transactions, then grouped summaries.

Foreign-key lesson: reviewed exercises/sqlite_relationships.py with categories
and transactions tables and PRAGMA foreign_keys = ON before writes. Initial
mentor run failed with OperationalError because INSERT used category instead
of the schema's name column. Explained correcting it to name, binding a one-item
tuple, and printing caught IntegrityError. Learner subsequently confirmed the
expected foreign-key error/result after editing; the corrected script was not
rerun by the mentor in this notes-only update. Record the successful result as
learner-confirmed, not independently verified. Concept guide covers one-to-many
relationships, primary versus foreign keys, per-connection enforcement, and
referential integrity. No application tests run. Next: JOIN to retrieve category
names alongside transaction data; cascade/deletion policies remain future work.

Reviewed exercises/sqlite_unique.py after learner edits and ran
.venv/bin/python -m exercises.sqlite_unique: exit 0, printed
"UNIQUE constraint failed: category.name" followed by [(1, 'Groceries')].
Current table is named category consistently. Two identical bound inserts are
attempted; the first is committed, the second rejected and caught, rollback
leaves the first committed row. Explained that catching/printing IntegrityError
avoids a traceback without making the rejected insert succeed. Concept guide
updated with business uniqueness and distinction from row identity/NOT NULL.
No application tests run for this standalone experiment. Next proposed topic:
foreign keys and relationships connecting transaction rows to category records.

Application storage boundary implemented in mybudget/storage.py with
initialize_database, save_transaction, and load_transactions. Caller injects the
connection and owns commits/rollback/close. Ran exercises/storage_demo with the
project interpreter: exit 0, saving/loading a Groceries Transaction with
Decimal('22.45') and date(2026, 10, 11). Reviewed final imports and resolved type
hints with typing.get_type_hints after correcting sqlite/sqlite3 and Connection
names. No undefined annotation names remain in those inspected functions.

Reviewed category CHECK(length(trim(category)) > 0) in initialize_database.
Valid demo still passed. Separate focused in-memory experiment using the actual
initializer rejected both empty and ordinary-space-only categories with
sqlite3.IntegrityError. Existing disk schema was not migrated or tested with
the new rule. Recorded model versus database enforcement, NULL/blank distinction,
trim/strip difference, and CREATE IF NOT EXISTS limitation in the concept guide.
Also recorded dependency injection and caller connection ownership as concepts;
implementation verification belongs here. No full application suite run for
these changes and no automated storage tests added yet.
Next proposed new concept: UNIQUE constraints and business uniqueness, using
category/budget configuration rather than incorrectly rejecting repeated expenses.
CLI integration, persisted budgets, and relationships remain pending.

Inspected exercises/sqlite_updates.py and ran
.venv/bin/python -m exercises.sqlite_updates: exit 0, printed
[(1, 'Groceries', '55.00')]. In-memory setup inserts two valid rows; parameterized
UPDATE targets ID 1 and DELETE targets ID 2 with commits. Final state confirms
both operations. Script prints the final state only; intermediate stage output
was not verified separately, and no further drill is required. Concept guide
updated with CRUD, SET/WHERE, binding, and commit boundaries. No application
suite run. Next: move learned SQL/model conversion behind an application storage
module, then connect it to the CLI without mixing SQL into calculation functions.

Verified named-row reconstruction in exercises/sqlite_queries.py: ran with the
project interpreter, exit 0, printed a list of three Transaction objects with
category Groceries, Decimal('40.00'), and date(2026, 11, 14). row_factory is
sqlite3.Row; saved strings are explicitly converted before model construction.

Inspected exercises/sqlite_transactions.py and ran
.venv/bin/python -m exercises.sqlite_transactions: exit 0, printed []. Confirmed
both inserts are present: valid Groceries/40.00 followed by None/20.00 violating
NOT NULL. Handler rolls back, commit is not reached, and finally queries before
closing the in-memory connection. Earlier invalid-only version was insufficient;
learner restored the valid first insert. Recorded atomicity, pending changes,
commit boundaries, targeted SQL errors, and exact :memory: spelling in the guide.
No application suite run for these standalone experiments. App persistence and
budget storage remain pending. Next proposed lesson: UPDATE/DELETE with bound
WHERE conditions, then a reusable application storage boundary.

Inspected and ran .venv/bin/python -m exercises.sqlite_queries: exit 0, returned
the three Groceries rows with IDs 1/2/3 in ascending order. Script uses a bound
one-item parameter tuple, WHERE category = ?, ORDER BY id, fetchall, and finally
connection cleanup; it performs no inserts. Gas/no-match behavior was explained
but not separately exercised by the mentor. Updated concept guide with filtering,
ordering, and parameter tuple syntax. No application tests run for this exercise.
Next: sqlite3.Row for named column access, then reconstruct Transaction objects
from stored strings. This next behavior is proposed, not yet implemented/verified.

Reviewed and ran .venv/bin/python -m exercises.sqlite_basics: exit 0, retrieved
three Groceries rows with amount "40.00" and date "2026-11-14", IDs 1/2/3.
Mentor execution inserted the third fictional row as expected. A separate Python
process reopened file:learning_budget.db?mode=ro and retrieved row 3, verifying
committed data persisted beyond the first process. CREATE and INSERT now use
separate execute calls; INSERT binds values, commits, then SELECT/fetchall reads
rows; finally closes the connection. Updated concept guide with SQL operations,
parameter binding, generated IDs, repeat-insert behavior, and file persistence.
No application test suite run for this standalone exercise; app storage integration
remains pending. Next proposed topic: WHERE filtering with bound parameters,
followed by reconstructing Transaction objects from stored rows.

SQLite lesson: inspected exercises/sqlite_basics.py; it imports sqlite3, opens
learning_budget.db, creates transactions with id/category/amount/date columns,
commits, and closes in finally. Learner reported running the module and showed
the schema query output [('transactions',)], confirming table existence in their
session. Mentor did not independently run the database exercise or schema query
during this notes-only update. No inserted rows or persistence-query workflow
has yet been verified. Next: parameterized INSERT, commit, and SELECT of a
fictional transaction. Database integration into the app remains pending.
Concept guide now covers relational/SQLite basics, result rows, library categories,
and internal packages hosted in Artifactory. Publishing/private-index setup was
not performed. No tests run or commit/push during this documentation update.

Milestone 1 integration reviewed on 2026-11-13. demo_data is consistently named
across definition/import/call. Focused CLI runs exited 0: calculate printed
424.75; October report showed -25.00/100.00/50.00/150.00 remaining; November
showed full budgets 500.00/200.00/250.00/150.00 because no transactions matched.
uv run --locked python -m pytest tests exercises -v passed all 44 cases, exit 0.
These are manual CLI checks plus existing automated calculation/model tests;
there are no new automated CLI/report tests. Next: first SQLite table exercise.
exercises/sqlite_basics.py was not present at this checkpoint. No database
implementation has been verified, and no commit/push was performed.

Reviewed mybudget/reports.py and verified the formatter on a focused fictional
500.00/40.00 example: returned a November report with 460.00 remaining. Learner
then moved demonstration data/printing under the main guard. Import verification
produced no output, exit 0. Final .venv/bin/python -m mybudget.reports run exited
0 and printed the October header plus remaining amounts Groceries -25.00,
Restaurants 100.00, Gas 50.00, miscellaneous 150.00. Formatting calls the monthly
calculation once and returns newline-joined text. This is integration practice
using existing concepts, not a new lesson. Removed the redundant formatter-specific
section from LEARNING_NOTES.md at the learner's request; implementation and
verification stay here. Update concept notes only for new concepts or meaningful
clarifications, not each application task.
No full test rerun during this review; latest full baseline remains 44 passing
cases before report addition. Next: connect a report CLI command using explicit
fictional demo data, verify the workflow and relevant checks, then close
Milestone 1 against its in-memory engine criteria. Do not mark it complete yet.

Recorded CPython reference counting, del versus destruction, weak references,
and unreachable reference cycles in the concept guide. Inspected and ran
.venv/bin/python -m exercises.object_lifetime: exit 0, printed True, True, True.
This verifies that the second strong reference keeps Note alive and removal of
both bindings permits reclamation in the project interpreter.
Cycle-collection example was explained and the learner restated the mechanism.
exercises/reference_cycle.py is not present; no saved cycle experiment was run
by the mentor. Do not mark that experiment executed. No application tests run
for this documentation/standalone-exercise update. Milestone 1 report integration
remains pending; no new hardening work is required before returning to it.

Encapsulation/naming lesson discussed before Milestone 1 closure. Recorded public
names, _internal (commonly "protected") convention, __private name mangling,
absence of enforced Java-style access restrictions, and __dunder__ distinction.
Explained accidental subclass attribute collisions on one instance, intentional
shared attributes, and properties as separate from hiding data.
exercises/encapsulation.py exists, but its contents and execution were not reviewed
during this notes-only update. Do not mark that exercise verified. Milestone 1
report integration remains pending; no new application tests run in this update.

Milestone 1 closure requested. Ran the required root command
uv run --locked python -m pytest tests exercises -v: 44 passed, exit 0
(38 application cases and 6 historical learning cases). Existing monthly demo
uses shared models and calculations but lives in exercises/monthly_budgets.py;
CLI currently exposes calculate only. Next learner task: extract reusable report
formatting into mybudget/reports.py, then connect a fictional-data monthly report
command to the CLI. Recheck the resulting workflow and update roadmap criteria
before marking the milestone complete. SQLite remains Milestone 2.

Inspected mybudget/cli.py after subcommand changes and ran three focused commands
with .venv/bin/python -m mybudget.cli: calculate --budget 500.00 --spent 75.25
printed 424.75, top-level --help listed calculate, and calculate --help listed
required --budget/--spent inputs. All exited 0. Corrected the learner's
parser.calculate_parser() call to parser.parse_args() through their edit.
Explained subparser registration, dest="command", required command selection,
command-specific arguments, and parsing versus function dispatch. Concept guide
updated. Only calculate is implemented; add/report are examples of future commands.
No automated suite run. Next proposed lesson: dispatch a second command to its
own handler, then connect transaction input to the existing model and persistence.

Inspected mybudget/cli.py with parse_amount and ran two focused commands using
the project interpreter. Valid --budget 500.00 --spent 75.25 printed 424.75,
exit 0. Invalid --budget hello --spent 75.25 printed usage and
"argument --budget: Enter a numeric amount, for example 500.00", exit 2,
without a traceback. Converter catches InvalidOperation and raises
argparse.ArgumentTypeError; both arguments use the callback and main receives
Decimals directly. Concept guide updated with callbacks, targeted catches,
error presentation, and status codes. No automated application suite run.
Subcommands were subsequently implemented and verified above. Non-finite inputs and sign policies
remain deferred; they are familiar validation concepts, not blockers to learning.

Inspected mybudget/cli.py and ran
.venv/bin/python -m mybudget.cli --budget 500.00 --spent 75.25: exit 0,
printed 424.75 after learner saved print(main()) in the main guard. main parses
required string arguments, converts them to Decimal, and returns the calculation.
Earlier --help run exited 0 and listed --budget, --spent, and -h/--help; that was
before moving parsing into main, not a separate rerun of the final help command.
Recorded argparse, CLI/package paths, main guard, and return versus print in the
concept guide. No full application suite or new CLI tests run for this update.
Friendly invalid-text handling was subsequently implemented and verified above.

Inspected exercises/static_methods.py and ran
.venv/bin/python -m exercises.static_methods: exit 0, printed False for spending
75.25 against 500.00 and True for spending 550.25. Static-method binding is
correct. Focused equal-limit check using the saved class returned True for
500.00 spent against 500.00: pending correction, because at-limit is not over.
Current condition is budget - spent <= 0; learner should use a strict comparison
such as spent > budget and add an equal-limit demonstration. Do not mark this
behavior complete until verified after their edit. No application tests run.
Concept guide records instance/class/static distinctions, optional class grouping,
Python module functions versus traditional Java utility classes, and boundary rule.

Class-method concept recorded: BudgetConfig.from_dict prepares dictionary data,
converts the limit to Decimal, calls cls(...), and returns the new instance.
Earlier mentor run of exercises/class_methods.py exited 0 with matching budget
representations, equality True, and both object types BudgetConfig. Learner
subsequently confirmed type(budget.limit) produced Decimal; that revised print
was not separately run by the mentor.
During experimentation the learner removed dataclass fields and encountered
constructor errors. Latest notes-only inspection finds the current file missing
both @dataclass and field declarations; it is not restored or verified working.
Before running this exercise again, restore the fields and @dataclass or define
an appropriate initializer. Explained that the factory uses, not replaces,
normal construction. A standalone conversion function remains a valid choice.
Also clarified abstract overrides containing pass count as concrete but perform
no useful work; that distinction is already covered in the concept guide.
No tests or exercise execution performed during this notes-only update.

Inspected exercises/abstract_destinations.py and ran
.venv/bin/python -m exercises.abstract_destinations: exit 0, printed
"MyBudget report". ConsoleDestination implements the inherited abstract write
method and is instantiable. Learner earlier reported the expected TypeError for
the incomplete subclass; that earlier failing version was not run by the mentor.
Explained ABC versus abstractmethod versus pass, instantiation-time enforcement,
and overriding an abstract method with a concrete implementation. Learner
confused this with overloading; reduced explanation to overriding and deferred
overloading alternatives rather than adding more mechanisms. Concept guide
updated. No application tests run for this standalone exercise.

Inspected exercises/report_destinations.py with LabeledConsoleDestination and
ran .venv/bin/python -m exercises.report_destinations: exit 0, printed
"LabeledConsoleDestination: Remaining budget: 424.75". Override delegates to
ConsoleDestination.write via super on the same instance. Current verified script
calls destination.write directly and comments out the original delivery calls;
suggested routing the subclass through deliver_report, but that follow-up has
not been verified. Unused dataclass import has been removed.
Recorded inheritance versus composition, overriding/adding methods, super as
delegation rather than inheritance itself, and instance data versus methods
stored on classes. Base/subclass initializer example was explained only.
No application tests run. Multiple inheritance and typing.Protocol remain future
topics; don't require more repetitive destination exercises before advancing.

Inspected exercises/report_destinations.py and ran
.venv/bin/python -m exercises.report_destinations: exit 0. Console printed
"Remaining budget: 424.75"; independently read polymorphism_report.txt and
confirmed the same text. Both destinations work through deliver_report's
destination.write(report) call without inheritance. Explained interchangeable
implementations, avoiding destination-specific branches, and classes that provide
behavior without instance attributes. Suggested removing unused dataclass import;
that cleanup was confirmed during the later inheritance review. Concept guide
updated by topic. No application tests run for this standalone exercise.
Basic inheritance was subsequently practiced; explicit typing.Protocol remains future.

Inspected exercises/budget_tracker.py with @property total_spent and executed
.venv/bin/python -m exercises.budget_tracker: exit 0; printed 40.00, 55.00,
and 0.00. Getter recalculates after another transaction is added, while the
second tracker's list remains independent. No application tests run.
Recorded property versus stored attribute and method, no automatic caching,
and getter-only assignment behavior (explained, not separately executed).
Learner questioned why property is necessary; clarified it is an optional
interface choice and a normal method is equally valid for this calculation.
Do not treat this choice as a mandatory improvement or assign repetitive total
tests. Setters/deleters and property internals have not been practiced.

Inspected exercises/budget_tracker.py and executed
.venv/bin/python -m exercises.budget_tracker: exit 0, printed False then True.
Both instances use the default factory; only first receives the transaction.
Subsequent inspection confirms the unused second class was removed. Covered
composition, instance methods on dataclasses, fresh empty-list defaults, explicit
arguments bypassing defaults, and shared references rather than copying.
Updated concept guide by topic. No application tests run for this exercise.
Learner asked to skip familiar function/refactoring and exception exercises;
prioritize new concepts instead of requiring repeated practice of known patterns.
Next topic should extend OOP understanding with a new concept, not another
serialization refactor or repetition of basic validation tests.

Inspected exercises/transaction_json.py and ran
.venv/bin/python -m exercises.transaction_json: exit 0. Printed reconstructed
Transaction(category='Groceries', amount=Decimal('40.00'),
transaction_date=datetime.date(2026, 10, 5)) and equality True. Independently read
transaction.json: category Groceries, amount string "40.00", date string
"2026-10-05". Corrected literal dictionary keys, amount source attribute, and
constructor keyword spelling through learner edits. Concept guide updated with
explicit conversion, reconstruction/validation, and value equality versus identity.
No application tests run for this standalone exercise.
Next proposed lesson: extract conversion into reusable functions, then apply
them to a collection of transactions without repeating serialization code.

Inspected exercises/json_basics.py and ran
.venv/bin/python -m exercises.json_basics: exit 0, printed Groceries, 424.75,
and <class 'decimal.Decimal'>. Earlier run also verified budget.json stored
{"category": "Groceries", "remaining": "424.75"}. Final code reconstructs the
Decimal after loading. Explained dump/dumps and load/loads, unsupported Decimal
serialization, and JSON text versus UTF-8 bytes. Concept guide updated by topic.
No application tests run for this standalone exercise.
Transaction round trip subsequently completed; see latest checkpoint above.

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

User requests **one concise interview-style revision guide**: LEARNING_NOTES.md.
Group questions by concept, lead with a direct answer, and keep supporting
explanations/examples short. No chronological lesson narratives or separate quiz
lists. Update existing answers for meaningful clarifications; add questions for
new concepts only. Implementation/verification stays here. This supersedes earlier
chronological-lesson convention. Session history is preserved in
learnings/SESSION_HISTORY.md; daily files are archives. Verification and next tasks
stay in this progress file. Update the latest teaching direction near the top
as the active lesson changes; older proposed next steps below it are historical.

## Session recovery and teaching preferences

Read LEARNING_MASTER_PROMPT.md, LEARNING_NOTES.md, ROADMAP.md, and this checkpoint.
Inspect actual files before assuming prior changes exist. Mentor first: let the
learner implement core code. Skip familiar material on request; pause at unfamiliar
concepts. When confused, use one change and one check at a time. SQL basics and
storage boundaries are now being learned in Milestone 2. Concurrency, GIL, and web
development remain future lessons. Mentioning a topic does not mean it was mastered.
Prefer concept breadth and pace over repeated practice of known mechanics.

## Repository

Branch main; origin: https://github.com/srmandli95/MyBudget.git.
Commit or push only as authorized. Saving learning notes does not itself mean
that they have been committed or uploaded.
