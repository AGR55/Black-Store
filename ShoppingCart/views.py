from django.shortcuts import redirect
from .shopping import ShoppingCart
from Store.models import Product

# Create your views here.


def add_product(request, product_id):
    cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    cart.add(product=product)
    return redirect('Store')


def subtract_product(request, product_id):
    cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    cart.subtract(product=product)
    return redirect('Store')


def remove_product(request, product_id):
    cart = ShoppingCart(request)
    product = Product.objects.get(id=product_id)
    cart.remove(product=product)
    return redirect('Store')


def clear_cart(request):
    cart = ShoppingCart(request)
    cart.clear()
    return redirect('Store')
