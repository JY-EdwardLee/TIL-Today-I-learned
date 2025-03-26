from django.shortcuts import render
import requests
from dotenv import load_dotenv
import os


load_dotenv()

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = os.getenv('API_KEY')

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],
        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)


def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        try:
            info = {
                'isbn': item['isbn'],
                'title': item['title'],
                'pubDate': item['pubDate'],
                'author': item['author'],
                'salesPoint': item['salesPoint'],
                'bestDuration': item['bestDuration']
            }
        except KeyError:
            info = {
                'isbn': item['isbn'],
                'title': item['title'],
                'pubDate': item['pubDate'],
                'author': item['author'],
                'salesPoint': item['salesPoint'],
                'bestDuration': item['bestRank']
            }
        result.append(info)
    result.sort(key=lambda x: x['salesPoint'])
    context = {
        'result': result,
    }
    return render(request, 'bestseller.html', context)