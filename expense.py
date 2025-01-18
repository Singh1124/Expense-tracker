#Importing the module for handling dates 
import datetime 

#Assiginging the global variable 
expenses = [] #list to store all expense entires as dictionaries

#Functions

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
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!")




def view_expenses():
    """Function to view all expenses. 
    """
    if not expenses:
        print("No expenses recorded yet.")
        return
    print("\n All Expenses:")
    print("Date      | Amount    |  Category       |  Description ")
    print("-"*50)
    for expense in expenses:
        print(f"{expense["date"]} | {expense['amount']:>7.2f}  | {expense['category']:<12} | {expense ['description']}")
        print("-"* 50)

def save_expenses(filename="expenses.txt"):
    """
    saves all expenses to a file

    Args:
        filename (str, optional): _description_. Defaults to "expenses.txt".
    """
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(f"{expense['date']}, {expense['amount']}, {expense['category']}, {expense['description']}\n")
    print(f"All expenses have been saved to {filename}.")


def view_expenses_by_filter():
    print("\nFilter Options:")
    print("1. View all expenses")
    print("2. Filter by date range")
    print("3. Filter by category")
    choice = input("Enter your choice: ")

    filtered_expenses = expenses  # Start with all expenses

    if choice == "2":
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        try:
            start_date = datetime.date.fromisoformat(start_date)
            end_date = datetime.date.fromisoformat(end_date)
            filtered_expenses = [
                e for e in expenses if start_date <= datetime.date.fromisoformat(e["date"]) <= end_date
            ]
        except ValueError:
            print("Invalid date(s). Showing all expenses.")
    elif choice == "3":
        category = input("Enter category to filter by: ")
        filtered_expenses = [e for e in expenses if e["category"].lower() == category.lower()]

    print("\nFiltered Expenses:")
    print("Date       | Amount  | Category      | Description")
    print("-" * 50)
    for expense in filtered_expenses:
        print(f"{expense['date']} | {expense['amount']:>7.2f} | {expense['category']:<12} | {expense['description']}")
    print("-" * 50)


def load_expenses(filename="expenses.txt"):
    """
    Loads expenses from a file into the program.
    Handles unexpected formatting in the file gracefully.
    """
    try:
        with open(filename, "r") as file:
            for line in file:
                # Split the line into parts
                parts = line.strip().split(",")
                
                # Ensure we have at least 4 parts
                if len(parts) < 4:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                
                # Reconstruct the fields
                date = parts[0]
                amount = float(parts[1])
                category = parts[2]
                description = ",".join(parts[3:])  # Handle extra commas in the description
                
                # Add the expense to the list
                expense = {
                    "date": date,
                    "amount": amount,
                    "category": category,
                    "description": description
                }
                expenses.append(expense)
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing file named {filename}. Starting fresh.")
    except ValueError as e:
        print(f"Error reading file: {e}. Please check the file format.")

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

import csv

def export_to_csv(filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])
        for expense in expenses:
            writer.writerow([expense["date"], expense["amount"], expense["category"], expense["description"]])
    print(f"Expenses exported to {filename}.")
 

from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def main_menu():
    """
    Function to display the main menu and handle user choices.
    """
    while True:
        print(Fore.CYAN + "\n=== Personal Expense Tracker ===")
        print(Fore.YELLOW + "1. Add Expense")
        print(Fore.YELLOW + "2. View Expenses")
        print(Fore.YELLOW + "3. Save Expenses")
        print(Fore.YELLOW + "4. Load Expenses")
        print(Fore.YELLOW + "5. Generate Summary")
        print(Fore.YELLOW + "6. Export to CSV")
        print(Fore.RED + "7. Exit")
        print(Fore.CYAN + "=" * 30)

        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses()
        elif choice == "4":
            load_expenses()
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            export_to_csv()
        elif choice == "7":
            print(Fore.RED + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

# Main program Logic 
if __name__ == "__main__":
    print("Welcome to the Personal Expense Tracker !")
    main_menu()

   