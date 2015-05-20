from django.db import models
from django.template.defaultfilters import slugify


class Country(models.Model):
    #Country "other" object has PK 1 and name "---" (loaded through fixture main/fixture/initinal_data.json)
    DEFAULT_PK = 1
    country = models.CharField(max_length = 200, unique=True)
    slug = models.CharField(max_length = 200, blank=True, unique=True)


    def __unicode__(self):
        return self.country


    def save(self, *args, **kwargs):
        #slugify: https://docs.djangoproject.com/en/1.8/ref/templates/builtins/#slugify
        #
        #slug is auto-generated using the field 'country' if not specified
        #slugifies the field 'slug' and trucates it to 200 chars
        #this is for dynamic urls
        if len(self.slug) == 0:
            self.slug = slugify(self.country)[:200]
        else:
            self.slug = slugify(self.slug)[:200]
        super(Country, self).save(*args, **kwargs)