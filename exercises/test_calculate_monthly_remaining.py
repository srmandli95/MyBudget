from decimal import Decimal
from mybudget.calculations import calculate_monthly_remaining
import pytest
from mybudget.models import Budget

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

def test_monthly_remaining_returns_empty_when_no_budgets(
    calculate_category_budgets,
):
    actual = calculate_monthly_remaining([], calculate_category_budgets, 2026, 10)

    assert actual == {}


@pytest.mark.parametrize("month", [0, 13])
def test_invalid_month(month):
    with pytest.raises(ValueError):
        calculate_monthly_remaining([], [], 2026, month)

def test_monthly_remaining_rejects_duplicates_budget_categories():
    with pytest.raises(ValueError):
        budgets = [

        Budget("Groceries", Decimal("500.00")),
        Budget("Groceries", Decimal("300.00"))

        ]

        calculate_monthly_remaining(budgets, [], 2026, 10)

