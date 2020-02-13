from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def cart(request):
    return HttpResponse('<h1>Bookstore Shopping Cart</h1>')