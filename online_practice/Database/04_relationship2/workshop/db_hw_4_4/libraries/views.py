from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Book, Review
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    reviews = book.review_set.all()
    form = ReviewForm()
    context = {
        'book': book,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def create_reviews(request, book_pk):
    book = Book.objects.get(pk=book_pk)
    if request.method == 'POST':
        reviewform = ReviewForm(request.POST)
        if reviewform.is_valid():
            review = reviewform.save(commit=False)
            review.user = request.user
            review.book = book
            review.save()
            return redirect('libraries:detail', book.pk)
    else:
        form = ReviewForm()
    context = {
        'form': form
    }
    return render(request, 'libraries/detail.html', context)

@login_required
def delete_reviews(request, book_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('libraries:detail', book_pk)