import requests
'''
전체 유저 데이터 수집 후 이름만 내뱉기
'''
# 무작위 유저 정보 요청 경로
API_URL = 'https://jsonplaceholder.typicode.com/users'
# API 요청
response = requests.get(API_URL)
# JSON -> dict 데이터 변환
parsed_data = response.json()

# print(parsed_data)

dummy_data = []

for i in range(len(parsed_data)):
    dummy_data.append(parsed_data[i]['name'])

print(dummy_data)
'''
유저 데이터 하나씩 호출 후 이름 내뱉기
'''

dummy_data = []

for i in range(1,11):
    API_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(API_URL)
    parsed_data = response.json()
    name = parsed_data["name"]
    dummy_data.append(name)

print(dummy_data)