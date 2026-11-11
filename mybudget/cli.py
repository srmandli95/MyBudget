import argparse
from mybudget.calculations import calculate_remaining
from decimal import Decimal, InvalidOperation

def parse_amount(text: str) -> Decimal:
    try: 
        return Decimal(text)
    except InvalidOperation:
        raise argparse.ArgumentTypeError(
            "Enter a numeric amount, for example 500.00"
        )

def main():
    parser = argparse.ArgumentParser(description="MyBudget")

    commands = parser.add_subparsers(dest="command", required=True)
    calculate_parser = commands.add_parser(
        "calculate",
        help="Calculate the remaining budget",
    )

    calculate_parser.add_argument("--budget", required=True, type=parse_amount)
    calculate_parser.add_argument("--spent", required=True, type=parse_amount)

    args = parser.parse_args()

    return calculate_remaining(args.budget, args.spent)


if __name__== "__main__":
    print(main())

    


