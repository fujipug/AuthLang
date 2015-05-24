from django.db import models
from main.models.content import Content
from main.models.category import Category


class ContentCategory(models.Model):
    content = models.ForeignKey('Content')
    category = models.ForeignKey('Category')