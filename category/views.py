from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

# Create your views here.

def home_page(request):
    categories = Category.objects.all()
    print(categories)
    return render(request, 'homepage.html', {'categories':categories})
    
