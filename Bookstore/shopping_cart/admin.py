from django.contrib import admin

from .models import OrderItem, Order, SaveItem, Saved, Transaction

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(SaveItem)
admin.site.register(Saved)
admin.site.register(Transaction)
