import sqlite3

# Create a SQLite database to store financial transactions
conn = sqlite3.connect('finance_tracker.db')
cursor = conn.cursor()

# Create a table to store transactions
cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        amount REAL,
        transaction_type TEXT,
        date DATE
    )
''')

# Function to add a transaction
def add_transaction(description, amount, transaction_type, date):
    cursor.execute('''
        INSERT INTO transactions (description, amount, transaction_type, date)
        VALUES (?, ?, ?, ?)
    ''', (description, amount, transaction_type, date))
    conn.commit()
    print("Transaction added successfully!")

# Function to view all transactions
def view_transactions():
    cursor.execute('SELECT * FROM transactions')
    transactions = cursor.fetchall()
    print("\nAll Transactions:")
    for transaction in transactions:
        print(transaction)

# Main menu
while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Transaction")
    print("2. View Transactions")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter transaction description: ")
        amount = float(input("Enter transaction amount: "))
        transaction_type = input("Enter transaction type (Income/Expense): ").capitalize()
        date = input("Enter transaction date (YYYY-MM-DD): ")
        add_transaction(description, amount, transaction_type, date)
    elif choice == '2':
        view_transactions()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
