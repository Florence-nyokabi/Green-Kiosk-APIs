from django.shortcuts import render
from rest_framework.views import APIView
from customer.models import Customer
from .serializers import CustomerSerializer
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
