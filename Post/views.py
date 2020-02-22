from django.shortcuts import render,redirect
from .models import Post
import json

# Create your views here.
def post_index(request):
	all1 = Post.objects.all()
	return render(request,'index.html',{'posts':all1[::-1]})

def post(request,post_id):
	try:
		if request.user.is_authenticated:
			post = Post.objects.get(post_id = post_id)
			readed = json.loads(post.readed)
			readed.append(request.user.username)
			post.readed = json.dumps(readed)
			post.save()
			return render(request,'Post/post.html',{'post':post})
		return redirect('index/')
	except :
		return redirect('index/')

def readed(request,post_id):
	try:
		if request.user.is_authenticated:
			post = Post.objects.get(post_id = post_id)
			readeds = json.loads(post.readed)
			return render(request,'Post/readed.html',{'readeds':readeds,'post':post})
		return redirect('/index')
	except :
		return redirect('index/')

def create_Post(request):
	if(not request.user.is_superuser):
		return redirect('index/')

	if(request.method == 'POST'):
		title = request.POST['title']
		content = request.POST['content']
		post_id = request.POST['post_id']
		readed = '[]'

		post = Post(title = title, content = content ,post_id = post_id, readed = readed)
		post.save()

	return render(request,'Post/create.html')



