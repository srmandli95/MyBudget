# Architecture

No application implementation yet.

First milestone: one local Python program with in-memory fictional transactions.
Budget calculations will be independent of terminal input and output so they can be
tested and later reused behind persistence and an API.

Target direction: a modular monolith. Introduce boundaries as responsibilities appear;
do not generate a framework or elaborate directory structure in advance.
