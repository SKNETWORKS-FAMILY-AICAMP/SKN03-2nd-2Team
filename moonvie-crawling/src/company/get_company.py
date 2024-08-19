import pandas as pd
import os

def read_csv_file(file_path, encoding='utf-8'):
    """CSV 파일을 읽어 데이터프레임을 반환합니다."""
    return pd.read_csv(file_path, encoding=encoding)

def split_code(code):
    """코드에서 쉼표와 공백을 제거하고 8자리씩 나누어 리스트로 반환합니다."""
    code = code.replace(',', '').replace(' ', '')
    return [code[i:i+8] for i in range(0, len(code), 8) if code[i:i+8].strip() != '']

def process_data(df):
    """데이터프레임을 처리하여 새로운 데이터프레임을 반환합니다."""
    new_rows = []

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

    return pd.DataFrame(new_rows)

def save_to_csv(df, output_path, encoding='utf-8-sig'):
    """데이터프레임을 CSV 파일로 저장합니다."""
    df.to_csv(output_path, index=False, encoding=encoding)

def main(file_path):
    """전체 프로세스를 수행하는 메인 함수입니다."""
    # CSV 파일 읽기
    df = read_csv_file(file_path)

    # 데이터 처리
    new_df = process_data(df)

    # 결과를 새 파일로 저장
    output_path = os.path.join(os.path.dirname(file_path), 'movies_2017_2024_updated.csv')
    save_to_csv(new_df, output_path)

    print(f"처리가 완료되었습니다. 결과가 {output_path}에 저장되었습니다.")

# 파일 경로 설정
file_path = r"C:\dev\SKN03-2nd-2Team\moonvie-crawling\data\company\movies_2017_2024.csv"

# 메인 함수 실행
if __name__ == "__main__":
    main(file_path)
