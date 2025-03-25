from django.shortcuts import render

# Create your views here.

def introduce_view(request, username):
    context = {
        'user': username
    }
    return render(request, 'my_app/introduce.html', context)