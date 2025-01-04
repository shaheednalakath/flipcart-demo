from django.db import models

# Create your models here.
from django.db import models
from Customer_app.models import Customers
from Products_app.models import Products


# Create your models here.

class Orders(models.Model):
    LIVE = 1
    DELETE = 0
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete'),
    )
    CART_STAGE = 0
    ORDER_CONFORMED = 1
    ORDER_PROCESSED = 2
    ORDER_DELIVERED = 3
    ORDER_REJECTED = 4
    STATUS_CHOICE = (
        (ORDER_PROCESSED, "ORDER_PROCESSED"),
        (ORDER_DELIVERED, "ORDER_DELIVERED"),
        (ORDER_REJECTED, "ORDER_REJECTED")
    )

    order_status = models.IntegerField(choices=STATUS_CHOICE, default=CART_STAGE)
    owner = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, related_name='orders')
    delete_status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)

    # Other fields for your order model

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "order-{}-{}".format(self.id, self.owner.user.username)


class OrderedItems(models.Model):
    products = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name="added_cart")
    quantity = models.IntegerField(default=1)
    size = models.CharField(max_length=10)
    price = models.IntegerField(default=0)
    owner = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name="added_items")

    @property
    def total_price(self):
        return self.products.price * self.quantity
