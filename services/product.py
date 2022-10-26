from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session

from models import *

def get_products(session: Session, categoryId):
    if categoryId:
        products = session.exec(select(Product).where(Product.category_id == categoryId)).scalars().all()
    else:
        products = session.exec(select(Product)).scalars().all()

    return products

def create_product(session: Session, product: ProductCreate):
    add_prod = Product.from_orm(product)
    session.add(add_prod)
    session.commit()
    session.refresh(add_prod)

    return add_prod

def update_product(session: Session, productId: int, product: ProductUpdate):
    db_prod = session.get(Product, productId)
    if not db_prod:
        raise HTTPException(status_code=404, detail="Product not found")
    prod_data = product.dict(exclude_unset=False)
    for key, value in prod_data.items():
        setattr(db_prod, key, value)
    session.add(db_prod)
    session.commit()
    session.refresh(db_prod)
    return db_prod

def patch_product(session: Session, productId: int, product: ProductUpdate):
    db_prod = session.get(Product, productId)
    if not db_prod:
        raise HTTPException(status_code=404, detail="Product not found")
    prod_data = product.dict(exclude_unset=True)
    for key, value in prod_data.items():
        setattr(db_prod, key, value)
    session.add(db_prod)
    session.commit()
    session.refresh(db_prod)
    return db_prod

def get_product(session: Session, productId: int):
    product = session.get(Product, productId)

    return product

def delete_product(session: Session, productId: int):
    prod = session.get(Product, productId)

    if not prod:
        raise HTTPException(status_code=404, detail="Product not found.")

    session.delete(prod)
    session.commit()

    return {"Success"}
