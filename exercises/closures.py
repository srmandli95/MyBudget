from mybudget.models import Transaction
from decimal import Decimal
from datetime import date

t1 = Transaction("Groceries", Decimal("10.00"), date(2026, 10, 5))
t2 = Transaction("Gas", Decimal("10.00"), date(2026, 10, 5))

def make_category_checker(category):
    def category_checker(transaction):
        return category == transaction.category
    
    return category_checker

category_checker = make_category_checker("Groceries")

print(category_checker(t1))
print(category_checker(t2))