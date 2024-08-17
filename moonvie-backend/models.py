from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class CodeTable(Base):
    __tablename__ = "code_table"

    code = Column(String, primary_key=True, index=True)
    code_name = Column(String)
    code_desc = Column(String)


class Season(Base):
    __tablename__ = "season"

    season_id = Column(Integer, primary_key=True, index=True)
    season_name = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)


class MovieInfo(Base):
    __tablename__ = "movie_info"

    movie_info_id = Column(Integer, primary_key=True, index=True)
    nation = Column(String)
    director = Column(String)
    open_date = Column(Date)
    movie_code = Column(String)
    production_code = Column(String)


class MovieGenre(Base):
    __tablename__ = "movie_genre"

    movie_genre_id = Column(Integer, primary_key=True, index=True)
    genre_name = Column(String)
    movie_info_id = Column(Integer, ForeignKey("movie_info.movie_info_id"))


class MovieStatistics(Base):
    __tablename__ = "movie_statistics"

    statistics_id = Column(Integer, primary_key=True, index=True)
    audience_cnt = Column(Integer)
    sales_amount = Column(Integer)
    screen_start = Column(Date)
    screen_end = Column(Date)
    screen_year = Column(Integer)
    screen_month = Column(Integer)
    movie_info_id = Column(Integer, ForeignKey("movie_info.movie_info_id"))
    season_id = Column(Integer, ForeignKey("season.season_id"))
    region_code = Column(String, ForeignKey("code_table.code"))
