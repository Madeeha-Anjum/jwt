from typing import Optional
from fastapi import Depends, APIRouter
import models
from db import Base, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user, get_user_exception

router = APIRouter(
    prefix="/address", tags=["address"], response={404: {"description": "Not found"}}
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Address(Base):
    address1: str
    address2: Optional[str] = None
    city: str
    state: str
    country: str
    postalcode: str


@router.post("/")
async def create():
    return
