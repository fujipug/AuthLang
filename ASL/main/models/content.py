from django.db import models


class Content(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    vocab = models.CharField(max_length=200, blank=True, null=True)
    #images = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200)
    video = models.URLField(max_length=200)
    #keywords = tags