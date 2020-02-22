from django.shortcuts import render,redirect

# Create your views here.
def home(request):
	return redirect('/index')

def about(request):
	return render(request,'about/about.html')