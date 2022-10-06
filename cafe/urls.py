from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    path('', views.cafe_list),
    path('<int:cafe_id>', views.cafe_detail),

    # path('', views.index),
    # path('search/', views.search, name='cafe_search')
]