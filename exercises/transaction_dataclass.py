from dataclasses import dataclass
from decimal import Decimal 
from copy import copy

@dataclass
class Transaction:

    merchant: str
    amount: Decimal
    category: str

t1 = Transaction('Costco', Decimal("59.99"), "groceries")

t2 = Transaction('Costco', Decimal("59.99"), "groceries")

print(t1.merchant, t1.amount, t1.category)
print(repr(t1))

t3 = copy(t1)
t3.category = "miscellaneous"
print("Equal values:", t1==t2)
print("same object:", t1 is t2)
print("shared refrence:", t1 is t3)

print(t1.category)


print(id(t1))
print(id(t2))
print(id(t3))