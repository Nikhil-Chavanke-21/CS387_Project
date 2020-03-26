from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.models import CustomUser

@login_required
def HomeView(request):
	template = 'home/home.html'
	context = {
		'title': 'Home',
		'user': request.user,
	}
	return render(request, template, context) 

def AccountView(request):
	template = 'home/page_user_profile_1_account.html'
	context = {
		'title': 'Account',
		'user': request.user,
	}
	return render(request, template, context)

def PersonalInfoSaveView(request):
	if request.method == 'POST':
		email = request.user
		user = CustomUser.objects.get(email=email)
		user.firstname = request.POST['firstname']
		user.lastname = request.POST['lastname']
		user.phonenumber = request.POST['phonenumber']
		user.building = request.POST['building']
		user.street = request.POST['street']
		user.city = request.POST['city']
		user.state = request.POST['state']
		user.save()
	return redirect('home:profile')

def AvatarSaveView(request):
	if request.method == 'POST':
		email = request.user
		user = CustomUser.objects.get(email=email)
		print(request.FILES)
		# user.save()
	return redirect('home:profile')
