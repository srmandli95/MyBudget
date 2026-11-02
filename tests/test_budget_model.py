from decimal import Decimal
from mybudget.models import Budget
import pytest

def test_budget_accepts_valid_configuration(budget_valid_configurations):
    actual = budget_valid_configurations

    assert actual.category == "Groceries"
    assert actual.limit == Decimal("50.00")

def test_budget_rejects_negative_limit():

    with pytest.raises(ValueError):
        actual = Budget("Groceries", Decimal("-1.00"))

@pytest.mark.parametrize("category", ["", " ", "\t"])
def test_budget_rejects_blank_category(category):
    with pytest.raises(ValueError):
        Budget(category, Decimal("100.00"))


def test_budget_limit_zero():
    actual = Budget("Groceries", Decimal("0.00"))

    assert actual.limit == Decimal("0.00")



