from django.shortcuts import render
from Products_app.models import Products


# Create your views here.
def index(request):
    latest_products = Products.objects.order_by('-id')[:4]
    featured_products = Products.objects.order_by('priority')[:4]

    context = {
        'latest_products': latest_products,
        'featured_products': featured_products
    }
    return render(request, "index.html", context)
