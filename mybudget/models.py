from decimal import Decimal
from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    category: str
    amount: Decimal
    transaction_date: date

    def __post_init__(self):
        if not self.category.strip():
            raise ValueError("category cannot be empty") 
        if not isinstance(self.amount, Decimal):
            raise TypeError("amount must be a Decimal integer")
        if not self.amount.is_finite():
            raise ValueError("amount must be a decimal")


@dataclass
class Budget:
    category: str
    limit: Decimal

    def __post_init__(self):
        if not self.category.strip():
            raise ValueError("Category cannot be empty")
        if self.limit < Decimal("0.00"):
            raise ValueError("Budget limits cannot be less than 0")


