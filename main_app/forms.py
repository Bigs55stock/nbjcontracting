from django import forms
from django.forms import ModelForm
from .models import Customer


class Customerform(ModelForm):
    class Meta:
        model = Customer
        fields = ('name','number','email','Inquiries')
        

        widgets = {
            'name': forms.TextInput(attrs={'div class':'field', 'class':'control', 'placeholder':'Name'}),
            'number': forms.TextInput(attrs={'div class':'field', 'class':'control', 'placeholder':'Number'}),
            'email': forms.EmailInput(attrs={'div class':'field', 'class':'control', 'placeholder':'Email'}),
            "Inquries": forms.TextInput(attrs={'div class':'field', 'class':'control', 'placeholder':'Inquries'}),
        }
