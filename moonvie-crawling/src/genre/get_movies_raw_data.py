import pandas as pd
import ray
import requests
from constants import ApiUrl, Parameters
from env import settings

ray.init()


def request_api(current_page):
    api_key = settings.KOFIC_API_KEY  # 여기에 발급받은 API 키를 입력하세요.

    url = ApiUrl.MOVIE_LIST.value
    params = {
        "key": api_key,
        "curPage": str(current_page),  # 현재 페이지
        "itemPerPage": Parameters.ITEM_PER_PAGE.value,  # 결과 ROW의 개수 (최대 100개로 설정)
        "openStartDt": Parameters.OPEN_START_DT.value,
        "openEndDt": Parameters.OPEN_END_DT.value,
    }

    # API 요청
    response = requests.get(url, params=params)

    # 응답 상태 코드 출력
    print(f"응답 상태 코드: {response.status_code} for page {current_page}")

    return response


@ray.remote
def process_get_movie(movie):
    movie_info = {
        "영화코드": movie.get("movieCd", "정보 없음"),
        "영화명(국문)": movie.get("movieNm", "정보 없음"),
        "영화명(영문)": movie.get("movieNmEn", "정보 없음"),
        "제작연도": movie.get("prdtYear", "정보 없음"),
        "개봉일": movie.get("openDt", "정보 없음"),
        "영화유형": movie.get("typeNm", "정보 없음"),
        "제작상태": movie.get("prdtStatNm", "정보 없음"),
        "제작국가": movie.get("nationAlt", "정보 없음"),
        "영화장르": movie.get("genreAlt", "정보 없음"),
        "대표제작국가": movie.get("repNationNm", "정보 없음"),
        "대표장르": movie.get("repGenreNm", "정보 없음"),
        # 감독 정보 추출
        "영화 감독 이름": ",".join(
            [
                director.get("peopleNm", "정보 없음")
                for director in movie.get("directors", [])
            ]
        ),
        # 제작사 정보 추출
        "제작사 코드": ",".join(
            [
                company.get("companyCd", "정보 없음")
                for company in movie.get("companys", [])
            ]
        ),
        # 제작사 정보 추출
        "제작사 명": ",".join(
            [
                company.get("companyNm", "정보 없음")
                for company in movie.get("companys", [])
            ]
        ),
    }
    return movie_info


def get_page_movies(movie_list_items):
    futures = [process_get_movie.remote(movie) for movie in movie_list_items]
    return ray.get(futures)


def get_movies() -> None:
    current_page = 1

    # 영화 정보를 저장할 리스트 생성
    movies = []

    while True:
        response = request_api(current_page)
        response_data = response.json()
        movie_list_items = response_data.get("movieListResult", {}).get("movieList", [])
        try:
            if not movie_list_items:
                raise Exception(
                    f"{current_page} 페이지에 데이터가 없습니다.\n 크롤링을 종료합니다."
                )
            # 데이터 가공
            if response.status_code != 200:
                raise Exception("API 요청 실패")
        except Exception as e:
            print(e)
            break
        else:
            # 데이터 가공
            try:
                movies.extend(get_page_movies(movie_list_items))
                # 페이지 번호 증가
                current_page += 1

            except ValueError as e:
                print(f"데이터 가공 실패: {e}")
    return movies


def save_movies2csv(movies):
    # 데이터프레임 생성
    movies_df = pd.DataFrame(movies).sort_values(by="개봉일")

    # CSV 파일로 저장
    csv_name = (
        f"movies_{Parameters.OPEN_START_DT.value}_{Parameters.OPEN_END_DT.value}.csv"
    )

    movies_df.to_csv(csv_name, index=False, encoding="utf-8-sig")
    print(f"데이터가 '{csv_name}'로 저장되었습니다.")


def main():
    movies = get_movies()
    save_movies2csv(movies)
    ray.shutdown()


if __name__ == "__main__":
    main()
