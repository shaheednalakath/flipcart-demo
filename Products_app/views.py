from django.shortcuts import render
from .templatetags import splitter
from .models import Products
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


# Create your views here.
def list_products(request):
    page = 1
    if request.GET:
        page = request.GET.get('page', 1)
    # product_list = Products.objects.all()
    product_list = Products.objects.order_by('priority')
    product_paginator = Paginator(product_list, 4)
    # page_number = request.GET.get('page')
    product_list = product_paginator.get_page(page)
    context = {'products': product_list}
    return render(request, "products.html", context)


@login_required(login_url="customer_app:register_login")
def single_product_details(request, pk):
    product_click = Products.objects.get(pk=pk)
    context = {"product_click": product_click}
    return render(request, "single_product_details.html", context)
