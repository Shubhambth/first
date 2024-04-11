from django.contrib import admin
from contactdata.models import ContactEnquiry
class ContactDetails(admin.ModelAdmin):
    list_display=('name','email','message')

admin.site.register(ContactEnquiry,ContactDetails)    
# Register your models here.
