# shipping_app/serializers.py
from rest_framework import serializers
from .models import ShippingAddress

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        read_only_fields = ['user', 'created_at']

    def validate_phone(self, value):
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError("Phone must be a 10-digit number.")
        return value

    def validate_postal_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Postal code must be numeric.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        if validated_data.get('is_default'):
            ShippingAddress.objects.filter(user=user, is_default=True).update(is_default=False)
        validated_data['user'] = user
        return super().create(validated_data)
