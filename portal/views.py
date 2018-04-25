from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import View
from django.template import loader
from . import loginUser
from .forms import UserForm

# Create your views here.
def index(request):
	tom = 'This is my first bit of text'
	context = {'tom': tom}
	return render(request, 'portal/index.html', context)

def home(request):
	url = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	admin = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	context = { 
		'url': url,
		'admin': admin
	}
	return render(request, 'portal/home.html', context)

def iframe(request):
	url = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	iframe = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	admin = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	context = { 
		'url': url,
		'iframe': iframe
	}
	return render(request, 'portal/iframe.html', context)

def reports(request):
	url = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	browse = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	admin = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	context = { 
		'url': url,
		'iframe': iframe,
		'browse': browse,
		'admin': admin
	}
	return render(request, 'portal/reports.html', context)

def yellowfinAdmin(request):
	url = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	browse = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	admin = loginUser.WebServices.login_user('tom.linton@yellowfin.bi', 'test')
	context = { 
		'url': url,
		'iframe': iframe,
		'browse': browse,
		'admin': admin
	}
	return render(request, 'portal/administration.html', context)

class UserFormView(View):
	form_class = UserForm
	template_name = 'portal/registration_form.html'

	# display a blank form
	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	# process form data
	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():

			user = form.save(commit=False)

			# cleaned normalized data
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()


			#returns User objects if credentials are correct
			user = authenticate(username=username, password=password)

			if user is not None:

				if user.is_active:
					login(request, user)
					return redirect('portal:home')

		return render(request, self.template_name, {'form': form})