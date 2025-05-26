from django.contrib import admin
from .models import BlogPost


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'published_at')
    list_filter = ('language',)
    search_fields = ('title', 'content_preview')
    prepopulated_fields = {"slug": ("title",)}

