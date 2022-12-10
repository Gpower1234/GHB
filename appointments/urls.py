from django.urls import path
from appointments import views
from appointments.views import ManageAppointments, AppointmentView, AppointmentHistory


urlpatterns = [
    path('manage-appointments', ManageAppointments.as_view(), name='manage_appointments'),
    path('appointment', views.AppointmentView, name='appointment'),
    path('appointment-history', views.AppointmentHistory, name='appointment-history'),
]
