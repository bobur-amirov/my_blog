from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser, Blog



class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = MyUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = MyUser
        fields = ['username', 'first_name', 'last_name', 'bio', 'location', 'birth_date', 'img']


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'slug', 'img', 'description', 'category', 'tags']
