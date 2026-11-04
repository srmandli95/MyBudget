from decimal import Decimal

def sample_generator():
    

    print("First Decimal amount")
    yield(Decimal("20.00"))

    print("Second Decimal amount")
    yield(Decimal("50.00"))

    print("Third Decimal amount")
    yield(Decimal("30.00"))

cursor = sample_generator()
print("Generator created")
print(next(cursor))
print(next(cursor))

