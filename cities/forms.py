from django import forms

from .models import City
from ckeditor.widgets import CKEditorWidget
from django.utils.safestring import mark_safe

class CityForm(forms.ModelForm):
    name=forms.CharField(label='Shaxar nomi',
                         widget=forms.TextInput(
                         attrs={'class':'form-control','placeholder':'misol: Buxoro'}))
    about_city=forms.CharField(widget=CKEditorWidget())
    shahar_haqida_qisqa=forms.CharField(label=mark_safe('shaxar haiqda qisqa'))

    class Meta:
        model=City
        fields=('name','shahar_haqida_qisqa','about_city')