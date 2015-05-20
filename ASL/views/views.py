from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def home(request):
    return render(request, "home.html", {})

def pages(request):
	return render(request, "page.html", {})

def facil_list(request):
	return render(request, "facil_list.html", {})