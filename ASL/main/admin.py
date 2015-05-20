from django.contrib import admin
from main.models import Content, Difficulty, Theme, Country


admin.site.register(Content)
admin.site.register(Difficulty)
admin.site.register(Theme)
admin.site.register(Country)