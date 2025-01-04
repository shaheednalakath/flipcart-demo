# Create your views here.
from django.shortcuts import render, redirect
from .models import Orders, OrderedItems
from Products_app.models import Products
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.


# def cart_items(request):
#     # Retrieve the user's cart object or create it if it doesn't exist
#     user = request.user
#     customer = user.customer_profiles
#     cart_obj, created = Orders.objects.get_or_create(
#         owner=customer,
#         order_status=Orders.CART_STAGE
#     )
#     total_price = sum(item.products.price * item.quantity for item in cart_obj.added_items.all())
#
#     # Pass the cart object to the template context
#     context = {
#         'cart': cart_obj,  # Passing the cart to the template
#         'total_price': total_price
#     }
#     return render(request, 'cart.html', context)

def cart_items(request):
    # Retrieve the user's cart object or create it if it doesn't exist
    user = request.user
    customer = user.customer_profiles
    cart_obj, created = Orders.objects.get_or_create(
        owner=customer,
        order_status=Orders.CART_STAGE
    )

    # Calculate total price (sum of all product prices times their quantity)
    total_price = sum(item.products.price * item.quantity for item in cart_obj.added_items.all())

    # Calculate total number of products in the cart
    total_products = sum(item.quantity for item in cart_obj.added_items.all())

    # Calculate total sum across all carts for the customer (if needed)
    total_sum_all_carts = sum(
        item.products.price * item.quantity
        for order in Orders.objects.filter(owner=customer)
        for item in order.added_items.all()
    )
    discount = total_sum_all_carts * 0.10

    # Calculate the total after applying the discount
    total_after_discount = total_sum_all_carts - discount
    # Pass the cart object and totals to the template context
    context = {
        'cart': cart_obj,  # Current cart object
        # 'total_price': total_price,  # Total price for this cart
        'total_products': total_products,  # Total number of products in this cart
        'total_sum_all_carts': total_sum_all_carts,
        'discount': discount,  # 10% discount
        'total_after_discount': total_after_discount  # Total after discount
        # Total sum of all carts for the user
    }
    return render(request, 'cart.html', context)


def add_to_cart(request):
    if request.POST:
        user = request.user
        customer = user.customer_profiles
        quantity = request.POST.get('quantity')
        product_id = request.POST.get('product_id')
        size = request.POST.get('size')
        cart_obj, created = Orders.objects.get_or_create(
            owner=customer,
            order_status=Orders.CART_STAGE
        )

        product = Products.objects.get(pk=product_id)
        price = product.price * int(quantity)
        ordered_items = OrderedItems.objects.create(
            owner=cart_obj,
            products=product,
            quantity=quantity,
            size=size,
            price=price
        )
    return redirect("order_app:cart_items")


# def cart_items_remove(request):
#     user = request.user
#     customer = user.customer_profiles
#     product_id = request.POST.get('product_id')
#     cart_obj, created = Orders.objects.get_or_create(
#         owner=customer,
#         order_status=Orders.ORDER_REJECTED
#     )
#     product = Products.objects.get(pk=product_id)
#     ordered_items = OrderedItems.objects.create(
#         owner=cart_obj,
#         products=product,
#         quantity=quantity,
#         size=size,
#     )
#     return redirect("order_app:cart_items")
# def cart_items_remove(request):
#     if request.method == "POST":
#         user = request.user
#         customer = user.customer_profiles
#         product_id = request.POST.get('product_id')
#
#         # Get the cart for the customer
#         cart_obj = get_object_or_404(
#             Orders,
#             owner=customer,
#             order_status=Orders.CART_STAGE
#         )
#
#         # Find the specific OrderedItems entry and delete it
#         ordered_items = get_object_or_404(
#             OrderedItems,
#             owner=cart_obj,
#             products_id=product_id
#         )
#         OrderedItems.objects.filter(owner=cart_obj, products_id=product_id).delete()
#
#     return redirect("order_app:cart_items")
def cart_items_remove(request):
    if request.method == "POST":
        user = request.user
        customer = user.customer_profiles
        product_id = request.POST.get('product_id')

        # Get the cart for the customer
        cart_obj = get_object_or_404(
            Orders,
            owner=customer,
            order_status=Orders.CART_STAGE
        )

        # Remove all matching items
        OrderedItems.objects.filter(owner=cart_obj, products_id=product_id).delete()

    return redirect("order_app:cart_items")


def order_conformed(request):
    user = request.user
    customer = user.customer_profiles

    # Try to get the order, or handle it if not found
    try:
        order_obj = Orders.objects.get(owner=customer, order_status=Orders.CART_STAGE)
        # Change order status to "ORDER_CONFORMED"

        order_obj.order_status = Orders.ORDER_CONFORMED
        order_obj.save()

        # Success message
        order_status_message = "Your order is confirmed and will be delivered within 7 working days."
        messages.success(request, order_status_message)

    except Orders.DoesNotExist:
        # If the order doesn't exist (i.e., no cart stage order found)
        order_status_message = "Oops! Unable to process. There are no items in your cart."
        messages.error(request, order_status_message)

    # Redirect to homepage or wherever needed
    return redirect('/')
