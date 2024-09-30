from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from app.models import *
from user.models import *




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'color', 'image', 'batafsil', 'narxi', 'category']

    def __init__(self, *a, **b) -> None:
        super().__init__(*a, **b)
        for i in self.fields:
            self.fields[i].widget.attrs.update({'class':'form-control'})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class SavatForm(forms.ModelForm):
    class Meta:
        model = Savat
        fields = ['user', 'product']

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'adress', 'image', 'phone']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)