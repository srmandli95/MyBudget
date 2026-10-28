from decimal import Decimal
from exercises.monthly_budgets import Transaction, calculate_category_total

def test_category_total_sums_only_matching_transactions():
    transctions = [
        Transaction("Groceries", Decimal("40.00")),
        Transaction("Gas", Decimal("20.00")),
        Transaction("Groceries", Decimal("10.00"))
    ]

    actual = calculate_category_total(transctions, "Groceries")

    assert actual == Decimal("50.00")

def test_category_total_returns_zero_for_empty_list():
    actual = calculate_category_total([], "Groceries")

    assert actual == Decimal("0.00")

def test_category_total_returns_when_no_category_match():
    transctions = [
        Transaction("Gas", Decimal("20.00"))
    ]

    actual = calculate_category_total(transctions, "Groceries")
    assert actual == Decimal("0.00")
