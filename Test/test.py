import database
from Test.database import update_laptop, delete_laptop


def delete_feature():
    id = int(input('Enter the id of the laptop to delete: '))
    delete_laptop(id)

def add_laptop_details():
    #id = int(input('Enter the id of the user to update: '))
    SINo = input('Enter the SINo: ')
    Model = input('Enter the Model: ')
    Brand = input('Enter the Brand: ')
    Price = input('Enter the Price: ')
    database.add_laptop(SINo, Model, Brand, Price)


def view_all_laptop():
    view_all = database.get_all()
    if not view_all:
        print('No laptops are available')
    else:
        for m in view_all:
            print(m)

def update_feature():
    id = int(input('Enter the id of the laptop to update: '))
    SINo = input('Enter the SINo: ')
    Model = input('Enter the Model: ')
    Brand = input('Enter the Brand: ')
    Price = input('Enter the Price: ')
    update_laptop(SINo, Model, Brand, Price, id)


print('1. ADD New Laptops')
print('2. View All Laptops')
print('3. Update Laptop Details')
print('4. Delete Laptop')
print('5. Exit')
choice = input('Enter the choice [1-5]:')
match choice:
    case '1':
        add_laptop_details()
    case '2': view_all_laptop()
    case '3':
            print('Enter the details of the Laptop for updating')
            update_feature()
    case '4': delete_feature()
    case '5':
        print('Exiting the Program')
        exit()
    case '_': print('Invalid choice, Please try again')
