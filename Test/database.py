import pymysql

sql_select_all='SELECT * FROM laptop'
sql_insert = 'INSERT INTO laptop(SINo, Model, Brand, Price) values (%s, %s, %s, %s)'
sql_update = 'UPDATE laptop SET SINo=%s, Model=%s, Brand=%s, Price=%s WHERE id = %s'
sql_delete = 'DELETE FROM laptop WHERE id = %s'

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'cdacacts',
    'db': 'LaptopInfo'
}

def get_all():
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_select_all)
        users = cursor.fetchall()
    except Exception as ex:
        print('Exception raised', ex)
    else:
        return users
    finally:
        cursor.close()
        connection.close()


def add_laptop(SINo, Model, Brand, Price):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        cursor.execute(sql_insert, (SINo, Model, Brand, Price))
        connection.commit()
    except Exception as ex:
        print('Failed to insert ', ex)
    finally:
        cursor.close()
        connection.close()

#add_laptop('YZFV', 'Lenovo1', 'Lenovo', 35000 )


def update_laptop(id, SINo, Model, Brand, Price):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    try:
        rows_affected = cursor.execute(sql_update, (id, SINo, Model, Brand, Price))
        connection.commit()
    except Exception as ex:
        print('Failed to update: ', ex)
    else:
        if rows_affected == 0:
            print('Laptop info failed to update as no Laptop was found by that id')
        else:
            print('Laptop info updated Successfully')
    finally:
        cursor.close()
        connection.close()


def delete_laptop(id):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    try:
        cursor.execute(sql_delete, id)
        connection.commit()
        all_data = get_all()
    except Exception as ex:
        print('Exception raised: ', ex)
    else:
        print(all_data)
    finally:
        cursor.close()
        connection.close()

