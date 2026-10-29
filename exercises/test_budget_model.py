from decimal import Decimal
from mybudget.models import Budget
import pytest

def test_budget_accepts_valid_configuration(budget_valid_configurations):
    actual = budget_valid_configurations

    assert actual.category == "Groceries"

def test_invalid_category():

    with pytest.raises(ValueError):
        actual = Budget("Groceries", Decimal("-1.00"))