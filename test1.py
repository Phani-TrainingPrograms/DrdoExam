import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='cdacacts',
        database='laptop_db'
    )


def add_laptop(cursor):
    sl_no = input("Enter Serial Number: ")
    model = input("Enter Model: ")
    brand = input("Enter Brand: ")
    price = float(input("Enter Price: "))
    cursor.execute("INSERT INTO laptop_information (SlNo, Model, Brand, Price) VALUES (%s, %s, %s, %s)",
                   (sl_no, model, brand, price))
    print("Laptop information added successfully.")


def display_laptops(cursor):
    cursor.execute("SELECT * FROM laptop_information")
    records = cursor.fetchall()
    if records:
        for record in records:
            id, sl_no, model, brand, price = record
            print(f"ID: {id}, Serial No: {sl_no}, Model: {model}, Brand: {brand}, Price: ₹{price:.2f}")
    else:
        print("No laptop information found.")


def update_laptop(cursor):
    laptop_id = int(input("Enter the ID of the laptop to update: "))
    cursor.execute("SELECT * FROM laptop_information WHERE Id = %s", (laptop_id,))
    if cursor.fetchone() is None:
        print(f"No laptop found with ID {laptop_id}.")
        return

    sl_no = input("Enter new Serial Number: ")
    model = input("Enter new Model: ")
    brand = input("Enter new Brand: ")
    price = float(input("Enter new Price: "))

    cursor.execute("UPDATE laptop_information SET SlNo = %s, Model = %s, Brand = %s, Price = %s WHERE Id = %s",
                   (sl_no, model, brand, price, laptop_id))
    print("Laptop information updated successfully.")


def delete_laptop(cursor):
    laptop_id = int(input("Enter the ID of the laptop to delete: "))
    cursor.execute("DELETE FROM laptop_information WHERE Id = %s", (laptop_id,))
    print("Laptop information deleted successfully.")


def main_menu():
    db_connection = connect_to_database()
    db_cursor = db_connection.cursor()

    while True:
        print("\nOptions Menu:")
        print("1. Add Laptop Information")
        print("2. View All Laptop Information")
        print("3. Update Laptop Information")
        print("4. Delete Laptop Information")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            add_laptop(db_cursor)
        elif choice == '2':
            display_laptops(db_cursor)
        elif choice == '3':
            update_laptop(db_cursor)
        elif choice == '4':
            delete_laptop(db_cursor)
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

        db_connection.commit()

    db_cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main_menu()
