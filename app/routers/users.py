from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import engine, SessionLocal
from pydantic import BaseModel
import models

from .auth import (
    get_current_user,
    get_user_exception,
    verify_password,
    get_password_hash,
)


router = APIRouter(
    prefix="/users", tags=["users"], responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)  # create the databases


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str


@router.get("/")
async def get_users(db=Depends(get_db)):
    return db.query(models.Users).all()


@router.get("/user/")
async def get_user_query(user_id: int, db=Depends(get_db)):
    user_model = db.query(models.Users).filter(models.Users.id == user_id).first()

    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_model


@router.put("/user/password")
async def update_password(
    user_verification: UserVerification,
    user: dict = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    user_model = db.query(models.Users).filter(models.Users.id == user.id).first()
    if user_model is not None:

        # verify the username and password
        if user_verification.username == user_model.username and verify_password(
            user_verification.password, user_model.hashed_password
        ):
            # update the password
            user_model.hashed_password = get_password_hash(
                user_verification.new_password
            )
            db.add(user_model)
            db.commit()

            return {"message": "Password updated successfully"}

        return {"message": "Username or password is incorrect"}


@router.delete("/user/")
async def delete_user(
    user: dict = Depends(get_current_user), db: Session = Depends(get_db)
):
    if user is None:
        raise get_user_exception()

    db.query(models.Users).filter(models.Users.id == user.id).delete()
    db.commit()

    return {"message": "User deleted successfully"}
