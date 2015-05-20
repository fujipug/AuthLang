from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content, Theme, Difficulty, Country


def home(request):
    return render(request, "main/home.html", {})


def content_details(request, id):
	content = Content.objects.get(id=id)
	return render(request, "main/content_details.html", {'content':content})


def difficulty(request, difficulty_slug):
    difficulty = Difficulty.objects.get(slug=difficulty_slug)
    themes = Theme.objects.filter(difficulty=difficulty)
    return render(request, "main/difficulty.html", {'difficulty': difficulty, 'themes': themes})


def country(request, difficulty_slug):
    difficulty = Difficulty.objects.get(slug=difficulty_slug)
    themes = Theme.objects.filter(difficulty=difficulty)
    return render(request, "main/difficulty.html", {'difficulty': difficulty, 'themes': themes})


#def theme(request, theme_slug):
#    theme = Theme.objects.get(slug = theme_slug)
#    return render(request, "main/theme.html", {theme': theme})


def difficulty_theme(request, difficulty_slug, theme_slug):
    difficulty = Difficulty.objects.get(slug = difficulty_slug)
    theme = Theme.objects.get(slug = theme_slug)
    contents = Content.objects.filter(difficulty = difficulty).filter(theme = theme)
    return render(request, "main/difficulty_theme.html", {'difficulty': difficulty, 'theme': theme, 'contents': contents})


def country_theme(request, country_slug, theme_slug):
    country = Country.objects.get(slug = country_slug)
    theme = Theme.objects.get(slug = theme_slug)
    contents = Content.objects.filter(country = country).filter(theme = theme)
    return render(request, "main/country_theme.html", {'country': country, 'theme': theme, 'contents': contents})