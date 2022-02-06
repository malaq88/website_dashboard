from rest_framework import viewsets
from user.api import serializers
from user import models
from django.contrib.auth.models import User

class UserViewset(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerizalizer
    queryset = User.objects.all()