from sqlalchemy import Column, INT, BIGINT, Date, VARCHAR
from sqlalchemy.orm import relationship
from database import Base


class CodeTable(Base):
    __tablename__ = "code_table"

    code = Column(INT, primary_key=True, autoincrement=True)
    code_name = Column(INT)
    code_desc = Column(VARCHAR(255))
    code_group = Column(VARCHAR(20))


class Director(Base):
    __tablename__ = "director"
    director_id = Column(INT, primary_key=True, autoincrement=True)
    director_name = Column(VARCHAR(50))


class MovieGenre(Base):
    __tablename__ = "movie_genre"
    movie_genre_id = Column(INT, primary_key=True, autoincrement=True)
    movie_code = Column(INT)


class MovieInfo(Base):
    __tablename__ = "movie_info"

    movie_info_id = Column(INT, primary_key=True, autoincrement=True)
    nation = Column(VARCHAR(10))
    open_date = Column(Date)
    movie_code = Column(INT)


class MovieInfoDirector(Base):
    __tablename__ = "movie_info_director"
    movie_info_id = Column(INT, primary_key=True)
    director_id = Column(INT, primary_key=True)


class MovieInfogenre(Base):
    __tablename__ = "movie_info_genre"
    movie_info_id = Column(INT, primary_key=True)
    movie_genre_id = Column(INT, primary_key=True)


class MovieInfoprodection(Base):
    __tablename__ = "movie_info_production"
    movie_info_id = Column(INT, primary_key=True)
    porduction_id = Column(INT, primary_key=True)


class MovieStatistics(Base):
    __tablename__ = "movie_statistics"
    statistics_id = Column(INT, primary_key=True, autoincrement=True)
    sales_amount = Column(BIGINT)
    region_code = Column(INT)
    audience_cnt = Column(BIGINT)
    movie_code = Column(INT)
    screen_start = Column(Date)
    screen_end = Column(Date)
    season_code = Column(INT)


class Production(Base):
    __tablename__ = "production"
    production_id = Column(INT, primary_key=True, autoincrement=True)
    porduction_code = Column(INT)
