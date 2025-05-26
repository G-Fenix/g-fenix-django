from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'category', 'start_date', 'end_date', 'is_visible')
    list_filter = ('language', 'category', 'is_visible')
    search_fields = ('title', 'description')

