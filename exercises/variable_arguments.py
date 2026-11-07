from decimal import Decimal

def total_expenses(*amounts):
    print(amounts)
    type(amounts)
    #return sum(amounts, Decimal("0.00"))

values = [Decimal("10.00"), Decimal("20.00"), Decimal("5.00")]

total_expenses(values)


def show(*args):       # Collect positional arguments into a tuple.
    print(args)

values = [10, 20, 30]
show(*values)         # Unpack the list into separate arguments.