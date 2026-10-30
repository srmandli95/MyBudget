from decimal import Decimal
from mybudget.calculations import calculate_monthly_remaining

def test_calculate_remining_budgets_2026_oct(calculate_category_budgets, sample_budget):

    actual = calculate_monthly_remaining(sample_budget, calculate_category_budgets, 2026, 10)

    assert actual["Groceries"] == Decimal("430.00")
    assert actual["Gas"] == Decimal("230.00")
    assert actual["Vacation"] == Decimal("200.00")


def test_calculate_remining_budgets_2027_oct(calculate_category_budgets, sample_budget):

    actual = calculate_monthly_remaining(sample_budget, calculate_category_budgets, 2027, 10)

    assert actual["Groceries"] == Decimal("500.00")
    assert actual["Gas"] == Decimal("250.00")
    assert actual["Vacation"] == Decimal("600.00")
