from decimal import Decimal 

import pytest

from exercises.transaction_dataclass_postinit import Transaction

def test_empty_merchant_name_value_error_exception():
    with pytest.raises(ValueError):
        Transaction("", Decimal("20.50"), "Food")

def test_white_space_merchant_value_error():
    with pytest.raises(ValueError):
        Transaction(" ", Decimal("49.59"), "Gas")

def test_valid_merchant_check():
    t1 = Transaction("Costco", Decimal("49.99"), "Gas")
    assert t1.merchant == "Costco"