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
        if username == '':
            return redirect('/signup/')
        try:
            userlist =  User.objects.get(username= username)
            return render(request, 'other/Error.html')
        except:
            print("3")

        email = request.POST['email']
        if email == '':
            return redirect('/signup/')
        try:
            userlist = User.objects.get(email= email)
            return render(request, 'other/Error.html')
        except:
            print("2")

        password = request.POST['password1']
        if password == '':
            return redirect('/signup/')
        if password != request.POST['password2']:
            print("1")
            return render(request, 'other/Error.html')


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name == '' and last_name == '':
            return redirect('/signup/')
        
        num = request.POST['num']
        phone = request.POST['phone']

        if num == None and phone == '':
            return redirect('/signup/')

        user = User.objects.create(username= username,email= email ,first_name=first_name ,last_name = last_name)
        user.save()
        user.set_password(password)
        user.save()

        profile = Profile(user=user,number=int(num),Phone=phone)
        profile.save()
        return redirect('/index/')
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
