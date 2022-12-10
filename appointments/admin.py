from django.contrib import admin
from .models import *

# Register your models here.

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'booked_item',  'phone_number', 'address', 'applied_on', 'date_scheduled']
    ordering = ['name']
    readonly_fields = ['name', 'booked_item', 'phone_number', 'address', 'applied_on',]

admin.site.register(Appointment, AppointmentAdmin)

