from django.contrib import admin
from .models import PageContent, TeamMember, SocialMediaLink

@admin.register(PageContent)
class PageContentAdmin(admin.ModelAdmin):
    list_display = ('page_key', 'language', 'title', 'updated_at')
    list_filter = ('language', 'page_key')
    search_fields = ('title', 'content')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'language')
    list_filter = ('language',)
    search_fields = ('name', 'role')

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'language')
    list_filter = ('language',)
    search_fields = ('platform', 'url')
