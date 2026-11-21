import argparse
import sqlite3
from mybudget.calculations import calculate_remaining
from decimal import Decimal, InvalidOperation
from mybudget.demo_data import demo_data
from mybudget.reports import format_monthly_report
from datetime import date
from mybudget.models import Transaction
from mybudget.storage import initialize_database, save_transaction, load_transactions


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

    add_parsers = commands.add_parser(
        "add",
        help="Adds amounts"
    )

    add_parsers.add_argument("--category", required=True, type=str)
    add_parsers.add_argument("--amount", required=True, type=parse_amount)
    add_parsers.add_argument("--date", required=True, type=date.fromisoformat)

    args = parser.parse_args()

    if args.command == "calculate":
        return calculate_remaining(args.budget, args.spent)

    elif args.command == "report":
        budgets, transactions = demo_data()
        return format_monthly_report(
            budgets, transactions, args.year, args.month
        )

    elif args.command == "add":
        transaction = Transaction(args.category, args.amount, args.date)
        connector = sqlite3.connect("mybudget.db")
        try:
            _ = initialize_database(connector)
            _ = save_transaction(connector, transaction)
            connector.commit()
            return "Transaction saved"
        except sqlite3.Error as error:
            connector.rollback()
            raise
        
        finally:
            connector.close()


if __name__== "__main__":
    print(main())

    


