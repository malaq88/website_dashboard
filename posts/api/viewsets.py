from rest_framework import viewsets
from posts.api import serializers
from posts import models

class PostsViewset(viewsets.ModelViewSet):
    serializer_class = serializers.PostsSerizalizer
    queryset = models.Posts.objects.all()