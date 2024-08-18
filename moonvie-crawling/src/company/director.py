import pandas as pd
import os

# 파일 경로 설정
input_file_path = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company\movies_2017_2024_updated.csv"
output_directory = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company"

# CSV 파일 읽기
df = pd.read_csv(input_file_path, encoding='utf-8-sig')

# '감독' 열만 선택하고 중복 제거
director_df = df[['영화 감독 이름']].drop_duplicates().dropna()

# 빈 문자열 제거
director_df = director_df[director_df['영화 감독 이름'].str.strip() != '']

# 인덱스를 'director_id'로 설정
director_df = director_df.reset_index(drop=True)
director_df['director_id'] = director_df.index + 1

# 열 순서 변경
director_df = director_df[['director_id', '영화 감독 이름']]

# 결과를 새 파일로 저장
output_file_path = os.path.join(output_directory, 'directors_list.csv')
director_df.to_csv(output_file_path, index=False, encoding='utf-8-sig')

print(f"처리가 완료되었습니다. 결과가 {output_file_path}에 저장되었습니다.")
print(f"총 {len(director_df)} 명의 고유한 감독이 추출되었습니다.")