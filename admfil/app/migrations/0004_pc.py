# Generated by Django 4.1.5 on 2023-01-26 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_alter_nmaepeople_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="PC",
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
                ("name", models.CharField(max_length=200, verbose_name="Название")),
                ("price", models.PositiveIntegerField(verbose_name="Цена")),
            ],
            options={
                "verbose_name": "ПК",
                "verbose_name_plural": "ПК",
            },
        ),
    ]
