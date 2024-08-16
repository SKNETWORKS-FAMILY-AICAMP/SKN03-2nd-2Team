from enum import Enum


class Parameters(Enum):
    ITEM_PER_PAGE = 100  # 페이지당 출력할 항목 수
    OPEN_START_DT = "2017"
    OPEN_END_DT = "2024"
    COLUMN_NAMES = [
        "영화 코드",
        "영화명(국문)",
        "개봉일",
        "영화장르",
        "대표 제작국가",
        "영화 감독 이름",
        "제작사 코드",
    ]


class ApiUrl(Enum):
    MOVIE_LIST = (
        "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
    )


class Path(Enum):
    CSV2CLEAN_FILE = "movies_2017_2024.csv"
    CSV2COMPARE_FILE = "compare_data.csv"
    FILTERED_CSV_FILE = "filtered_movies_2017_2024.csv"
