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


def difficulty(request, difficulty_slug):
    difficulty = Difficulty.objects.get(slug=difficulty_slug)
    themes = Theme.objects.filter(difficulty=difficulty)
    return render(request, "main/difficulty.html", {'difficulty': difficulty, 'themes': themes})


def country(request, country_slug):
    country = Country.objects.get(slug=country_slug)
    themes = Theme.objects.filter(country=country)
    return render(request, "main/country.html", {'country': country, 'themes': themes})


# def theme(request, theme_slug):
#    theme = Theme.objects.get(slug = theme_slug)
#    return render(request, "main/theme.html", {theme': theme})


def difficulty_theme(request, difficulty_slug, theme_slug):
    difficulty = Difficulty.objects.get(slug = difficulty_slug)
    theme = Theme.objects.get(slug = theme_slug)
    contents = Content.objects.filter(
        difficulty = difficulty).filter(theme = theme)
    return render(request, "main/difficulty_theme.html", {'difficulty': difficulty, 'theme': theme, 'contents': contents})


def country_theme(request, country_slug, theme_slug):
    country = Country.objects.get(slug = country_slug)
    theme = Theme.objects.get(slug = theme_slug)
    contents = Content.objects.filter(country = country).filter(theme = theme)
    return render(request, "main/country_theme.html", {'country': country, 'theme': theme, 'contents': contents})


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