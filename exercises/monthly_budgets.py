from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Transaction:
    category: str
    amount: Decimal

budgets = {
    "Groceries": Decimal("500.00"),
    "Restaurants": Decimal("200.00"),
    "Gas": Decimal("250.00"),
    "miscellaneous": Decimal("150.00"),
}
print("Total budget:", sum(budgets.values(), Decimal("0.00")))

budget_limit = dict()

t1 = Transaction("Groceries", Decimal("400.00"))
t2 = Transaction("Restaurants", Decimal("100.00"))
t3 = Transaction("Gas", Decimal("200.00"))   
t4 = Transaction("Groceries", Decimal("125.00"))

transactions = [t1, t2, t3, t4]

def calculate_category_total(transactions: list[Transaction], category: str) -> Decimal:
    total = Decimal("0.0")
    for transaction in transactions:
        if transaction.category == category:
            total += transaction.amount
    return total

for category, limit in budgets.items():
    spend = calculate_category_total(transactions,category)
    budget_limit[category] = limit - spend

for category, limit in budgets.items():
    print(f"category: {category}, limit: {limit}, remaining: {budget_limit[category]}")


assert calculate_category_total(transactions, "Groceries") == Decimal("525.00")
assert calculate_category_total([], "Groceries") == Decimal("0.00")
print("Both checks passed")