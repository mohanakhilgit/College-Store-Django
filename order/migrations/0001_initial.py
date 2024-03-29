# Generated by Django 4.1.5 on 2023-01-13 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Department",
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
                ("name", models.CharField(max_length=100, unique=True)),
            ],
            options={
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Order",
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
                ("name", models.CharField(max_length=250)),
                ("dob", models.DateField()),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=10)),
                ("phone", models.IntegerField()),
                ("mail", models.EmailField(max_length=254)),
                ("address", models.TextField(blank=True)),
                (
                    "purpose",
                    models.CharField(
                        choices=[
                            ("enquiry", "Enquiry"),
                            ("place_order", "Place Order"),
                            ("return", "Return"),
                        ],
                        default="Place Order",
                        max_length=100,
                    ),
                ),
                (
                    "material",
                    models.CharField(
                        choices=[
                            ("note_book", "Note Book"),
                            ("pencil", "Pencil"),
                            ("pen", "Pen"),
                            ("scale", "Scale"),
                            ("box", "Box"),
                            ("exam_paper", "Exam Paper"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "courses",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="order.course"
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="order.department",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="course",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="order.department"
            ),
        ),
    ]
