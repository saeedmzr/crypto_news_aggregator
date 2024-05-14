from datetime import datetime

from django.db import models


# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    next_fetch_at = models.DateTimeField(null=True)
    last_fetch_at = models.DateTimeField(null=True)
    last_post_date = models.CharField(max_length=100, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['next_fetch_at']),
            models.Index(fields=['last_fetch_at']),
            models.Index(fields=['last_post_date']),
        ]


class Message(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(default=datetime.now)
