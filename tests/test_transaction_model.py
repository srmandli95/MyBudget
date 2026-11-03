from decimal import Decimal
from mybudget.models import Transaction
from datetime import date
import pytest

@pytest.mark.parametrize("category", ["", " ", "\t"])
def test_transaction_rejects_blank_category(category):
    with pytest.raises(ValueError):
        Transaction(category, Decimal("100"), date(2025,10,10))

@pytest.mark.parametrize("amount", [100, 100.00, "100.00"])
def test_transaction_rejects_non_decimal_amount(amount):
    with pytest.raises(TypeError):
        Transaction("Groceries", amount, date(2025,10,10))

@pytest.mark.parametrize("value", ["NaN", "Infinity", "-Infinity"])
def test_transaction_rejects_non_finite_amount(value):
    with pytest.raises(ValueError):
        Transaction("Groceries", Decimal(value), date(2025,10,10))