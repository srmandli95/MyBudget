from decimal import Decimal

class BudgetMath:

    @staticmethod
    def calculate_remaining(budget: Decimal, spent: Decimal) -> Decimal:
        return budget -spent

    @staticmethod
    def is_over_budget(budget: Decimal, spent:Decimal) -> bool:
        if budget - spent <= 0:
            return True
        else:
            return False

    
remaining = BudgetMath.calculate_remaining(
    Decimal("500.00"),
    Decimal("75.25")
)

remaining1 = BudgetMath.is_over_budget(
    Decimal("500.00"),
    Decimal("75.25")
)

remaining2 = BudgetMath.is_over_budget(
    Decimal("500.00"),
    Decimal("550.25")
)
print(remaining1)
print(remaining2)