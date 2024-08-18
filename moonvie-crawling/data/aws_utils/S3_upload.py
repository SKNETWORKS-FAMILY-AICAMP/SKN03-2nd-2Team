import boto3

def upload_file_to_s3(local_file_path, bucket_name, s3_file_path):
    try:
        # S3 클라이언트 생성
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2"  # 버킷의 지역과 일치해야 함
        )
        
        # 파일 업로드
        s3.upload_file(
            Filename=local_file_path,
            Bucket=bucket_name,
            Key=s3_file_path
        )
        
        print("File uploaded successfully!")
    except Exception as e:
        print(f"Error: {e}")

# 실제 경로와 버킷 이름을 여기에 지정하세요
local_file_path = "./src/genre/movies_2017_2024.csv"  # 로컬 파일 경로
bucket_name = "moonvie-bucket"  # 정확한 버킷 이름 확인
s3_file_path = "moonvie-csv/movies_2017_2024.csv"  # S3 내 파일 경로

upload_file_to_s3(local_file_path, bucket_name, s3_file_path)
