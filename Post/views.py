from _ctypes import sizeof

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

from accounts.models import Profile
from .models import Post
import json, markdown as markdown2
from accounts.views import generateUuid


# Create your views here.
def post_index(request):
    if request.user.is_authenticated:
        if request.user.profile.uuid == "None":
            profile = request.user.profile
            profile.uuid = generateUuid()
            profile.save()
        all1 = Post.objects.all().order_by('post_id')
        return render(request, 'index.html', {'posts': all1[::-1]})
    return redirect('/login/')


def post(request, post_id):
    try:
        if request.user.is_authenticated:
            post = Post.objects.get(post_id=post_id)
            readeds = json.loads(post.readed)
            time = int(0)
            for user in readeds:
                if user == request.user.profile.uuid:
                    time = time + 1
            if time == 0:
                readeds.append(request.user.profile.uuid)
            post.readed = json.dumps(readeds)
            post.save()
            content = markdown2.markdown("# [" + post.title + "]\n" + post.content)
            return render(request, 'Post/post.html', {'content': content, 'title': post.title})
    except:
        return render(request, 'other/Error.html')


def readed(request, post_id):
    try:
        if request.user.is_authenticated:
            post = Post.objects.get(post_id=post_id)
            readeds = json.loads(post.readed)

            user_readeds = []
            for user in readeds:
                user_readeds.append(User.objects.get(profile__uuid=user))

            profileList = list(User.objects.all().order_by('profile__number'))


            for user in user_readeds:
                profileList.remove(user)


            return render(request, 'Post/readed.html',
                          {'readeds': user_readeds, 'post': post, 'non_readeds': profileList})
    except:
        return render(request, 'other/Error.html')


def create_Post(request):
    if (not request.user.is_superuser):
        return redirect('index/')

    if (request.method == 'POST'):
        title = request.POST['title']
        content = request.POST['content']
        post_id = get_post_id()
        readed = '[]'
        preview = request.POST['preview']

        post = Post(title=title, content=content, post_id=post_id, readed=readed, preview=preview)
        post.save()
        return redirect('/index/')

    return render(request, 'Post/create.html')


def del_Post(request, post_id):
    if request.user.is_superuser:
        post = Post.objects.get(post_id=post_id)
        post.delete()
    return redirect('/index/')


def get_post_id():
    posts = Post.objects.all()
    num_max = int(0)
    for post in posts:
        numcache = int(post.post_id)
        if num_max < numcache:
            num_max = numcache
    return num_max + 1


def edit(request, post_id):
    if not request.user.is_superuser:
        return redirect('/index/')
    post = Post.objects.get(post_id=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.preview = request.POST['preview']
        post.save()
        return redirect('/post/' + post_id)
    return render(request, 'Post/edit.html', {'content': post})


def top(request, post_id):
    if not request.user.is_superuser:
        return redirect('/index')
    post = Post.objects.get(post_id=post_id)
    post_id = get_post_id()
    post.post_id = post_id
    post.save()
    return redirect('/post/' + str(post_id) + '/')

###del_check###
