from pydantic import BaseModel
from typing import Union
from datetime import date


class TopMovies(BaseModel):
    audience_cnt: int
    sales_amount: int
    open_date: date


# class SeasonMovies(BaseModel):
#     season_code: int
#     audience_cnt: int
#     sales_amount: int
#     open_date: date
