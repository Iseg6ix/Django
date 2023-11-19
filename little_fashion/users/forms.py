from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=100)
    phone_number = forms.CharField(max_length=11)

    class Meta():
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=150)
    detail = forms.Textarea()
    class Meta:
        model = Profile
        fields = ['email']