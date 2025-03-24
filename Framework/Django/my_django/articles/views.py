from django.shortcuts import render

# Create your views here.
def index(request):    
    # 메인 페이지 응답 (request) = 약속 객체 반환
    return render(request, 'articles/index.html')
