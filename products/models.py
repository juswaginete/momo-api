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

    class Meta:
        verbose_name = "Product Type"
        verbose_name_plural = "Product Types"

    def __str__(self):
        return(self.product_type_name)

def nameFile(instance, filename):
    # import pdb; pdb.set_trace();
    return '/'.join(['images', "products", filename])
    
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

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return(self.product_name)


class ProductImages(models.Model):
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_images", **optional)
    image = models.ImageField(upload_to=nameFile, **optional)

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return(self.products.product_name)