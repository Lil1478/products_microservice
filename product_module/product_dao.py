import re
from sqlalchemy.orm import validates
from fastapi import status, HTTPException

from database import SessionLocal
from models.product_model import Product

db = SessionLocal()


class ProductDAO:
    def __init__(self, ):
        self.collection_name = "Products"

    def get_all(self):
        products = db.query(Product).all()
        return products

    def add_product(self, product: Product):
        product = Product(product.name, product.price)
        db.add(product)
        db.commit()
        return self.get_product(product.product_id)

    def get_product(self, product_id):
        product_db = db.query(Product).filter(Product.product_id == product_id).first()
        return product_db

    def delete_user(self, product_id):
        product_db = db.query(Product).filter(Product.product_id == product_id).first()
        if product_db is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Resource Not Found")
        db.delete(product_db)
        db.commit()
        return "SUCCESS"
