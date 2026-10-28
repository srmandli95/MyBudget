from decimal import Decimal

def test_decimal_substraction():

    assert Decimal("10.0") - Decimal("5.0") == Decimal("5.0")
