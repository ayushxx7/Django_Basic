from django.shortcuts import render,redirect
# from .models import user
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def register(request):

	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		user_name = request.POST['user_name']
		if User.objects.filter(username=user_name).exists():
			print('Username Taken!')
			messages.error(request,'Username Taken!')
			return redirect('register_form')
		email = request.POST['email']
		if User.objects.filter(email=email).exists():
			messages.error(request,'Email Taken!')
			return redirect('register_form')		
		password = request.POST['password']
		conf_password = request.POST['conf_password']
		if password != conf_password:
			messages.error(request,'Password not same!')
			return redirect('register_form')
		
		user = User.objects.create_user(username=user_name,password=password,email=email,first_name=first_name,last_name=last_name)
		user.save()

		print('Saved User!')
		return redirect('/bs')
	else:
		return render(request,'register.html')

def login(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		
		if user is not None:
			auth.login(request,user)
			return redirect('register_form')
		else:
			messages.error(request,'Invalid Credentials!')
			return redirect('login')
	else:
		print('what up!')
		return render(request,'login.html')

def logout(request):

	auth.logout(request)
	return redirect('register_form')