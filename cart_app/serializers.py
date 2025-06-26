from rest_framework import serializers
from .models import Cart, CartItem
from product_app.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.name')
    product_price = serializers.ReadOnlyField(source='product.final_price')

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'added_at']

    def validate_quantity(self, value):
        product = self.initial_data.get('product')
        product_obj = Product.objects.filter(id=product).first()
        if not product_obj:
            raise serializers.ValidationError("Invalid product.")
        if value > product_obj.stock:
            raise serializers.ValidationError("Requested quantity exceeds available stock.")
        return value


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'created_at', 'items']
        read_only_fields = ['user']
