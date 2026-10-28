from decimal import Decimal
from exercises.monthly_budgets import Transaction, calculate_category_total
import pytest

@pytest.fixture
def sample_transaction():
    return [
        Transaction("Groceries", Decimal("40.00")),
        Transaction("Gas", Decimal("20.00")),
        Transaction("Groceries", Decimal("10.00"))
    ]

def test_category_total_sums_only_matching_transactions(sample_transaction):
    

    actual = calculate_category_total(sample_transaction, "Groceries")
    assert actual == Decimal("50.00")

def test_calculate_total_gas(sample_transaction):

    actual = calculate_category_total(sample_transaction, "Gas")
    
    assert actual == Decimal("20.00")


def test_category_total_returns_zero_for_empty_list():
    actual = calculate_category_total([], "Groceries")

    assert actual == Decimal("0.00")

def test_category_total_returns_when_no_category_match():
    transctions = [
        Transaction("Gas", Decimal("20.00"))
    ]

    actual = calculate_category_total(transctions, "Groceries")
    assert actual == Decimal("0.00")
