from django.contrib import admin
from django.urls import include,path
from django.http import HttpResponseRedirect
from . import views

urlpatterns = [
    path('', views.UserFormView.as_view(), name='index'),
    # path('register/', views.UserFormView.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('iframe/', views.iframe, name='iframe'),
    path('reports/', views.reports, name='reports'),
    path('administration/', views.yellowfinAdmin, name='administration')
]