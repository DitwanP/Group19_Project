from django.shortcuts import render, get_object_or_404

from .models import Cart_item

def cart(request):

    items = Cart_item.objects.all()

    return render(request, 'shopping_cart/cart.html', {'items' : items})