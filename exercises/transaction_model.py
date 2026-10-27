from decimal import Decimal

class Transaction:

    def __init__(self, merchant: str, amount: Decimal, category: str):
        self.merchant = merchant
        self.amount = amount
        self.category = category


t1 = Transaction("Costco", Decimal("59.89"), "Groceries")
t2 = Transaction("AMB", Decimal("10.99"), "Entertainment")

print("merchant:", t1.merchant,"," , "amount:", t1.amount)

print("merchant:" , t2.merchant,"," ,  "amount:", t2.amount)

print(f"Total sum of tranction {t1.amount + t2.amount}")