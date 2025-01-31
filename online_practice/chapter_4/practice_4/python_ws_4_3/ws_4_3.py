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
type(parsed_data)
# print(parsed_data)

dummy_data = []
name_data = ['name']
geo_data = ['lat', 'lng']

for i in range(len(parsed_data)):
    geo_info = {}
    for data in geo_data:
        user_data = parsed_data[i]["address"]["geo"][data]
        geo_info[str(data)] = user_data
    if -80 < float(geo_info['lat']) < 80 and -80 < float(geo_info['lng']) < 80:
        user_info = {}
        user_name = parsed_data[i]["name"]
        company_name = parsed_data[i]["company"]["name"]
        user_info["company_name"] = company_name        
        user_info['lat'] = geo_info['lat']
        user_info['lng'] = geo_info['lng']
        user_info["name"] = user_name
        dummy_data.append(user_info)
    
print(*dummy_data, sep='\n')
