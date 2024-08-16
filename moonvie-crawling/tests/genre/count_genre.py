import pandas as pd
from constants import Path


def count_genre():
    # CSV 파일 읽기
    df = pd.read_csv(Path.FILTERED_CSV_FILE.value)

    # 장르별 영화 개수 세기
    genre_cnt = df["영화장르"].value_counts()

    return genre_cnt


def main():
    genre_cnt = count_genre()
    print(genre_cnt)


if __name__ == "__main__":
    main()
