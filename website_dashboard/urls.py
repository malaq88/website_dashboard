from posixpath import basename
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from posts.api import viewsets as postsviewsets
route = routers.DefaultRouter()

route.register('posts', postsviewsets.PostsViewset, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(route.urls))
]
