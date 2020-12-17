from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


# form for signing up
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
