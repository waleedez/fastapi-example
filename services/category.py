from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlmodel import Session

from models import *

def get_categories(session: Session):
    categories = session.exec(select(Category)).scalars().all()

    return categories
