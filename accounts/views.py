from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth, User
from accounts.models import Profile


# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('/index')
    if request.method == 'POST':
        username = request.POST['username']
        try:
            userlist =  User.objects.get(username= username)
            return render(request,'about/Error.html')
        except:
            print("3")
        email = request.POST['email']
        try:
            userlist = User.objects.get(email= email)
            return render(request,'about/Error.html')
        except:
            print("2")
        password = request.POST['password1']
        if password != request.POST['password2']:
            print("1")
            return render(request, 'about/Error.html')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user = User.objects.create(username= username,email= email ,first_name=first_name ,last_name = last_name)
        user.save()
        user.set_password(password)
        user.save()
        num = request.POST['num']
        phone = request.POST['phone']
        profile = Profile(user=user,number=int(num),Phone=phone)
        profile.save()
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
