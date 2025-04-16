from django.conf import settings
from django.db import models


# Create your models here.
class Group(models.Model):
    slug = models.SlugField(max_length=32)
    name = models.CharField(max_length=32)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='own_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participating_groups', blank=True)
