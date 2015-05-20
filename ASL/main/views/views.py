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


def difficulty(request, difficulty_level):
    difficulty = Difficulty.objects.get(level=difficulty_level)
    themes = Theme.objects.filter(difficulty=difficulty)
    return render(request, "main/difficulty.html", {'difficulty': difficulty, 'themes': themes})


def theme(request, difficulty_level, theme):
    difficulty = Difficulty.objects.get(level=difficulty_level)
    theme = Theme.objects.get(theme=theme)
    contents = Content.objects.filter(difficulty=difficulty).filter(theme=theme)
    return render(request, "main/theme.html", {'difficulty': difficulty, 'theme': theme, 'contents': contents})