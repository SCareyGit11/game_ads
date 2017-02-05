from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.

def welcome(request):
	return render(request, 'users/welcome.html')

def create(request):
	if request.method == 'POST':
		user = User.objects.register(request.POST['username'],
				request.POST['password'])
		if 'newuser' in user:
			print user['newuser'].id
			request.session['id'] = user['newuser'].id
			request.session['username'] = user['newuser'].username
			return render(request, 'users/success.html')

		elif 'errors' in user:
			print 50*'x'
			print user['errors']
			if 'exists' in user['errors']:
				messages.error(request, 'Username is already registered, please Log In or register with different name', extra_tags='exists')
				return redirect('/')
			if 'field' in user['errors']:
				messages.error(request, 'Please complete all fields', extra_tags='field')
			if 'username' in user['errors']:
				messages.error(request, 'Name must contain at least 2 characters', extra_tags='username')
			
			if 'password' in user['errors']:
				messages.error(request, 'Password must contain at least 8 characters', extra_tags='password')
			
			return redirect('/')

def show(request):
	if request.method == 'POST':
		user = User.objects.login(request.POST['username'], request.POST['password'])
		print 50*'?'
		print user
		if 'member' in user:
			print user['member'].id
			request.session['id'] = user['member'].id
			request.session['username'] = user['member'].username
			return render(request, 'users/success.html')
		elif 'login' in user['errors']:
			messages.error(request, 'Login not found', extra_tags='login')
			return redirect('/')
