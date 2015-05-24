from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content, Theme, Difficulty, Country
from django import forms
from main.forms import ContentForm, CountryForm, ThemeForm, DifficultyForm


def home(request):
    return render(request, "main/home.html", {'difficulties':  Difficulty.objects.all, 'countries': Country.objects.all})


def content_details(request, id):
    content = Content.objects.get(id=id)
    return render(request, "main/content_details.html", {'content': content})


def category_details(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    return render(request, "main/category_details.html", {'category': category, 'subcategories': subcategories = Subcategory.objects.filter(category=category)})


# def theme(request, theme_slug):
#    theme = Theme.objects.get(slug = theme_slug)
#    return render(request, "main/theme.html", {theme': theme})


def subcategory_details(request, category_slug, subcategory_slug):
    category = Category.objects.get(slug=category_slug)
    subcategory = Theme.objects.get(slug = subcategory_slug)
    content_category = Content
    contents = Content.objects.filter(difficulty = difficulty).filter(theme = theme)
    return render(request, "main/difficulty_theme.html", {'category': Category.objects.get(slug=category_slug), 'theme': theme, 'contents': contents})


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


def theme_manager(request):
    if request.method == 'POST':
        form = ThemeForm(request.POST)
        if form.is_valid():
            #messages.success(request, 'Your changes have been saved.')
            edited_data = form.save()
            return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    elif request.method == 'GET':
        form = ThemeForm()
    else:
        return HttpResponseRedirect('/') #'/user/edit/' + str(num))
    return render(request, 'main/theme_form.html', { 'form': form })


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