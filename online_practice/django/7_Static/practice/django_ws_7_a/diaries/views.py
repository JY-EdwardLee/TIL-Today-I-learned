from django.shortcuts import render, redirect
from .models import Diaries
from .forms import DiariesForm

# Create your views here.
def index(request):
    if request.method == 'GET':
        diaries = Diaries.objects.all()
        context = {
            'diaries': diaries
        }
        return render(request, 'diaries/index.html', context)


def create(request):
    if request.method == 'POST':
        form = DiariesForm(request.POST)
        if form.is_valid():
            diaries = form.save()
            return redirect('diaries:index')
    else:
        form = DiariesForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)