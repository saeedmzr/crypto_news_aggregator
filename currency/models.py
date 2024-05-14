from datetime import datetime

from django.db import models


# Create your models here.


class Currency(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=30)

    class Meta:
        indexes = [
            models.Index(fields=['abbreviation']),  # Index on title and publish_date
        ]


class Price(models.Model):
    title = models.CharField(max_length=100)
    first_symbol = models.CharField(max_length=30)
    second_symbol = models.CharField(max_length=30)
    amount = models.FloatField(default=1.0)
    created_at = models.DateTimeField(default=datetime.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['first_symbol']),
            models.Index(fields=['second_symbol']),
            models.Index(fields=['amount']),
            models.Index(fields=['first_symbol', 'second_symbol']),
        ]
