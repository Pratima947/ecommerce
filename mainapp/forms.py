from django.core import validators
from django import forms 
from .models import Employee


# def starts_with_s(value):
#     if(value[0]!='v'):
#       raise forms.ValidationError("Name Should be starts with s") 
					
# class Registration(forms.Form):
#     name=forms.CharField(required=True,validators=[validators.MinLengthValidator(2)])
#     email=forms.EmailField(required=True,validators=[validators.MinLengthValidator(10)])
#     salary=forms.IntegerField(required=True)
    # def clean_name(self):
    #     self.cleaned_data=super().clean()
    #     val_name=self.cleaned_data['name']
    #     val_email=self.cleaned_data['email']
    #     if(len(val_name)<3):
    #         raise forms.ValidationError("Enter the more than 2 char Name")
    #     if(len(val_email)<=13):
    #         raise forms.ValidationError("Enter the more than 13 char Email")

      #  def clean_name(self):      
      #   val_name=self.cleaned_data['name']
      #   if(len(val_name)<3):
      #       raise forms.ValidationError("Enter the more than 2 char Name")
      #   return val_name

      #  def clean_email(self): 
      #    val_name=self.cleaned_data['email']
      #    if(len(val_email)<=13):
      #       raise forms.ValidationError("Enter the more than 13 char Email")
      #    return val_name

class Registration(forms.ModelForm):
  class Meta:
    model=Employee
    fields=['name','email','salary']
    labels={'name':"Enter Employee Name","email":"Enter Emp Email",'salary':"Enter Salary"}

class ManagerRegistration(Registration):
  class Meta(Registration.Meta):    
    labels={'name':"Enter Manager Name","email":"Enter Manager Email",'salary':"Manager Salary"}

# class Registration(forms.Form):
#   name=forms.CharField()
#   email=forms.EmailField()
#   salary=forms.IntegerField()
