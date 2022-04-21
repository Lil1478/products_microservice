from fastapi import APIRouter
from starlette.requests import Request
import requests, time

from product_module.product_dao import ProductDAO
from product_module.product_repository import ProductRepository
from schemas.product_schemas import Product

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

# class ProductControllers:
#     def __init__(self, repository):
#         self.repository = repository
#         print('ProductControllers')

product_dao = ProductDAO()
product_repository = ProductRepository(product_dao)


@router.post("/")
def add_product(new_product: Product):
    result = product_repository.add_product(new_product)
    return result


@router.get("/")
async def get_products():
    return product_repository.get_products()


@router.get("/{product_id}")
async def get_product(product_id: int):
    # return {
    #     'id': 1,
    #     "owner_id": 1,
    #     'name': "product name",
    #     'price': 10
    # }
    product = product_repository.get_product_by_id(product_id)
    print("2222222 ", product)
    user = requests.get('http://localhost:8000/users/%s' % product.owner_id).json()
    print("Products owner ", user)
    return {'id': 1, "owner_id": 1, 'name': "product name", 'price': 10, 'owner_first_name': user['first_name']}
    # return product_repository.get_product_by_id(product_id)


@router.put("/{product_id}")
def update_product(product_id: int, new_product: Product):
    return {"product_name": new_product.name, "product_id": product_id}


@router.delete("/{product_id}")
async def delete_product(product_id: int):
    return product_repository.delete_product(product_id)
