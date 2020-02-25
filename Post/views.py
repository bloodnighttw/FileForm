from django.shortcuts import render,redirect
from django.contrib.auth.models import User

from accounts.models import Profile
from .models import Post
import json,markdown as markdown2

# Create your views here.
def post_index(request):
	all1 = Post.objects.all().order_by('post_id')
	return render(request,'index.html',{'posts':all1[::-1]})

def post(request,post_id):
	try:
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
			content = markdown2.markdown("# ["+post.title+"]\n"+post.content)
			return render(request,'Post/post.html',{'content':content , 'title': post.title})
	except:
		return render(request, 'other/Error.html')


def readed(request,post_id):
	try:
		if request.user.is_authenticated:
			post = Post.objects.get(post_id = post_id)
			readeds = json.loads(post.readed)
			no_reads = []
			user_readeds = []
			for no_read in User.objects.all():
				no_reads.append(no_read)

			for readed in readeds:
				user_readeds.append(User.objects.get(username = readed.get('username')))
				no_reads.remove(User.objects.get(username = readed.get('username')))

			qset = Profile.objects.all().order_by('number')
			profilelist = []
			for g in qset:
				profilelist.append(g)

			for readed in user_readeds:
				profile = Profile.objects.get(user = readed)
				profilelist.remove(profile)

			###To user list


			return render(request,'Post/readed.html',{'readeds':user_readeds,'post':post,'non_readeds':profilelist})
	except:	
		return render(request, 'other/Error.html')
	

def create_Post(request):

	if(not request.user.is_superuser):
		return redirect('index/')

	if(request.method == 'POST'):
		title = request.POST['title']
		content = request.POST['content']
		post_id = get_post_id()
		readed = '[]'
		preview = request.POST['preview']

		post = Post(title = title, content = content ,post_id = post_id, readed = readed ,preview = preview)
		post.save()
		return redirect('/index/')

	return render(request,'Post/create.html')

def del_Post(request,post_id):
	if request.user.is_superuser:
		post = Post.objects.get(post_id = post_id)
		post.delete()
	return redirect('/index/')


def get_post_id():
	posts = Post.objects.all()
	num_max = int(0)
	for post in posts:
		numcache = int(post.post_id)
		if num_max < numcache:
			num_max = numcache
	return num_max+1

def edit(request,post_id):
	if not request.user.is_superuser:
		return redirect('/index/')
	post = Post.objects.get(post_id = post_id)
	if request.method == 'POST':
		post.title = request.POST['title']
		post.content = request.POST['content']
		post.preview = request.POST['preview']
		post.save()
		return redirect('/post/'+post_id)
	return render(request,'Post/edit.html',{'content':post})


###del_check###