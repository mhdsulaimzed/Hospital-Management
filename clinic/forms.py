from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from clinic.models import Appoinment,Doctor,TimeSlot





class SigninForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput())
    password=forms.CharField(widget=forms.PasswordInput())
    
class SignupForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput())
    password2=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        
class AppoinmentForm(ModelForm):
    date=forms.DateField(label="select slot",widget=forms.NumberInput(attrs={"type":"date"}))
    patient_name=forms.CharField(label="Enter name of Patient",widget=forms.TextInput(attrs={"class":"form-control"}))
   
    age=forms.CharField(label="Age",widget=forms.NumberInput(attrs={"type":"age"}))
    class Meta:
        model=Appoinment
        fields=["patient_name","gender","doctor","age","date","time_slot","status"]
        
class StaffUserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
class DoctorsForm(ModelForm):
    class Meta:
        model=Doctor
        fields="__all__"
        
class TimeslotForm(ModelForm):
    class Meta:
        model=TimeSlot
        fields="__all__"
        