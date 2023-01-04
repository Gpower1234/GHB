from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(help_text='Required')
    first_name = forms.CharField(max_length=50, help_text='Required')
    last_name = forms.CharField(max_length=50, help_text='Required')

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]


class ContactForm(forms.Form):
    name = forms.CharField(max_length=60)
    subject = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


