from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,ListView,UpdateView,DeleteView
from clinic.forms import SigninForm,SignupForm,AppoinmentForm,StaffUserForm,DoctorsForm,TimeslotForm
from django.contrib.auth import authenticate, login,logout
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django .contrib.auth.views import LoginView
from clinic.models import Appoinment,Doctor,TimeSlot
from django.utils.decorators import method_decorator
from django.contrib import messages
# Create your views here.
def signin_required(fn):
    def wrapper(request,*args,**kw):
        if not request.user.is_authenticated:
            messages.error(request,"please login to perform the action")
            return redirect("log-in")
        else:
            return fn(request,*args,**kw)
    return wrapper

def sign_out_view(request,*args,**kw):
    logout(request)
    return redirect("log-in")
        
        


class IndexView(View):
        def get(self,request,*args,**kw):
         return render(request,"index.html")
     
class SignupView(CreateView):
    model=User
    form_class=SignupForm
    template_name="signup.html"
    success_url=reverse_lazy("log-in")    
    
    
#all users admin ,user and super user have same login page and redirected to their consicutive dashboards     
class SigninView(View):
    def get(self,request,*args,**kw):
        form = SigninForm()
        return render(request, "login.html", {"form": form})

    def post(self, request, *args, **kw):
        form = SigninForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            usr = authenticate(request, username=uname, password=pwd)
            print(usr)
            if usr is not None:
            
                login(request, usr)
                if usr.is_superuser:
                    return redirect('superadmindash')  # Replace 'superuser_dashboard' with the URL name of the staff dashboard page
                elif usr.is_staff:
                    return redirect('admindash')
                else:
                    return redirect('patientdash')  # Replace 'patient_dashboard' with the URL name of the normal user dashboard page
            else:
            
                return render(request, "login.html", {"form": form})
            
      #for taking an apponiment
@method_decorator(signin_required,name="dispatch")       
class AppoinmentView(CreateView,ListView):
    template_name="patient_dash.html"
    form_class=AppoinmentForm
    model=Appoinment
    success_url=reverse_lazy("patientdash")
    context_object_name="appointments"
    
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return Appoinment.objects.filter(user=self.request.user)
    
    
@method_decorator(signin_required,name="dispatch")     
class AdminDash(ListView):
    model=Appoinment
    template_name="admin_dash.html"
    context_object_name="appointments"
    
    
    
@method_decorator(signin_required,name="dispatch") 
class SuperadminDash(ListView):
    model=Appoinment
    context_object_name="appointments"
    template_name="super-admindash.html"

#super user can create is_staff user or the admin user    
@method_decorator(signin_required,name="dispatch")    
class AdminCreation(CreateView):
    model=User
    form_class=SignupForm
    template_name="create-admin.html"
    success_url=reverse_lazy("superadmindash")
    
    def post(self,request,*args,**kw):
        form=StaffUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            admin_user = User.objects.create_user(username=username,email=email,password=password,is_staff=True)
            admin_user.save()
            return redirect("superadmindash")
        else:
            return render(request,"create-admin.html",{"form":form})
        
 #admin user can approve or reject by updating the status        
@method_decorator(signin_required,name="dispatch") 
class AppoinmentsUpdate(UpdateView):
    model=Appoinment
    form_class=AppoinmentForm
    template_name="appointment-update.html"
    success_url=reverse_lazy("admindash")
    pk_url_kwarg="id"
#admin user can add doctors 
@method_decorator(signin_required,name="dispatch")     
class DoctorsView(CreateView,ListView):
    model=Doctor
    template_name="doctors-list.html"
    success_url=reverse_lazy("admindash")
    form_class=DoctorsForm
    context_object_name="doctors"
#admin user can also update the doctors details 
@method_decorator(signin_required,name="dispatch")  
class DoctorsUpdate(UpdateView):
    model=Doctor
    form_class=DoctorsForm
    template_name="doctors-update.html"
    success_url=reverse_lazy("doctors")
    pk_url_kwarg="id" 
      
@method_decorator(signin_required,name="dispatch")     
class Doctordelete(View):
    def get(self, request, *args, **kw):
        id = kw.get("pk")
        Doctor.objects.filter(id=id).delete()
        return redirect('doctors')
    
#admin user can ADD TIME SLOTS for requesting appoinment    
@method_decorator(signin_required,name="dispatch")     
class TimeslotView(CreateView,ListView):
    model=TimeSlot
    template_name="time-slot.html"
    success_url=reverse_lazy("timeslot")
    form_class=TimeslotForm
    context_object_name="time"
    
    
    


