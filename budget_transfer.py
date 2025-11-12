import argparse
from budget_services import get_budgets

def parse_cli(args=None) -> int:
    parser = argparse.ArgumentParser(
        prog="budget-transfer",
        description="Budget transfer utility",
    )
    parser.add_argument(
        "-m",
        "--month",
        type=int,
        choices=range(1, 13),
        metavar="1-12",
        required=True,
        help="Month number (1-12)",
    )
    ns = parser.parse_args(args)
    return ns.month


def main() -> None:
    month = parse_cli()
    print(f"Month selected: {month}")
    get_budgets(month)


if __name__ == "__main__":
    main()

