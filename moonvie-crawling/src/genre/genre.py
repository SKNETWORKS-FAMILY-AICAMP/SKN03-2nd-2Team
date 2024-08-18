import pandas as pd
import os

# 파일 경로 설정
input_file_path = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company\movies_2017_2024_updated.csv"
output_directory = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company"

# CSV 파일 읽기
df = pd.read_csv(input_file_path, encoding='utf-8-sig')

# '대표장르' 열만 선택하고 빈 값 제거
genre_df = df[['대표 장르']].dropna().drop_duplicates().reset_index(drop=True)

# 빈 문자열 제거
genre_df = genre_df[genre_df['대표 장르'].str.strip() != '']

# 인덱스를 'genre_id'로 설정
genre_df['genre_id'] = genre_df.index + 1

# 열 순서 변경
genre_df = genre_df[['genre_id', '대표 장르']]

# 결과를 새 파일로 저장
output_file_path = os.path.join(output_directory, 'genres.csv')
genre_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print(f"처리가 완료되었습니다. 결과가 {output_file_path}에 저장되었습니다.")
print(f"총 {len(genre_df)} 개의 고유한 대표장르가 추출되었습니다.")