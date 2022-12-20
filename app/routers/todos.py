from typing import Optional
from fastapi import Depends, HTTPException, APIRouter
from db import engine, SessionLocal
import models
from pydantic import BaseModel, Field

# . means from the same directory
from .auth import get_current_user, get_user_exception


router = APIRouter(
    prefix="/todos", tags=["todos"], responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str] = None
    priority: int = Field(gt=0, lt=6, description="Priority must be between 1 and 5")
    complete: bool


@router.get("/")
async def read_all(db: SessionLocal = Depends(get_db)):
    # the todos table
    return db.query(models.Todos).all()


@router.post("/")
async def create_todo(
    todo: Todo,
    user: dict = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
):
    if user is None:
        raise get_user_exception()

    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()
    return todo_model


@router.put("/{todo_id}")
async def update_todo(
    todo_id: int,
    todo: Todo,
    user: dict = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
):
    if user is None:
        raise get_user_exception()
    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )

    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get("id")

    db.add(todo_model)
    db.commit()
    return todo_model


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    user: dict = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
):
    if user is None:
        raise get_user_exception()
    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.id == todo_id)
        .filter(models.Todos.owner_id == user.get("id"))
        .first()
    )
    if todo_model is None:
        raise http_exception(status_code=404, detail="Todo not found")
    db.delete(todo_model)
    db.commit()
    return todo_model


@router.get("/user")
async def read_all_by_users(
    user: dict = Depends(get_current_user), db: SessionLocal = Depends(get_db)
):

    if user is None:
        raise get_user_exception()
    # print(user)  encode = { "username": username, "id": user_id }
    # dictionary user["id"] or user.get("id")
    todo_model = (
        db.query(models.Todos).filter(models.Todos.owner_id == user.get("id")).all()
    )

    return todo_model


@router.post("/{todo_id}")
async def read_todos(
    todo_id: int,
    user: dict = Depends(get_current_user),
    db: SessionLocal = Depends(get_db),
):
    print("hi")
    if user is None:
        raise get_user_exception()

    todo_model = (
        db.query(models.Todos)
        .filter(models.Todos.owner_id == user.get("id"))
        .filter(models.Todos.id == todo_id)
        .first()
    )

    if todo_model is None:
        return {"message": "Todo not found"}
    else:
        return todo_model


def http_exception(status_code: int, detail: str):
    return HTTPException(status_code=status_code, detail=detail)
