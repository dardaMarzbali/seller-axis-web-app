# Generated by Django 3.2.14 on 2023-07-18 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("retailer_commercehub_sftp", "0002_alter_retailercommercehubsftp_retailer"),
    ]

    operations = [
        migrations.AddField(
            model_name="retailercommercehubsftp",
            name="confirm_xml_format",
            field=models.CharField(blank=True, default="", max_length=225),
        ),
        migrations.AddField(
            model_name="retailercommercehubsftp",
            name="inventory_xml_format",
            field=models.CharField(blank=True, default="", max_length=225),
        ),
        migrations.AddField(
            model_name="retailercommercehubsftp",
            name="invoice_xml_format",
            field=models.CharField(blank=True, default="", max_length=225),
        ),
        migrations.AddField(
            model_name="retailercommercehubsftp",
            name="payment_xml_format",
            field=models.CharField(blank=True, default="", max_length=225),
        ),
        migrations.AddField(
            model_name="retailercommercehubsftp",
            name="return_xml_format",
            field=models.CharField(blank=True, default="", max_length=225),
        ),
    ]
