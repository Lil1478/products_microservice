from pydantic import BaseModel


class Product(BaseModel):
    name: str
    owner_id: int
    price: float
