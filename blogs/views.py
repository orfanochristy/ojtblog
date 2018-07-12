from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
	context = {}
	context['posts'] = Post.objects.filter(archive=False)
	context['name'] = 'Posts'
	return render(request, 'blogs/index.html', context)

def createpost(request):
	form = PostForm()
	if request.method == "POST":
		form = PostForm(data=request.POST)
		if form.is_valid():
			form = form.save(commit=False)
			form.author = request.user
			form.date_created = timezone.now()
			form.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'blogs/createpost.html', {"form": form})
	else:
		return render(request, 'blogs/createpost.html', {"form": form})

def editpost(request, post_id):
	template = 'blogs/editpost.html'
	post = get_object_or_404(Post, id=post_id)
	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
	else:
		form =PostForm(instance=post)
		args = {'form':form}
		return render(request, 'blogs/editpost.html', args)

def archivepost(request, post_id):
	post = get_object_or_404(Post, id=post_id, author=request.user)
	post.archive=True
	post.save()
	return HttpResponseRedirect(reverse('index'))

def unarchivepost(request, post_id):
	post = get_object_or_404(Post, id=post_id, author=request.user)
	post.archive=False
	post.save()
	return HttpResponseRedirect(reverse('index'))

def archivelist(request):
	context = {}
	context['posts'] = Post.objects.filter(archive=True)
	context['name'] = 'Posts'
	return render(request, 'blogs/archivelist.html', context)