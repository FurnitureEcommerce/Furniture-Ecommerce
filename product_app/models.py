from django.db import models

from category_app.models import Category


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    final_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    stock = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    material = models.CharField(max_length=100, blank=True, null=True)
    color = models.CharField(max_length=50, blank=True, null=True)
    dimensions = models.CharField(max_length=100, help_text="e.g. 80x120x60 cm")
    weight = models.DecimalField(max_digits=6, decimal_places=2, help_text="in kg", blank=True, null=True)
    image = models.ImageField(upload_to='product_images/')
    tags = models.CharField(max_length=255, help_text="Comma-separated", blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.final_price = self.price - (self.price * self.discount / 100)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name