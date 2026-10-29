from decimal import Decimal
from mybudget.models import Transaction
from mybudget.calculations import calculate_category_total, calculate_remaining
from datetime import date
if __name__ == "__main__":

    budgets = {
        "Groceries": Decimal("500.00"),
        "Restaurants": Decimal("200.00"),
        "Gas": Decimal("250.00"),
        "miscellaneous": Decimal("150.00"),
    }
    print("Total budget:", sum(budgets.values(), Decimal("0.00")))

    budget_limit = dict()

    t1 = Transaction("Groceries", Decimal("400.00"), date(2026, 10, 5))
    t2 = Transaction("Restaurants", Decimal("100.00"), date(2026, 10, 5))
    t3 = Transaction("Gas", Decimal("200.00"), date(2026, 10, 5))   
    t4 = Transaction("Groceries", Decimal("125.00"), date(2026, 10, 5))

    transactions = [t1, t2, t3, t4]



    for category, limit in budgets.items():
        spend = calculate_category_total(transactions,category)
        budget_limit[category] = calculate_remaining(limit, spend)

    for category, limit in budgets.items():
        print(f"category: {category}, limit: {limit}, remaining: {budget_limit[category]}")


    assert calculate_category_total(transactions, "Groceries") == Decimal("525.00")
    assert calculate_category_total([], "Groceries") == Decimal("0.00")
    print("Both checks passed")