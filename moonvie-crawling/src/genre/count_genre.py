import pandas as pd


# csv파일에서 데이터를 읽어와서 장르별 영화 개수를 세는 함수를 작성하세요.
def count_genre():
    # CSV 파일 읽기
    df = pd.read_csv("movies2017_to_2024.csv")

    # 장르별 영화 개수 세기
    genre_count = df["대표 장르"].value_counts()

    return genre_count


def main():
    genre_count = count_genre()
    print(genre_count)


if __name__ == "__main__":
    main()
