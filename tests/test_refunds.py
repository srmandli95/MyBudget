from decimal import Decimal
from mybudget.calculations import calculate_monthly_remaining


def test_refund_reduces_monthly_spending(refund_sample_transaction, sample_budget):
    actual = calculate_monthly_remaining(sample_budget, refund_sample_transaction, 2026, 10)

    assert actual["Groceries"] == Decimal("425.00")

def test_refund_different_month(refund_sample_transaction_differnt_month, sample_budget):
    actual = calculate_monthly_remaining(sample_budget, refund_sample_transaction_differnt_month, 2026, 11)

    assert actual["Groceries"] == Decimal("525.00")