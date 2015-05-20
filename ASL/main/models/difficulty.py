from django.db import models


class Difficulty(models.Model):
    #Difficulty "other" object has PK 1 and name "other" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK=1
    level = models.CharField(max_length = 200, unique=True, default="---")
    

    def __unicode__(self):
        return self.level