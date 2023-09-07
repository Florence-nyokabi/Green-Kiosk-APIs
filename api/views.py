from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Customer
from inventory.models import Product
from orders.models import Order
from product_cart.models import ProductCart
from .serializers import CustomerSerializer, InventorySerializer, OrderSerializer, ProductCartSerializer
from rest_framework.response import Response
from rest_framework import status



# Create your views here.
class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many = True)  # this serializes the data
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class CustomerDetailView(APIView):
    def get(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        serializer = CustomerSerializer(customer, request.data) #compares the data with the data that was previously
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Todo- add the correct status code
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("Customer Deleted", status= status.HTTP_204_NO_CONTENT)



class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = InventorySerializer(products, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InventorySerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    

class ProductDetailView(APIView):
    def get(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = ProductDetailView(product)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        product = Product.objects.get(id=id)
        serializer = InventorySerializer(product, request.data) #compares the data with the data that was previously
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Todo- add the correct status code
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        product = Product.objects.get(id=id)
        product.delete()
        return Response("Product Deleted", status= status.HTTP_204_NO_CONTENT)


class OrdersListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class OrderDetailView(APIView):
    def get(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderDetailView(order)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = OrderSerializer(order, request.data) #compares the data with the data that was previously
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Todo- add the correct status code
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        order = Order.objects.get(id=id)
        order.delete()
        return Response("Order Deleted", status= status.HTTP_204_NO_CONTENT)


class ProductCartListView(APIView):
    def get(self, request):
        product_cart = Order.objects.all()
        serializer = ProductCartSerializer(product_cart, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductCartSerializer(data = request.data)
        if serializer.is_valid ():
            serializer.save()
            return  Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400)
    
class ProductCartDetailView(APIView):
    def get(self, request, id, format=None):
        product_cart = ProductCart.objects.get(id=id)
        serializer = ProductCartSerializer(product_cart)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        order = Order.objects.get(id=id)
        serializer = ProductCartSerializer(order, request.data) #compares the data with the data that was previously
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) # Todo- add the correct status code
        return Response(serializer.errors, status = status.HTTP_400)
    
    def delete(self, request, id, format=None):
        product_cart= ProductCart.objects.get(id=id)
        product_cart.delete()
        return Response("Product cart deleted", status= status.HTTP_204_NO_CONTENT)
