from .models import Tenis
from rest_framework import viewsets
from rest_framework.response import Response
from .serial import TenisSerializer


class TenisViewSet(viewsets.ModelViewSet):
    queryset = Tenis.objects.all().order_by('-año_lanzamiento')
    serializer_class = TenisSerializer