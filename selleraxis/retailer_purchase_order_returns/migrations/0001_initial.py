# Generated by Django 3.2.14 on 2023-12-11 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("retailer_purchase_orders", "0029_alter_retailerpurchaseorder_status"),
        ("retailer_warehouses", "0004_auto_20230814_0814"),
    ]

    operations = [
        migrations.CreateModel(
            name="RetailerPurchaseOrderReturn",
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
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_returns",
                        to="retailer_purchase_orders.retailerpurchaseorder",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="warehouse_returns",
                        to="retailer_warehouses.retailerwarehouse",
                    ),
                ),
            ],
        ),
    ]
