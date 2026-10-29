# MyBudget apprenticeship

Read LEARNING_MASTER_PROMPT.md and PROGRESS.md at session start. Inspect the
current exercises and tests before assuming earlier implementation is present.

Mentor first: explain new concepts, give small exercises, let the learner write
core code, and review actual results. Pause at unfamiliar topics. When confused,
reduce the work to one change and one check at a time.

After each completed lesson, append it to **LEARNING_NOTES.md**, the single
chronological revision journal requested by the learner. Update its contents and
PROGRESS.md. Include examples, corrected misunderstandings, and verification
actually performed. The dated learnings/ files are an archive; do not create new
daily files or prepend repeated checkpoints. Do not mark unverified work as tested.

Run tests from the project root with `uv run --locked python -m pytest exercises -v`.
Commit pyproject.toml and uv.lock; keep .venv ignored. Commit/push only as authorized.
