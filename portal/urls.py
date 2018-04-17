from django.contrib import admin
from django.urls import include,path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('iframe/', views.iframe, name='iframe'),
    path('reports/', views.reports, name='reports')
]