from django.shortcuts import render, redirect
from .models import Restaurant, Menu, Category
from .forms import RestaurantForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context ={
        'restaurants': restaurants,
    }
    return render(request, 'restaurants/index.html', context)


def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurants:index')
    else:
        forms = RestaurantForm()
    context = {
        'forms': forms
    }
    return render(request, 'restaurants/create.html', context)


def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    context = {
        'restaurant': restaurant
    }
    return render(request, 'restaurants/detail.html', context)