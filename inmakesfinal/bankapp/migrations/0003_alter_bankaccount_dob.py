# Generated by Django 4.2.6 on 2023-10-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bankapp", "0002_remove_bankaccount_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bankaccount",
            name="DOB",
            field=models.DateField(verbose_name="Date of Birth"),
        ),
    ]
