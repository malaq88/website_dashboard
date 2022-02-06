from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from posixpath import basename
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

from posts.api import viewsets as postsviewsets
route = routers.DefaultRouter()

route.register('posts', postsviewsets.PostsViewset, basename="posts")

urlpatterns = [
    path('admin/', admin.site.urls),

    # YOUR PATTERNS
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api-auth/', include('rest_framework.urls')),
    path('', include(route.urls)),
    path('swagger/', schema_view),
]