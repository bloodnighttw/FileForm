from django.contrib import admin

# Register your models here.
from Post import models

admin.site.register(models.Post)
