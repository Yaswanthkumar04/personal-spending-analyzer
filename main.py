import json
from tracker import add_expense, load_expenses
from analyzer import get_weekly_totals, compare_weeks
from chart import draw_chart

def main():
    print("\n=== Personal Spending Analyzer ===")
    while True:
        print("\n1. Add Expense")
        print("2. View This Week")
        print("3. Compare Weeks")
        print("4. Exit")
        choice = input("\nChoose: ")
        if choice == "1":
            amount = float(input("Amount: "))
            category = input("Category (Food/Transport/Fun/Other): ")
            note = input("Note: ")
            add_expense(amount, category, note)
            print("Saved!")
        elif choice == "2":
            data = load_expenses()
            totals = get_weekly_totals(data, 0)
            draw_chart(totals)
        elif choice == "3":
            data = load_expenses()
            compare_weeks(data)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()