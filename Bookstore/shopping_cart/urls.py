from django import views
from django.conf.urls import url
from django.urls import path

from .views import (
    add_to_cart,
    add_to_cart_from_saved,
    add_to_cart_from_detail,
    increase_item_quantity,
    decrease_item_quantity,
    add_to_saved,
    add_to_saved_from_cart,
    delete_from_cart,
    delete_from_saved,
    order_details,
    checkout,
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^add-to-cart-from-saved/(?P<item_id>[-\w]+)/$', add_to_cart_from_saved, name="add_to_cart_from_saved"),
    url(r'^add-to-cart-from-detail/(?P<item_id>[-\w]+)$', add_to_cart_from_detail, name="add_to_cart_from_detail"),
    url(r'^increase_item_quantity/(?P<item_id>[-\w]+)/$', increase_item_quantity, name="increase_item_quantity"),
    url(r'^decrease_item_quantity/(?P<item_id>[-\w]+)/$', decrease_item_quantity, name="decrease_item_quantity"),
    url(r'^add-to-saved/(?P<item_id>[-\w]+)/$', add_to_saved, name="add_to_saved"),
    url(r'^add-to-saved_from_cart/(?P<item_id>[-\w]+)/$', add_to_saved_from_cart, name="add_to_saved_from_cart"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^item/delete_saved/(?P<item_id>[-\w]+)/$', delete_from_saved, name='delete_item_from_saved'),
    url(r'^checkout/$', checkout, name='checkout'),
]