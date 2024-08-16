from enum import Enum


class Parameters(Enum):
    ITEM_PER_PAGE = 100  # 페이지당 출력할 항목 수
    OPEN_START_DT = "2017"
    OPEN_END_DT = "2024"


class ApiUrl(Enum):
    MOVIE_LIST = (
        "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"
    )
