from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
def userAdminPanel(request):
    if request.user.is_superuser:
        userList = User.objects.all().order_by('profile__number')
        return render(request, 'admin/admin.html', {'us': userList})
