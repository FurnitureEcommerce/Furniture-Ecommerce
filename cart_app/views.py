from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from rest_framework.permissions import IsAuthenticated
from product_app.models import Product

class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Prevent duplicate cart creation for a user
        if Cart.objects.filter(user=self.request.user).exists():
            raise serializers.ValidationError("Cart already exists for this user.")
        serializer.save(user=self.request.user)


class CartItemViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        # Check if product exists and is active
        if not product.is_active:
            raise serializers.ValidationError("This product is not available anymore.")

        # Check stock
        if quantity > product.stock:
            raise serializers.ValidationError("Requested quantity exceeds available stock.")

        # Get or create user's cart
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

    def perform_update(self, serializer):
        product = serializer.validated_data['product']
        quantity = serializer.validated_data['quantity']

        if not product.is_active:
            raise serializers.ValidationError("This product is no longer available.")

        if quantity > product.stock:
            raise serializers.ValidationError("Insufficient stock.")

        serializer.save()
