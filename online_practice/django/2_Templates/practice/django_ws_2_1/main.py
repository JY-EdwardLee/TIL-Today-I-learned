import requests
from dotenv import load_dotenv
import os
import pprint

load_dotenv()

API_URL = 'http://127.0.0.1:8000'
API_KEY = os.getenv('API_KEY')

def call_api():
    url = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'SearchTarget': 'Book',
        'Output': 'JS',
        'start': 1,
        'MaxResults': 50,
        'Version': 20131101,
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        # 책 제목, 저자, 출간일, 국제 표준 도서 번호 (ISBN)
        result = []
        for item in data.get('item'):
            temp = {}
            temp['국제 표준 도서 번호'] = item.get('isbn')
            temp['저자'] = item.get('author')
            temp['제목'] = item.get('title')
            temp['출간일'] = item.get('pubDate')
            result.append(temp)
        pprint.pprint(result)
    except requests.exceptions.RequestException as e:
        print(e)


if __name__ == "__main__":
    call_api()