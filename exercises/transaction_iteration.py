from decimal import Decimal

amounts = [
    Decimal("40.00"),
    Decimal("20.00"),
    Decimal("10.00"),
]


cursor = iter(amounts)

print(next(cursor))

print("first cursor loop")
for i in cursor:
    print(i)

print("loop over the cursor agian")
for j in cursor:
    print(j)

print("Finally, loop over the original amounts list.")

for amount in amounts:
    print(amount)
