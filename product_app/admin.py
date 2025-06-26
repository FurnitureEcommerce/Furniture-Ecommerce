from django.contrib import admin
from django import forms
from .models import Product

# Custom form for validation
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_discount(self):
        discount = self.cleaned_data['discount']
        if discount < 0 or discount > 100:
            raise forms.ValidationError("Discount must be between 0 and 100.")
        return discount

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price

    def clean_stock(self):
        stock = self.cleaned_data['stock']
        if stock < 0:
            raise forms.ValidationError("Stock cannot be negative.")
        return stock

# Admin config for Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ['id', 'name', 'price', 'final_price', 'category', 'stock', 'brand', 'is_active']
    list_filter = ['category', 'brand', 'is_active']
    search_fields = ['name', 'brand', 'tags']
    readonly_fields = ['final_price', 'created_at']

    # Only superuser can add/update/delete
    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser


