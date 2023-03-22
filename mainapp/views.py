from django.shortcuts import render
from .forms import Registration
from .models import Employee


# from .forms import  ManagerRegistration
# Create your views here.
def learn_django(request):
      return render(request,'course/learndjango.html',{"dj":"Django Language",'trueData':False})
def learn_python(request):
      return render(request,'course/learnpython.html',{"py":"Python Language"})
def info(request):
      return render(request,'info/info.html',{"_Info":"Django & Python Information"})
def about(request):
      return render(request,'course/about.html')
def registration(request):     
      if(request.method=="POST"):
            form=Registration(request.POST)
            if(form.is_valid()):
                  print("Cleaned Data")
                  nme=form.cleaned_data['name']
                  email=form.cleaned_data['email']
                  sal=form.cleaned_data['salary']
                  print("Name:",nme,"Email:",email,"Sallary:",sal)
                  # e=Employee(name=nme,email=email,salary=sal)
                  e=Employee(eid=3,name=nme,email=email,salary=sal)
                  e=Employee(eid=7)
                  e.delete()
                  # e.save()                  
                  return render(request,'course/success.html',{"Name":nme,"Email":email,"Sallary":sal})     
      else:
            form=Registration(auto_id=True)
      return render(request,'course/registration.html',{"Form":form})


def mgrRegistration(request):     
      if(request.method=="POST"):
            form=ManagerRegistration(request.POST)
            
            if(form.is_valid()):
                  print("Cleaned Data")
                  nme=form.cleaned_data['name']
                  email=form.cleaned_data['email']
                  sal=form.cleaned_data['salary']
                  print("Name:",nme,"Email:",email,"Sallary:",sal)
                  e=Employee(name=nme,email=email,salary=sal)
                  e.save()                  
                  return render(request,'course/mgrsuccess.html',{"Name":nme,"Email":email,"Sallary":sal})     
      else:
            form=ManagerRegistration(auto_id=True)
      return render(request,'course/registration.html',{"Form":form})