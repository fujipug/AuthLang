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
            category_type = self.request.query_params.get('category_type', None)
            if category_type is not None:
                queryset = queryset.filter(category_type=category_type)
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


def category_details(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, "main/category_details.html", {'category': category, 'subcategories': Subcategory.objects.filter(category=category)})


def subcategory_details(request, category_slug, subcategory_slug):
    category = Category.objects.get(slug=category_slug)
    subcategory = Subcategory.objects.get(slug = subcategory_slug)
    content_category = ContentCategory.objects.get(category = category)
    content_subcategory = ContentSubcategory.objects.get(subcategory = subcategory)
    contents = Content.objects.filter(id = content_category.content.id).filter(id = content_subcategory.content.id)
    return render(request, "main/subcategory_details.html", {'category': Category.objects.get(slug=category_slug), 'subcategory': subcategory, 'contents': contents})


def category_manager(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = CategoryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/category_form.html', { 'form': form })


def category_type_manager(request):
    if request.method == 'POST':
        form = CategoryTypeForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = CategoryTypeForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/category_type_form.html', { 'form': form })


def content_category_manager(request):
    if request.method == 'POST':
        form = ContentCategoryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ContentCategoryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/content_category_form.html', { 'form': form })


def content_manager(request):
    if request.method == 'POST':
        form = ContentForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ContentForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/content_form.html', { 'form': form })


def difficulty_manager(request):
    if request.method == 'POST':
        form = DifficultyForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = DifficultyForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/difficulty_form.html', { 'form': form })


def country_manager(request):
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = CountryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/country_form.html', { 'form': form })


# def index_table(request):
#     contents = Content.objects.all().order_by('-id')[:5]
#     return render(request, "main/base/index_table.html", {'contents': contents})


def search_table(request):
    contents = Content.objects.all()
    return render(request, "main/search_table.html", {'contents': contents})


def signin_manager(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                #messages.error(request, 'Incorrect username or password')
                return HttpResponseRedirect('/signin/')
    elif request.method == 'GET':
        form = SigninForm()
    else:
        return HttpResponseRedirect('/signin/')
    return render(request, "main/sign_in.html", {"form": form})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def admin_forms(request):
    return render(request, "main/admin_forms.html", {})       