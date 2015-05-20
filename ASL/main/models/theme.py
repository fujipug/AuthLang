from django.db import models
from main.models.difficulty import Difficulty
from main.models.country import Country


class Theme(models.Model):
    #Theme "other" object has PK 1 and name "no theme" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK = 1
    difficulty = models.ForeignKey('Difficulty', default=Difficulty.DEFAULT_PK)
    country = models.ForeignKey('Country', default=Country.DEFAULT_PK)
    theme = models.CharField(max_length = 200, unique=True)


    def __unicode__(self):
        return self.theme