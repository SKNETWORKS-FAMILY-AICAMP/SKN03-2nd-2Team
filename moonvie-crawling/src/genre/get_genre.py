import pandas as pd
import os

def read_csv_file(file_path, encoding='utf-8-sig'):
    """CSV 파일을 읽어 데이터프레임을 반환합니다."""
    return pd.read_csv(file_path, encoding=encoding)

def process_genre_data(df):
    """'대표 장르' 열만 선택하고 빈 값 및 중복을 제거하여 처리된 데이터프레임을 반환합니다."""
    genre_df = df[['대표 장르']].dropna().drop_duplicates().reset_index(drop=True)
    genre_df = genre_df[genre_df['대표 장르'].str.strip() != '']
    genre_df['genre_id'] = genre_df.index + 1
    genre_df = genre_df[['genre_id', '대표 장르']]
    return genre_df

def save_to_csv(df, output_path, encoding='utf-8-sig'):
    """데이터프레임을 CSV 파일로 저장합니다."""
    df.to_csv(output_path, index=False, encoding=encoding)

def main(input_file_path, output_directory):
    """전체 프로세스를 수행하는 메인 함수입니다."""
    df = read_csv_file(input_file_path)
    genre_df = process_genre_data(df)
    output_file_path = os.path.join(output_directory, 'genres.csv')
    save_to_csv(genre_df, output_file_path)
    print(f"처리가 완료되었습니다. 결과가 {output_file_path}에 저장되었습니다.")
    print(f"총 {len(genre_df)} 개의 고유한 대표장르가 추출되었습니다.")

# 파일 경로와 디렉토리 설정
input_file_path = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company\movies_2017_2024_updated.csv"
output_directory = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company"

# 메인 함수 실행
main(input_file_path, output_directory)
