from django.db import models
from main.models.difficulty import Difficulty

class Theme(models.Model):
	difficulty = models.ForeignKey('Difficulty')
	theme = models.CharField(max_length = 200)