import requests
from datetime import datetime
from env.api_key import API_KEY
import csv
import os


# API 호출 함수
def fetch_movie_data(
    api_key: str,
    target_date: str,
    region: set,
    item_per_page="10",
    week_gb="0",
):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
    params = {
        "key": api_key,
        "targetDt": target_date,
        "itemPerPage": item_per_page,
        "weekGb": week_gb,
        "wideAreaCd": region[0],
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None


# 날짜를 주차별로 계산하는 함수
def get_week_start_date(year: str, week: str) -> str:
    d = datetime.strptime(f"{year}-W{int(week)}-1", "%Y-W%W-%w")
    return d.strftime("%Y%m%d")


# CSV로 저장하는 함수
def save_csv(data, csv_file: csv, region: str) -> None:
    csv_columns = [
        "박스오피스종류",
        "상영기간",
        "조회연도및주차",
        "순번",
        "박스오피스 순위",
        "전일대비 증감분",
        "신규진입여부",
        "영화대표코드",
        "제목",
        "개봉일",
        "해당일자 매출액",
        "해당일자 상영작 대비 해당영화 매출비율",
        "전일대비 매출액 증감분",
        "전일대비 매출액 증감비율",
        "누적 매출액",
        "해당일 관객수",
        "전일대비 관객수 증감분",
        "전일대비 관객수 증감비율",
        "누적 관객수",
        "해당일자 상영 스크린수",
        "해당일자 상영 횟수",
        "지역",
    ]

    file_exists = os.path.isfile(csv_file)

    try:
        with open(csv_file, "a", newline="", encoding="utf-8-sig") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not file_exists:
                writer.writeheader()
            result = data["boxOfficeResult"]
            boxofficeType = result["boxofficeType"]
            showRange = result["showRange"]
            yearWeekTime = result["yearWeekTime"]
            for movie in result["weeklyBoxOfficeList"]:
                writer.writerow(
                    {
                        "박스오피스종류": boxofficeType,
                        "상영기간": showRange,
                        "조회연도및주차": yearWeekTime,
                        "순번": movie["rnum"],
                        "박스오피스 순위": movie["rank"],
                        "전일대비 증감분": movie["rankInten"],
                        "신규진입여부": movie["rankOldAndNew"],
                        "영화대표코드": movie["movieCd"],
                        "제목": movie["movieNm"],
                        "개봉일": movie["openDt"],
                        "해당일자 매출액": movie["salesAmt"],
                        "해당일자 상영작 대비 해당영화 매출비율": movie["salesShare"],
                        "전일대비 매출액 증감분": movie["salesInten"],
                        "전일대비 매출액 증감비율": movie["salesChange"],
                        "누적 매출액": movie["salesAcc"],
                        "해당일 관객수": movie["audiCnt"],
                        "전일대비 관객수 증감분": movie["audiInten"],
                        "전일대비 관객수 증감비율": movie["audiChange"],
                        "누적 관객수": movie["audiAcc"],
                        "해당일자 상영 스크린수": movie["scrnCnt"],
                        "해당일자 상영 횟수": movie["showCnt"],
                        "지역": region,
                    }
                )
        print(f"{yearWeekTime}: Data successfully saved to {csv_file}")
    except IOError as e:
        print(f"Error saving to file: {e}")


def main():
    # API 키를 입력하세요
    api_key = API_KEY

    # 날짜 설정
    start_year = 2017
    end_year = 2024
    regions = [
        (None, "전국"),
        ("0105001", "서울시"),
        ("0105002", "경기도"),
        ("0105003", "강원도"),
        ("0105004", "충청북도"),
        ("0105005", "충청남도"),
        ("0105006", "경상북도"),
        ("0105007", "경상남도"),
        ("0105008", "전라북도"),
        ("0105009", "전라남도"),
        ("0105010", "제주도"),
        ("0105011", "부산시"),
        ("0105012", "대구시"),
        ("0105013", "대전시"),
        ("0105014", "울산시"),
        ("0105015", "인천시"),
        ("0105016", "광주시"),
        ("0105017", "세종시"),
    ]

    for region in regions:
        for year in range(start_year, end_year + 1):
            for week in range(1, 53):  # 1년은 52주차까지 존재
                target_date = get_week_start_date(year, week)

                try:
                    # 데이터 호출
                    movie_data = fetch_movie_data(api_key, target_date, region)

                    # 현재 경로에 CSV 파일을 생성
                    current_directory = os.getcwd()
                    csv_file = os.path.join(
                        current_directory, f"{region[1]}_WeeklyBoxOfficeData.csv"
                    )

                    # CSV 파일로 저장
                    if movie_data:
                        save_csv(movie_data, csv_file, region[1])
                    else:
                        print(f"No data for year {year}, week {week}")
                except KeyError:
                    print("#" * 20, "Next Region", "#" * 20)


if __name__ == "__main__":
    main()
