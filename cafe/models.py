from django.db import models
from django.urls import reverse

class Cafe(models.Model):
    '''
    카페 정보 테이블
    '''
    id = models.IntegerField(primary_key=True)
    place_name = models.TextField(null=False)
    address_name = models.TextField(null=True)
    road_address_name = models.TextField(null=True)
    phone = models.TextField(null=True)
    category_group_name = models.TextField(null=True)
    category_name = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place_name