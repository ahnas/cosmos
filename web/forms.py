# web/forms.py
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import CycleService,ShuttleService,FitnessServiceOnsite,FitnessServiceBranch
from django.forms.widgets import SelectMultiple, TextInput, Textarea, EmailInput, CheckboxInput,URLInput, Select, NumberInput, RadioSelect, FileInput


class CycleServiceForm(forms.ModelForm):
    class Meta:
        model = CycleService
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Number'}),
            'nearestBranch': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Nearest Branch'}),
            'details': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Desciption'}),
        }

class ShuttleServiceForm(forms.ModelForm):
    class Meta:
        model = ShuttleService
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Number'}),
            'nearestBranch': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Nearest Branch'}),
            'details': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Desciption'}),
        }

class FitnessServiceOnsiteForm(forms.ModelForm):
    class Meta:
        model = FitnessServiceOnsite
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Number'}),
            'nearestBranch': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Nearest Branch'}),
            'details': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Desciption'}),
        }

class FitnessServiceBranchForm(forms.ModelForm):
    class Meta:
        model = FitnessServiceBranch
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Name'}),
            'number': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Your Number'}),
            'nearestBranch': TextInput(attrs={'class': 'required form-control', 'placeholder': 'Nearest Branch'}),
            'details': Textarea(attrs={'class': 'required form-control', 'placeholder': 'Desciption'}),
        }
        