import pandas as pd
import os

# 파일 경로 설정
file_path = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company\movies_2017_2024.csv"

# CSV 파일 읽기 (인코딩은 파일에 맞게 조정하세요)
df = pd.read_csv(file_path, encoding='utf-8')

# 새로운 데이터프레임 생성
new_rows = []

def split_code(code):
    # 코드에서 쉼표와 공백 제거
    code = code.replace(',', '').replace(' ', '')
    # 8자리씩 나누기
    return [code[i:i+8] for i in range(0, len(code), 8) if code[i:i+8].strip() != '']

# 각 행을 순회하면서 처리
for index, row in df.iterrows():
    company_codes = split_code(str(row['제작사 코드']))
    
    if company_codes:
        # 유효한 코드가 있는 경우
        for code in company_codes:
            new_row = row.copy()
            new_row['제작사 코드'] = code
            new_rows.append(new_row)
    else:
        # 유효한 코드가 없는 경우, 해당 열을 비우기
        new_row = row.copy()
        new_row['제작사 코드'] = None  # 빈 값을 설정, 해당 셀은 빈 칸으로 표시됨
        new_rows.append(new_row)

# 새로운 데이터프레임 생성
new_df = pd.DataFrame(new_rows)

# 결과를 새 파일로 저장
output_path = os.path.join(os.path.dirname(file_path), 'movies_2017_2024_updated.csv')
new_df.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"처리가 완료되었습니다. 결과가 {output_path}에 저장되었습니다.")
