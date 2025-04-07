from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('profiles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('profiles:index')

def signup(request):
    if request.method == 'POST':
        forms = CustomUserCreationForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('profiles:index')
    else:
        forms = CustomUserCreationForm()
    context = {
        'forms': forms,
    }
    return render(request, 'accounts/signup.html', context)

def update(request):
    if request.method == 'POST':
        forms = CustomUserChangeForm(request.POST, instance=request.user)
        if forms.is_valid():
            forms.save()
            return redirect('profiles:index')
    else:
        forms = CustomUserChangeForm(instance=request.user)
    context= {
        'forms': forms
    }
    return render(request, 'accounts/update.html', context)