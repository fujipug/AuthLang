from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content, Theme, Difficulty


def home(request):
    return render(request, "main/home.html", {})


def content_details(request, id):
	content = Content.objects.get(id=id)
	return render(request, "main/content_details.html", {'content':content})


def difficulty(request, difficulty):
    #themes = Theme.objects.filters(difficulty=difficulty)
    themes = Theme.objects.all
    return render(request, "main/theme.html", {'difficulty': difficulty, 'themes': themes})


def theme(request, difficulty, theme):
	#if content.difficulty
	return render(request, "main/theme.html", {'difficulty': difficulty, 'theme': theme})