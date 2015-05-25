from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content, CategoryType, Category, Subcategory, ContentCategory, ContentSubcategory
from django import forms
from main.forms import ContentForm, CategoryTypeForm, CategoryForm, SubcategoryForm, ContentCategoryForm, ContentSubcategoryForm
from django.core import serializers
from main.serializers import ContentSerializer, CategoryTypeSerializer, CategorySerializer, SubcategorySerializer, ContentCategorySerializer, ContentSubcategorySerializer
from rest_framework import generics


#Serializer Stuff
class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class CategoryTypeList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class CategoryTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoryType.objects.all()
    serializer_class = CategoryTypeSerializer


class CategoryList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubcategoryList(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer


class ContentCategoryList(generics.ListCreateAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer


class ContentCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentCategory.objects.all()
    serializer_class = ContentCategorySerializer


class ContentSubcategoryList(generics.ListCreateAPIView):
    queryset = ContentSubcategory.objects.all()
    serializer_class = ContentSubcategorySerializer


class ContentSubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ContentSubcategory.objects.all()
    serializer_class = ContentSubcategorySerializer
#End Serializer Stuff


def home(request):
    return render(request, "main/home.html", {'categories': Category.objects.all, 'category_types': CategoryType.objects.all})


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


def content_subcategory_manager(request):
    if request.method == 'POST':
        form = ContentSubcategoryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ContentSubcategoryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/content_subcategory_form.html', { 'form': form })


def subcategory_manager(request):
    if request.method == 'POST':
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = SubcategoryForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/subcategory_form.html', { 'form': form })


def index_table(request):
    contents = Content.objects.all().order_by('-id')[:5]
    return render(request, "main/base/index_table.html", {'contents': contents})


def search_table(request):
    contents = Content.objects.all()
    return render(request, "main/search_table.html", {'contents': contents})