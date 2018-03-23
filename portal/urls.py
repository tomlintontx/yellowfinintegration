from django.contrib import admin
from django.urls import include,path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('page/', views.index, name='index'),
]