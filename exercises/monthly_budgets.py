from decimal import Decimal
from mybudget.models import Transaction, Budget
from mybudget.calculations import calculate_category_total, calculate_remaining, calculate_monthly_category_total
from datetime import date

if __name__ == "__main__":

    report_year = 2026
    report_month = 12

    print(f"Budget report: {report_year}-{report_month:02d}")

    budgets = [
        Budget("Groceries", Decimal("500.00")),
        Budget("Restaurants", Decimal("200.00")),
        Budget("Gas", Decimal("250.00")),
        Budget("miscellaneous", Decimal("150.00")),
    ]
    total_budget = Decimal("0.00")
    for budget in budgets:
        total_budget += budget.limit

    print("Total budget:", total_budget)

    budget_limit = dict()

    t1 = Transaction("Groceries", Decimal("400.00"), date(2026, 10, 5))
    t2 = Transaction("Restaurants", Decimal("100.00"), date(2026, 10, 5))
    t3 = Transaction("Gas", Decimal("200.00"), date(2026, 10, 5))   
    t4 = Transaction("Groceries", Decimal("125.00"), date(2026, 10, 5))

    transactions = [t1, t2, t3, t4]



    for budget in budgets:
        spend = calculate_monthly_category_total(transactions, budget.category, report_year, report_month)
        budget_limit[budget.category] = calculate_remaining(budget.limit, spend)

    for budget in budgets:
        print(f"category: {budget.category}, limit: {budget.limit}, remaining: {budget_limit[budget.category]}")


    assert calculate_category_total(transactions, "Groceries") == Decimal("525.00")
    assert calculate_category_total([], "Groceries") == Decimal("0.00")
    print("Both checks passed")