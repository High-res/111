from flask import jsonify
import pymysql

from src.config.config import HOST, USER, PASSWORD, DB_NAME


class HalykSmartpoint:
    def add(sku, product_name, price, loan_period, pp1, pp2, pp3, pp4, pp6, pp7, pp8, pp9, pp10, pp12, pp15, pp16):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor()
        try:
            insert_query = "INSERT INTO `halyk_smartpoint_products` (sku, product_name, price, loan_period, pp1, pp2, pp3, pp4, pp6, pp7, pp8, pp9, pp10, pp12, pp15, pp16) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);" 
            cursor.execute(insert_query, (sku, product_name, price, loan_period, pp1, pp2, pp3, pp4, pp6, pp7, pp8, pp9, pp10, pp12, pp15, pp16))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def get():
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            select_all_rows = "SELECT * FROM `halyk_smartpoint_products`"
            cursor.execute(select_all_rows)
            product = jsonify(cursor.fetchall())
            return product
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
    
    def update(sku, price, loan_period, pp1, pp2, pp3, pp4, pp6, pp7, pp8, pp9, pp10, pp12, pp15, pp16, stock_sum):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            update_query = "UPDATE `halyk_smartpoint_products` SET price=%s, loan_period=%s, pp1=%s, pp2=%s, pp3=%s, pp4=%s, pp6=%s, pp7=%s, pp8=%s, pp9=%s, pp10=%s, pp12=%s, pp15=%s, pp16=%s, stock_sum=%s WHERE sku=%s;"
            cursor.execute(update_query, (price, loan_period, pp1, pp2, pp3, pp4, pp6, pp7, pp8, pp9, pp10, pp12, pp15, pp16, stock_sum, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()

    def delete(sku):
        connection = pymysql.connect(host=HOST, port=3306, user=USER, password=PASSWORD, database=DB_NAME, charset='utf8')
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        try:
            delete_query = "DELETE FROM `halyk_smartpoint_products` WHERE sku=%s;"
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
            select_all_rows = f"SELECT * FROM `halyk_smartpoint_products` WHERE (`sku` LIKE '%{s}%' OR `product_name` LIKE '%{s}%')"
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
            update_query = "UPDATE `halyk_smartpoint_products` SET stock_sum=%s WHERE sku=%s;"
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
            update_query = "UPDATE `halyk_smartpoint_products` SET price=%s, loan_period=%s WHERE sku=%s;"
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
            update_query = "UPDATE `halyk_smartpoint_products` SET price=%s WHERE sku=%s;"
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
            update_query = "UPDATE `halyk_smartpoint_products` SET loan_period=%s WHERE sku=%s;"
            cursor.execute(update_query, (loan, sku))
            connection.commit()
        except Exception as ex :
            print(ex)
        finally:
            connection.close()
