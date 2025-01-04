from django.urls import path
from Orders_app import views

app_name = "order_app"

urlpatterns = [

    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("cart_items", views.cart_items, name="cart_items"),
    path("cart_items_remove", views.cart_items_remove, name="cart_items_remove"),
    path("order_conformed", views.order_conformed, name="order_conformed")
]
