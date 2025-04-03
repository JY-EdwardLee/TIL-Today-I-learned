from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User

# Create your views here.
def index(request):
    persons = User.objects.all().order_by('-score')
    context = {
        'persons': persons
    }
    return render(request, 'accounts/index.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


def score(request, person_pk):
    account = User.objects.get(pk=person_pk)
    if request.method == 'POST':    
        account.score += 100
        account.save()
        return redirect('accounts:index')
    else:
        context = {
            'account':account
        }
        return render(request, 'accounts/index.html', context)