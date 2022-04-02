from flask_restful import Resource, reqparse

import src.resourses as res


class Product(Resource):
    def get(self, merchant, shop_name, sku):
        if merchant == 'forte':
            return res.ForteResourse.sku_get(shop_name, sku)
        elif merchant == 'halyk':
            return res.HalykResourse.sku_get(shop_name, sku)
        elif merchant == 'jmart':
            return res.JmartResourse.sku_get(shop_name, sku)

    def delete(self, merchant, shop_name, sku):
        if merchant == 'forte':
            return res.ForteResourse.sku_delete(shop_name, sku)
        elif merchant == 'halyk':
            return res.HalykResourse.sku_delete(shop_name, sku)
        elif merchant == 'jmart':
            return res.JmartResourse.sku_delete(shop_name, sku)

    def put(self, merchant, shop_name, sku):
        parser = reqparse.RequestParser()
        if merchant == 'forte':
            return res.ForteResourse.sku_put(shop_name, parser, sku)
        elif merchant == 'halyk':
            return res.HalykResourse.sku_put(shop_name, parser, sku)
        elif merchant == 'jmart':
            return res.JmartResourse.sku_put(shop_name, parser, sku)

class Products(Resource):
    def get(self, merchant, shop_name):
        if merchant == 'forte':
            return res.ForteResourse.get(shop_name)
        elif merchant == 'halyk':
            return res.HalykResourse.get(shop_name)
        elif merchant == 'jmart':
            return res.JmartResourse.get(shop_name)

    def post(self, merchant, shop_name):
        parser = reqparse.RequestParser()
        if merchant == 'forte':
            return res.ForteResourse.post(shop_name, parser)
        elif merchant == 'halyk':
            return res.HalykResourse.post(shop_name, parser)
        elif merchant == 'jmart':
            return res.JmartResourse.post(shop_name, parser)