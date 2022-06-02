import configparser
from models.product_model import Product
import requests

config = configparser.ConfigParser()
config.read('configuration.ini')
gateway_host = config['gateway']['host']


class ProductRepository:
    def __init__(self, product_dao):
        self.product_dao = product_dao
        print("ProductRepository")

    def add_product(self, product: Product, logged_user):
        user_id = logged_user['user_id']
        new_product = Product(product.name, user_id,
                              product.price, product.description)
        return self.product_dao.add_product(new_product)

    def get_products(self):
        return self.product_dao.get_all()
        # return "product getted"

    def get_products_user(self, logged_user):
        user_id = logged_user['user_id']
        return self.product_dao.get_products_by_user_id(user_id)

    def update_product(self, product_id, new_product):
        return self.product_dao.update_product(product_id, new_product)

    def get_product_by_id(self, product_id):
        return self.product_dao.get_product(product_id)
        # return "product getted by id"

    def delete_product(self, product_id):
        return self.product_dao.delete_product(product_id)
        # return "product deleted"


def check_user(request):
    gateway = config['gateway']['host']
    token = request.headers['Authorization']
    logged_user = requests.get(
        gateway + '/users/current', headers={'Authorization': token}).json()
    if 'detail' in logged_user:
        if logged_user['detail'] == 'Could not validate credentials':
            return "AUTH_ERROR"
    return logged_user
