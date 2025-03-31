from django.db import models
from django import forms

# Create your models here.

# 게시글이 저장될 테이블 설계 클래스
class Article(models.Model): # Model이라는 부모 클래스가 이미 작성되어 있고 상속 받는다
	# 필드(열) 이름 = models.데이터의 유형(제약조건)
	title = models.CharField(max_length=10) # 제목
	content = models.TextField() # 내용
	created_at = models.DateTimeField(auto_now_add=True) # auto_now_add 데이터가 첨 생성
	updated_at = models.DateTimeField(auto_now=True) # auto_now 데이터가 저장될 때마다

