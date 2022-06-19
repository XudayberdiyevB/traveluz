"""juniorTZ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from routes.views import (
    find_routes, home, add_routes, save_route, RouteListView, RouteDetailView,
    RouteDeleteView,
)
from .views import team

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', home, name='home'),
                  path('find_routes/', find_routes, name='find_routes'),
                  path('cities/', include('cities.urls')),
                  path('trains/', include('trains.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('add_routes/', add_routes, name='add_routes'),
                  path('save_route/', save_route, name='save_route'),
                  path('list/', RouteListView.as_view(), name='list'),
                  path('route/<int:pk>', RouteDetailView.as_view(), name='route_detail'),
                  path('route/<int:pk>/delete/', RouteDeleteView.as_view(), name='route_delete'),
                  path('team/', team, name='team'),
                  path('ckdeditor/', include('ckeditor_uploader.urls'))

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
