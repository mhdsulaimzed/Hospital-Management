

from django.urls import path
from clinic import views


urlpatterns = [
    

path("signup",views.SignupView.as_view(),name="sign-up"),
path("signin",views.SigninView.as_view(),name="log-in"), 
path('patient',views.AppoinmentView.as_view(),name="patientdash"),
path("admindash",views.AdminDash.as_view(),name="admindash"),
path("superdash",views.SuperadminDash.as_view(),name="superadmindash"),
path("adminregister",views.AdminCreation.as_view(),name="admin-register"),
path("appointment/<int:id>/edit",views.AppoinmentsUpdate.as_view(),name="app-update"),
path("doctors",views.DoctorsView.as_view(),name="doctors"),
path("doctor/<int:id>/edit",views.DoctorsUpdate.as_view(),name="doctor-update"),
path("doctor/<int:id>/remove",views.Doctordelete.as_view(),name="doctor-delete"),
path("timeslot",views.TimeslotView.as_view(),name="time-slot"),
path("logout",views.sign_out_view,name="log-out"),


path("",views.IndexView.as_view(),name="index") 
]