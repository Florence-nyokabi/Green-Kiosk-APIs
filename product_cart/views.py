from django.shortcuts import render, redirect
from .models import Product_Cart
from .models import Product
from .forms import ProductCartForm
from datetime import datetime

# Create your views here.
def add_to_cart(request, id):
    product = Product.objects.get(id=id)

    cart_item = Product_Cart (
        product_name = product.name,
        product_price = product.price,
        product_image = product.image,
        product_quantity = 1,
        date_added=datetime.now(),
    )
    cart_item.save()

    return redirect("product_list_view")


def view_cart(request):
    product_cart = Product_Cart.objects.all()
    
    total_cart_price = 0

    for item in product_cart:
        item.total_price = item.product_price * item.product_quantity
        total_cart_price += item.total_price

    return render(request, "product_cart/view_cart.html", {"product_cart": product_cart, "total_cart_price": total_cart_price})


def update_cart(request, id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = Product_Cart.objects.get(id=id)
        if quantity > 0:
            cart_item.product_quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

def remove_item(request, id):
    cart_item = Product_Cart.objects.get(id=id)
    cart_item.delete()

    return redirect('view_cart')


def empty_cart(request):
    Product_Cart.objects.all().delete()
    return redirect("view_cart")