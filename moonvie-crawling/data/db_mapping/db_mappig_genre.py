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
genres_df = pd.read_csv(
    "C:\dev\github\SKN03-2nd-2Team\moonvie-crawling\data\genre\genres.csv"
)
# 장르 이름을 고유 코드로 매핑하기 위한 딕셔너리 생성
genre_mapping = pd.Series(
    genres_df["genre_id"].values, index=genres_df["대표 장르"]
).to_dict()

# CSV 파일 열기 및 데이터 읽기
with open(csv_file_path, mode="r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        movie_code = row["영화 코드"]
        genre = row["영화장르"]

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

        # 장르 이름을 고유 코드로 변환
        genre_code = genre_mapping.get(genre)

        if genre_code is None:
            print(f"'{genre_code}' not found in genre mapping.")
            continue  # 장르가 없으면 다음 행으로 넘어가기

        cursor.execute(
            "SELECT movie_genre_id FROM movie_genre WHERE genre_code = %s",
            (genre_code,),
        )
        genre_result = cursor.fetchone()

        if genre_result:
            movie_genre_id = genre_result[0]
        else:
            print(f"'{genre}' not found in movie_genre table.")
            continue

        # movie_info_genre 테이블에 데이터 삽입
        cursor.execute(
            "INSERT INTO movie_info_genre (movie_info_id, movie_genre_id) VALUES (%s, %s)",
            (movie_info_id, movie_genre_id),
        )

# 변경사항 커밋
db.commit()

# 연결 종료
cursor.close()
db.close()

print("Data successfully inserted.")
