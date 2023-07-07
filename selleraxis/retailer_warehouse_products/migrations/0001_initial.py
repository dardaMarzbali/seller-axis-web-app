# Generated by Django 3.2.14 on 2023-07-07 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("retailer_warehouses", "0001_initial"),
        ("product_alias", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetailerWarehouseProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "product_alias",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product_alias.productalias",
                    ),
                ),
                (
                    "retailer_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="retailer_warehouses.retailerwarehouse",
                    ),
                ),
            ],
        ),
    ]
