import re
from sqlalchemy.orm import validates
from fastapi import status, HTTPException

from database import SessionLocal
from models.product_model import Product

db = SessionLocal()


class ProductDAO:
    def __init__(self, ):
        self.collection_name = "products"

    def get_all(self):
        products = db.query(Product).all()
        return products

    def add_product(self, product: Product):
        db.add(product)
        db.commit()
        return self.get_product(product.product_id)

    def get_product(self, product_id):
        product_db = db.query(Product).filter(
            Product.product_id == product_id).first()
        return product_db

    def get_products_by_user_id(self, user_id):
        products_db = db.query(Product).filter(
            Product.owner_id == user_id).all()
        return products_db

    def delete_product(self, product_id):
        product_db = db.query(Product).filter(
            Product.product_id == product_id).first()
        if product_db is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
        db.delete(product_db)
        db.commit()
        return "SUCCESS"

    def update_product(self, product_id, new_product: Product):
        db_product = db.query(Product).filter(
            Product.product_id == product_id).first()
        if db_product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Order Not Found")
        db_product.name = new_product.name
        db_product.description = new_product.description
        db_product.price = new_product.price
        return self.get_product(product_id)
