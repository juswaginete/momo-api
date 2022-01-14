from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Products, ProductTypes

class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTypes
        fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer):
    """
    Serializer class for Products model
    """

    class Meta:
        model = Products
        fields = '__all__'

    def create_product(self, validated_data):

        product_name = self.data.get('product_name')
        product_description = self.data.get('product_description')
        # TODO: product_location = self.data.get('product_location')
        product_price = self.data.get('price')

        product_type_id = self.data.get('product_type')
        # TODO: product_type = ProductTypes.objects.get(id=product_type_id)
        # TODO: product_image

        date_created = self.data.get('date_created')
        date_updated = self.data.get('date_updated')

        try:
            product = Products(
                product_name=product_name,
                product_description=product_description,
                # TODO: product_location=product_location,
                product_price=product_price,

                # TODO: product_type=product_type,
                # TODO: product_image=product_image

                date_created=date_created,
                date_updated=date_updated,
            )

            product.save()

            return {
                "id": product.id,
                "product_name": product.product_name,
                "product_description": product.product_description,
                # TODO: "product_location":
                "product_price": product.product_price,

                # "product_type": {
                #     "id": product.product_type.id,
                #     "product_type_name": product.product_type.product_type_name,
                #     "date_created": product.product_type.date_created,
                #     "date_updated": product.product_type.date_updated,
                # },

                #TODO: product image

                "date_created": product.date_created,
                "date_updaed": product.date_updated,
            }
        except Exception as e:
            raise e
