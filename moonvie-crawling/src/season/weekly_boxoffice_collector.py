import requests
from datetime import datetime
import csv
import os

# API 호출 함수
def fetch_movie_data(api_key, target_date, item_per_page='100', week_gb='1'):
    url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json"
    params = {
        'key': api_key,
        'targetDt': target_date,
        'itemPerPage': item_per_page,
        'weekGb': week_gb,
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

# 날짜를 주차별로 계산하는 함수
def get_week_start_date(year, week):
    d = datetime.strptime(f'{year}-W{int(week)}-1', "%Y-W%W-%w")
    return d.strftime('%Y%m%d')

# CSV로 저장하는 함수
def save_to_csv(data, csv_file):
    csv_columns = [
        'boxofficeType', 'showRange', 'yearWeekTime', 'rnum', 'rank', 'rankInten', 'rankOldAndNew', 'movieCd', 'movieNm', 'openDt',
        'salesAmt', 'salesShare', 'salesInten', 'salesChange', 'salesAcc',
        'audiCnt', 'audiInten', 'audiChange', 'audiAcc', 'scrnCnt', 'showCnt'
    ]
    
    file_exists = os.path.isfile(csv_file)

    try:
        with open(csv_file, 'a', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            if not file_exists:
                writer.writeheader()
            result = data["boxOfficeResult"]
            boxofficeType = result['boxofficeType']
            showRange = result['showRange']
            yearWeekTime = result['yearWeekTime']
            for movie in result['weeklyBoxOfficeList']:
                writer.writerow({
                    'boxofficeType': boxofficeType,
                    'showRange': showRange,
                    'yearWeekTime': yearWeekTime,
                    'rnum': movie['rnum'],
                    'rank': movie['rank'],
                    'rankInten': movie['rankInten'],
                    'rankOldAndNew': movie['rankOldAndNew'],
                    'movieCd': movie['movieCd'],
                    'movieNm': movie['movieNm'],
                    'openDt': movie['openDt'],
                    'salesAmt': movie['salesAmt'],
                    'salesShare': movie['salesShare'],
                    'salesInten': movie['salesInten'],
                    'salesChange': movie['salesChange'],
                    'salesAcc': movie['salesAcc'],
                    'audiCnt': movie['audiCnt'],
                    'audiInten': movie['audiInten'],
                    'audiChange': movie['audiChange'],
                    'audiAcc': movie['audiAcc'],
                    'scrnCnt': movie['scrnCnt'],
                    'showCnt': movie['showCnt'],
                })
        print(f"Data successfully saved to {csv_file}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def main():
    # API 키를 입력하세요
    api_key = "0f35de3c784f1ab75c7dce384c175c64"
    
    # 날짜 설정
    start_year = 2023
    end_year = 2023
    week_gb_options = ['0', '1', '2']  # 주간(0), 주말(1), 주중(2)

    # 추가적인 필터링 옵션 설정
    item_per_page = "100"  # 페이지 당 결과 수
    week_gb = "0"
    '''	주간/주말/주중을 선택 입력합니다
        “0” : 주간 (월~일)
        “1” : 주말 (금~일) (default)
        “2” : 주중 (월~목)
    '''
    # multi_movie_yn = ""  # 다양성 영화 여부 ("Y" or "N", default: 전체)
    # rep_nation_cd = ""  # 영화 국가 구분 ("K" for 한국영화, "F" for 외국영화, default: 전체)
    # wide_area_cd = ""  # 상영 지역 코드 (default: 전체)

    for year in range(start_year, end_year + 1):
        for week in range(1, 53):  # 1년은 52주차까지 존재
            target_date = get_week_start_date(year, week)
            
            for week_gb in week_gb_options:
                # 데이터 호출
                movie_data = fetch_movie_data(api_key, target_date, item_per_page, week_gb)
                
                # 현재 경로에 CSV 파일을 생성
                current_directory = os.getcwd() + '/weekly/'
                csv_file = os.path.join(current_directory, f"{week_gb}_WeeklyBoxOfficeData.csv")

                # CSV 파일로 저장
                if movie_data:
                    save_to_csv(movie_data, csv_file)
                else:
                    print(f"No data for year {year}, week {week}, weekGb {week_gb}")

if __name__ == "__main__":
    main()
