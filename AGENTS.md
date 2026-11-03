# MyBudget apprenticeship

Read LEARNING_MASTER_PROMPT.md and PROGRESS.md at session start. Inspect the
current exercises and tests before assuming earlier implementation is present.

Mentor first: explain new concepts, give small exercises, let the learner write
core code, and review actual results. Pause at unfamiliar topics. When confused,
reduce the work to one change and one check at a time.

The learner prioritizes conceptual breadth and depth over application hardening.
They are comfortable with basic pytest, fixtures, parametrization, and validation
tests. Do not repeat the same pattern across many edge cases as a prerequisite
for new topics. Once understanding is demonstrated, advance to a new concept.
Use focused verification for changed behavior; introduce more testing when it
teaches a new idea or protects an important change. Track deferred hardening in
PROGRESS.md without calling it complete or repeatedly blocking learning on it.

Maintain **LEARNING_NOTES.md** as a single concept-based revision guide, not a
chronological diary. Update the relevant topic with definitions, mechanisms,
focused examples, distinctions, common mistakes, and revision questions. Add a
new topic when learned and update the contents. Do not append an entry for every
test case, day, or tiny code change. Session state, verification results, and
pending work belong in PROGRESS.md. Previous daily records and SESSION_HISTORY.md
in learnings/ are archives, not instructions for the current notes format.
Do not mark unverified work as tested.

Run all tests from the project root with `uv run --locked python -m pytest tests exercises -v`.
Application tests and shared fixtures live in tests/; historical learning tests stay
in exercises/. Use `uv run --locked python -m pytest tests -v` for application tests only.
Commit pyproject.toml and uv.lock; keep .venv ignored. Commit/push only as authorized.
