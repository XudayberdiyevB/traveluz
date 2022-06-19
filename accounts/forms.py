from django import forms
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

User = get_user_model()


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label=mark_safe('<b>Username</b>'),
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label=mark_safe('<b>Password</b>'),
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label=mark_safe('<b>Confirm password</b>'),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Enter password again'}))

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise ValidationError('Passwords didn\'t match!')
        return password2


class UserLoginForm(forms.Form):
    username = forms.CharField(label=mark_safe('<b>Username</b>'),
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter username'}))
    password = forms.CharField(label=mark_safe('<b>Password</b>'),
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': 'Enter password'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise ValidationError('User doesn\'t exist')
            if not check_password(password, qs[0].password):
                raise ValidationError('Incorrect password!')
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('No active account')
        return super().clean(*args, **kwargs)
