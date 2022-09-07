from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('search/', view.search, name='cafe_search')
]