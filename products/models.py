from django.db import models

from accounts.models import Profiles

optional = {
    'null': True,
    'blank': True,
}


class ProductTypes(models.Model):
    product_type_name = models.CharField(max_length=30, unique=True, **optional)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.product_type_name)

# change to be Products -> ProductTypes
class Products(models.Model):
    product_name = models.CharField(max_length=255, **optional)
    product_description = models.TextField(**optional)
    # TODO: product_location must be dynamic
    product_price = models.DecimalField(max_digits=20, decimal_places=8, **optional)
    product_type = models.ForeignKey(ProductTypes, on_delete=models.CASCADE, related_name="products", **optional)
    user_profile = models.ForeignKey(Profiles, on_delete=models.CASCADE, related_name="products", **optional)
    # TODO: product_image will be done later

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.product_name)
