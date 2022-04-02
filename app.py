from flask import Flask
from flask_restful import Api

import src.resourses as res


app = Flask(__name__)
api = Api(app)


api.add_resource(res.Product, '/v1/products/<merchant>/<shop_name>/<sku>')
api.add_resource(res.Products, '/v1/products/<merchant>/<shop_name>')
# /v1/products/<merchant>/<shop_name>/<sku> Done
# User api with authoruzation
# order_history with autorization

if __name__ == '__main__':
    app.run(debug=True, port=3000)