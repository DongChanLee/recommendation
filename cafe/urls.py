from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('', views.index),
    path('search/', views.search, name='cafe_search')
]