from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'book_browsing'

urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('book/', views.book, name='book'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('order/', views.order, name='order'),
    path('new-book/', views.newBook, name='new-book'),
    path('search/', views.search, name='search'),
    path('fantasy/', views.fantasy, name='fantasy'),
    path('romance/', views.romance, name='romance'),
    path('fiction/', views.fiction, name='fiction'),
    path('history/', views.history, name='history'),
    path('thriller/', views.thriller, name='thriller'),
    path('new-release/', views.newRelease, name='new-release'),
    path('top-sellers/', views.topSeller, name='top-sellers'),
    path('filter-data/', views.filterData, name='filter-data'),
    path('filter-released-data/', views.filterReleasedData, name='filter-released-data'),
    path('get-book-details/', views.getBookDetailsById, name='get-book-details'),
    path('ajax-submit/', views.ajaxSubmit, name='ajax-submit')
]