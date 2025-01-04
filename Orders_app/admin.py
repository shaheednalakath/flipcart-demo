from django.contrib import admin
from .models import Orders, OrderedItems

# Register your models here.
admin.site.register(Orders)
admin.site.register(OrderedItems)
