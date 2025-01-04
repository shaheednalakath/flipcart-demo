from django.db import models
from django.contrib.auth.models import User
from django.db.models import CharField


class Customers(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )

    name = models.CharField(max_length=200)
    address = models.TextField()
    description = models.CharField(max_length=400)  # Changed to CharField for max_length
    phone = models.CharField(max_length=10)
    images = models.ImageField(upload_to='media/')  # Ensure MEDIA_ROOT and MEDIA_URL are configured
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_profiles")
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> CharField:  # Fixed return type annotation
        return self.user.username
