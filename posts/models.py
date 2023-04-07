from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Draft'
        PUBLISHED = 1, 'Published'

    title = models.CharField(max_length=255)
    summary = models.TextField(help_text='In markdown format')
    content = models.TextField(help_text='In markdown format')
    status = models.IntegerField(choices=Status.choices, default=Status.PUBLISHED)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
