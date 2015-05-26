from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from main.models import Content, Difficulty, Country, CategoryType, Category, ContentCategory
from django import forms
from main.forms import ContentForm, DifficultyForm, CountryForm, CategoryTypeForm, CategoryForm, ContentCategoryForm, SigninForm
from django.core import serializers
from main.serializers import ContentSerializer, DifficultySerializer, CountrySerializer, CategoryTypeSerializer, CategorySerializer, ContentCategorySerializer
from rest_framework import filters
from rest_framework import generics


#Serializer Stuff
class ContentList(generics.ListCreateAPIView):
    model = Content
    serializer_class = ContentSerializer
    def string_contains(self, string, substring):
        if substring is not None:
            if substring in string:
                return True
            else:
                return False
        return True

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a 'title' query parameter in the URL.
        """
        queryset = []

        
        # url variables
        first_name = self.request.query_params.get('first_name', None)
        last_name = self.request.query_params.get('last_name', None)
        country = self.request.query_params.get('country', None)
        title = self.request.query_params.get('title', None)
        order_by = self.request.query_params.get('order_by', None)
        if order_by is not None:
            contents = Content.objects.all().order_by(order_by)
        else:
            contents = Content.objects.all()

        for content in contents:
            print(content.country)
            if not self.string_contains(content.first_name, first_name):
                continue
            if not self.string_contains(content.last_name, last_name):
                continue
            if not self.string_contains(content.country.category, country):
            #if not content.country.country == country and country is not None:
                continue
            if not self.string_contains(content.title, title):
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


class ContentCategoryList(generics.ListCreateAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer


class ContentCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer
#End Serializer Stuff


def home(request):
    contents = Content.objects.all().order_by('-id')[:5]
    return render(request, "main/home.html", {'categories': Category.objects.all, 'category_types': CategoryType.objects.all, 'contents': contents})


def content_details(request, id):
    content = Content.objects.get(id=id)
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
        #fix later
        contents = Content.objects.all()
    return render(request, "main/content_list_by_category.html", {'category': category, 'category_type': category_type,'contents': contents})


def search_table(request):
    contents = Content.objects.all()
    return render(request, "main/search_table.html", {'contents': contents})