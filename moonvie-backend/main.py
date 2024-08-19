from fastapi import FastAPI, Depends
from database import Base, engine
from database import get_db
import models
from sqlalchemy.orm import Session
from routers import movies_router

# SQLAlchemy 모델 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(movies_router.router)


@app.get("/")
def home():
    return {"message": "Welcome to the Moonvie"}
