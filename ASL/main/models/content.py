from django.db import models
from main.models.difficulty import Difficulty
from main.models.country import Country
from main.models.theme import Theme
Country, Theme
#from main.models.difficulty import Difficulty
#from main.models.theme import Theme
#from main.models.country import Country
from embed_video.fields import EmbedVideoField


class Content(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    vocab = models.CharField(max_length = 200, blank = True, null = True)
    # images = models.CharField(max_length = 200, blank = True, null = True)
    # video = models.URLField(max_length = 200)
    video = EmbedVideoField()  # same like models.URLField()
    # keywords = tags
    difficulty = models.ForeignKey('Difficulty', default = Difficulty.DEFAULT_PK)
    country = models.ForeignKey('Country', default = Country.DEFAULT_PK)
    theme = models.ForeignKey('Theme', default = Theme.DEFAULT_PK)