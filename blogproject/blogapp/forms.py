from django import forms
from django.contrib.auth.models import User
from .models import Comment


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()



class CommentForm(forms.ModelForm):
        class Meta:
            model = Comment
            fields = ('body', 'name')


