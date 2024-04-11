from django.contrib import admin
from service.models import Service

class ServiceAdmin(admin.ModelAdmin):
    list_display=('post_title','post_description','post_image')

admin.site.register(Service,ServiceAdmin)    

# Register your models here.
