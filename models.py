from pickletools import decimalnl_short
from tokenize import Number
from unicodedata import category, decimal, numeric
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List

class ProductBase(SQLModel):
    name: str
    price: float
    quantity: float
    imgurl: str
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")


class Product(ProductBase, table=True):
    id: int = Field(default=None, primary_key=True)

    category: Optional["Category"] = Relationship(back_populates="products")


class ProductCreate(ProductBase):
    pass


class ProductUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None
    quantity: Optional[float] = None
    imgurl: Optional[str] = None
    category_id: Optional[int] = None

class CategoryBase(SQLModel):
    name: str


class Category(CategoryBase, table=True):
    id: int = Field(default=None, primary_key=True)

    products: List[Product] = Relationship(back_populates="category")


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(SQLModel):
    name: Optional[str]
