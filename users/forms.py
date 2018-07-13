from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','first_name','last_name','password']
    def save(self, commit=False, *args, **kwargs):
        instance = super(UserForm, self).save(commit, *args, **kwargs)
        instance.set_password(self.cleaned_data.get('password'))
        instance.is_active=True 
        instance.save()
        return instance

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name','image')

class UserSignup(forms.Form):
    email=forms.EmailField(max_length=150,widget=forms.EmailInput)
    first_name=forms.CharField(max_length=150,widget=forms.TextInput)
    last_name=forms.CharField(max_length=150,widget=forms.TextInput)
    password=forms.CharField(max_length=150,widget=forms.PasswordInput)
    confirm_password=forms.CharField(max_length=150,widget=forms.PasswordInput) 
    
    def clean(self):
        password=self.cleaned_data['password']
        confirm_password=self.cleaned_data['confirm_password']

        if password != confirm_password:
            raise forms.ValidationError("Password did not Match")
            
class UserLogin(forms.Form):
    email=forms.CharField(max_length=150,widget=forms.EmailInput)
    password=forms.CharField(max_length=150,widget=forms.PasswordInput)

    def clean(self):
        user=authenticate(email=self.cleaned_data['email'],password=self.cleaned_data['password'])
        if not user:
            raise forms.ValidationError("Incorrect Username or Password")

    def sign_in(self):
        user=authenticate(email=self.cleaned_data['email'],password=self.cleaned_data['password'])
        return user
