from rest_framework import serializers
from services import models

class ServicesSerizalizer(serializers.ModelSerializer):
    class Meta:
        
        model = models.Services
        fields = ['_id', 'title', 'description', 'price']