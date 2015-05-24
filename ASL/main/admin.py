from django.contrib import admin
from main.models import Content, CategoryType, Category, Subcategory, ContentCategory, ContentSubcategory


admin.site.register(Content)
admin.site.register(CategoryType)
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(ContentCategory)
admin.site.register(ContentSubcategory)