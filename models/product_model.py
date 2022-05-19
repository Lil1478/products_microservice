from sqlalchemy import Column, Integer, String, true

from database import Base


class Product(Base):
    __tablename__ = 'products'
    product_id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, nullable=False)
    name = Column(String(120), nullable=False)
    description = Column(String(820), nullable=True)
    price = Column(Integer(), nullable=False)

    def __init__(self, name, owner_id, price, description):
        self.name = name
        self.owner_id = owner_id
        self.price = price
        self.description = description

    def to_json(self):
        return {
            'id': self.product_id,
            "owner_id": self.owner_id,
            'name': self.name,
            'price': self.price,
            'description': self.description
        }
