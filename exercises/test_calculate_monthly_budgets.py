from mybudget.calculations import calculate_monthly_category_total
from datetime import date
from decimal import Decimal
import pytest

def test_monthly_category_total_sums_matching_transactions(calculate_category_budgets):

    actual = calculate_monthly_category_total(calculate_category_budgets, "Groceries", 2026, 10)

    assert actual == Decimal("70.00")

def test_no_montly_transction():

    actual = calculate_monthly_category_total([],"Groceries", 2026, 10)

    assert actual == Decimal("0.00")
    assert isinstance(actual, Decimal)

def test_monthly_total_returns_zero_when_no_dates_match(
    calculate_category_budgets
):
    actual = calculate_monthly_category_total(
        calculate_category_budgets,
        "Groceries",
        2026,
        12,
    )

    assert actual == Decimal("0.00")
    assert isinstance(actual, Decimal)

def test_monthly_total_rejects_invalid_month(calculate_category_budgets):

    with pytest.raises(ValueError):
        calculate_monthly_category_total(
            calculate_category_budgets,
            "Groceries",
            2026,
            13,
        )