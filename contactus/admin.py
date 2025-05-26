from django.contrib import admin
from .models import ContactInfo

@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('language', 'email', 'phone')
    list_filter = ('language',)
    search_fields = ('address', 'email', 'phone')

