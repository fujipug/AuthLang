from django.db import models
from main.models.category import Category
from embed_video.fields import EmbedVideoField


class Content(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    vocab = models.CharField(max_length = 200, blank = True, null = True)
    country = models.ForeignKey('Category')
    # images = models.CharField(max_length = 200, blank = True, null = True)
    # video = models.URLField(max_length = 200)
    video = EmbedVideoField()  # same like models.URLField()
    # keywords = tags