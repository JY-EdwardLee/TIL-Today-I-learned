from rest_framework import serializers
from .models import Article


# 전체 게시글 데이터를 직렬화하는 클래스
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "title", "content",)


# 단일 게시글 전체 필드를 직렬화하는 클래스
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"