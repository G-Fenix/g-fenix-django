from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'language', 'price', 'is_active')
    list_filter = ('language', 'is_active')
    search_fields = ('name', 'description')

