from django import forms
from .models import Train
from cities.models import City


class TrainForm(forms.ModelForm):
    name = forms.CharField(label='Poyezd raqami',
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'misol: Bux123'}))
    travel_time=forms.IntegerField(label='Sayohat vaqti',
                                    widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'misol: 56'}))
    from_city=forms.ModelChoiceField(label='Qaysi shaxardan',empty_label='shaxar tanlang',
                                    queryset=City.objects.all(),
                                    widget=forms.Select(attrs={'class':'form-control'}))
    to_city = forms.ModelChoiceField(label='Qaysi shaxarga',empty_label='shaxar tanlang',
                                    queryset=City.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model=Train
        fields='__all__'
