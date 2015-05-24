from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from main.models import Content, Country, Difficulty, Theme


#class UserForm(UserCreationForm):
#    model = User
#    fields = ['username', 'password']
#
#
#class MyUserForm(forms.ModelForm):
#    class Meta:
#        model = MyUser
#        fields = ['email', 'name', 'city', 'state', 'birth', 'zipcode']
#
#
#class SignInForm(forms.Form):
#    username = forms.CharField(label='Username', max_length=30)
#    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)


class ContentForm(forms.ModelForm):
    
    class Meta:
        model = Content
        fields = ['first_name', 'last_name', 'title', 'description', 'vocab', 'video', 'difficulty', 'country', 'theme']


class CountryForm(forms.ModelForm):
    
    class Meta:
        model = Country
        fields = ['country', 'slug']


class DifficultyForm(forms.ModelForm):
    
    class Meta:
        model = Difficulty
        fields = ['level', 'slug']


class ThemeForm(forms.ModelForm):
    
    class Meta:
        model = Theme
        fields = ['theme', 'slug', 'difficulty', 'country']



