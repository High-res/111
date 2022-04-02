from flask import jsonify
import pymysql

from src.config.config import HOST, USER, PASSWORD, DB_NAME


class Forte:
    def add(sku, product_name, brand, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor()
        try:
            insert_query = "INSERT INTO `forte_products` (sku, product_name, brand, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(insert_query, (sku, product_name, brand, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def get():
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            select_all_rows = "SELECT * FROM `forte_products`"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def update(sku, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `forte_products` SET price=%s, pp1=%s, pp2=%s, pp3=%s, pp4=%s, pp5=%s, pp6=%s, pp7=%s, pp8=%s, pp9=%s, pp10=%s, pp11=%s, pp12=%s, pp13=%s, pp14=%s, pp15=%s, pp16=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def delete(sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            delete_query = "DELETE FROM `forte_products` WHERE sku=%s;"
            cursor.execute(delete_query, (sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def search(s):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            select_all_rows = f"SELECT * FROM `forte_products` WHERE (`sku` LIKE '%{s}%' OR `product_name` LIKE '%{s}%')"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()