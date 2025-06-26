# shipping_app/admin.py
from django.contrib import admin
from .models import ShippingAddress

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'is_default', 'created_at')
    list_filter = ('city', 'is_default')
