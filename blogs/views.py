from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone

def index(request):
	context = {}
	context['posts'] = Post.objects.all()
	context['name'] = 'Posts'
	return render(request, 'blogs/index.html', context)
	#return render(request, 'blogs/index.html')

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
	

	#return render(request, 'blogs/createpost.html', {'form': form})
		#form = Post()
def editpost(request, post_id):
	template = 'blogs/createpost.html'
	post = Post.objects.get(id=post_id)
	if request.method == 'POST':
		data = request.POST.copy()
		data["Post"]=request.post.id
		form = PostForm(request.POST, instance = post)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('index'))
		else:
			return render(request, 'blogs/editpost.html', {"form": form})
	else:
		return render(request, 'blogs/editpost.html')