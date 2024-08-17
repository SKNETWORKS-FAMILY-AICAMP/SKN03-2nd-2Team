from fastapi import APIRouter

router = APIRouter()


@router.get("/movie/top/")
def top_movies():
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
