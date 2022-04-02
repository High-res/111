from flask import jsonify
import pymysql

from src.config.config import HOST, USER, PASSWORD, DB_NAME


class JmartMil:
    def add(sku, product_name, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor()
        try:
            insert_query = "INSERT INTO `jmart_mil_products` (sku, product_name, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" 
            cursor.execute(insert_query, (sku, product_name, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def get():
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            select_all_rows = "SELECT * FROM `jmart_mil_products`"
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
            update_query = "UPDATE `jmart_mil_products` SET price=%s, pp1=%s, pp2=%s, pp3=%s, pp4=%s, pp5=%s, pp6=%s, pp7=%s, pp8=%s, pp9=%s, pp10=%s, pp11=%s, pp12=%s, pp13=%s, pp14=%s, pp15=%s, pp16=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def update_preorder(sku, price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16, preOrder_1, preOrder_2, preOrder_3, preOrder_4, preOrder_5, preOrder_6, preOrder_7, preOrder_8, preOrder_9, preOrder_10, preOrder_11, preOrder_12, preOrder_13, preOrder_14, preOrder_15, preOrder_16):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `jmart_mil_products` SET price=%s, pp1=%s, pp2=%s, pp3=%s, pp4=%s, pp5=%s, pp6=%s, pp7=%s, pp8=%s, pp9=%s, pp10=%s, pp11=%s, pp12=%s, pp13=%s, pp14=%s, pp15=%s, pp16=%s, preOrder_1=%s, preOrder_2=%s, preOrder_3=%s, preOrder_4=%s, preOrder_5=%s, preOrder_6=%s, preOrder_7=%s, preOrder_8=%s, preOrder_9=%s, preOrder_10=%s, preOrder_11=%s, preOrder_12=%s, preOrder_13=%s, preOrder_14=%s, preOrder_15=%s, preOrder_16=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, pp1, pp2, pp3, pp4, pp5, pp6, pp7, pp8, pp9, pp10, pp11, pp12, pp13, pp14, pp15, pp16, preOrder_1, preOrder_2, preOrder_3, preOrder_4, preOrder_5, preOrder_6, preOrder_7, preOrder_8, preOrder_9, preOrder_10, preOrder_11, preOrder_12, preOrder_13, preOrder_14, preOrder_15, preOrder_16, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def delete(sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            delete_query = "DELETE FROM `jmart_mil_products` WHERE sku=%s;"
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
            select_all_rows = f"SELECT * FROM `jmart_mil_products` WHERE (`sku` LIKE '%{s}%' OR `product_name` LIKE '%{s}%')"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()