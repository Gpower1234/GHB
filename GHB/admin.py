from django.contrib import admin
from .models import *
from django.http import HttpResponse

class GalleryAdmin(admin.ModelAdmin):
    def add_view(self, request):
        if request.method == 'POST':
            if Gallery.objects.count() > 3:
                return HttpResponse("<h2 style='color: red;'>Oops</h2>Maximum image to be added reached")
        return super(GalleryAdmin, self).add_view(request)


admin.site.register(Profile)
admin.site.register(Gallery, GalleryAdmin)

