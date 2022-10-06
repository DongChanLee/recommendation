"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/cafe/', include('cafe.urls'))
]


schema_view = get_schema_view(
    openapi.Info(
        title = '추천시스템 API',
        default_version = 'v1',
        description = '추천시스템 기능 관리를 위한 API 문서 \n 개발자: KT 이동찬',
        terms_of_service = 'https://www.google.com/policies/terms/',
        contact = openapi.Contact(name='Dongchan Lee', email='evanlee0407@gmail.com'),
        license = openapi.License(name='Recommendation System API')
    ),
    public = True,
    permission_classes = (permissions.AllowAny,),
    patterns = urlpatterns,
)

urlpatterns += [
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]