from decimal import Decimal

def to_cents(amount: Decimal) -> int:
    if not amount.is_finite():
        raise ValueError("amount should be finite")
    
    scaled = amount * 100

    if scaled != scaled.to_integral_value():
        raise ValueError("Amount must represent whole cents")

    return int(scaled)

print(to_cents(Decimal("15.25")))
print(to_cents(Decimal("-2.50")))
print(to_cents(Decimal("15.250")))

print(to_cents(Decimal("nan")))