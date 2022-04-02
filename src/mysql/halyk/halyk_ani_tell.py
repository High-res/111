from flask import jsonify
import pymysql

from src.config.config import HOST, USER, PASSWORD, DB_NAME


class HalykAniTell:
    def add(sku, product_name, price, loan_period, pp1, pp2, pp3):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor()
        try:
            insert_query = "INSERT INTO `halyk_ani_tell_products` (sku, product_name, price, loan_period, pp1, pp2, pp3) VALUES (%s,%s,%s,%s,%s,%s,%s);" 
            cursor.execute(insert_query, (sku, product_name, price, loan_period, pp1, pp2, pp3))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def get():
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            select_all_rows = "SELECT * FROM `halyk_ani_tell_products`"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def update(sku, price, loan_period, pp1, pp2, pp3, stock_sum):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_ani_tell_products` SET price=%s, loan_period=%s, pp1=%s, pp2=%s, pp3=%s, stock_sum=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, loan_period, pp1, pp2, pp3, stock_sum, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def delete(sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            delete_query = "DELETE FROM `halyk_ani_tell_products` WHERE sku=%s;"
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
            select_all_rows = f"SELECT * FROM `halyk_ani_tell_products` WHERE (`sku` LIKE '%{s}%' OR `product_name` LIKE '%{s}%')"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def stock_sum(stock_sum, sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_ani_tell_products` SET stock_sum=%s WHERE sku=%s;"
            cursor.execute(update_query, (stock_sum, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def loan_price(price, loan, sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_ani_tell_products` SET price=%s, loan_period=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, loan, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def price(price, sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_ani_tell_products` SET price=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def loan(loan, sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_ani_tell_products` SET loan_period=%s WHERE sku=%s;"
            cursor.execute(update_query, (loan, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()