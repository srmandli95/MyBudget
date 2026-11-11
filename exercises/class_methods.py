from dataclasses import dataclass
from decimal import Decimal

@dataclass
class BudgetConfig:
    category: str
    limit: Decimal

    @classmethod
    def from_dict(cls, data):
        return cls(
            category=data["category"],
            limit=Decimal(data["limit"]),
        )
    
budget = BudgetConfig.from_dict({
    "category": "Groceries",
    "limit": "500.00",
})

budget_constructor = BudgetConfig("Groceries", Decimal("500.00"))

print(budget)
print(budget_constructor)

print(budget == budget_constructor)

print(type(budget.limit))

print(type(budget))
print(type(budget_constructor))