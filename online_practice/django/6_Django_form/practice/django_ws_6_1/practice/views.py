from django.shortcuts import render, redirect
from .forms import MemoForm
from .models import Memo

# Create your views here.
def index(request):
    memos = Memo.objects.all()
    context = {
        'memos': memos
    }
    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            memo = form.save()
        redirect('memos:detail', memo.pk)
    else:
        form = MemoForm()
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def detail(request, pk):
    memo = Memo.objects.get(pk = pk)
    context = {
        'memo': memo,
    }
    return render(request, 'detail.html', context)


def delete(request, pk):
    memo = Memo.objects.get(pk=pk)
    memo.delete()
    return redirect('memos:index')