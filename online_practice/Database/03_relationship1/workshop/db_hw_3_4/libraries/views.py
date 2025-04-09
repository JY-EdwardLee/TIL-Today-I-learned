from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import BookForm

# Create your views here.
def index(request):
    authors = Author.objects.all()
    context = {
        'authors': authors
    }
    return render(request, 'libraries/index.html', context)

def detail(request, author_pk):
    author = Author.objects.get(pk=author_pk)
    books = author.book_set.all
    books_form =  BookForm()
    context = {
        'author': author,
        'books': books,
        'books_form': books_form
    }
    return render(request, 'libraries/detail.html', context)

def books_create(request, author_pk):
    books_form = BookForm(request.POST)
    author = Author.objects.get(pk=author_pk)
    if books_form.is_valid():
        book = books_form.save(commit=False)
        book.author = author
        book.save()
        return redirect('libraries:detail', author_pk)