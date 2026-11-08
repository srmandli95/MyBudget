from decimal import Decimal

def announce(operation):
    def wrapper(*args, **kwargs):

        print("Starting operation")
        result = operation(*args, **kwargs)
        print("Finished operation")

        return result

    return wrapper

@announce
def calculate(budget, spent):
    return budget - spent

@announce
def describe_category(category):
    return f"Calculate: {category}"

@announce
def empty_call():
    return "Empty function call"

print(calculate(Decimal("500.00"), spent=Decimal("75.00")))
print(describe_category(category="Groceries"))
print(empty_call())