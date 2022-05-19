from database import Base, engine
from models.product_model import Product

print("Create database...")
Base.metadata.create_all(engine)