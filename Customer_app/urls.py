from django.urls import path
from Customer_app import views

app_name = "customer_app"
urlpatterns = [

    path("register_login", views.register_login, name="register_login"),
    path("register_logout", views.register_logout, name="register_logout")
]
