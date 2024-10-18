import mysql.connector
from mysql.connector import Error

# Database configuration
config = {
    'user': 'root',  # Replace with your MySQL username
    'password': 'cdacacts',  # Replace with your MySQL password
    'host': 'localhost',  # Hostname (usually localhost)
    'database': 'LaptopInformation'  # Name of the database you created
}


# Step 1: Create the database and table
def create_database():
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS LaptopInformation (
            Id INT AUTO_INCREMENT PRIMARY KEY,
            SlNo INT NOT NULL,
            Model VARCHAR(255) NOT NULL,
            Brand VARCHAR(255) NOT NULL,
            Price DECIMAL(10, 2) NOT NULL
        )
        ''')

        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Step 2: Insert data into the table
def insert_laptop(sl_no, model, brand, price):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute('''
        INSERT INTO LaptopInformation (SlNo, Model, Brand, Price) VALUES (%s, %s, %s, %s)
        ''', (sl_no, model, brand, price))

        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Step 3: Fetch and display all laptop information
def fetch_laptop_info():
    laptops = []
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute('SELECT * FROM LaptopInformation')
        laptops = cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    return laptops


# Step 4: Update laptop information
def update_laptop(id, sl_no, model, brand, price):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute('''
        UPDATE LaptopInformation
        SET SlNo = %s, Model = %s, Brand = %s, Price = %s
        WHERE Id = %s
        ''', (sl_no, model, brand, price, id))

        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Step 5: Delete laptop information
def delete_laptop(id):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute('DELETE FROM LaptopInformation WHERE Id = %s', (id,))

        connection.commit()
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Step 6: Menu-driven interface
def menu():
    while True:
        print("\nMenu:")
        print("1. Add Laptop")
        print("2. View Laptops")
        print("3. Update Laptop")
        print("4. Delete Laptop")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            sl_no = int(input("Enter Serial Number: "))
            model = input("Enter Model: ")
            brand = input("Enter Brand: ")
            price = float(input("Enter Price: "))
            insert_laptop(sl_no, model, brand, price)
            print("Laptop added successfully!")

        elif choice == '2':
            laptops = fetch_laptop_info()
            print("\nLaptop Information:")
            for laptop in laptops:
                print(laptop)

        elif choice == '3':
            id = int(input("Enter Laptop ID to update: "))
            sl_no = int(input("Enter New Serial Number: "))
            model = input("Enter New Model: ")
            brand = input("Enter New Brand: ")
            price = float(input("Enter New Price: "))
            update_laptop(id, sl_no, model, brand, price)
            print("Laptop updated successfully!")

        elif choice == '4':
            id = int(input("Enter Laptop ID to delete: "))
            delete_laptop(id)
            print("Laptop deleted successfully!")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


# Main script execution
if __name__ == "__main__":
    create_database()  # Create the database and table
    menu()  # Run the menu-driven interface
