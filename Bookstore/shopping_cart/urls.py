from django.urls import path
from django.conf.urls import url

from .views import (
    cart,
    add_to_cart,
    delete_from_cart,
    order_details,
    success
)

app_name = 'shopping_cart'

urlpatterns = [
    path('', cart, name='cart'),
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^order-summary/$', cart, name="order_summary"),
    url(r'^success/$', success, name='purchase_success'),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
]