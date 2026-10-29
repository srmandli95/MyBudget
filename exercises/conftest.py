from decimal import Decimal 
from datetime import date
import pytest 

from mybudget.models import Transaction

@pytest.fixture
def sample_transaction():
    return [
        Transaction("Groceries", Decimal("40.00"), date(2026,10,5)),
        Transaction("Gas", Decimal("20.00"), date(2026,9,1)),
        Transaction("Groceries", Decimal("10.00"), date(2026,2,1))
    ]
@pytest.fixture
def sample_no_groceries():
    return [
        Transaction("party", Decimal("40.00"), date(2026,10,5)),
        Transaction("Gas", Decimal("20.00"), date(2026,9,1)),
        Transaction("party", Decimal("10.00"), date(2026,2,1))
    ]

@pytest.fixture
def calculate_category_budgets():
    return [
        Transaction("Groceries", Decimal("40.00"), date(2026,10,5)),
        Transaction("Groceries", Decimal("20.00"), date(2026,10,1)),
        Transaction("Groceries", Decimal("10.00"), date(2026,10,8)),
        Transaction("Groceries", Decimal("40.00"), date(2026,11,5)),
        Transaction("Gas", Decimal("20.00"), date(2026,10,1)),
        Transaction("Groceries", Decimal("10.00"), date(2025,10,8))
    ]
