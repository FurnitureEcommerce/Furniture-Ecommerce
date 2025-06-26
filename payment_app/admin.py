from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'amount', 'paid', 'created_at']
    list_filter = ['paid', 'created_at']
    search_fields = ['name', 'email', 'razorpay_order_id']
