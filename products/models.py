from django.db import models
from django.conf import settings

def product_image_path(instance, filename):
    return f'images/{filename}'

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to=product_image_path,
        blank=True,
        null=True,
    )
    
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )
    
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_products"
    )
    
    def __str__(self):
        return self.name