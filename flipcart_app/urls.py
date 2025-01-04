from django.urls import path
from flipcart_app import views

app_name = 'flipcart_app'
urlpatterns = [
    path('', views.index, name="index")
]
