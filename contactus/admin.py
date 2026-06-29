from django.contrib import admin
from .models import ContactMessage, NewsletterSubscriber

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display    = ('first_name', 'last_name', 'email', 'subject', 'created_at', 'is_read')
    list_filter     = ('is_read', 'created_at')
    search_fields   = ('first_name', 'last_name', 'email', 'subject')
    readonly_fields = ('first_name', 'last_name', 'email', 'subject', 'message', 'created_at')
    ordering        = ('-created_at',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        obj = self.get_object(request, object_id)
        if obj and not obj.is_read:
            obj.is_read = True
            obj.save(update_fields=['is_read'])
        return super().change_view(request, object_id, form_url, extra_context)

    def has_add_permission(self, request):
        return False


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display    = ('email', 'created_at', 'is_active')
    list_filter     = ('is_active', 'created_at')
    search_fields   = ('email',)
    readonly_fields = ('email', 'created_at')
    ordering        = ('-created_at',)

    def has_add_permission(self, request):
        return False