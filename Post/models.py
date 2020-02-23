from django.db import models

# Create your models here
class Post(models.Model):
	title = models.CharField( max_length = 200 )
	content = models.TextField()
	preview = models.CharField(max_length = 150 )
	post_id = models.IntegerField()
	readed = models.TextField()
