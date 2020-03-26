from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import CustomUser
from .forms import UserCreationForm, LoginForm

def SignupView(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			form.save()
			return redirect('users:login')
	form = UserCreationForm()
	template = 'users/signup.html'
	context = {
		'title': 'Signup',
		'form': form,
	}
	return render(request, template, context)

def LoginView(request):
	if request.method == 'POST':
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, email=email, password=password)
		if user is not None:
			login(request, user)
			return redirect('home:home')
	form = LoginForm()
	template = 'users/page_user_login_5.html'
	context = {
		'title': 'Login',
		'form': form,
	}
	return render(request, template, context)

def LogoutView(request):
	logout(request)
	return redirect('users:login') 

