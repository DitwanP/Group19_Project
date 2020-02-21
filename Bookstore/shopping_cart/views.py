from django.shortcuts import render, get_object_or_404

def cart(request):
    return render(request, 'shopping_cart/cart.html')