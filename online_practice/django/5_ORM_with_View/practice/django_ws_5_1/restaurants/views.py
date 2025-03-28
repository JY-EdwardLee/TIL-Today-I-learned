from django.shortcuts import render, redirect
from .models import Restaurant

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context ={
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)


def new(request):
    return render(request, 'restaurants/new.html')


def create(request):
    restaurant = Restaurant()    
    restaurant.title = request.POST.get('title')
    restaurant.call = request.POST.get('call')
    restaurant.address = request.POST.get('address')
    restaurant.describtion = request.POST.get('describtion')
    restaurant.save()
    return redirect('restaurants:index')