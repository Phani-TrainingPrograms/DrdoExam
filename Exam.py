import pymysql

sql_insert = "INSERT INTO LaptopInfo (id, slno,model,brand,price) values (%s, %s, %s,%s, %s)"
sql_update = "UPDATE LaptopInfo SET (slno = %s, model = %s, brand = %s,price = %s) WHERE id = %s "
sql_delete = "DELETE FROM LaptopInfo WHERE id = %s"
sql_select_all ="SELECT * FROM LaptopInfo"
sql_select_by_id = "SELECT * FROM LaptopInfo WHERE id = %s"

db_config ={
    'host' : 'localhost',
    'user' : 'root',
    'password' : 'cdacacts',
    'db' : 'laptopdb'
}

def add_laptop(id,slno,model,brand,price):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_insert, (id,slno,model,brand,price))
        connection.commit()
    except Exception as ex:
        print("Failed to insert: ", ex)
    else:
        print("Laptop added successfully")
    finally:
        cursor.close()
        connection.close()

def get_all_laptop():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_select_all)
        laptops = cursor.fetchall()
    except Exception as ex:
        print("Exception raised: ", ex)
    else:
        return laptops
    finally:
        cursor.close()
        connection.close()

def get_laptop_by_id(id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_select_by_id, id)
        laptop = cursor.fetchone()
        print(laptop)
    except Exception as ex:
        print("Exception while fetching single record: ", ex)
    else:
        return laptop

    finally:
        cursor.close()
        connection.close()

def update_laptop(slno,model,brand,price,id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_update,slno,model,brand,price,id)
        laptop = cursor.fetchone()
        print("Laptop updated successfully")
    except Exception as ex:
        print("Exception while updating laptop info: ", ex)
    else:
        return laptop
    finally:
        cursor.close()
        connection.close()

def delete_laptop(id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_delete, (id))
        connection.commit()
        print("Laptop deleted successfully")
    except Exception as ex:
        print("Failed to delete: ", ex)
    finally:
        cursor.close()
        connection.close()

print("****************Laptop Corner****************")
print("Enter 1 for add_laptop")
print("Enter 2 for get_all_laptop")
print("Enter 3 for update_laptop")
print("Enter 4 for get_laptop_by_id")
print("Enter 5 for delete_laptop")
print("Enter 6 for exit")
choice= input("Enter the choice of operations: ")
match choice:
    case "1":
        id = int(input("Enter the ID: "))
        slno = input("Enter the serial number: ")
        model = input("Enter the model: ")
        brand = (input("Enter the brand: "))
        price = int(input("Enter the price: "))
        add_laptop(id, slno,model,brand,price)
        pass
    case "2":
        laptops=get_all_laptop()
        if not laptops:
            print("No laptops found")
        else:
           for l in laptops:
                print(l)
        pass
    case "3":
        id= int(input("Enter the id of laptop to be updated:"))
        slno = input("Enter the new serial number: ")
        model = input("Enter the new model: ")
        brand = (input("Enter the new brand: "))
        price = int(input("Enter the new price: "))
        update_laptop(slno,model,brand,price,id)
        pass
    case "4":
        id= input("Enter the id of laptop to be updated:")
        get_laptop_by_id(id)
        pass
    case "5":
        id = input("Enter the id of laptop to be deleted:")
        delete_laptop(id)
        pass
    case "6":
        print("Application exited successfully ")
        pass
    case _:
        print("Invalid choice")


