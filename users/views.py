from django.shortcuts import render, redirect
from . models import User
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserSignup, UserLogin, UserForm, EditProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse


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
                    return HttpResponseRedirect(reverse('welcome'))

    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('base'))
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
                return HttpResponseRedirect(reverse('welcome'))
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('base'))                
    else:
        return render(request,'users/signin.html',{'form':form})

def profile(request):
    context = {}
    context['users'] = User.objects.all()
    context['name'] = 'Users'
    return render(request, 'users/profile.html', context)

def welcome(request):
    return render(request,'users/welcome.html')
    
def editprofile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, files=request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
    return render(request, 'users/accountsettings.html', args)

def Logout(request):
    if request.user.is_authenticated:
        logout(request) 
    return HttpResponseRedirect(reverse('base'))

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect(reverse('welcome'))
        else:
            return redirect(reverse('changepassword'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'users/changepassword.html', args)


def home(request):
    return render(request,'users/home.html')

def base(request):
    return render(request,'users/base.html')
