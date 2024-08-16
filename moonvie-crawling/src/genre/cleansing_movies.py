import pandas as pd
from constants import Parameters, Path


def clean_file():
    # CSV 파일 읽기
    raw_movies_df = pd.read_csv(Path.CSV2CLEAN_FILE.value)
    box_movies_df = pd.read_csv(Path.CSV2COMPARE_FILE.value)

    # B.csv에서 영화명 칼럼만 추출하여 집합으로 변환 (중복 제거)
    box_movie_names = set(box_movies_df["제목"])

    # A.csv에서 영화명이 B.csv에 없는 행 제거
    filtered_df = raw_movies_df[raw_movies_df["영화명(국문)"].isin(box_movie_names)]

    column_filtered_df = filtered_df[Parameters.COLUMN_NAMES.value]
    column_filtered_df.rename(columns={"영화명(국문)": "영화명"}, inplace=True)
    # 변환된 CSV 파일 저장 (덮어쓰기)
    column_filtered_df.to_csv(
        Path.FILTERED_CSV_FILE.value, index=False, encoding="utf-8-sig"
    )


def main():
    clean_file()


if __name__ == "__main__":
    main()
