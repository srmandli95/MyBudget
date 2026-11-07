from decimal import Decimal
def show_budget(**details):
    for key, value in details.items():
        print(key, value)

details = {
    "category": "Groceries",
    "limit": Decimal("500.00"),
}

show_budget(**details)