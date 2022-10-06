from django.contrib import admin
from .models import Original

# Register your models here.

@admin.register(Original)
class OriginalAdmin(admin.ModelAdmin):
    # pk = id필드
    list_display = ['id', 'place_area', 'place_name', 'road_address_name', 'phone', 'place_url', 'is_public', 'update_dt']
    # list_display = ['id', 'place_name', 'road_address_name', 'phone', 'place_url', 'placename_length']
    list_display_links = ['place_name']
    list_filter = ['update_dt', 'is_public', 'place_area']
    search_fields = ['place_name']