from django.urls import path
from Products_app import views

app_name = 'product_app'
urlpatterns = [

    path('', views.index, name="index"),
    path('list_products', views.list_products, name="list_products"),
    path('single_product_details/<pk>', views.single_product_details, name="single_product_details"),

]
