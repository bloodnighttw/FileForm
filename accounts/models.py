from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from Form import settings


class form(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2','first_name','last_name']

class Profile(models.Model):
	user = models.OneToOneField(
		User,
		on_delete=models.CASCADE,
		primary_key=True
	)
	Phone = models.CharField(max_length=30)
	number = models.IntegerField()
