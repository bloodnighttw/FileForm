"""Form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views as view1
from Post.views import post_index,post,readed,create_Post,del_Post
from other.views import home,about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',view1.login),
    path('signup/',view1.register),
    path('logout/',view1.logout),
    path('index/',post_index),
    path('create/', create_Post),
    path('about/',about),
    path('<str:post_id>/',post),
    path('<str:post_id>/readed',readed),
    path('<str:post_id>/del',del_Post),
    path('',home),

]
