import uuid
from django.db import models
import uuid


class Posts(models.Model):
    _id = models.UUIDField(primary_key = True,
                               default = uuid.uuid4,
                               editable = False)
    title = models.CharField(u'Título', max_length=200)
    content = models.TextField(u'Conteúdo')
    author = models.CharField(u'Autor', max_length=50)
    created_at = models.DateField(auto_now=True)