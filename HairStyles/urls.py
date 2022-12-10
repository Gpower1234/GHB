from HairStyles import views
from django.urls import path
from .views import *

app_name = 'HairStyles'

urlpatterns = [
    path('service/', views.booking_available_view, name='service'),
]