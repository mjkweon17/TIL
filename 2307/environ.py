import os

# 'API_KEY' 환경 변수가 설정되었는지 또는 비어있는지 확인
if os.environ.get('API_KEY') is None:
    print("API_KEY가 설정되지 않았습니다.")
else:
    # 'API_KEY' 환경 변수의 값을 가져오기
    api_key = os.environ['API_KEY']
    print("API_KEY:", api_key)