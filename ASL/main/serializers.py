from django.forms import widgets
from rest_framework import serializers
from main.models import Content, CategoryType, Category, ContentCategory


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Content
        fields = ('id', 'first_name', 'last_name', 'title', 'description', 'vocab', 'video', 'country')


class CategoryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CategoryType
        fields = ('id', 'category_type', 'slug')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = ('id', 'category_type', 'category', 'slug')



class ContentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = ContentCategory
        fields = ('id', 'content', 'category')