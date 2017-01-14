from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'homepage.html', {'categories':categories})

def products(request, category_id):
    category = Category.objects.get(pk=category_id)
    return render(request, 'products.html', {'category': category})

    
