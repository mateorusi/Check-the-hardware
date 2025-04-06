import sqlite3

# Connect to the database (it will create a new database if it doesn't exist)
conn = sqlite3.connect('customer_management.db')
cursor = conn.cursor()

# Create a table for customers in the database
cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    address TEXT NOT NULL,
                    phone_number TEXT NOT NULL)''')

# Function to add a new customer to the database
def add_customer(name, address, phone_number):
    cursor.execute('INSERT INTO customers (name, address, phone_number) VALUES (?, ?, ?)', 
                   (name, address, phone_number))
    conn.commit()
    print("Customer added successfully!")

# Function to display all customers from the database
def view_customers():
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    if customers:
        for customer in customers:
            print(f"ID: {customer[0]}, Name: {customer[1]}, Address: {customer[2]}, Phone: {customer[3]}")
    else:
        print("No customers found.")

# Function to delete a customer from the database
def delete_customer(customer_id):
    cursor.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    print(f"Customer with ID {customer_id} deleted successfully!")

# Main menu
def menu():
    while True:
        print("\nCustomer Management System")
        print("1. Add Customer")
        print("2. View Customers")
        print("3. Delete Customer")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer name: ")
            address = input("Enter customer address: ")
            phone_number = input("Enter customer phone number: ")
            add_customer(name, address, phone_number)
        elif choice == '2':
            view_customers()
        elif choice == '3':
            customer_id = int(input("Enter the ID of the customer to delete: "))
            delete_customer(customer_id)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Program starts here
if __name__ == "__main__":
    menu()

# Close the connection to the database when the program ends
conn.close()
