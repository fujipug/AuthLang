from django.db import models


class Content(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    vocab = models.CharField(max_length=200, blank=True, null=True)
    #images = models.CharField(max_length=200, blank=True, null=True)
    video = models.URLField(max_length=200)
    #keywords = tags
    DIFFICULTY_CHOICES = (
        ('Facil', 'Facil'),
        ('Mediano', 'Mediano'),
        ('Duro', 'Duro'),
        ('Otro', 'Otro'),
    )
    difficulty = models.CharField(max_length = 200, choices = DIFFICULTY_CHOICES, default = "Otro")
    COUNTRY_CHOICES = (
        ('Mexico', 'Mexico'),
        ('Colombia', 'Colombia'),
        ('Espana', 'Espana'),
        ('Otro', 'Otro'),
    )
    country = models.CharField(max_length = 200, choices = COUNTRY_CHOICES, default = "Otro")