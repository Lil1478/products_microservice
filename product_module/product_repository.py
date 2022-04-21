from models.product_model import Product


class ProductRepository:
    def __init__(self, account_dao):
        self.account_dao = account_dao
        print("ProductRepository")

    def add_product(self, product: Product):
        # return self.account_dao.add_product(product)
        return "product added"

    def get_products(self):
        # return self.account_dao.get_all()
        return "product getted"

    def get_product_by_id(self, product_id):
        # return self.account_dao.get_product(product_id)
        return "product getted by id"

    def delete_product(self, product_id):
        # return self.account_dao.delete_product(product_id)
        return "product deleted"
