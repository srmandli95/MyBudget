from decimal import Decimal
from mybudget.models import Transaction
from datetime import date
import pytest

@pytest.mark.parametrize("category", ["", " ", "\t"])
def test_transaction_rejects_blank_category(category):
    with pytest.raises(ValueError):
        Transaction(category, Decimal("100"), date(2025,10,10))