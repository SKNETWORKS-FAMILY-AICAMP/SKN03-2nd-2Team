from fastapi import FastAPI
from routers import movie

# # SQLAlchemy 모델 생성
# Base.metadata.create_all(bind=engine)

app = FastAPI()

# 라우터 등록
app.include_router(movie.router)


@app.get("/")
def home():
    return {"message": "Welcome to the Moonvie"}
