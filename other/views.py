from django.contrib.auth.models import User
from django.shortcuts import render,redirect


# Create your views here.
def home(request):
	return redirect('/index')

def about(request):
	return render(request, 'other/about.html')

def profileEdit(request):
	if request.user.is_authenticated:
		user = request.user
		if request.method == 'POST':

			profile0 = user.profile
			profile0.number = request.POST['num']
			profile0.Phone = request.POST['phone']

			user.save()
			profile0.save()
			return redirect('/index/')
		return render(request,'other/profileEdit.html',{'user':user})


