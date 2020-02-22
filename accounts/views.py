from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import form as form_with_email


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        form = form_with_email(request.POST)
        if form.is_valid():
            print(request.POST['first_name'])
            form.save()
        return redirect('/index')
    return render(request, 'account/signup.html')


def login(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("redit")
            return redirect("/index")
        else:
            messages.info(request, "Login failed")
            print("sssddddd")
            return redirect("/login")
    else:
        print("bangssss")
        return render(request, 'account/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/index')
