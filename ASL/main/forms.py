from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from main.models import Content, Category, Subcategory, ContentSubcategory, ContentCategory, CategoryType


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
        fields = ['first_name', 'last_name', 'title', 'description', 'vocab', 'video']


class CategoryForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields = ['category', 'category_type']


class CategoryTypeForm(forms.ModelForm):
    
    class Meta:
        model = CategoryType
        fields = ['category_type', 'slug']


class ContentCategoryForm(forms.ModelForm):
    
    class Meta:
        model = ContentCategory
        fields = ['content', 'category']


class ContentSubcategoryForm(forms.ModelForm):
    
    class Meta:
        model = ContentSubcategory
        fields = ['content', 'subcategory']


class SubcategoryForm(forms.ModelForm):
    
    class Meta:
        model = Subcategory
        fields = ['subcategory', 'slug', 'category']
