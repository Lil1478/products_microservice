from sqlalchemy import Column, Integer, String

from database import Base


class Product(Base):
    __tablename__ = 'Products'
    product_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    price = Column(Integer(), nullable=False)

    def __init__(self, name, owner_id, price):
        self.name = name
        self.owner_id = owner_id
        self.price = price

    def to_json(self):
        return {
            'id': self.product_id,
            "owner_id": self.owner_id,
            'name': self.name,
            'price': self.price
        }
