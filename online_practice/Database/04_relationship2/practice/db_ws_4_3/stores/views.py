from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm

# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)

def detail(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    form = ProductForm()
    products = store.product_set.all()
    context = {
        'store': store,
        'form': form,
        'products': products,
    }
    return render(request, 'stores/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form
    }
    return render(request, 'stores/create.html', context)

def create_products(request, store_pk):
    store = Store.objects.get(pk=store_pk)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = store.user
            product.store = store
            product.save()
            return redirect('stores:detail', store.pk)
    else:
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, 'stores/detail.html', context)