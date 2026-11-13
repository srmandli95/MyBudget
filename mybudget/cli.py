import argparse
from mybudget.calculations import calculate_remaining
from decimal import Decimal, InvalidOperation
from mybudget.demo_data import demo_data
from mybudget.reports import format_monthly_report

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

    report_parser = commands.add_parser(
        "report",  
        help="Display a monthly report using fictional data",
        )

    report_parser.add_argument("--year", required=True, type=int)
    report_parser.add_argument("--month", required=True, type=int)

    args = parser.parse_args()

    if args.command == "calculate":
        return calculate_remaining(args.budget, args.spent)

    elif args.command == "report":
        budgets, transactions = demo_data()
        return format_monthly_report(
            budgets, transactions, args.year, args.month
        )

if __name__== "__main__":
    print(main())

    


