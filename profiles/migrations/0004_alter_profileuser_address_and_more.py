# Generated by Django 4.1.2 on 2022-10-21 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_profileuser_address_profileuser_company_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profileuser",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profileuser",
            name="company_name",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="profileuser",
            name="state",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]