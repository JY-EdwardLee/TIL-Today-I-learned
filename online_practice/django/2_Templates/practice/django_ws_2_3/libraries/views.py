from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os


# Create your views here.
def index(request):
    return render(request, 'index.html')

# call_api for recommending books
def call_api():
    # API_settings
    load_dotenv()

    API_URL = 'http://127.0.0.1:8000'
    API_KEY = os.getenv('API_KEY')
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
        books = []
        for item in data.get('item'):
            temp = {}
            temp['제목'] = item.get('title')
            temp['저자'] = item.get('author')
            books.append(temp)
    except requests.exceptions.RequestException as e:
        print(e)
    return books


def recommend(request):
    recoms = call_api()
    context = {
        'books': recoms
    }
    return render(request, 'recommend.html', context)