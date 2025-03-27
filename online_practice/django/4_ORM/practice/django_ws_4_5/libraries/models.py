from django.db import models
import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

API_URL = 'http://127.0.0.1:8000'
API_KEY = os.getenv('API_KEY')

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    category_name = models.TextField()
    category_id = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()

    @classmethod
    def insert_data(cls):
        params = {
            'ttbkey': API_KEY,
            'QueryType': 'ItemNewAll',
            'SearchTarget': 'Book',
            'Output': 'JS',
            'start': 1,
            'MaxResults': 10,
            'Version': 20131101,
        }
        response = requests.get("http://www.aladin.co.kr/ttb/api/ItemList.aspx/", params=params)
        data = response.json()
        print(data.get('item')[0].keys())
        for item in data.get('item'):
            book = cls(isbn = item['isbn'],
                        author = item['author'],
                        title = item['title'],
                        category_name = item['categoryName'],
                        category_id = item['categoryId'],
                        price = item['priceSales'],
                        fixed_price = item['fixedPrice'],
                        pub_date = item['pubDate'])
            book.save()