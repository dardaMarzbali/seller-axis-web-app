# Generated by Django 3.2.14 on 2023-09-27 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0008_remove_organization_gs1"),
    ]

    operations = [
        migrations.AddField(
            model_name="organization",
            name="qbo_access_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="qbo_access_token_exp_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="qbo_refresh_token",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="qbo_refresh_token_exp_time",
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name="organization",
            name="realm_id",
            field=models.TextField(blank=True, null=True),
        ),
    ]
