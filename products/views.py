from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Products, ProductTypes
from .serializers import ProductsSerializer, ProductTypesSerializer



class ProductTypesView(APIView):

    # Handles api endpoints for pet types

    def get(self, request, format=None):
        product_types = ProductTypes.objects.all()
        serializer = ProductTypesSerializer(product_types, many=True)
        return Response(serializer.data)

    def post(self, request):
            serializer = ProductTypesSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsView(APIView):
    """
    Handles API endpoints for Products
    """

    def get(self, request, format=None):
        """
        GET endpoint to list all products in Products model/table
        """
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

    def post(self, request):
        """
        POST endpoint for creating a product in Products model/table
        """
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.create_product(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductObjectView(APIView):
    """
    Handles the API endpoints for getting a specific product
    """

    def get_object(self, pk):
        try:
            return Products.objects.get(pk=pk)

        except Products.DoesNotExist:
            return Response({
                'error': 'True',
                'message': 'Product not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        """
        GET endpoint to list a specific product in Products model/table
        """
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        PUT endpoint to update a specific product in Products model/table
        """
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        DELETE endpoint to destroy a specific product in Products model/table
        """
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
