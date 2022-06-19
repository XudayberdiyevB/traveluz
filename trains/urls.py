from django.urls import path
from .views import (home, TrainListView, TrainDetailView,
                    TrainUpdateView, TrainCreateView,
                    TrainDeleteView)

app_name='trains'

urlpatterns=[
    path('',TrainListView.as_view(),name='home'),
    path('<int:pk>',TrainDetailView.as_view(),name='detail'),
    path('add/',TrainCreateView.as_view(),name='create'),
    path('update/<int:pk>/',TrainUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',TrainDeleteView.as_view(),name='delete')
]