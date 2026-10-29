from decimal import Decimal
from mybudget.models import Transaction
from mybudget.calculations import calculate_category_total

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
