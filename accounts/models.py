from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class form_with_email(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']