from django.contrib import admin
from main.models import Content, CategoryType, Category, ContentCategory


admin.site.register(Content)
admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(ContentCategory)