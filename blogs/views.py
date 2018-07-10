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
