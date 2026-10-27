# Architecture

Current implementation consists of standalone Python exercises with in-memory
fictional transactions; there is no integrated application, database, or API yet.
`exercises/transaction_totals.py` uses a dataclass to hold transaction fields and
a standalone function to calculate category spending. Earlier exercises explore
Decimal calculations and validation. Classes are deliberately repeated across
exercises until shared modules and imports are taught.

First milestone: one local Python program with in-memory fictional transactions.
Budget calculations will be independent of terminal input and output so they can be
tested and later reused behind persistence and an API.

Target direction: a modular monolith. Introduce boundaries as responsibilities appear;
do not generate a framework or elaborate directory structure in advance.
