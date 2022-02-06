import uuid
from django.db import models
import uuid


class Services(models.Model):
    _id = models.UUIDField(primary_key = True,
                               default = uuid.uuid4,
                               editable = False)
    title = models.CharField(u'Título', max_length=200)
    description = models.TextField(u'Conteúdo')
    price = models.BigIntegerField(u'Preço')

    created_at = models.DateField(auto_now=True)