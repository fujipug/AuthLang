from django.forms import widgets
from rest_framework import serializers
from main.models import Content, Difficulty, Country, CategoryType, Category, ContentCategory


class ContentSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Content
        fields = ('id', 'first_name', 'last_name', 'title', 'description', 'vocab', 'video', 'difficulty', 'country')


class DifficultySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Difficulty
        fields = ('id', 'difficulty', 'slug')


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Country
        fields = ('id', 'country', 'slug')


class CategoryTypeSerializer(serializers.ModelSerializer):

    class Meta:
        
        model = CategoryType
        fields = ('id', 'category_type', 'slug')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = Category
        fields = ('id', 'category_type', 'category', 'slug')
        depth = 1



class ContentCategorySerializer(serializers.ModelSerializer):

    class Meta:
        
        model = ContentCategory
        fields = ('id', 'content', 'category')