from django.db import models

class ProductType(models.Model):
	name = models.CharField(max_length = 30)
	date_created = models.DateTimeField(auto_now_add=True)
	date_updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
