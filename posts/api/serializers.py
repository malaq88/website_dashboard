from rest_framework import serializers
from posts import models

class PostsSerizalizer(serializers.ModelSerializer):
    class Meta:
        
        model = models.Posts
        fields = ['post_id', 'title', 'content', 'author']