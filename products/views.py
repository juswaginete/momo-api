from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Products, ProductTypes
from .serializers import ProductsSerializer, ProductTypesSerializer



class ProductTypesView(APIView):
    """
    Handles API endpoints for Product Types
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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

class ProductTypeView(APIView):
    """
    Handles the API endpoints in a specific product type
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return ProductTypes.objects.get(pk=pk)

        except ProductTypes.DoesNotExist:
            return Response({
                'error': 'True',
                'message': 'Product type not found'
            }, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        """
        GET endpoint to list a specific product type (for testing purposes, not in the trello list)
        """
        product_type = self.get_object(pk)
        serializer = ProductTypesSerializer(product_type)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        """
        PUT endpoint to update a specific ProductType
        """
        product_type = self.get_object(pk)
        serializer = ProductTypesSerializer(product_type, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        DELETE endpoint to delete a ProductType
        """
        product_type = self.get_object(pk)
        product_type.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsView(APIView):
    """
    Handles API endpoints for Products
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        GET endpoint to list all products in Products model/table
        """
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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
