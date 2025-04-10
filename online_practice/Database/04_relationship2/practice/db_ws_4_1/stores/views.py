from django.shortcuts import render
from .models import Store
# Create your views here.
def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores
    }
    return render(request, 'stores/index.html', context)


def detail(request, store_id):
    store = Store.objects.get(id=store_id)
    context = {
        'store': store
    }
    return render(request, 'stores/detail.html', context)   