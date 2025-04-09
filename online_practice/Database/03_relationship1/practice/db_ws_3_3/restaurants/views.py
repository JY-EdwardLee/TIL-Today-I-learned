from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm, MenuForm

# Create your views here.
def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants': restaurants
    }
    return render(request, 'restaurants/index.html', context)

def create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save()
            return redirect('restaurants:detail', restaurant.pk)
    else:
        form = RestaurantForm()
    context = {
        'form': form
    }
    return render(request, 'restaurants/create.html', context)

def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    menus = restaurant.menu_set.all()
    menus_form = MenuForm()
    context = {
        'restaurant': restaurant,
        'menus_form': menus_form,
        'menus': menus,
    }
    return render(request, 'restaurants/detail.html', context)

def menus_create(request, restaurant_pk):
    menus_form = MenuForm(request.POST)
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    if menus_form.is_valid():
        menu = menus_form.save(commit=False)
        menu.restaurant = restaurant
        menu.save()
        return redirect('restaurants:detail', restaurant_pk)
    
