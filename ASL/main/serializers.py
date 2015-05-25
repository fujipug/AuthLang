from django.forms import widgets
from rest_framework import serializers
from main.models import Content, CategoryType, Category, Subcategory, ContentCategory, ContentSubcategory


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Content
        fields = ('first_name', 'last_name', 'title', 'description', 'vocab', 'video')


class CategoryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CategoryType
        fields = ('category_type')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = ('category_type', 'category')


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Subcategory
        fields = ('category', 'subcategory')


class ContentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = ContentCategory
        fields = ('content', 'category')


class ContentSubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = ContentSubcategory
        fields = ('content', 'subcategory')