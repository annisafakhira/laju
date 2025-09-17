import uuid
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    CATEGORY_CHOICES = [
        ('wear', 'Wear'),
        ('shoes', 'Shoes'),
        ('equipment', 'Equipment'),
        ('merchandise', 'Merchandise'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    is_featured = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)
    product_views = models.PositiveIntegerField(default=0)
    brand = models.CharField(max_length=35, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    @property
    def is_product_hot(self):
        return self.product_views > 200
        
    def increment_views(self):
        self.product_views += 1
        self.save()