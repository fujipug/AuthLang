from django.db import models
from main.models.content import Content
from main.models.subcategory import Subcategory


class ContentSubcategory(models.Model):
    content = models.ForeignKey('Content')
    subcategory = models.ForeignKey('Subcategory')