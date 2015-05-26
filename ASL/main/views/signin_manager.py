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