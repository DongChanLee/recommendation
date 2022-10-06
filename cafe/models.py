from email import message
from django.db import models
from django.urls import reverse

class Original(models.Model):
    '''
    카페 정보 원본 테이블
    '''
    id = models.IntegerField(primary_key=True)
    place_area = models.CharField(max_length=10)
    place_name = models.TextField(verbose_name='상호명')
    address_name = models.TextField(verbose_name='지번 주소')
    road_address_name = models.TextField(verbose_name='도로명 주소')
    phone = models.CharField(max_length=20, verbose_name='전화번호')
    category_group_name = models.CharField(max_length=20)
    category_name = models.TextField(blank=True)
    place_url = models.URLField(max_length=200, verbose_name='위치정보 URL')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True, verbose_name='최종 수정 날짜')

    def __str__(self):
        return self.place_name
    
    # def placename_length(self):
    #     return len(self.place_name)
    # placename_length.short_description = '장소 글자수'

    class Meta:
        managed = True
        verbose_name = '카페 정보'
        verbose_name_plural = '카페 목록'
        # db_table = 'Cafe_Original'

    