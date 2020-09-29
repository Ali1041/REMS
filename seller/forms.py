from .models import *
from django import forms


class SellerForm(forms.ModelForm):
    class Meta:
        model = SellerProperty
        exclude = ('by',)


class Contactform(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    message = forms.CharField(max_length=254)
