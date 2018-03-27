from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	tom = 'This is my first bit of text'
	context = {'tom': tom}
	return render(request, 'portal/index.html', context)

def home(request):
	context = {}
	return render(request, 'portal/home.html', context)