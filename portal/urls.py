from django.contrib import admin
from django.urls import include,path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]