import pymysql

#Sql Statements
sql_select_all='SELECT * FROM userinfo'
sql_select_by_id = 'SELECT * FROM userinfo WHERE id = %s'
sql_insert = 'INSERT INTO USERINFO(username, password, emailaddress) values (%s, %s, %s)'
sql_update = 'UPDATE userinfo SET username=%s, emailaddress=%s, password=%s WHERE id = %s'
sql_delete = 'DELETE FROM userinfo WHERE id = %s'

#MySQL configurations
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'cdacacts',
    'db': 'sampledb'
}


#root, cdacacts
def get_all_users():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        #sql_statement = 'SELECT * FROM userinfo'
        cursor.execute(sql_select_all)
        users = cursor.fetchall()
    except Exception as ex:
        print('Exception raised', ex)
    else:
        #print(users)
        #for user in users:
        #    print(f'Username: {user[1]}, Email-address: {user[3]}')
        return users
    finally:
        cursor.close()
        connection.close()

def get_user_by_id(id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_select_by_id, id)
        user = cursor.fetchone()
        if user == None:
            print('User not found')
    except Exception as ex:
        print('Exception while fetching single recored', ex)
    else:
        return user
    finally:
        cursor.close()
        connection.close()

def add_user(username, password, email):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute(sql_insert, (username, password, email))
        connection.commit()
    except Exception as ex:
        print('Failed to insert ', ex)
    finally:
        cursor.close()
        connection.close()

def update_user(id, name, pwd, email):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        rows_affected = cursor.execute(sql_update, (name, email, pwd, id))
        connection.commit()
    except Exception as ex:
        print('Failed to update: ', ex)
    else:
        if rows_affected == 0:
            print('User info failed to update as no user was found by that id')
        else:
            print('User info updated Successfully')
    finally:
        cursor.close()
        connection.close()

def delete_user(id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_delete, id)
        connection.commit()
        users = get_all_users()
    except Exception as ex:
        print('Exception raised: ', ex)
    else:
        for user in users:
            print(user[1])
    finally:
        cursor.close()
        connection.close()
# users = get_all_users()
# for user in users:
#     print(f'{user[1]} with email: {user[3]} identified as {user[0]}')

# user = get_user_by_id(2)
# print(user)
'''
try:
    id = int(input('Enter the id of the user to update: '))
    name=input('Enter the name: ')
    pwd = input('Enter the password: ')
    email = input('Enter the email: ')

    #add_user(name, pwd, email)
    update_user(id, name, pwd, email)
    users = get_all_users()
except:
    print('Error occured')
else:
    for user in users:
        print(f"{user[1]} with email: {user[3]} is identified as {user[0]}")
finally:
    print('End of the application')
'''
delete_user(1)