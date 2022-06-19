from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {'User': 'Bekzod'})


def team(request):
    return render(request, 'team.html', {})
