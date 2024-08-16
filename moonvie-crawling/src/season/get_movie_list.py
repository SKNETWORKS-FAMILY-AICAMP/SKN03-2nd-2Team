import requests
import pandas as pd

# API 키와 요청 URL 설정
api_key = "b257d0a2d88b253e52ce02b6c8476bee"  # 여기에 발급받은 API 키를 입력하세요.
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"

# 영화 정보를 저장할 리스트 생성
all_movie_list = []

# 페이지 번호 초기화
current_page = 1
max_pages = 25  # 최대 페이지 수 설정

while current_page <= max_pages:
    # 요청 파라미터 설정
    params = {
        "key": api_key,
        "curPage": str(current_page),  # 현재 페이지
        "itemPerPage": "100",  # 결과 ROW의 개수 (최대 100개로 설정)
        "openStartDt": "2017",
        "openEndDt": "2017",
    }

    # API 요청
    response = requests.get(url, params=params)

    # 응답 상태 코드 출력
    print(f"응답 상태 코드: {response.status_code} for page {current_page}")

    # 응답 내용 처리
    if response.status_code == 200:
        try:
            data = response.json()

            # 데이터 가공
            movie_list_result = data.get("movieListResult", {})
            movie_list_items = movie_list_result.get("movieList", [])

            if not movie_list_items:
                print(
                    f"페이지 {current_page}에서 더 이상 데이터가 없습니다. 종료합니다."
                )
                break

            # 영화 정보를 저장
            for movie in movie_list_items:
                movie_info = {
                    "영화 코드": movie.get("movieCd", "정보 없음"),
                    "영화명(국문)": movie.get("movieNm", "정보 없음"),
                    "영화명(영문)": movie.get("movieNmEn", "정보 없음"),
                    "제작연도": movie.get("prdtYear", "정보 없음"),
                    "개봉일": movie.get("openDt", "정보 없음"),
                    "영화유형": movie.get("typeNm", "정보 없음"),
                    "제작상태": movie.get("prdtStatNm", "정보 없음"), #제작상태에서 개봉된 영화면 불러오는 로직 작성 필요
                    "제작국가": movie.get("nationAlt", "정보 없음"),
                    "영화장르": movie.get("genreAlt", "정보 없음"),
                    "대표 제작국가": movie.get("repNationNm", "정보 없음"),
                    "대표 장르": movie.get("repGenreNm", "정보 없음"),
                    # 감독 정보 추출
                    "영화 감독 이름": [
                        director.get("peopleNm", "정보 없음")
                        for director in movie.get("directors", [])
                    ],
                    # 제작사 정보 추출
                    "제작사 코드": [
                        company.get("companyCd", "정보 없음")
                        for company in movie.get("companys", [])
                    ],
                }
                
                all_movie_list.append(movie_info)

            # 페이지 번호 증가
            current_page += 1

        except ValueError as e:
            print(f"JSON 디코딩 오류: {e}")
            break
    else:
        print(f"API 요청 실패: {response.status_code}")
        break

# 데이터프레임 생성
df = pd.DataFrame(all_movie_list)

# CSV 파일로 저장
csv_file = "movies_2017_pages_1_to_20.csv"
df.to_csv(csv_file, index=False, encoding="utf-8-sig")
print(f"데이터가 '{csv_file}'로 저장되었습니다.")
