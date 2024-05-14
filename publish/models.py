from datetime import datetime

from django.db import models

from news.models import Message


# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=255)
    is_personal = models.BooleanField(default=True)
    info = models.JSONField(max_length=255)


class Publish(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)
    sent_at = models.DateTimeField(default=datetime.now())
