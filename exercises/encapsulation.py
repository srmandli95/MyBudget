from decimal import Decimal

class BudgetTracker:
    def __init__(self):
        self._transactions = []
        self.__label = "MyBudget"

    def add_transaction(self, transaction):
        self._transactions.append(transaction)

    @property
    def transaction_count(self):
        return len(self._transactions)


transaction = [Decimal("30.00"), Decimal("40.00")]

tracker = BudgetTracker()
tracker.add_transaction(transaction)

print(tracker._transactions)
print(tracker._BudgetTracker__label)
print(tracker.transaction_count)
