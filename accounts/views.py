from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm
from accounts.forms import UserRegisterForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.info(request, 'Great! You sign in your account')
        return redirect('home')
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.warning(request, 'Your signed out!')
    return redirect('home')


def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data.get('password'))
            new_user.save()
            messages.info(request, 'Registration successfully')
            return redirect('accounts:login')
        return render(request, 'accounts/register.html', {'form': form})
    else:
        return render(request, 'accounts/register.html', {'form': form})
