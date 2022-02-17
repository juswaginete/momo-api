from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers

from .models import Products, ProductTypes, ProductImages

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
        product_price = self.data.get('product_price')

        product_type_id = self.data.get('product_type')
        user_profile_id = self.data.get('user_profile')
        user = Profiles.objects.get(id=user_profile_id)
        product_type = ProductTypes.objects.get(id=product_type_id)
        # product_image = self.data.get('product_image')

        # date_created = self.data.get('date_created')
        # date_updated = self.data.get('date_updated')

        try:
            if product_type:
                product = Products(
                    product_name=product_name,
                    product_description=product_description,
                    # TODO: product_location=product_location,
                    user_profile=user,
                    product_price=product_price,

                    product_type=product_type,
                    # TODO: product_image=product_image

                    # date_created=date_created,
                    # date_updated=date_updated,
                )

                product.save()

                return {
                    "id": product.id,
                    "user": {
                        "id": product.user_profile.id,
                        "email": product.user_profile.user.email,
                        "first_name": product.user_profile.user.first_name,
                        "last_name": product.user_profile.user.last_name
                    },

                    "product_type": {
                        "id": product.product_type.id,
                        "product_type_name": product.product_type.product_type_name,
                        "date_created": product.product_type.date_created,
                        "date_updated": product.product_type.date_updated,
                    },

                    #TODO: product image
                    "product_name": product.product_name,
                    "product_description": product.product_description,
                    # TODO: "product_location":
                    "product_price": product.product_price,
                    "date_created": product.date_created,
                    "date_updated": product.date_updated,
                }
        except Exception as e:
            raise e


class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = '__all__'