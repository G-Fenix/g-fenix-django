from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'category', 'is_featured')
    list_filter = ('language', 'category', 'is_featured')
    search_fields = ('title', 'description')

