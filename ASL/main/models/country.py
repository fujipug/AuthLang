from django.db import models


class Country(models.Model):
    #Country "other" object has PK 1 and name "---" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK=1
    country = models.CharField(max_length = 200, unique=True)


    def __unicode__(self):
        return self.country