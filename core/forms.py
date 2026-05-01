from django import forms
from .models import Action, Agenda


class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['name', 'active', 'order', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = ['action', 'name', 'file_name', 'order', 'date']
        widgets = {'date': forms.DateInput(attrs={'type': 'date'})}
