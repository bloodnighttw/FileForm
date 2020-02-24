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
			profile = user.profile
			profile.number = request.POST['num']
			profile.Phone = request.POST['phone']
			user.email = request.POST['email']
			user.save()
			profile.save()
			return redirect('/index/')
		return render(request,'other/profileEdit.html',{'user':user})


