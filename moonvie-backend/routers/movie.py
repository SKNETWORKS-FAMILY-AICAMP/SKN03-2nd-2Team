from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()


@router.get("/movie/top/")
def top_movies(db: Session = Depends(get_db)):
    return {"message": "Top Movies"}


@router.get("/movie/genre/")
def genre_rank():
    return {"message": "Genre"}


@router.get("/movie/season/")
def season_rank():
    return {"message": "Season"}


@router.get("/movie/region/")
def region():
    return {"message": "Region"}


@router.get("/movie/wordcloud/")
def word_cloud():
    return {"message": "Word Cloud"}
