from django.urls import path
from . import views
from rest_framework import routers
# from cafe.views import PostViewSet

app_name = 'cafe'

# router = routers.DefaultRouter()
# # router.register(r'user', UserViewSet)
# router.register(r'post', PostViewSet)

# app 이름/table 이름/
# app 이름/table 이름/<int>/

# ex
# cafe/post/
# cafe/post/99/
# DRF는 상세 동작을 url이 아닌, 메소드로 표현


urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index),
    path('search/', views.search, name='cafe_search')
]