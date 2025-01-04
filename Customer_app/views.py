from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customers
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, "index.html")


# def register_login(request):
#     if request.method == "POST" and 'submit_register' in request.POST:
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#
#         # Check if the username or email already exists
#         if User.objects.filter(username=username).exists():
#             messages.error(request,"username already taken")
#             return redirect("customer_app:register_login")
#         if User.objects.filter(email=email).exists():
#             messages.error(request,"email already taken")
#             return redirect("customer_app:register_login")
#
#         # Create and save the user with a hashed password
#         user = User.objects.create_user(
#             username=username,
#             password=password,  # Automatically hashes the password
#             email=email
#         )
#
#         # Create and save the customer profile
#         customer = Customers.objects.create(user=user, phone=phone, address=address)
#
#         # Log the user in (optional)
#         # from django.contrib.auth import login
#         # login(request, user)
#
#         return redirect('/')
#
#     return render(request, "register_login.html")

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customers


def register_login(request):
    context_form_select = {}
    # Handle user registration
    if request.method == "POST" and 'submit_register' in request.POST:
        context_form_select["register"] = True
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        # Check if the username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
            return redirect("customer_app:register_login")
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already taken")
            return redirect("customer_app:register_login")

        # Create and save the user with a hashed password
        user = User.objects.create_user(
            username=username,
            password=password,  # Automatically hashes the password
            email=email

        )

        # Create and save the customer profile
        customer = Customers.objects.create(name=username, user=user, phone=phone, address=address)

        messages.success(request, "Registration successful. Please log in.")
        return redirect("customer_app:register_login")  # Redirect to the same page for login

    # Handle user login
    if request.method == "POST" and 'submit_login' in request.POST:
        context_form_select["register"] = False
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/')
            messages.success(request, "Login successful!")
            return redirect(next_url)  # Redirect to the home page
        else:
            messages.error(request, "Invalid username or password")
            return redirect("customer_app:register_login")

    # Render the template for GET requests
    return render(request, "register_login.html", context_form_select)


def register_logout(request):
    logout(request)
    return redirect('/')
