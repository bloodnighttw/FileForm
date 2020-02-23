from django.shortcuts import render,redirect
from .models import Post
import json,markdown2

# Create your views here.
def post_index(request):
	all1 = Post.objects.all()
	return render(request,'index.html',{'posts':all1[::-1]})

def post(request,post_id):

	if request.user.is_authenticated:
		post = Post.objects.get(post_id = post_id)
		readeds = json.loads(post.readed)
		time = int(0)
		for readed in readeds:
			user = readed.get('username')
			if user == request.user.username:
				time = time+1
		if time == 0 :
			name = request.user.first_name + request.user.last_name
			readeds.append({'username':request.user.username,'name':name})
		post.readed = json.dumps(readeds)
		post.save()
		content = markdown2.markdown(post.content)
		return render(request,'Post/post.html',{'post':post,'content':content})
	return redirect('/index/')
	

def readed(request,post_id):
		if request.user.is_authenticated:
			post = Post.objects.get(post_id = post_id)
			readeds = json.loads(post.readed)

			return render(request,'Post/readed.html',{'readeds':readeds,'post':post})
		return redirect('/index')
	

def create_Post(request):

	if(not request.user.is_superuser):
		return redirect('index/')

	if(request.method == 'POST'):
		title = request.POST['title']
		content = request.POST['content']
		post_id = request.POST['post_id']
		readed = '[]'
		preview = request.POST['preview']

		post = Post(title = title, content = content ,post_id = post_id, readed = readed ,preview = preview)
		post.save()

	return render(request,'Post/create.html')

def del_Post(request,post_id):
	if request.user.is_superuser:
		post = Post.objects.get(post_id = post_id)
		post.delete()
	return redirect('/index/')


###del_check###
'''
def del_check(request,post_id):
	if request.is_superuser:
		post = Post.objects.get(post_id = post_id)
'''