from django.shortcuts import render,HttpResponseRedirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm,EditUserProfileCreation,EditAdminProfileCreation
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash 
from django.contrib.auth.decorators import login_required
# Create your views here.
def fees_django(request):
      return render(request,'fees/djfees.html')
def fees_python(request):
      return render(request,'fees/pyfees.html')
def info1(request):
      return render(request,'info/info.html')
# def signup(request):
#       print("Hello")
#       if(request.method=="POST"):
#             print("Hello2")
#             fm=UserCreationForm(request.POST)
#             print("Hello3")
#             if(fm.is_valid()):
#                   print("Valid Data")
#             return render(request,'fees/signup.html',{'Form':fm})
#       else:
#             fm=UserCreationForm()
#       return render(request,'fees/signup.html',{'Form':fm})


def signup(request):  
      if(request.method=="POST"):         
            fm=SignUpForm(request.POST)
            if(fm.is_valid()): 
                  fm.save()               
                  messages.success(request,"Account is Created")            
      else: 
            fm=SignUpForm()
      return render(request,'fees/signup.html',{'Form':fm})

def userlogin(request):
   # if user not login 
   if(not request.user.is_authenticated):
      if(request.method=="POST"):
         log=AuthenticationForm(request=request,data=request.POST)  
         print("Hello")
         if(log.is_valid()):
               print("Valid Data") 
               uname=log.cleaned_data['username']
               pwd=log.cleaned_data['password']  
               print(uname,pwd)
               #matched data from the database
               user=authenticate(username=uname,password=pwd)
               if( user is not None ):
                  print("Authenticated user")
                  #if user have correct data 
                  login(request,user)                 
                  return HttpResponseRedirect('/fee/dashboard/')      
      else:
            log=AuthenticationForm()
      return render(request,'fees/login.html',{'Login':log})

   else:
      # if user has already login 
      return HttpResponseRedirect('/fee/profile/') 


def profile(request):
      # if user has already login 
      if(request.user.is_authenticated):
          if(request.method=="POST"):  
            if(request.user.is_superuser==True): 
                        print("Hello Admin")
                        pfl=EditAdminProfileCreation(request.POST,instance=request.user)
                        if(pfl.is_valid()):
                              print("Valid Admin")
                              pfl.save()
                              messages.success(request,"Admin Profile Updated!!!!") 
                        users=User.objects.all()                             
            else:          
                 pfl=EditUserProfileCreation(request.POST,instance=request.user)
                 print("Hello User")
                 if(pfl.is_valid()):
                       messages.success(request,"User Profile Updated!!!!")
                       pfl.save()
                 users=None 
          else:
            if(request.user.is_superuser==True):
                 pfl=EditAdminProfileCreation(instance=request.user)
                 users=User.objects.all()  
            else:
                 pfl=EditUserProfileCreation(instance=request.user) 
                 users=None
          return render(request,'fees/profile.html',{"Profile":pfl,"User":request.user.get_full_name()})
      else: 
            # if user not login 
           return HttpResponseRedirect('/fee/login/')

# def userDetails(request,eid):
#       if(request.user.is_authenticated):
#             pi=User.objects.get(pk=eid)
#             user=EditUserProfileCreation(instance=pi) 
#             return render(request,'fees/profiledetails.html',{"Profile":user})
#       else:
#             return HttpResponseRedirect('/fee/login/')

def dashboard(request):
      # if user has already login 
      if(request.user.is_authenticated):
      
          return render(request,'fees/dashboard.html',{"User":request.user.get_full_name()})
      else: 
            # if user not login 
           return HttpResponseRedirect('/fee/login/')

def userlogout(request):
      logout(request)
      return HttpResponseRedirect('/fee/login/')

# with old password
# def changepass(request):
#  # if user has already login 
#  if(request.user.is_authenticated):     
#    if(request.method=="POST"):
#       changepwd=PasswordChangeForm(user=request.user,data=request.POST)
#       if(changepwd.is_valid()):
#             changepwd.save() 
#             update_session_auth_hash(request,changepwd.user)
#             messages.success(request,"Password has been changed successfully!!!!")
#             return HttpResponseRedirect('/fee/profile/')
#    else:   
#             changepwd=PasswordChangeForm(user=request.user)
#    return render(request,'fees/changepass.html',{"Change":changepwd})
#  else:
#        # if user not login 
#       return HttpResponseRedirect('/fee/login/')


# with new password
def changepass(request):
 # if user has already login 
 if(request.user.is_authenticated):     
   if(request.method=="POST"):
      changepwd=SetPasswordForm(user=request.user,data=request.POST)
      if(changepwd.is_valid()):
            changepwd.save() 
            update_session_auth_hash(request,changepwd.user)
            messages.success(request,"Password has been changed successfully!!!!")
            return HttpResponseRedirect('/fee/profile/')
   else:   
            changepwd=SetPasswordForm(user=request.user)
   return render(request,'fees/changepass.html',{"Change":changepwd})
 else:
       # if user not login 
      return HttpResponseRedirect('/fee/login/')


def setCookie(request):
      response=render(request,'fees/setcookie.html')
      re=response.set_cookie('name','Arpita')
      print(re)
      return response

def getCookie(request):
      name=request.COOKIES['name']
      print(name)
      return render(request,'fees/getcookie.html',{"Name":name})
