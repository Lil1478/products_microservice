from fastapi import APIRouter, status, HTTPException
from starlette.requests import Request
import requests
import time

from product_module.product_dao import ProductDAO
from product_module.product_repository import ProductRepository, check_user, check_user_exist
from schemas.product_schemas import Product

router = APIRouter(
    prefix="/products",
    tags=["products"],
    responses={404: {"description": "Not found"}},
)

product_dao = ProductDAO()
product_repository = ProductRepository(product_dao)

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


@router.post("")
def add_product(request: Request, new_product: Product):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        return credentials_exception
    result = product_repository.add_product(new_product, checked_user)
    return result


@router.get("")
async def get_products(request: Request,):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        raise credentials_exception
    return product_repository.get_products()


@router.get("/user")
async def get_products(request: Request, user_id: int):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        raise credentials_exception
    exist_user = check_user_exist(request, user_id)
    if exist_user is None:
        raise HTTPException(
            status_code=404, detail="User with such id does not exist")
    if exist_user == "ERROR":
        raise HTTPException(
            status_code=500, detail="Internal error")
    return product_repository.get_products_user(user_id)


@router.get("/{product_id}")
async def get_product(request: Request, product_id: int):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        raise credentials_exception
    return product_repository.get_product_by_id(product_id)


@router.put("/{product_id}")
def update_product(request: Request, product_id: int, new_product: Product):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        raise credentials_exception
    result = product_repository.update_product(
        checked_user['user_id'], product_id, new_product)
    return result


@router.delete("/{product_id}")
async def delete_product(request: Request, product_id: int):
    checked_user = check_user(request)
    if checked_user == 'AUTH_ERROR':
        raise credentials_exception
    return product_repository.delete_product(product_id)
