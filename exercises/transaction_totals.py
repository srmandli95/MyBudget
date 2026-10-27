from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Transaction:
    merchant: str
    amount: Decimal
    category: str



def calculate_category_total(transaction: list[Transaction], category: str) -> Decimal:

    total = Decimal("0.00")

    for trans in transaction:
        if trans.category == category:
            total += trans.amount
    
    return total

transactions = [
    Transaction("Costco", Decimal("59.49"), "Food"),
    Transaction("BJs", Decimal("59.49"), "Gas"),
    Transaction("Target", Decimal("59.49"), "Food")
    
]

print(calculate_category_total(transactions, "Subscriptions"))
print(calculate_category_total([], "Food"))