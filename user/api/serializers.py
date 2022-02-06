from dataclasses import field
from rest_framework import serializers
from user import models
from django.contrib.auth.models import User


class UserSerizalizer(serializers.ModelSerializer):
    class Meta:
        
        model = User
        fields = ["username","first_name","last_name","email","password","is_active"]
