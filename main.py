from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session
from typing import Union

from dal.db import init_db, get_session
from models import *

import services.category as category_service
import services.product as product_service

app = FastAPI()


@app.get("/categories", response_model=List[Category])
def get_categories(*, session: Session = Depends(get_session)):
    categories = category_service.get_categories(session)

    return categories

@app.get("/products", response_model=List[Product])
def get_products(*, session: Session = Depends(get_session), categoryId: Union[int, None] = None ):
    products = product_service.get_products(session, categoryId)

    return products

@app.post("/products", response_model=Product)
def create_product(*, session: Session = Depends(get_session), product: ProductCreate):
    added_prod = product_service.create_product(session, product) 

    return added_prod

@app.put("/products/{productId}", response_model=Product)
def update_product(*, session: Session = Depends(get_session), productId: int, product: ProductUpdate):
    updated_prod = product_service.update_product(session, productId, product) 

    return updated_prod

@app.patch("/products/{productId}", response_model=Product)
def patch_product(*, session: Session = Depends(get_session), productId: int, product: ProductUpdate):
    updated_prod = product_service.patch_product(session, productId, product) 

    return updated_prod

@app.get("/products/{productId}", response_model=Product)
def get_product(*, session: Session = Depends(get_session), productId: int):
    product = product_service.get_product(session, productId)

    return product

@app.delete("/products/{productId}")
def patch_product(*, session: Session = Depends(get_session), productId: int):
    result = product_service.delete_product(session, productId) 

    return result
