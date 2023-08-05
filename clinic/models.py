from django.db import models
from django.contrib.auth.models import User

# Create your models here.

    
class Doctor(models.Model):
    departments=[('Cardiologist','Cardiologist'),
('Neurology','Neurology'),
('General Medicine','General Medicine'),
('Ortho','Ortho')

]
    doctor_name=models.CharField(max_length=50)
    department=models.CharField(choices=departments,max_length=200,default="General Medicicne")
    qualification=models.CharField(max_length=200)
    photo=models.ImageField(upload_to="images",null=True,blank=True)
    
    def __str__(self):
        return self.doctor_name
    
class TimeSlot(models.Model):
    # doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    time_slot=models.TimeField()
    
    def __str__(self):
        return f"{self.time_slot.strftime('%H:%M')}"
    
class Appoinment(models.Model):
    patient_name=models.CharField(max_length=200)
    option=(("Male","Male"),
            ("Female","Female"),
            ("Others","Others"))
    gender=models.CharField(max_length=20,choices=option)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    age=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField()
    time_slot=models.ForeignKey(TimeSlot,on_delete=models.CASCADE)
    status=models.CharField(max_length=200,choices=[("approved","approved"),("rejected","rejected"),("pending","pending")],default="pending")
    
    def __str__(self):
        return self.patient_name, self.gender


    

    
