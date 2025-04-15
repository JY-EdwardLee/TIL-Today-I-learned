from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    """
    M:N 관계 설정 시 그냥 복수형으로 이름을 짓는 것 보다,
    지금 우리가 만드는 기능이 무엇인지 생각해보고 명시적인 Manager이름을 설정하는 것이 좋다.

    게시글1.users.all() => 게시글1.like_users.all()

    Article과 User는 N:1관계 N:M 관계 두번의 관계가 맺어져 있다.
    이 때에 article 쪽에 user를 manytomany 관계를 맺게 되면
    user.article_set 매니저명이 겹치는 문제가 발생생
    """
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

