from django.contrib import admin
from .models import creditCards
from .models import shippingAddress
from .models import Profile

admin.site.register(Profile)
admin.site.register(shippingAddress)
admin.site.register(creditCards)