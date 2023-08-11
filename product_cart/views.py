from django.shortcuts import render, redirect
from .models import Product_Cart
from .forms import ProductCartForm

# Create your views here.

def upload_products(request):
    if request.method=="POST":
        form = ProductCartForm(request.POST)
        
        if form.is_valid():
            cart=form.save()
            cart.save()
    else:
        form=ProductCartForm()
    return render(request, "shoppingcart/upload_products.html",{"form":form})            

    
def display_cart_products(request):
    cart= Product_Cart.objects.all()
    return render (request, "shoppingcart/display_cart_products.html", {"cart":cart})


def edit_cart_details(request,id):
    cart= Product_Cart.objects.all(id = id)
    
    if request.method=="POST":
         form= ProductCartForm(request.POST, instance=cart)
         if form.is_valid():
             form.save()
         return redirect("cart_detail_view", id=cart.id)    
     
    else:
        form = ProductCartForm(instance= cart)
        return render(request, "shoppingcart/ edit_cart_details.html", {"form":form})
    
def clear_product_cart(request, id):
    product_cart = Product_Cart.objects.get(id=id)
    product_cart.delete()
    return redirect("product_cart_list")