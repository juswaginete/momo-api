# Generated by Django 4.0.1 on 2022-02-03 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttypes',
            name='product_type_name',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
