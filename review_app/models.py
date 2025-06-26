from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from product_app.models import Product  # adjust path based on your project

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'product']  # One review per user per product

    def __str__(self):
        return f'{self.user} - {self.product} ({self.rating})'
