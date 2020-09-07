# from django.conf.urls import url
from django.urls import path #, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('collections', views.collections, name='collections'),
    path('collections/<int:collection_id>', views.show_collection, name='show_collection'),
    path('contact', views.contact, name='contact'),
]