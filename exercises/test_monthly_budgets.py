from decimal import Decimal
from mybudget.models import Transaction
from mybudget.calculations import calculate_category_total
from mybudget.calculations import calculate_remaining


def test_remaining_budget_when_under_limit():
    actual = calculate_remaining(
        Decimal("500.00"),
        Decimal("425.00")
    )

    assert actual == Decimal("75.00")

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
