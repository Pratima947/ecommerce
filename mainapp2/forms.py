from django import forms 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    password2=forms.CharField(label="RePassword",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':"User Email"}

class EditUserProfileCreation(UserChangeForm):
    Password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','date_joined']
        labels={'email':"User Email"}

class EditAdminProfileCreation(UserChangeForm):
    Password=None
    class Meta:
        model=User
        fields='__all__'
        labels={'email':"User Email"}