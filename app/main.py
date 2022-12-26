from fastapi import FastAPI, Depends
from db import engine
import models
from routers import auth, todos, users

print(
    "\x1b[6;30;42m"
    + "Congratulations the backend is running on http://localhost:8000"
    + "\x1b[0m"
)
print(
    "\x1b[6;30;42m"
    + "Congratulations the API docs are running on http://localhost:8000/docs"
    + "\x1b[0m"
)
print(
    "\x1b[6;30;42m"
    + "Congratulations pgAdmin is running on http://localhost:8080"
    + "\x1b[0m"
)


app = FastAPI()


models.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(users.router)
