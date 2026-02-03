from loader import load_transactions
from summariser import add_categories


def main():
    df = load_transactions("data/sample_transactions.csv")
    df = add_categories(df)

    print(df)
    print("\nTotals by category (spend only):")
    spend = df[df["amount"] < 0]
    print(spend.groupby("category")["amount"].sum().sort_values())


if __name__ == "__main__":
    main()
