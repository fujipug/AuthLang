from django.db import models
from django.template.defaultfilters import slugify
from main.models.difficulty import Difficulty
from main.models.country import Country


class Theme(models.Model):
    #Theme "other" object has PK 1 and name "no theme" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK = 1
    difficulty = models.ForeignKey('Difficulty', default=Difficulty.DEFAULT_PK)
    country = models.ForeignKey('Country', default=Country.DEFAULT_PK)
    theme = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, blank=True, unique=True)


    def __unicode__(self):
        return self.theme


    def save(self, *args, **kwargs):
        #slugify: https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#slugify
        #
        #slug is auto-generated using the field 'theme' if not specified
        #slugifies the field 'slug' and trucates it to 200 chars
        #this is for dynamic urls
        if len(self.slug) == 0:
            self.slug = slugify(self.theme)[:200]
        else:
            self.slug = slugify(self.slug)[:200]
        super(Theme, self).save(*args, **kwargs)