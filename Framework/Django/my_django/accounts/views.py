from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:read')
    else:
        form = AuthenticationForm() # form instance 만들기
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        # 회원가입 템플릿 + 회원정보 작성을 위한 form을 응답
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def delete(request):
    # 이미 로그인 된 상태이기 때문에 굳이 유저 조회를 할 필요가 없다.
    # (원래 삭제할 때는 조회 먼저하는게 국룰이었지만...)
    request.user.delete()   # request 안에 유저 정보 들어있음
    return redirect('accounts:login')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) # POST 받은 값, request 유저 정보
        if form.is_valid():
            form.save()
            return redirect('articles:read')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request, user_pk):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) # 세션 갱신 함수
            return redirect('articles:read')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/change_password.html', context)