from mybudget.models import Transaction
from decimal import Decimal 
from datetime import date
import json


transaction = Transaction(
    category="Groceries",
    amount=Decimal("40.00"),
    transaction_date=date(2026, 10, 5),
)

transaction_dict = {}

transaction_dict["category"] = transaction.category
transaction_dict["amount"] = str(transaction.amount)
transaction_dict["transaction_date"] = transaction.transaction_date.isoformat()

with open("transaction.json", "w", encoding="utf-8") as file:
    json.dump(transaction_dict, file)

with open("transaction.json", "r", encoding="utf-8") as file:
    loaded = json.load(file)

restored = Transaction(
    category = loaded["category"],
    amount = Decimal(loaded["amount"]),
    transaction_date=date.fromisoformat(loaded["transaction_date"]),
)

print(restored)
print(restored == transaction)