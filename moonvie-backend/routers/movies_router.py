from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from typing import List
from datetime import date
import crud, models, schemas


router = APIRouter()


@router.get("/top/", response_model=List[schemas.TopMovies])
async def read_top_movies(
    startdate: date = "2024-01-01",  # startDate 쿼리 파라미터
    enddate: date = "2024-01-20",  # endDate 쿼리 파라미터
    db: Session = Depends(get_db),
):
    try:
        limit = 10
        movies = crud.get_top_movies(db, startdate, enddate, limit)
        return movies
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("/season/", response_model=List[schemas.SeasonMovies])
# async def read_season_rank(
#     season: 100,
#     db: Session = Depends(get_db),
# ):
#     try:
#         limit = 10
#         movies = crud.get_season_movies(db, season, limit)
#         return movies
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


@router.get("/region/")
async def read_region_rank(db: Session = Depends(get_db)):
    return {"message": "Region"}


@router.get("/genre/season/")
async def read_genre_season_rank(db: Session = Depends(get_db)):
    return {"message": "genre season"}


@router.get("/genre/holiday/")
async def read_genre_holiday_rank(db: Session = Depends(get_db)):
    return {"message": "/genre/holiday"}


@router.get("/genre/covid/")
async def get_genre_covid_rank():
    return {"message": "/genre/covid"}


@router.get("/covid/money/")
async def get_covid_stats():
    return {"message": "covid money"}


@router.get("/covid/people/")
async def get_covid_stats():
    return {"message": "covid people"}
