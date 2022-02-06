import uuid
from django.db import models
import uuid
from django.contrib.auth.models import User


class Posts(models.Model):
    _id = models.UUIDField(primary_key = True,
                               default = uuid.uuid4,
                               editable = False)
    title = models.CharField(u'Título', max_length=200)
    content = models.TextField(u'Conteúdo')
    author = models.ForeignKey(User, related_name='Author', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)