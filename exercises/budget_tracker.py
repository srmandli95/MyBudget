from mybudget.models import Transaction
from decimal import Decimal
from datetime import date
from dataclasses import dataclass, field


@dataclass
class BudgetTracker1:
    transactions: list[Transaction] = field(default_factory=list)

    def add_transaction(self, transaction:Transaction) -> None:
        self.transactions.append(transaction)

    @property
    def total_spent(self) -> Decimal:
        return sum(
            (transaction.amount for transaction in self.transactions),
            Decimal("0.00"),
        )


first = BudgetTracker1()
second = BudgetTracker1()





transaction = Transaction(
    category="Groceries",
    amount=Decimal("40.00"),
    transaction_date=date(2026, 10, 5), 
)

first.add_transaction(transaction)
print(first.total_spent)  

first.add_transaction(
    Transaction("Gas", Decimal("15.00"), date(2026, 10, 5))
)


print(first.total_spent)
print(second.total_spent)
