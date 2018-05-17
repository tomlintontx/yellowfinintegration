from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from . import loginUser
from .forms import UserForm
import django.contrib.sessions

# Create your views here.
def index(request):
	return render(request, 'portal/index.html')

def logout_user(request):
	logout(request)
	return render(request, 'portal/logout.html')

def home(request):
	username = request.session.get('username')
	url = loginUser.WebServices.login_user(username)
	admin = loginUser.WebServices.login_user(username)
	context = { 
		'url': url,
		'admin': admin
	}
	return render(request, 'portal/home.html', context)

def iframe(request):
	username = request.session.get('username')
	url = loginUser.WebServices.login_user(username)
	iframe = loginUser.WebServices.login_user(username)
	admin = loginUser.WebServices.login_user(username)
	context = { 
		'url': url,
		'iframe': iframe
	}
	return render(request, 'portal/iframe.html', context)

def reports(request):
	username = request.session.get('username')
	url = loginUser.WebServices.login_user(username)
	browse = loginUser.WebServices.login_user(username)
	admin = loginUser.WebServices.login_user(username)
	context = { 
		'url': url,
		'iframe': iframe,
		'browse': browse,
		'admin': admin
	}
	return render(request, 'portal/reports.html', context)

def yellowfinAdmin(request):
	username = request.session.get('username')
	url = loginUser.WebServices.login_user(username)
	browse = loginUser.WebServices.login_user(username)
	admin = loginUser.WebServices.login_user(username)
	context = { 
		'url': url,
		'iframe': iframe,
		'browse': browse,
		'admin': admin
	}
	return render(request, 'portal/administration.html', context)

class UserFormView(View):
	form_class = UserForm
	template_name = 'portal/index.html'

	# display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		request.session.flush()
		form = self.form_class(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		request.session['username'] = username

		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return redirect('/portal/home')

		return render(request, self.template_name, {'form': form})