from django.conf.urls import url
from django.urls import path, include, re_path
from . import views

app_name = 'homepage'

urlpatterns = [
    url(r'^home/$', views.homepage_view, name = 'the_homepage'),
]