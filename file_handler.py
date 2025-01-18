# file_handler.py

def save_expenses(expenses, filename="expenses.txt"):
    """
    Saves all expenses to a file.
    """
    with open(filename, "w") as file:
        for expense in expenses:
            file.write(
                f"{expense['date']},{expense['amount']},{expense['category']},{expense['description']}\n"
            )
    print(f"All expenses have been saved to {filename}.")



def load_expenses(expenses, filename="expenses.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 4:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                date = parts[0]
                amount = float(parts[1])
                category = parts[2]
                description = ",".join(parts[3:])
                expenses.append(
                    {"date": date, "amount": amount, "category": category, "description": description}
                )
        print(f"Expenses loaded from {filename}.")
    except FileNotFoundError:
        print(f"No existing file named {filename}. Starting fresh.")
        



import csv

def export_to_csv(filename="expenses.csv"):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])
        for expense in expenses:
            writer.writerow([expense["date"], expense["amount"], expense["category"], expense["description"]])
    print(f"Expenses exported to {filename}.")
