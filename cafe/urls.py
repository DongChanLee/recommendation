from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    # path('', views.index),
    path('', views.cafe_list),
    # path('list', views.cafe_list),
    path('<int:cafe_id>', views.cafe_detail),
    # path('search/', views.search, name='cafe_search')
]