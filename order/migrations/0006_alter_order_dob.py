# Generated by Django 4.1.5 on 2023-01-14 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0005_alter_order_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="dob",
            field=models.DateField(),
        ),
    ]
