from django.shortcuts import render
from .models import Post

# Create your views here.
def post_index(request):
	all1 = Post.objects.all()
	return render(request,'index.html',{'posts':all1})

def post(request,post_id):
	try:
		post = Post.objects.get(post_id = post_id)
		return render(request,'Post/post.html',{'post':post})
	except :
		return render(request,'index.html',{'posts':Post.objects.all()})

