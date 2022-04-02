import pymysql

from src.config.config import HOST, USER, PASSWORD, DB_NAME


def get_user() :
    try: 
        connection = pymysql.connect(
            host=HOST, 
            port=3306,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                select_all_rows = "SELECT * FROM `users`"
                cursor.execute(select_all_rows)
                user = cursor.fetchall()
                return user
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)

def add_user(name, password, role, email):
    try: 
        connection = pymysql.connect(
            host=HOST, 
            port=3306,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
           with connection.cursor() as cursor :
                insert_query = "INSERT INTO `users` (name, password, role, email) VALUES (%s,%s,%s,%s);" 
                cursor.execute(insert_query, (name, password, role, email))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Failed to connection ...")
        print(ex)

def update_user(id, name, password, role, email):
    try :
        connection = pymysql.connect(
            host=HOST, 
            port=3306,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        try :
            with connection.cursor() as cursor :
                update_query = "UPDATE `users` SET name=%s, password=%s, role=%s, email=%s WHERE id=%s;"
                cursor.execute(update_query, (name, password, role, email, id))
                connection.commit()
        finally:
            connection.close()
    except Exception as ex :
        print("Не подключилось")
        print(ex)