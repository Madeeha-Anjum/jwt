from db import engine, SessionLocal
from fastapi import FastAPI, Depends
import models
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class User(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    hashed_password: str


@app.get("/")
async def read_all(db: SessionLocal = Depends(get_db)):
    # the todos table
    return db.query(models.Todos).all()


@app.put("/users")
async def add_user(user: User, db: SessionLocal = Depends(get_db)):
    # the users table
    users_model = models.Users()

    users_model.email = user.email
    users_model.username = user.username
    users_model.first_name = user.first_name
    users_model.last_name = user.last_name
    users_model.hashed_password = user.hashed_password

    db.add(users_model)
    db.commit()

    return db.query(models.Users).all()


# ========================================================
class CreateUser(BaseModel):
    username: str
    email: Optional[str]
    first_name: str
    last_name: str


@app.post("/create/user")
async def create_user(user: CreateUser):
    create_user_model = models.Users()
    create_user_model.username = user.username
    create_user_model.email = user.email
    create_user_model.first_name = user.first_name
    create_user_model.last_name = user.last_name
    create_user_model.hashed_password = user.password
    create_user_model.is_active = True

    return create_user_model
