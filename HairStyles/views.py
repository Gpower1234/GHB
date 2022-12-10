from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.


def booking_available_view(request):
    categories = Category.objects.all()
    hairTypes = HairType.objects.all().order_by('category')
    context = {
        'hairTypes': hairTypes,
        'categories': categories, 
    }

    return render(request, 'HairStyles/hairtype_list.html', context)


   

