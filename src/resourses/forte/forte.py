from flask import jsonify

import src.mysql as mysql

class ForteResourse:
    def sku_get(shop_name, sku):
        if shop_name == 'protel':
            return mysql.Forte.search(sku)

    def sku_delete(shop_name, sku):
        if shop_name == 'protel':
            mysql.Forte.delete(sku)
            return jsonify('Удалено успешно')

    def sku_put(shop_name, parser, sku):
        if shop_name == 'protel':
            parser.add_argument(f'{sku}', type=str)
            parser.add_argument('product_name', type=str)
            parser.add_argument('brand', type=str)
            parser.add_argument('price', type=str)
            parser.add_argument('pp1', type=str)
            parser.add_argument('pp2', type=str)
            parser.add_argument('pp3', type=str)
            parser.add_argument('pp4', type=str)
            parser.add_argument('pp5', type=str)
            parser.add_argument('pp6', type=str)
            parser.add_argument('pp7', type=str)
            parser.add_argument('pp8', type=str)
            parser.add_argument('pp9', type=str)
            parser.add_argument('pp10', type=str)
            parser.add_argument('pp11', type=str)
            parser.add_argument('pp12', type=str)
            parser.add_argument('pp13', type=str)
            parser.add_argument('pp14', type=str)
            parser.add_argument('pp15', type=str)
            parser.add_argument('pp16', type=str)
            mysql.Forte.update = parser.parse_args()
            return jsonify('Обновлено успешно')

    def get(shop_name):
        if shop_name == 'protel':
            return mysql.Forte.get()

    def post(shop_name, parser):
        if shop_name == 'protel':
            parser.add_argument('sku', type=str)
            parser.add_argument('product_name', type=str)
            parser.add_argument('brand', type=str)
            parser.add_argument('price', type=str)
            parser.add_argument('pp1', type=str)
            parser.add_argument('pp2', type=str)
            parser.add_argument('pp3', type=str)
            parser.add_argument('pp4', type=str)
            parser.add_argument('pp5', type=str)
            parser.add_argument('pp6', type=str)
            parser.add_argument('pp7', type=str)
            parser.add_argument('pp8', type=str)
            parser.add_argument('pp9', type=str)
            parser.add_argument('pp10', type=str)
            parser.add_argument('pp11', type=str)
            parser.add_argument('pp12', type=str)
            parser.add_argument('pp13', type=str)
            parser.add_argument('pp14', type=str)
            parser.add_argument('pp15', type=str)
            parser.add_argument('pp16', type=str)
            mysql.Forte.add = parser.parse_args()
            return jsonify('Добавлено успешно')