import requests
import pandas as pd
from env import settings

# API 키 및 URL 설정
api_key = settings.KOFIC_API_KEY
url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/company/searchCompanyList.json'

def company_data(api_key, url, current_page, max_pages):
    all_movie_list = []  # 모든 영화사 정보를 저장할 리스트
    
    while current_page <= max_pages:
        # 요청 파라미터 설정
        params = {
            "key": api_key,
            "curPage": str(current_page),  # 현재 페이지
            "itemPerPage": "100",  # 페이지당 항목 수 (최대 100개)
            "companyNm": "",  # 회사 이름 필터 (빈 문자열은 모든 회사 포함)
        }

        try:
            # API 요청
            response = requests.get(url, params=params)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 처리

            # 응답 상태 코드 출력
            print(f"응답 상태 코드: {response.status_code} for page {current_page}")

            # JSON 데이터 파싱
            data = response.json()
            company_list = data.get('companyListResult', {}).get('companyList', [])

            # 더 이상 데이터가 없으면 반복 종료
            if not company_list:
                print("더 이상 데이터가 없습니다.")
                break

            # 회사 정보를 리스트에 추가
            for company in company_list:
                company_cd = company.get('companyCd', '정보없음')
                company_nm = company.get('companyNm', '정보없음')
                print(f'영화사 코드: {company_cd}, 영화사명: {company_nm}')

                all_movie_list.append({
                    'companyCd': company_cd,
                    'companyNm': company_nm
                })

            # 다음 페이지로 이동
            current_page += 1

        except requests.RequestException as e:
            # 요청 중 오류가 발생한 경우 출력
            print(f'요청 중 오류 발생: {e}')
            break

    return all_movie_list

def save_to_csv(data, filename):
    # 데이터를 DataFrame으로 변환
    df = pd.DataFrame(data)
    # DataFrame을 CSV 파일로 저장
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"데이터가 {filename} 파일로 저장되었습니다.")

def main():
    current_page = 1  # 시작 페이지
    max_pages = 200  # 최대 페이지 수 설정
    # 영화사 데이터 가져오기
    all_movie_list = company_data(api_key, url, current_page, max_pages)
    # 데이터를 CSV 파일로 저장
    save_to_csv(all_movie_list, 'movie_company.csv')

if __name__ == "__main__":
    main()
