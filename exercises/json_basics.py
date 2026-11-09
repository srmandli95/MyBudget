from mybudget.calculations import calculate_remaining
import json
from decimal import Decimal 

remaining = calculate_remaining(Decimal("500.00"), Decimal("75.25"))

data = {
    "category": "Groceries",
    "remaining": str(remaining)
}

with open("budget.json", "w", encoding="utf-8") as file:
    json.dump(data, file)

with open("budget.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

print(loaded["category"])
amount = Decimal(loaded["remaining"])

print(amount)
print(type(amount))