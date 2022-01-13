from django.shortcuts import render
from django.http import Http404

from rest_framework import status
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Products, ProductTypes
from .serializers import ProductsSerializer
# TODO:, ProductTypesSerializer


class ProductsView(APIView):
    """
    Handles api endpoints for pets
    """

    def get(self, request, format=None):
        """
        GET endpoint to list all pets in Pets model/table
        """
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)

        return Response(serializer.data)

    def post(self, request):
        """
        POST endpoint for creating a pet in Pets model/table
        """
        serializer = ProductsSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.create_product(request))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ProductObjectView(APIView):
    """
    Handles the api endpoint for getting specific product
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
        GET endpoint to list all pets in Pets model/table
        """
        product = self.get_object(pk)
        serializer = ProductsSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductsSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)