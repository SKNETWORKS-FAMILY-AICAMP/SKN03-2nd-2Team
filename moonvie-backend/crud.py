from sqlalchemy.orm import Session
from datetime import date
import models


# 제목, 장르, 개봉일, 누적 관객, 누적매출액
def get_top_movies(db: Session, startdate: date, enddate: date, limit: int = 10):
    return (
        db.query(
            models.MovieInfo.open_date,
            models.MovieStatistics.audience_cnt,
            models.MovieStatistics.sales_amount,
        )
        .join(
            models.MovieInfo,
            models.MovieInfo.movie_code == models.MovieStatistics.movie_code,
        )
        .filter(models.MovieStatistics.screen_start >= startdate)
        .filter(models.MovieStatistics.screen_end <= enddate)
        .order_by(models.MovieStatistics.audience_cnt.desc())
        .limit(limit)
        .all()
    )
