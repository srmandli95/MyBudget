from decimal import Decimal 

import pytest 

from mybudget.models import Transaction

@pytest.fixture
def sample_transaction():
    return [
        Transaction("Groceries", Decimal("40.00")),
        Transaction("Gas", Decimal("20.00")),
        Transaction("Groceries", Decimal("10.00"))
    ]