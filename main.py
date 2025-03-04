#PERSONAL EXPENSE TRACKER

import csv
from datetime import datetime

# Log an expense
def log_expense(amount, category, date=None):
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')  # Use today's date if none provided
    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])
    print(f"Logged: ${amount} for {category} on {date}")


def summarize_by_category():
    category_totals = {}
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, amount, category = row
                amount = float(amount)
                if category in category_totals:
                    category_totals[category] += amount
                else:
                    category_totals[category] = amount
    except FileNotFoundError:
        print("No expenses recorded yet.")

    print("Spending by Category:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")


def monthly_summary():
    monthly_totals = {}
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                date, amount, category = row
                month = date[:7]  # Extract 'YYYY-MM' format
                amount = float(amount)
                if month in monthly_totals:
                    monthly_totals[month] += amount
                else:
                    monthly_totals[month] = amount
    except FileNotFoundError:
        print("No expenses recorded yet.")

    print("Monthly Spending Summary:")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")


import shutil

def export_expenses():
    export_filename = f"exported_expenses_{datetime.today().strftime('%Y%m%d')}.csv"
    try:
        shutil.copy('expenses.csv', export_filename)
        print(f"Expenses exported to {export_filename}")
    except FileNotFoundError:
        print("No expenses to export.")



def menu():
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Log Expense")
        print("2. View Summary by Category")
        print("3. View Monthly Summary")
        print("4. Export Expenses")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            amount = input("Enter amount: ")
            category = input("Enter category: ")
            date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
            log_expense(amount, category, date)
        elif choice == '2':
            summarize_by_category()
        elif choice == '3':
            monthly_summary()
        elif choice == '4':
            export_expenses()
        elif choice == '5':
            print("Goodbye!!!")
            break
        else:
            print("Invalid choice. Please try again.")

menu()
