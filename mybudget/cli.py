import argparse
from mybudget.calculations import calculate_remaining
from decimal import Decimal

def main():
    parser = argparse.ArgumentParser(description="MyBudget calculations")
    parser.add_argument("--budget", required=True)
    parser.add_argument("--spent", required=True)

    args = parser.parse_args()

    return calculate_remaining(Decimal(args.budget), Decimal(args.spent))


if __name__== "__main__":
    print(main())

    


