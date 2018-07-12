from django.shortcuts import render
from.forms import UserSignup, UserLogin, UserForm, UserImage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout, authenticate
from django.urls import reverse
from .models import User
from django.template import loader

def Register(request):
    form=UserSignup()
    if request.method=='POST' and request.POST.get('register')=='register':
        data=request.POST.copy()
        form2=UserForm(data)
        form=UserSignup(data)
        if form.is_valid():
            form2.save()
            user = authenticate(email = request.POST['email'], password = request.POST['password'])
            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))
    else:                
        return render(request,'users/signup.html',{'form':form})


def Signin(request):
    form=UserLogin()
    if request.method=='POST' and request.POST.get('Signin')=='Signin':
        form=UserLogin(request.POST)
        #import pdb;pdb.set_trace()
        if form.is_valid():
            user=form.sign_in()
            login(request,user)
            if user.is_authenticated:
                return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))                
    else:
        return render(request,'users/signin.html',{'form':form})


def Dashboard(request,user_id):
    if request.user.is_authenticated:
        if request.method=='POST' and request.POST.get('Upload')=='Upload':
            form=UserImage()
            userid=User.objects.get(id=user_id)
            data2=request.FILES.copy()
            data2["image"]=request.FILES.get("user_image")
            form=UserImage(data2,data2, instance=userid)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))    
            else:
                return HttpResponse(form.errors)
        
        if request.method=='POST' and request.POST.get('publish_blog')=='publish_blog':
            blog_image=request.POST.copy()
            blog_text=request.FILES.copy()
            
        return render(request,'users/dashboard.html')
        #return HttpResponse(template.render(context,request))    
    else:
        return HttpResponseRedirect(reverse('Signin'))

    
def Logout(request):
    if request.user.is_authenticated:
        logout(request) 
    return HttpResponseRedirect(reverse('Signin'))
