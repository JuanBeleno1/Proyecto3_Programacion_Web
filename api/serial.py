from rest_framework import serializers

from .models import Tenis

class TenisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tenis
        fields = ['id','nombre','marca','color','año_lanzamiento','imagen']