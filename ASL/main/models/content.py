from django.db import models
from embed_video.fields import EmbedVideoField


class Content(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    vocab = models.CharField(max_length=200, blank=True, null=True)
    #images = models.CharField(max_length=200, blank=True, null=True)
    #video = models.URLField(max_length=200)
    video = EmbedVideoField()  # same like models.URLField()
    #keywords = tags
    DIFFICULTY_CHOICES = (
        ('Principante', 'Principante'),
        ('Intermedio', 'Intermedio'),
        ('Dificil', 'Dificil'),
        ('Otro', 'Otro'),
    )
    difficulty = models.CharField(max_length = 200, choices = DIFFICULTY_CHOICES, default = "Otro")
    COUNTRY_CHOICES = (
        ('Mexico', 'Mexico'),
        ('Colombia', 'Colombia'),
        ('Espana', 'Espana'),
        ('Argentina', 'Argentina'),
        ('Chile', 'Chile'),
        ('Costa Rica', 'Costa Rica'),
        ('Peru', 'Peru'),
        ('Venezuela', 'Venezuela'),
        ('Guatemala', 'Guatemala'),
        ('Republica Dominicana', 'Republica Dominicana'),
        ('Otro', 'Otro'),
    )
    country = models.CharField(max_length = 200, choices = COUNTRY_CHOICES, default = "Otro")