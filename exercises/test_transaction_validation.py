from decimal import Decimal 

import pytest

from exercises.transaction_dataclass_postinit import Transaction


def test_valid_merchant_check():
    t1 = Transaction("Costco", Decimal("49.99"), "Gas")
    assert t1.merchant == "Costco"

@pytest.mark.parametrize("merchant", ["", " ", "   ", "\t"])
def test_rejects_blank_merchant(merchant):
    with pytest.raises(ValueError):
        Transaction(merchant, Decimal("59.99"), "Gas")
