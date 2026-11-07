from decimal import Decimal

def total_expenses(*amounts):
    print(amounts)

    return sum(amounts, Decimal("0.00"))

print(total_expenses(Decimal("10.00"), Decimal("20.00")))
print(total_expenses(Decimal("10.00"), Decimal("20.00"), Decimal("5.00")))
print(total_expenses())
