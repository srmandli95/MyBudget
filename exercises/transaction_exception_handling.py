from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Transaction:

    merchant: str
    amount: Decimal
    category: str

    def __post_init__(self):
        if not self.merchant.strip():
            raise ValueError("Merchant cannot be empty")
      
        if not self.category.strip():
            raise ValueError("category cannot be empty")


try:
    t1 = Transaction("Costco", Decimal("49.99"), "Food")
except ValueError as error:
    print("Could not create a transcation, due to invalid value:", error)

print("Continues")