from django.shortcuts import render
import random

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


def detail(request, num):   # variable routing의 변수를 num으로 받음 (request 다음)
    context = {
        'num': num
    }
    return render(request, 'articles/detail.html', context)