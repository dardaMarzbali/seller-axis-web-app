# Generated by Django 3.2.14 on 2023-11-24 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("invoice", "0002_alter_invoice_add_live_qbo_info"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="live_doc_number",
        ),
        migrations.RemoveField(
            model_name="invoice",
            name="live_invoice_id",
        ),
    ]
