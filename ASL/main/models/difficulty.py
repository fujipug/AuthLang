from django.db import models
from django.template.defaultfilters import slugify


class Difficulty(models.Model):
    #Difficulty "other" object has PK 1 and name "other" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK = 1
    level = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, blank=True, unique=True)


    def __unicode__(self):
        return self.level


    def save(self, *args, **kwargs):
        #slugify: https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#slugify
        #
        #slug is auto-generated using the field 'level' if not specified
        #slugifies the field 'slug' and trucates it to 200 chars
        #this is for dynamic urls
        if len(self.slug) == 0:
            self.slug = slugify(self.level)[:200]
        else:
            self.slug = slugify(self.slug)[:200]
        super(Difficulty, self).save(*args, **kwargs)