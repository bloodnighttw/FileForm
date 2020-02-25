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
            messages.warning(request,'username empty')
            return redirect('/signup/')
        try:
            userlist =  User.objects.get(username= username)
            messages.warning(request,'username has been registered')
            return redirect('/signup/')
        except:
            print("3")

        email = request.POST['email']
        if email == '':
            messages.warning(request,'email empty')
            return redirect('/signup/')
        try:
            userlist = User.objects.get(email= email)
            messages.warning(request,'email has been registered')
            return redirect('/signup/')
        except:
            print("2")

        password = request.POST['password1']
        if password == '':
            messages.warning(request,'password empty')
            return redirect('/signup/')
        if password != request.POST['password2']:
            messages.warning(request,'密碼確認不正確')
            print("1")
            return redirect('/signup/')


        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if first_name == '' or last_name == '':
            messages.warning(request,'姓名為空')
            return redirect('/signup/')
        
        num = request.POST['num']
        phone = request.POST['phone']

        if num == None :
            messages.warning(request,'座號 為空')
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
