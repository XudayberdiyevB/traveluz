import random
from datetime import timedelta, datetime

import requests as requests
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from cities.models import City
from trains.models import Train
from .forms import RouteForm, RouteModelForm
from .models import Route
from .test_ticket import create_ticket
from .utils import get_routes


def home(request):
    form = RouteForm()
    return render(request, 'routes/home.html', {'form': form})


def find_routes(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            try:
                context = get_routes(request, form)
            except ValueError as e:
                messages.error(request, e)
                return render(request, 'routes/home.html', {'form': form})
            messages.success(request, 'Search results')
            return render(request, 'routes/home.html', context)
        return render(request, 'routes/home.html', {'form': form})
    else:
        form = RouteForm()
        return render(request, 'routes/home.html', {'form': form})


def add_routes(request):
    if request.method == 'POST':
        context = {}
        data = request.POST
        if data:
            from_city_id = int(data['from_city'])
            to_city_id = int(data['to_city'])
            total_time = int(data['total_time'])
            end_date = data['end_date']
            datetime_object = datetime.strptime(end_date, '%B %d, %Y')
            month_name = datetime_object.strftime('%B')
            end = f'{datetime_object.day}-{month_name}'
            trains = data['trains'].split(',')
            trains_lst = [int(t) for t in trains if t.isdigit()]
            qs = Train.objects.filter(id__in=trains_lst).select_related('from_city', 'to_city')
            cities = City.objects.filter(id__in=[from_city_id, to_city_id]).in_bulk()
            ticket_num = random.randint(100, 10000)
            form = RouteModelForm(
                initial={
                    'from_city': cities[from_city_id],
                    'to_city': cities[to_city_id],
                    'trains': qs,
                    'travel_times': total_time,
                    'ticket_number': ticket_num,
                    'passenger': request.user.id,
                }
            )
            junash_vaqti = qs[0].start_train_time
            borish = sum([i.travel_time for i in qs])

            def vaqt(soat, delta, minut):
                hmd = timedelta(hours=soat + delta, minutes=minut)
                return hmd

            t = vaqt(junash_vaqti.hour, borish, junash_vaqti.minute)
            v = t.seconds // 3600
            m = (t.seconds // 60) % 60
            all = f'{v}:{m}'

            create_ticket(f'{qs[0].name}', f'{qs[0].start_train_time}', f'{all}', f'{qs[0].place}', ticket_num,
                          cities[from_city_id], cities[to_city_id], end)
            context['form'] = form
        return render(request, 'routes/create.html', context)
    else:
        messages.error(request, 'Save route error')
        return redirect('/')


def save_route(request):
    if request.method == 'POST':
        form = RouteModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Saved your route!')
            return redirect('/list/')
        return render(request, 'routes/create.html', {'form': form})
    else:
        messages.error(request, 'Save error !')
        return redirect('/')


user = requests


class RouteListView(LoginRequiredMixin, ListView):
    paginate_by = 10
    model = Route
    template_name = 'routes/list.html'

    def get_queryset(self):
        queryset = Route.objects.filter(passenger=self.request.user)
        return queryset


class RouteDetailView(DetailView):
    queryset = Route.objects.all()
    template_name = 'routes/detail.html'


class RouteDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Route
    success_url = reverse_lazy('home')
    redirect_field_name = 'login'
    success_message = 'Delete route fro list'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Delete route!')
        return super().post(request, *args, **kwargs)
