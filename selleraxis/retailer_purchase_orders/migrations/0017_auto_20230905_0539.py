# Generated by Django 3.2.14 on 2023-09-05 09:39

from django.db import migrations, models
import django.db.models.deletion


def avoid_errors_migration(apps, schema_editor):
    RetailerPurchaseOrder = apps.get_model(
        "retailer_purchase_orders", "RetailerPurchaseOrder"
    )
    RetailerPurchaseOrder.objects.all().update(ship_from=None, verified_ship_to=None)


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0001_initial"),
        ("retailer_purchase_orders", "0016_alter_retailerpurchaseorder_status"),
    ]

    operations = [
        migrations.RunPython(avoid_errors_migration),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="ship_from",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ship_from_orders",
                to="addresses.address",
            ),
        ),
        migrations.AlterField(
            model_name="retailerpurchaseorder",
            name="verified_ship_to",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="verified_ship_to_orders",
                to="addresses.address",
            ),
        ),
    ]
