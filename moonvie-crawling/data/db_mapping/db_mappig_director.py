import csv
import pymysql
import pandas as pd

# MySQL 연결 설정
db = pymysql.connect(
    host="",  # MySQL 서버 주소
    user="",  # MySQL 사용자명
    password="",  # MySQL 비밀번호
    database="",  # 사용할 데이터베이스 이름
)

cursor = db.cursor()

# CSV 파일 경로
csv_file_path = "C:\dev\github\SKN03-2nd-2Team\moonvie-crawling\data\genre\movies_separated_genres.csv"
directors_df = pd.read_csv(
    "C:\dev\github\SKN03-2nd-2Team\moonvie-crawling\data\company\directors_list.csv"
)

# CSV 파일 열기 및 데이터 읽기
with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movie_code = row["영화 코드"]
        director = row["영화 감독 이름"]

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

        if director is None:
            print(f"'{director}' not found in director mapping.")
            continue  # 장르가 없으면 다음 행으로 넘어가기

        cursor.execute(
            "SELECT director_id FROM director WHERE director_name = %s",
            (director,),
        )
        director_result = cursor.fetchone()

        if director_result:
            director_id = director_result[0]
        else:
            print(f"'{director}' not found in director table.")
            continue

        # 중복 여부 확인
        cursor.execute(
            "SELECT * FROM movie_info_director WHERE movie_info_id = %s AND director_id = %s",
            (movie_info_id, director_id),
        )
        existing_entry = cursor.fetchone()

        if existing_entry:
            print(
                f"Entry for (movie_info_id: {movie_info_id}, director_id: {director_id}) already exists."
            )
        else:
            # movie_info_director 테이블에 데이터 삽입
            cursor.execute(
                "INSERT INTO movie_info_director (movie_info_id, director_id) VALUES (%s, %s)",
                (movie_info_id, director_id),
            )

# 변경사항 커밋
db.commit()

# 연결 종료
cursor.close()
db.close()

print("Data successfully inserted.")
