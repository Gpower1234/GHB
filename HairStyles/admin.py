from django.contrib import admin
from .models import *


@admin.action(description='Marked selected stories as published')
def make_published(modeladmin, request, queryset):
    pass

class HairTypeAdmin(admin.ModelAdmin):
    list_display = ['subCategory', 'price']
    ordering = ['subCategory']
    actions = [make_published]

admin.site.register(HairType, HairTypeAdmin)
admin.site.register(Category)
