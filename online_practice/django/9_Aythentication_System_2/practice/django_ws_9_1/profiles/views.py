from django.shortcuts import render
from .models import User

# Create your views here.
def index(request):
    profiles = User.objects.all()
    context = {
        'profiles': profiles
    }
    return render(request, 'profiles/index.html', context)