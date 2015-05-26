from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Content, Difficulty, Country, CategoryType, Category
from django import forms
from main.forms import ContentForm, DifficultyForm, CountryForm, CategoryTypeForm, CategoryForm, SigninForm
from django.core import serializers
from main.serializers import ContentSerializer, DifficultySerializer, CountrySerializer, CategoryTypeSerializer, CategorySerializer
from rest_framework import filters
from rest_framework import generics


#Serializer Stuff
class ContentList(generics.ListCreateAPIView):
    model = Content
    serializer_class = ContentSerializer
    def string_contains_substring(self, string, substring):
        if substring is not None:
            if substring in string:
                return True
            else:
                return False
        return True

    def content_has_any_categories(self, categories, content_categories):
        if categories is None:
            return True
        else:
            if content_categories is None:
                return False
            for category in categories:
                for content_category in content_categories:
                    if content_category.category == category:
                        return True
            return False


    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a 'title' query parameter in the URL.
        """
        queryset = []

        
        # url variables
        first_name_substring= self.request.query_params.get('first_name', None)
        last_name_substring = self.request.query_params.get('last_name', None)
        country_substring = self.request.query_params.get('country', None)
        title_substring = self.request.query_params.get('title', None)
        category_substring_list = self.request.query_params.get('categories', None)

        #get categories based off category substring list
        filtered_categories = []
        if category_substring_list is not None:
            category_substrings = [x.strip() for x in category_list.split(',')]
            categories = Categories.objects.all()
            for category in categories:
                for category_substring in category_substrings:
                    if self.string_contains_substring(category.slug, category_substring):
                        filtered_categories.append(category)
                        break

        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            contents = Content.objects.all().order_by(order_by)
        else:
            contents = Content.objects.all()

        for content in contents:
            if category_substring_list is not None:
                content_categories = ContentCategory.objects.filter(content = content)
                if not self.content_has_any_categories(filtered_categories, content_categories):
                    continue

            if not self.string_contains_substring(content.first_name, first_name_substring):
                continue
            if not self.string_contains_substring(content.last_name, last_name_substring):
                continue
            if not self.string_contains_substring(content.country.slug, country_substring):
            #if not content.country.country == country and country is not None:
                continue
            if not self.string_contains_substring(content.title, title_substring):
                continue
            queryset.append(content)

        return queryset


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class DifficultyList(generics.ListCreateAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class DifficultyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer


class CountryList(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CountryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CategoryTypeList(generics.ListCreateAPIView):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryList(generics.ListCreateAPIView):
    model = Category
    serializer_class = CategorySerializer
    def get_queryset(self):
            """
            Optionally restricts the returned purchases to a given user,
            by filtering against a 'category_type' query parameter in the URL.
            """
            queryset = Category.objects.all()
            category_type_id = self.request.query_params.get('category_type', None)
            if category_type_id is not None:
                #category_type = CategoryType.objects.get(slug = category_type_slug)
                queryset = queryset.filter(category_type=category_type_id)
            return queryset


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
#End Serializer Stuff


def home(request):
    contents = Content.objects.all().order_by('-id')[:5]
    return render(request, "main/home.html", {'categories': Category.objects.all, 'category_types': CategoryType.objects.all, 'contents': contents})


def content_details(request, id):
    content = Content.objects.get(id = id)
    return render(request, "main/content_details.html", {'content': content})


def content_list_by_category(request, category_type_slug, category_slug):
    if category_type_slug == 'difficulty':
        category_type = "Difficulty"
        category = Difficulty.objects.get(slug = category_slug)
        contents = Content.objects.filter(difficulty = category)
    elif category_type_slug == 'country':
        category_type = "Country"
        category = Country.objects.get(slug = category_slug)
        contents = Content.objects.filter(country = category)
    else:
        category_type = CategoryType.objects.get(slug=category_type_slug)
        category = Category.objects.get(slug = category_slug)
        contents = Content.objects.filter(categories=category)
    return render(request, "main/content_list_by_category.html", 
        {'category': category, 'category_type': category_type,'contents': contents})


def search_table(request):
    contents = Content.objects.all()
    return render(request, "main/search_table.html", {'contents': contents})