from rest_framework import viewsets
from services.api import serializers
from services import models

class ServicesViewset(viewsets.ModelViewSet):
    serializer_class = serializers.ServicesSerizalizer
    queryset = models.Services.objects.all()