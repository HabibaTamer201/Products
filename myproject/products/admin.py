from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'release_date', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category', 'release_date')
