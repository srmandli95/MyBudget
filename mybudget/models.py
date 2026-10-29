from decimal import Decimal
from dataclasses import dataclass

@dataclass
class Transaction:
    category: str
    amount: Decimal