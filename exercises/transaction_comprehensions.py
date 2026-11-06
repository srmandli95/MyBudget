from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

transactions = [
    
    Transaction("Groceries", Decimal("40.00"), date(2026,10,5)),
        Transaction("Groceries", Decimal("20.00"), date(2026,10,1)),
        Transaction("Groceries", Decimal("10.00"), date(2026,10,8)),
        Transaction("Groceries", Decimal("40.00"), date(2026,11,5)),
        Transaction("Gas", Decimal("20.00"), date(2026,10,1)),
        Transaction("Groceries", Decimal("10.00"), date(2025,10,8)),
        Transaction("Vacation", Decimal("400.00"), date(2026,10,8))

]

grocery_amounts = (
    transaction.amount for transaction in transactions if transaction.category == 'Groceries'
)

print(next(grocery_amounts))
print(next(grocery_amounts))
print(next(grocery_amounts))
print(next(grocery_amounts))
print(next(grocery_amounts))
print(next(grocery_amounts))

