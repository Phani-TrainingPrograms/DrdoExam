import pymysql


# Database connection
def connect_db():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='cdacacts',
        database='laptop'
    )


# Create a new laptop entry
def create_laptop():
    serial = input("Enter serial number: ")
    model = input("Enter model: ")
    brand = input("Enter brand: ")
    price = float(input("Enter price: "))

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO laptop_info (serial, model, brand, price) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (serial, model, brand, price))
        connection.commit()
        print("Laptop added successfully!")
    finally:
        connection.close()


# Read all laptops
def read_laptops():
    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM laptop_info"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                print(row)
    finally:
        connection.close()


# Update a laptop entry
def update_laptop():
    laptop_id = int(input("Enter the ID of the laptop to update: "))
    serial = input("Enter new serial number: ")
    model = input("Enter new model: ")
    brand = input("Enter new brand: ")
    price = float(input("Enter new price: "))

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE laptop_info SET serial=%s, model=%s, brand=%s, price=%s WHERE id=%s"
            cursor.execute(sql, (serial, model, brand, price, laptop_id))
        connection.commit()
        print("Laptop updated successfully!")
    finally:
        connection.close()


# Delete a laptop entry
def delete_laptop():
    laptop_id = int(input("Enter the ID of the laptop to delete: "))

    connection = connect_db()
    try:
        with connection.cursor() as cursor:
            sql = "DELETE FROM laptop_info WHERE id=%s"
            cursor.execute(sql, (laptop_id,))
        connection.commit()
        print("Laptop deleted successfully!")
    finally:
        connection.close()


# Menu-driven program
def menu():
    while True:
        print("\n--- Laptop Information Management ---")
        print("1. Add Laptop")
        print("2. View Laptops")
        print("3. Update Laptop")
        print("4. Delete Laptop")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_laptop()
        elif choice == '2':
            read_laptops()
        elif choice == '3':
            update_laptop()
        elif choice == '4':
            delete_laptop()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()
