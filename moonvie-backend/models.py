from sqlalchemy import Column, INT, BIGINT, Date, VARCHAR, Year
from sqlalchemy.orm import relationship
from database import Base


class CodeTable(Base):
    __tablename__ = "code_table"

    code = Column(VARCHAR, primary_key=True, index=True)
    code_name = Column(VARCHAR)
    code_desc = Column(VARCHAR)


class Season(Base):
    __tablename__ = "season"

    season_id = Column(INT, primary_key=True, index=True)
    season_name = Column(VARCHAR)
    start_date = Column(Date)
    end_date = Column(Date)


class MovieInfo(Base):
    __tablename__ = "movie_info"

    movie_info_id = Column(INT, primary_key=True, index=True)
    nation = Column(VARCHAR)
    director = Column(VARCHAR)
    open_date = Column(Date)
    movie_code = Column(VARCHAR)
    production_code = Column(VARCHAR)


class MovieGenre(Base):
    __tablename__ = "movie_genre"

    movie_genre_id = Column(INT, primary_key=True, index=True)
    genre_name = Column(VARCHAR)
    movie_info_id = Column(INT)


class MovieStatistics(Base):
    __tablename__ = "movie_statistics"

    statistics_id = Column(INT, primary_key=True, autoincrement=True, nullbase=False)
    audience_cnt = Column(BIGINT)
    sales_amount = Column(INT)
    screen_start = Column(Date, nullbase=False)
    screen_end = Column(Date, nullbase=False)
    screen_year = Column(Year, nullbase=False)
    movie_info_id = Column(INT)
    season_id = Column(INT)
    region_code = Column(INT, nullbase=False)
