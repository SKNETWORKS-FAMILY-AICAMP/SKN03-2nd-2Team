import csv
import pymysql
import pandas as pd

# MySQL 연결 설정
db = pymysql.connect(
    host="moonvie-database.ctimca2y05aw.ap-northeast-2.rds.amazonaws.com",  # MySQL 서버 주소
    user="admin",  # MySQL 사용자명
    password="1234qwer",  # MySQL 비밀번호
    database="moonvieDB",  # 사용할 데이터베이스 이름
)

cursor = db.cursor()

# CSV 파일 경로
csv_file_path = "C:\dev\github\SKN03-2nd-2Team\moonvie-crawling\data\genre\movies_separated_genres.csv"
companies_df = pd.read_csv(
    "C:\dev\github\SKN03-2nd-2Team\moonvie-crawling\data\company\movie_company.csv"
)

# CSV 파일 열기 및 데이터 읽기
with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movie_code = row["영화 코드"]
        companies_code = row["제작사 코드"].split(",")

        # 영화 코드 가져오기
        cursor.execute(
            "SELECT movie_info_id FROM movie_info WHERE movie_code = %s", (movie_code,)
        )
        movie_info_result = cursor.fetchone()

        if movie_info_result:
            movie_info_id = movie_info_result[0]
        else:
            print(f"Movie '{movie_code}' not found in movie_info table.")
            continue  # 영화가 없으면 다음 행으로 넘어가기

        # 각 제작사 코드에 대해 반복
        for company_code in companies_code:
            company_code = company_code.strip()  # 공백 제거
            if company_code is None:
                print(f"'{company_code}' not found in company mapping.")
                continue  # 제작사가 없으면 다음 행으로 넘어가기

            cursor.execute(
                "SELECT production_id FROM production WHERE production_code = %s",
                (company_code,),
            )
            company_result = cursor.fetchone()

            if company_result:
                production_id = company_result[0]
            else:
                print(f"'{company_code}' not found in production table.")
                continue

            # 중복 여부 확인
            cursor.execute(
                "SELECT * FROM movie_info_production WHERE movie_info_id = %s AND production_id = %s",
                (movie_info_id, production_id),
            )
            existing_entry = cursor.fetchone()

            if existing_entry:
                print(
                    f"Entry for (movie_info_id: {movie_info_id}, production_id: {production_id}) already exists."
                )
            else:
                # movie_info_production 테이블에 데이터 삽입
                cursor.execute(
                    "INSERT INTO movie_info_production (movie_info_id, production_id) VALUES (%s, %s)",
                    (movie_info_id, production_id),
                )

# 변경사항 커밋
db.commit()

# 연결 종료
cursor.close()
db.close()

print("Data successfully inserted.")
