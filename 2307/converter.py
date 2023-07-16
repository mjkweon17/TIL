import csv
import json

# JSON 파일 읽기
with open('users.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)

users = data['users']

# CSV 파일 쓰기
with open('users.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)

    # 헤더 작성
    headers = users[0].keys()
    writer.writerow(headers)

    # 데이터 작성
    for user in users:
        writer.writerow(user.values())

print("CSV 파일이 생성되었습니다.")
