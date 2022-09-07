import json
import urllib.request
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

def index(request):
    return HttpResponse("안녕하세요 cafe 추천시스템에 오신것을 환영합니다.")

@api_view(['GET'])
def search(request):
    '''
    curl -X GET "https://dapi.kakao.com/v2/local/search/keyword.json?page=1&size=15&sort=accuracy&query=%EA%B0%95%EB%82%A8%EA%B5%AC+%EC%B9%B4%ED%8E%98&category_group_code=CE7" \
	-H "Authorization: KakaoAK {REST_API_KEY}"
    
    '''
    url = ''
    rest_api_key = 'bee1015770eee9e6100f8661def9a7d0'

    #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
