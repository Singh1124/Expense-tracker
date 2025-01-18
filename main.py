# main.py

from expense_manager import add_expense, view_expenses, generate_summary, expenses
from file_handler import save_expenses, load_expenses
from colorama import Fore, init

init(autoreset=True)

def main_menu():
    while True:
        print(Fore.CYAN + "\n=== Personal Expense Tracker ===")
        print(Fore.YELLOW + "1. Add Expense")
        print(Fore.YELLOW + "2. View Expenses")
        print(Fore.YELLOW + "3. Save Expenses")
        print(Fore.YELLOW + "4. Load Expenses")
        print(Fore.YELLOW + "5. Generate Summary")
        print(Fore.RED + "6. Exit")
        choice = input(Fore.GREEN + "Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            save_expenses(expenses)
        elif choice == "4":
            load_expenses(expenses)
        elif choice == "5":
            generate_summary()
        elif choice == "6":
            print(Fore.RED + "Goodbye!")
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
