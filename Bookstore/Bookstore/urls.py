"""Bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
   https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
   1. Add an import:  from my_app import views
   2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
   1. Add an import:  from other_app.views import Home
   2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
   1. Import the include() function: from django.urls import include, path
   2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from book_details import views
from . import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', include('book_browsing.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'cart/', include('shopping_cart.urls', namespace='shopping_cart')),
    url(r'^products/', include('products.urls', namespace='products')),
    url('profiles/', include('profile_management.urls', namespace='profile_management')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^author/(\d+)/$', views.bookAuthorsView.as_view(), name='book_author'),
    path('book/<int:pk>', views.bookDetailsView.as_view(), name='book'),
    path('author/<int:pk>', views.bookAuthorsView.as_view(), name='book-author'),
    url(r'^book/(?P<pk>\d+)/$', views.bookDetailsView.as_view(), name='book_details')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
