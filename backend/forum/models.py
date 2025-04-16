from django.conf import settings
from django.db import models

from groups.models import Group


# Create your models here.

class AbstractContent(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    slug = models.SlugField(max_length=32)


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='posts')
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    audience = models.ManyToManyField(Group, related_name='available_posts', blank=True)
    tags = models.ManyToManyField(Tag, related_name='related_posts', blank=True)


class Content(AbstractContent):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='content_history')


class Comment(AbstractContent):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comments')
