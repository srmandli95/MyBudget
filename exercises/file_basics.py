from mybudget.calculations import calculate_remaining
from decimal import Decimal

with open("budget_note.txt", "w", encoding="utf-8") as file:
    file.write(f"Remaining budget: {calculate_remaining(Decimal("500.00"), Decimal("75.25"))}\n")

with open("budget_note.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)