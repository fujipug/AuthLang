from django.db import models

class Difficulty(models.Model):
	level = models.CharField(max_length = 200)


	def __unicode__(self):
		return self.level