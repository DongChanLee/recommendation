from rest_framework import serializers
from .models import *

class OriginalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Original
        fields = '__all__'