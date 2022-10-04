from django.db import models
from django.urls import reverse

class Original(models.Model):
    '''
    카페 정보 원본 테이블
    '''
    id = models.IntegerField(primary_key=True)
    place_name = models.TextField()
    address_name = models.TextField()
    road_address_name = models.TextField()
    phone = models.CharField(max_length=20)
    category_group_name = models.CharField(max_length=10)
    category_name = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place_name