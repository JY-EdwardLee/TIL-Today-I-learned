from django.shortcuts import render, redirect
import random
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    context = {
        'name': 'napoie',
    }
    # 메인 페이지 응답 (request) = 약속 객체 반환
    return render(request, 'articles/index.html', context)


def digimon(request):
    partner_digimons = ['아구', '파피', '팔', '피요', '파닥', '쉬라', '텐타']
    partners = {
        '아구': '태일',
        '파피': '메튜',
    }
    picked = random.choice(partner_digimons)
    if picked not in ['아구', '파피']:
        partners[picked] = '조연'
    context = {
        'who': partner_digimons,
        'digimon': picked,
        'partner': partners[picked]
    }
    return render(request, 'articles/digimon.html', context)


def search(request):
    return render(request, 'articles/search.html')


def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    print(request)                      # <WSGIRequest: GET '/catch/?message=%E3%85%87%E3%85%87'>
    print(type(request))                # <class 'django.core.handlers.wsgi.WSGIRequest'>
    print(request.GET)                  # <QueryDict: {'message': ['ㅇㅇ']}>
    print(request.GET.get('message'))   # ㅇㅇ
    context = {}
    context['message'] = request.GET.get('message')
    return render(request, 'articles/catch.html', context)


# ORM wit view
# READ
def detail(request, pk):   # variable routing의 변수를 pk으로 받음 (request 다음)
    # 1. DB에 단일 게시글 요청
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)


def read_all(request):
    # 1. DB에 전체 게시글 요청
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/read.html', context)


# CREATE
## 1. new 함수 (create할 값을 입력할 페이지를 렌더링)
def new(request):
    form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


## 2. create 함수
def create_(request):
    # 1. 기본값
    # 사용자로부터 입력값 추출
    '''
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()
    return redirect('articles:detail', article.pk)  # POST는 redirect가 어울림
    '''
    # 2 ModelForm으로 create
    # request를 POST형식으로 받은 querydict를 articleform의 인자로 하여 form 함수에 선언
    form = ArticleForm(request.POST)
    if form.is_valid():     # 유효성 검사
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form, # 유효성 검사 실패 사유 담기
    }    
    return render(request, 'articles/create.html', context)


# 3. new + create 함수
def create(request):
    # 1. 요청 메서드가 POST라면
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # 꼭 키워드 인자 안해도 됨
        if form.is_valid():     # 유효성 검사
            article = form.save()
            return redirect('articles:detail', article.pk)
    # 2. 요청 메서드가 POST가 아니라면 (PUT, DELETE도 나올 수도 있음..)
    else:    
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def delete(request, pk):
    # 어떤 게시글을 지우는지 먼저 조회
    article = Article.objects.get(pk=pk)
    # DB에 삭제 요청
    article.delete()
    return redirect('articles:read')


def edit(request, pk):
    # 어떤 게시글 정보 가져올지 조회
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instane=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

def update_(request, pk):
    # 어떤 글을 수정할지 조회
    article = Article.objects.get(pk=pk)
    # Modelform을 썼을 때, 
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid(): # 유효성 검사
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
    # # POST로 받은 값을 기존 인스턴스에 오버라이드
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # # DB에 저장 요청
    # article.save()
    # return redirect('articles:detail', article.pk)  # POST는 redirect가 어울림


def update(request, pk):
    # 어떤 글을 수정할지 조회
    article = Article.objects.get(pk=pk)
    # Modelform을 썼을 때, 
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid(): # 유효성 검사
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)