from django.shortcuts import render
from.forms import UserSignup, UserLogin, UserForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login,logout, authenticate
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
                    return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))
            else:
                return HttpResponse("Wrong")
    return render(request,'users/signup.html',{'form':form})

def Signin(request):
    form=UserLogin()
    if request.method=='POST' and request.POST.get('Signin')=='Signin':
        form=UserLogin(request.POST)
        if form.is_valid():
            user=form.sign_in()
            login(request,user)
            if user.is_authenticated:
                return HttpResponseRedirect(reverse('Dashboard',args=(request.user.id,)))
    return render(request,'users/signin.html',{'form':form})

def Dashboard(request,user_id):
    return HttpResponse("This is dashboard")
