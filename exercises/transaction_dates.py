from datetime import date

for i in range(9,11):
    purchase_date = date(2026,i,1)
    print(f"year: {purchase_date.year}, month: {purchase_date.month}, day: {purchase_date.day}")
    if purchase_date.month == 10 and purchase_date.year == 2026:
        print("This date belongs to october 2026")
