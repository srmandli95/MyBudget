from decimal import Decimal
from dataclasses import dataclass
from datetime import date

@dataclass
class Transaction:
    category: str
    amount: Decimal
    transaction_date: date