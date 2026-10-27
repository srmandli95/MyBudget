from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Transaction:
    merchant: str
    amount: Decimal
    category: str



def calculate_total(transaction: list[Transaction]) -> Decimal:

    total = Decimal("0.00")

    for trans in transaction:
        total += trans.amount
    
    return total

trancsaction = [
    Transaction("Costco", Decimal("59.49"), "Food"),
    Transaction("BJs", Decimal("59.49"), "Food"),
    Transaction("Target", Decimal("59.49"), "Food")
    
]

print(calculate_total(trancsaction))