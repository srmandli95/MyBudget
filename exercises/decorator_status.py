from decimal import Decimal 
from mybudget.calculations import calculate_remaining

def report_status(calculate):
    def wrapper(budget, spent):
        balance = calculate(budget,spent)
        if balance >= 0:
            print("within budget")
        else:
            print("over budget")
        return balance
    return wrapper

@report_status
def calculate(budget, spent):

    return calculate_remaining(budget, spent)
    

print(calculate(Decimal("500.00"), Decimal("75.00")))
print(calculate(Decimal("500.00"), Decimal("525.00")))


