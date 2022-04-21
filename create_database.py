from database import Base, engine
from models.product_model import User

print("Create database...")
Base.metadata.create_all(engine)