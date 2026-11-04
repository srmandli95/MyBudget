from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

def generate_transactions(count):

    for i in range(count):
        yield Transaction("Groceries", Decimal("10.00"), date(2026, 10, 5))

cursor = generate_transactions(3)

amount = Decimal("0.00")
for transaction in cursor:
    print(transaction)
    amount+= transaction.amount 

print(amount)


