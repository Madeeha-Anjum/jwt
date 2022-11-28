from db import engine, SessionLocal
from fastapi import FastAPI, Depends
import models


app = FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def read_all(db: SessionLocal = Depends(get_db)):
    # the todos table
    return db.query(models.Todos).all()
