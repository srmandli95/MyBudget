from mybudget.calculations import calculate_monthly_category_total
from datetime import date
from decimal import Decimal

def test_monthly_category_total_sums_matching_transactions(calculate_category_budgets):

    actual = calculate_monthly_category_total(calculate_category_budgets, "Groceries", 2026, 10)

    assert actual == Decimal("70.00")

def test_no_montly_transction():

    actual = calculate_monthly_category_total([],"Groceries", 2026, 10)

    assert actual == Decimal("0.00")
    assert isinstance(actual, Decimal)
