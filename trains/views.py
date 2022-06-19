from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.shortcuts import render, Http404, get_object_or_404
from django.urls import reverse_lazy
from .forms import TrainForm
from .models import Train
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView, ListView)


def home(request):
    qs=Train.objects.all()
    lst=Paginator(qs,2)
    page_number=request.GET.get('page')
    page_obj=lst.get_page(page_number)
    context={'page_obj':page_obj}
    return render(request,'trains/home.html',context)


class TrainListView(ListView):
    model=Train
    template_name='trains/home.html'
    paginate_by=5
    context_object_name='trains'

class TrainDetailView(DetailView):
    model=Train
    template_name = 'trains/detail.html'
    context_object_name = 'detail'

class TrainUpdateView(SuccessMessageMixin,LoginRequiredMixin,UpdateView):
    model=Train
    template_name = 'trains/create.html'
    form_class = TrainForm
    success_url = reverse_lazy('trains:home')
    success_message='Poyezd malumotlari o`zgartrildi!'

class TrainCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model=Train
    template_name = 'trains/create.html'
    form_class = TrainForm
    success_url = reverse_lazy('trains:home')
    success_message = 'Poyezd yaratildi!'

class TrainDeleteView(SuccessMessageMixin,LoginRequiredMixin,DeleteView):
    model = Train
    template_name = 'trains/delete_city.html'
    success_url = reverse_lazy('trains:home')
    success_message = 'Poyezd o`chirildi!'