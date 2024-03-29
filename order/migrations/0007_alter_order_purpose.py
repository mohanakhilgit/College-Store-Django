# Generated by Django 4.1.5 on 2023-01-14 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0006_alter_order_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="purpose",
            field=models.CharField(
                choices=[
                    ("enquiry", "Enquiry"),
                    ("place_order", "Place Order"),
                    ("return", "Return"),
                ],
                default="place_order",
                max_length=100,
            ),
        ),
    ]
