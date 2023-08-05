from django.contrib import admin
from clinic.models import Appoinment,Doctor,TimeSlot

# Register your models here.
admin.site.register(Appoinment)
admin.site.register(Doctor)
admin.site.register(TimeSlot)