from dataclasses import dataclass
from decimal import Decimal 

@dataclass
class Transaction:

    merchant: str
    amount: Decimal
    category: str

    def __post_init__(self) -> None:
        if not self.merchant.strip():
            raise ValueError("marchant should not be blank")

if __name__ == "__main__":
    t1 = Transaction(" ", Decimal("29.49"), "food")
