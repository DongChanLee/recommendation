from django.db import models
from django.urls import reverse

# s(settings.py) - M(models.py) - U(urls.py) - V(views.py) - T(templates)

class Original(models.Model):
    '''
    카페 정보 테이블
    '''
    id = models.IntegerField(primary_key=True)
    place_name = models.TextField()
    address_name = models.TextField()
    road_address_name = models.TextField()
    phone = models.CharField(max_length=13)
    category_group_name = models.CharField(max_length=15)
    category_name = models.CharField(max_length=50)
    place_url = models.URLField(max_length=200)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.place_name


# class Post(models.Model):
#     category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True)
#     tags = models.ManyToManyField('Tag', blank=True)
#     title = models.CharField('TITLE', max_length=50)
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')
#     # image = models.ImageField('IMAGE', upload_to='blog/%Y/%m/', blank=True, null=True)
#     content = models.TextField('CONTENT')
#     create_dt = models.DateTimeField('CREATE DT', auto_now_add=True)
#     update_dt = models.DateTimeField('UPDATE DT', auto_now=True)
#     like = models.PositiveSmallIntegerField('LIKE', default=0)

#     class Meta:
#         ordering = ('update_dt',)

#     def __str__(self):
#         return self.title


# class Category(models.Model):
#     name = models.CharField(max_length=50, unique=True)  # 카페, 한식, 일식, 중식, 양식
#     description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple one-line text.')

#     def __str__(self):
#         return self.name


# class Tag(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name