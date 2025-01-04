from django.db import models

# Create your models here.
from django.db.models import CharField


# Create your models here.
class Products(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )

    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField(max_length=400)
    images = models.ImageField(upload_to='media/')  # Corrected path
    priority = models.IntegerField(default=0)  # Add validation if necessary
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)  # Renamed for convention
    updated_at = models.DateTimeField(auto_now=True)  # Renamed for convention

    def __str__(self) -> CharField:  # Fixed annotation
        return self.title
