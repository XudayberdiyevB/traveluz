from django.urls import path
from .views import (home, CityDetailView, CityCreateView,
                    CityUpdateView, CityDeleteView,
                    CityListView)
app_name='cities'

urlpatterns=[
    path('',CityListView.as_view(),name='home'),
    path('<int:pk>',CityDetailView.as_view(),name='detail'),
    path('add/',CityCreateView.as_view(),name='create'),
    path('update/<int:pk>/',CityUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',CityDeleteView.as_view(),name='delete'),
]