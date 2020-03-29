from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'book_browsing'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^account/$', views.account, name='account'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.login, name='login'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('sales-off/', views.salesOff, name='sales-off'),
    path('blog-details/', views.blogDetails, name='blog-details'),
    path('order/', views.order, name='order'),
    path('new-book/', views.newBook, name='new-book'),
    path('cart/', views.cart, name='cart'),
    path('search/', views.search, name='search')
]
