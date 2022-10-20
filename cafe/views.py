import json
from urllib import response
import urllib.request
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
# from rest_framework.renderers import JSONRenderer
from .serializers import *
from .models import Original

'''
View 호출에 대한 리턴값: 필수적으로 HttpResponse 객체를 리턴해야 한다.
'''

def index(request):
    cafe_list = Original.objects.all()
    context = {'cafe_list': cafe_list}
    return render(request, 'cafe/cafe_list.html', context)
    # return HttpResponse("안녕하세요 추천시스템에 오신것을 환영합니다.")

@api_view(['GET'])
# @renderer_classes([JSONRenderer])
def cafe_list(request):
    ''' 
    전체 카페 정보 조회
    '''
    cafes = Original.objects.all()
    serializers = OriginalSerializer(cafes, many=True)

    return Response({'status': 'success', 'data': serializers.data}, status=status.HTTP_200_OK)
    #return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def cafe_detail(request, cafe_id):
    '''
    특정 카페 정보 조회
    '''
    cafe = get_object_or_404(Original, id=cafe_id)
    serializers = OriginalSerializer(cafe)
    return Response({'status': 'success', 'data': serializers.data}, status=status.HTTP_200_OK)