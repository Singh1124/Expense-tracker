# expense_manager.py

import datetime

expenses = []

def add_expense():
    date = input("Enter the date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.date.today().isoformat()
    else:
        try:
            datetime.date.fromisoformat(date)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return

    try:
        amount = float(input("Enter the expense amount: "))
        if amount <= 0:
            print("Amount must be a positive number.")
            return
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return

    category = input("Enter the category (e.g., Food, Transport): ")
    description = input("Enter a description (optional): ")

    expense = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }
    expenses.append(expense)
    print("Expense added successfully!")


def view_expenses():
    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\nAll Expenses:")
    print("Date       | Amount  | Category      | Description")
    print("-" * 50)
    for expense in expenses:
        print(
            f"{expense['date']} | {expense['amount']:>7.2f} | {expense['category']:<12} | {expense['description']}"
        )
    print("-" * 50)


def generate_summary():
    print("\nExpense Summary:")
    total_expenses = sum(e["amount"] for e in expenses)
    print(f"Total Expenses: {total_expenses:.2f}")

    categories = {}
    for e in expenses:
        categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]

    print("\nExpenses by Category:")
    for category, amount in categories.items():
        print(f"{category}: {amount:.2f}")

    if expenses:
        average_expense = total_expenses / len(expenses)
        print(f"\nAverage Expense: {average_expense:.2f}")
    else:
        print("No expenses recorded.")

