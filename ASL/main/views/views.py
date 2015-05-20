from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from main.models import Content


def home(request):
    return render(request, "main/home.html", {})


def content_details(request, id):
	return render(request, "main/content_details.html", {})


def facil_list(request):
	return render(request, "main/facil_list.html", {})