# Generated by Django 3.2.14 on 2023-07-21 05:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "product_warehouse_static_data",
            "0009_alter_productwarehousestaticdata_product_warehouse",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="productwarehousestaticdata",
            name="status",
        ),
    ]
