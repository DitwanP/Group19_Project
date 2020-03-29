from django.conf.urls import url

from .views import (
    add_to_cart,
    add_to_cart_from_saved,
    add_to_cart_from_detail,
    add_to_saved,
    add_to_saved_from_cart,
    add_to_saved_from_detail,
    delete_from_cart,
    delete_from_saved,
    order_details,
    checkout,
)

app_name = 'shopping_cart'

urlpatterns = [
    url(r'^add-to-cart/(?P<item_id>[-\w]+)/$', add_to_cart, name="add_to_cart"),
    url(r'^add-to-cart-from-saved/(?P<item_id>[-\w]+)/$', add_to_cart_from_saved, name="add_to_cart_from_saved"),
    url(r'^add-to-cart-from-detail/(?P<item_id>[-\w]+)/$', add_to_cart_from_detail, name="add_to_cart_from_detail"),
    url(r'^add-to-saved/(?P<item_id>[-\w]+)/$', add_to_saved, name="add_to_saved"),
    url(r'^add-to-saved_from_cart/(?P<item_id>[-\w]+)/$', add_to_saved_from_cart, name="add_to_saved_from_cart"),
    url(r'^add-to-saved_from_detail/(?P<item_id>[-\w]+)/$', add_to_saved_from_detail, name="add_to_saved_from_detail"),
    url(r'^order-summary/$', order_details, name="order_summary"),
    url(r'^item/delete/(?P<item_id>[-\w]+)/$', delete_from_cart, name='delete_item'),
    url(r'^item/delete_saved/(?P<item_id>[-\w]+)/$', delete_from_saved, name='delete_item_from_saved'),
    url(r'^checkout/$', checkout, name='checkout'),
]