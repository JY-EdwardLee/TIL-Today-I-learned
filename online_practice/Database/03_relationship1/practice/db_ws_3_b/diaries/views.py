from django.shortcuts import render, redirect
from .models import Diary, Comment
from .forms import DiaryForm, CommentForm

# Create your views here.
def index(request):
    diaries = Diary.objects.all()
    comments_form = CommentForm()
    context = {
        'diaries': diaries,
        'comments_form': comments_form,
    }
    return render(request, 'diaries/index.html', context)

def create(request):
    if request.method == 'POST':
        form = DiaryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('diaries:index')
    else:
        form = DiaryForm()
    context = {
        'form': form
    }
    return render(request, 'diaries/create.html', context)

def comments_create(request, diary_pk):
    comments_form = CommentForm(request.POST)
    diary = Diary.objects.get(pk=diary_pk)
    if comments_form.is_valid():
        comments = comments_form.save(commit=False)
        comments.diary = diary
        comments.save()
        return redirect('diaries:index')